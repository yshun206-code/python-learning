student = dict()
def append_student(data):
    while True:
        name = input("请输入学生姓名：\n")
        if name == ("q"):
            break
        while True:
            try:
                score = int(input("请输入学生成绩：\n"))
                if score > 100 or score < 0:
                    print("成绩必须在0~100之间，请重新输入")
                else:
                    data[name] = score  # 字典在建立key找到value
                    break
            except ValueError:
                print("输入错误，成绩必须是整数！请重新输入")


def show_students(data):
    for name in data:
        print(name + ":", data[name])#使用+是字符串的拼接

def find_student(data):
    want_name = input("请输入要查询的姓名：\n")
    if want_name not in data:
        print("没有找到该学生姓名")
        return
    print(want_name + "的成绩是：", data[want_name])

#找最高分和最高分对应的名字
def find_max(data):
    if len(data) == 0:
        print("当前没有学生数据")
        return
    first_name = next(iter(data))#iter()是一个遍历字典key的工具
    max_score_student = first_name
    max_score = data[first_name]
    for name in data:
        if data[name] > max_score:
            max_score = data[name]
            max_score_student = name
    print("最高分学生：\n", max_score_student)
    print("最高分：\n", max_score)

while True:
    print("===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 显示所有学生")
    print("3. 查询学生")
    print("4. 查看最高分")
    print("0. 退出")

    choice = input("请选择功能：")
    if choice == "1":
        append_student(student)
    elif choice == "0":
        break
    elif choice == "2":
        show_students(student)
    elif choice == "3":
        find_student(student)
    elif choice == "4":
        find_max(student)
    else:
        print("输入错误，请重新选择")
