def modA(x, y):
    return x + y
def a():
    print('A')
def b():
    print('B')
def c():
    print('C')
def d():
    print('D')
#限制导入的使用方法
__all__ = ['a','b']