"""" Побудувати декоратор, який перевіряє, чи містить функція, що
декорується, тільки ключові параметри. Якщо ні, то ініціює виключення.
Виконати перевірку роботи декоратора для деякої функції f.
 """

class Exception1(Exception):
    def __init__(self):
        super()
    def __str__(self):
        return "Є неключовий параметр"


def decorator1 (y):
    def funktion2 (*vargs, **qvargs):
        if len(vargs) > 0:
            raise Exception1
        i = y(*vargs, **qvargs)
        return i
    return funktion2

@decorator1
def funktion1 (x):
    x += x
    return x

@decorator1
def funktion2 (**qvargs):
    value = 0
    for x,y in qvargs.items():
        value += y
    return value

@decorator1
def funktion3 (x=1,y=2):
    return x+y

if __name__ == "__main__":
    try:
        funktion1(4)
    except:
        print("Помилка")

    y = funktion2(x=1, y=3, z=5)
    print(y)
    y = funktion3()
    print(y)
