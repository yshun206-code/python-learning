bills = []
def add_bill(data):
    while True:
        name = input("请输入支出的名称")
        if name == "q":
            break
        while True:
            try:
                cost = float(input("请输入支出的金额"))
                if cost <= 0:
                    print("金额必须大于零，请重新输入")
                else:
                    break
            except ValueError:
                print("输入的金额形式错误，只能是数字")
        category = input("请输入支出的种类")
        data.append({"name":name,"cost":cost,"category":category})

def show_bills(data):
    if len(data) == 0:
        print("当前账单为空")
        return
    for bill in data:
        print(bill["name"],bill["cost"],bill["category"])

def find_bills(data):
    while True:
        want_name = input("请输入你要查找的账单支出名称")
        if want_name == "q":
            return
        for bill in data:
            if bill["name"] == want_name:
                print(bill["name"],bill["cost"],bill["category"])
                return
        print("没找到该账单，请重新输入")

def total_bills(data):
    if len(data) == 0:
        print("当前没有账单")
        return
    total = 0
    for bill in data:
        total += bill["cost"]
    print(f"当前总支出为{total}")

def max_bills(data):
    if len(data) == 0:
        print("当前账单为空")
        return
    max_bill = data[0]
    for bill in data:
        if bill["cost"] > max_bill["cost"]:
            max_bill = bill
    print(f"最大一笔支出：{max_bill['name']}")
    print(f"金额{max_bill['cost']}")
    print(f"分类{max_bill['category']}")

while True:
    print("===== 个人账单管理系统 =====")
    print("1. 添加账单")
    print("2. 显示所有账单")
    print("3. 查询账单")
    print("4. 查询账单总花费")
    print("5. 查看花费最高账单")
    print("0. 退出")

    choice = input("请选择功能：")
    if choice == "1":
        add_bill(bills)
    elif choice == "0":
        break
    elif choice == "2":
        show_bills(bills)
    elif choice == "3":
        find_bills(bills)
    elif choice == "4":
        total_bills(bills)
    elif choice == "5":
        max_bills(bills)
    else:
        print("输入错误，请重新选择")