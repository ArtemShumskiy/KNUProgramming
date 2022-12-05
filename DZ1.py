A = ((1, 2, 3) , (4, 5, 6) , (7, 8, 9))
B = ((1, 2, 3) , (4, 5, 6) , (7, 8, 9))
C = {'1':1, '2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}


def decorator(f):
    def check(*args,**kw):
        for i in kw:
            if not type(i) == type(kw):
                kw = f.items
        for l in args:
            if not type(l) == type(args):
                args = f.items
        print('Вигляд  списку: ')
        print(f(*args,**kw))
    return check

@decorator
def arraysSr4(A, C):
    print("Преобразований словник: ", C)
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    for r in result:
        if r:
            print(r)


print(arraysSr4(A,B))