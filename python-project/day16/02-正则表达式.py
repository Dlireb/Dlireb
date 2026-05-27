import re
str_all = '''
fjlas
13256454651
ff1a31da3
d1af35s1
abdfagaabdafsdf
#$%^&*GYH*TI561581
13570073844
__dfasga516__vgad52
http://www.baidu.com
    safd   dafa wef 
   http://qq.com
'''
'''
    #简单操作
    # 匹配纯数字字符串（如：123、0987），不包含其他字符。
    new_str = re.findall(r'\d+',str_all)
    print(f'匹配数字：{new_str}')
    # 匹配纯英文字母（大小写均可，如：Abc、hello）。
    new_str = re.findall(r'\w+',str_all)
    print(f'匹配字母：{new_str}')
    # 匹配手机号（简单版：11 位纯数字）。
    new_str = re.findall(r'(?<!\d)1\d{10}(?!\d)',str_all)
    print(f'匹配手机号码：{new_str}')
    # 匹配长度为 3~6 位的数字。
    new_str = re.findall(r'\d{3,6}',str_all)
    print(f'匹配3-6位数字：{new_str}')
    # 匹配包含下划线的单词（由字母、数字、下划线组成）。
    new_str = re.findall(r'\w+',str_all)
    print(f'匹配包含下划线的单词（由字母、数字、下划线组成）：{new_str}')
    # 匹配以 http 开头的字符串。
    new_str = re.findall(r'http.*\.com',str_all)
    print(f'匹配以 http 开头的字符串：{new_str}')
    # 匹配以 .com 结尾的字符串（如 baidu.com）。
    new_str = re.findall(r'\S.*\.com',str_all)
    print(f'匹配以 .com 结尾的字符串：{new_str}')
    # 匹配空白字符（空格 / 制表符）。
    new_str = re.findall(r'\s+*',str_all)
    print(f'匹配空白字符：{new_str}')
    # 匹配非数字的任意字符。
    new_str = re.findall(r'\D+',str_all)
    print(f'匹配非数字的任意字符：{new_str}')
    # 匹配 ab 出现 1 次及以上的字符串（如 ab、abab、aabbb 不匹配）。
    new_str = re.findall(r'(ab)+',str_all)
    print(f'匹配 ab 出现 1 次及以上的字符串：{new_str}')
'''
'''
    答案：
    正则：^\d+$
    解析：^ 开头，\d+ 至少 1 个数字，$ 结尾，确保整串都是数字。
    正则：^[A-Za-z]+$
    解析：[A-Za-z] 大小写字母，+ 至少 1 位。
    正则：^\d{11}$
    解析：精准匹配 11 位数字。
    正则：^\d{3,6}$
    解析：数字长度 3 到 6 位。
    正则：\w*_\w*
    解析：\w 字母 / 数字 / 下划线，中间必须包含 _。
    正则：^http
    解析：匹配以 http 开头的内容。
    正则：\.com$
    解析：. 是正则元字符，需要 \ 转义，匹配结尾为 .com。
    正则：\s
    解析：内置符号，匹配所有空白符。
    正则：\D
    解析：\d 取反，匹配非数字。
    正则：(ab)+
    解析：分组 (ab)，+ 表示该分组重复 1 次及以上。
    '''

#进阶练习题
# 匹配简单用户名：4~16 位，只能由字母、数字、下划线组成，不能以数字开头。

# 匹配邮箱（简易版）：格式 xxx@xxx.xx，@ 前后至少有 1 个字符，后缀 2~4 位。
# 匹配身份证号（简易 18 位）：18 位纯数字，最后一位可以是数字或大写 X。
# 匹配固定格式日期 yyyy-MM-dd（如 2025-12-01）。
# 匹配整数（包含正整数、负整数，如 123、-456，不匹配小数）。
# 匹配 IP 地址（简易版，四段数字，用 . 分隔，如 192.168.1.1）。


#实战场景
# 提取字符串中所有数字，示例文本：订单号：20260526，金额：99.9 元。
# MySQL 场景：查询表中 url 字段，匹配所有包含 https 的记录。
# 匹配国内标准手机号（严格版）：以 1 开头，第二位为 3/4/5/6/7/8/9，总共 11 位。
# 过滤文本：匹配所有中文汉字。
