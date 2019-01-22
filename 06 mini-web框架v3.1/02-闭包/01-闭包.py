def line(k, b):
    def create_y(x):
        print(k * x + b)

    return create_y


line6 = line(1, 2)
