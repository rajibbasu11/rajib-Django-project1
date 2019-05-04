#
#
# for i in range(100):
#     for j in range(i):
#         print("*", end=" ")
#
#     print("@")
#
#
#
#


def Myfunc(n):
    print(n)
    return lambda a: a + n


fnc = Myfunc(200)

print(fnc(2))
