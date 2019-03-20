# coding:utf-8
from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.models import User, Area
from ihome import db, constants, redis_store
from datetime import datetime
from ihome.utils.image_storage import storage
import json

area_li = None


@api.route("/areas", method=["GET"])
def get_area_info():
    # 获取城区信息
    try:
        resp_json = redis_store.get("area_json")
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json is not None:
            # redis有缓存数据
            return resp_json, 200, {"Content-Type": "application/json"}
    try:
        area_li = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库错误")
    area_dict_li = []
    # 将对象转换为字典
    for area in area_li:
        area_dict_li.append(area.to_dict())
    # 将数据转换为json字符串
    resp_dict = dict(errno=RET.OK, errmsg="OK", data=area_dict_li)
    resp_json = json.dumps(resp_dict)
    # 将数据保存到redis中
    try:
        redis_store.setex("area_info", constants.AREA_INFO_REDIS_CACHE_EXPIRES, resp_json)
    except Exception as e:
        current_app.logger.error(e)

    return resp_json, 200, {"Content-Type": "application/json"}


@api.route("/houses/info", method=["POST"])
@login_required
def save_house_info():
    user_id = g.user_id
    house_data = request.get_json()
    title = house_data.get("title")
    price = house_data.get("price")
    area_id = house_data.get("area_id")
    address = house_data.get("address")
    room_count = house_data.get("room_count")
    acreage = house_data.get("acreage")
    unit = house_data.get("unit")
    capacity = house_data.get("capacity")
    beds = house_data.get("beds")
    deposit = house_data.get("deposit")
    min_days = house_data.get("min_days")
    max_days = house_data.get("max_days")
    if not all(
            [title, price, area_id, address, room_count, acreage, unit, capacity, beds, deposit, min_days, max_days]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")
    # 判断金额是否正确
    try:
        price = int(float(price) * 100)
        deposit = int(float(deposit) * 100)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")
    # 判断城区id是否存在
    try:
        area = Area.query.get(area_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="参数错误")
    if area is None:
        return jsonify(errno=RET.NODATA, errmsg="城区信息有误")
    # 保存房屋信息
    house = House(
        user_id=user_id,
        area_id=area_id,
        title=title,
        price=price,
        room_count=room_count,
        acreage=acreage,
        unit=unit,
        capacity=capacity,
        beds=beds,
        deposit=deposit,
        min_days=min_days,
        max_days=max_days,
    )
    try:
        db.session.add(house)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存数据异常")
    db.session.add(house)
    facility_ids = house_data.get("facility")
    if facility_ids:
        try:
            facilities = Facility.query.filter(Facility.id.in_(facility_ids))
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(error=RET.DBERR, errmsg="数据库异常")
    if facilities:
        # 表示有合法数据
        house.facilities = facilities
        try:
            db.session.add(house)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            db.session.rollback()
            return jsonify(errno=RET.DBERR, errmsg="保存数据失败")
        return jsonify(errno=RET.OK, errmsg="保存数据成功", data={"house_id": house.id})


@api.route("/house/image", methods=["POST"])
@login_required
def save_house_image():
    # 保存房屋的图片
    image_file = request.files.get("house_image")
    house_id = request.form.get("house_id")
    if not all([image_file, house_id]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")
    # 判断house_id 正确性
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")
    if house is None:
        return jsonify(errno=RET.NODATA, errmsg="房屋不存在")
    # 保存图片到七牛中
    image_data = image_file.read()
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="保存图片失败")
    house_image = HouseImage(house_id=house_id, url=file_name)
    db.session.add(house_image)
    if not house.index_image_url:
        house.index_image_url = file_name
        db.session.add(house)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="保存图片数据异常")
    image_url = constants.QINIU_URL_DOMAIN + file_name
    return jsonify(errno=RET.OK, errmsg="OK", data={"image_url": image_url})


@api.route("/houses")
def get_house_list():
    start_date = request.args.get("sd")
    end_date = request.args.get("ed")
    area_id = request.args.get("aid")
    sort_key = request.args.get("sk")
    page = request.args.get("p")
    try:
        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date:
            end_date = datetime.strptime(end_date, "%y-%m-%d")
        if start_date and end_date:
            assert start_date <= end_date
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="日期参数有误")
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1
    li = []
    filter_params = []
    if start_date and end_date:
        conflict_orders = Order.query.filter(Order.begin_date <= end_date, Order.end_date >= start_date).all()
    elif start_date:
        conflict_orders = Order.query.filter(Order.end_date >= start_date).all()
    elif end_date:
        conflict_orders = Order.query.filter(Order.begin_date <= end_date).all()
    if conflict_orders:
        conflict_orders_ids = [order.house_id for order in conflict_orders]
        if conflict_orders_ids:
            filter_params.append(House.id.notin_(conflict_orders_ids))
    if area_id:
        filter_params.append(House.area_id == area_id)

    if sort_key == "booking":
        house_query = House.query.filter(*filter_params).order_by(House.order_count.desc())
    elif sort_key == "price-inc":
        house_query = House.query.filter(*filter_params).order_by(House.price.asc())
    elif sort_key == "price-des":
        house_query = House.query.filter(*filter_params).order_by(House.price.desc())
    else:
        house_query = House.query.filter(*filter_params).order_by(House.create_time.desc())
    page_obj = house_query.pageinate(page=page, per_page=constants.HOUSE, err_out=False)
    house_li = page_obj.items
    houses = []
    for house in houses:
        houses.append(house.to_basic_dict())
    total_page = page_obj.pages
    resp_dict = dict(errno=RET.OK, errmsg="OK", data={"total_page": total_page, "houses": houses, "current_page": page})
    resp_json = json.dumps(resp_dict)
    if page<=total_page:
        redis_key = "house_%s_%s_%s_%s" % (start_date, end_date, area_id, sort_key)
        try:
            # redis_store.hset(redis_key,page,resp_json)
            pipeline = redis_store.pipeline()
            pipeline.multi()
            pipeline.hset(redis_key, page, resp_json)
            pipeline.expire(redis_key,constants.xxxxx)
            pipeline.execute()
        except Exception as e:
            current_app.logger.error(e)
    return resp_json,200,{"Content-Type":"application/json"}