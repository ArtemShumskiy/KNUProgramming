counter = 0


def alter(f):
    def _alter(*args, **kwargs):
        global counter
        try:
            return f(*args, **kwargs)
        except Exception as e:
            if counter == 0:
                file = open('file_of_errors', 'w')
                counter += 1
            else:
                file = open('file_of_errors', 'a')
            file.write(str(repr(e)) + '\n')
            file.close()

    return _alter


def catch_exceptions(cls):
    lst = cls.__dict__.items()
    for name, method in lst:
        if callable(method):
            setattr(cls, name, alter(method))
    return cls


@catch_exceptions
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    def a(self):
        return self.x + self.y

    def b(self):
        return self.x / self.y


if __name__ == '__main__':
    obj_1 = MyClass(1, '1')
    obj_2 = MyClass(1, 0)
    obj_3 = MyClass(1, 2, 3)
    print(obj_1)
    print(obj_2)
    print(obj_1.a(), obj_1.b())
    print(obj_2.a(), obj_2.b())