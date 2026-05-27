# 1.输入你的姓名和爱好，使用 f-string 格式化输出简介，同时用 len() 统计姓名字符长度并打印。

name = input("请输入姓名：")
ider = input("请输入爱好：")
print(f'姓名:{name},爱好:{ider},名字长度:{len(name)}')

# 2.输入两个整数，使用比较运算符 + if 分支，输出两个数中较大的数字。

try:
    macth_num = int(input('请输入第一个数字:'))
    macth_num1 = int(input('请输入第二个数字:'))
except Exception:
    print('输入错误！')
if macth_num > macth_num1:
    print(f'最大数为:{macth_num}')
else:
    print(f'最大数为:{macth_num1}')
'''
try和except作用域没记清楚，导致输入错误后if仍然会运行，没起到警示作用
'''


# 3.输入一段带有首尾空格的文本，先用 strip() 去除空格，再用 split() 按空格分割成列表，打印最终列表。

text = input('请输入一个文本:')
new_text = text.strip()
print(new_text)
print(new_text.split(' '))

'''
split用法不清楚，如果输入需要切割的字符串中包含两个以上的空格，会导致切割出空字符串。
'''