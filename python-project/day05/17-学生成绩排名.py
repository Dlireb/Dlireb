# 案例18:学生成绩管理系统
# # 学生成绩数据（列表包含字典）
# students = [
#     {"id": 1, "name": "张三", "scores": {"语文": 88, "数学": 92, "英语": 79}},
#     {"id": 2, "name": "李四", "scores": {"语文": 95, "数学": 87, "英语": 90}},
#     {"id": 3, "name": "王五", "scores": {"语文": 76, "数学": 88, "英语": 82}}
# ]
# # 1. 计算每个学生的平均分
# # 2. 按平均分排序
# # 3. 输出结果:学生成绩排名
students = [
    {"id": 1, "name": "张三", "scores": {"语文": 88, "数学": 92, "英语": 79}},
    {"id": 2, "name": "李四", "scores": {"语文": 95, "数学": 87, "英语": 90}},
    {"id": 3, "name": "王五", "scores": {"语文": 76, "数学": 88, "英语": 82}}
]
# 1. 计算每个学生的平均分
student_averge = []
for item in students:
    scores = list(item['scores'].values())
    average = round(sum(scores)/len(scores),2)
    student_averge.append({'name':item['name'],'avg':average})
# 2. 按平均分排序
stu_avr = [stu['avg'] for stu in student_averge]
stu_avr.sort(reverse=1)
count = 1 
for avg in stu_avr:
    for stu in student_averge:
        if stu['avg'] == avg:
            print(f"第{count}名是{stu['name']},平均分是{stu['avg']}")




