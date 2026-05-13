# 案例7: 给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个
#     字符：
#     'A' : Absent，缺勤
#     'L' : Late，迟到
#     'P' : Present，到场
#     如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),
#     那么这个学生会被奖赏。
#     你需要根据这个学生的出勤纪录判断他是否会被奖赏。
#     示例 1:
#     输入: "PPALLP"
#     输出: True
#     示例 2:
#     输入: "PPALLL"
item = input("请输入学生考勤记录：")
Absent = 0
Late = 0
Present = 0
for x in range(len(item)):
    if item[x] == 'A':
        Absent+=1
    elif item[x] == 'L':
        if  x+1 == len(item):
            if item[x] == 'L':
                Late += 1
        elif item[x+1]=='L':
            Late += 2
        if Late < 2:
            Late = 0           
        Late += 1
    else:
        Present += 0
if Absent > 1 or Late > 1:
    print(False)
else:
    print(True)