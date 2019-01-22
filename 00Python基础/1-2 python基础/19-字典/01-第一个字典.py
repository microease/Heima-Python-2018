xiaoming = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75
}
print(xiaoming["name"])

xiaoming.update({"xx":"11"})
print(xiaoming)

xiaoming.pop("xx")

print(xiaoming)

# xiaoming.clear()
# print(xiaoming)

for key in xiaoming:
    print(xiaoming[key])