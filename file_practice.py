# with open ('test.txt', 'w', encoding="utf-8") as file:
#     file.write("hello python")
# with open ('test.txt', 'r', encoding="utf-8") as file:
#     content = file.read()
#     print(content)
import json
bills = [
    {"name": "午饭", "cost": 25.5, "category": "餐饮"},
    {"name": "地铁", "cost": 4, "category": "交通"}
]
with open("bills.json", 'w', encoding="utf-8") as file:
    json.dump(bills, file, ensure_ascii=False, indent=4)
with open("bills.json", 'r', encoding="utf-8") as file:
    bills = json.load(file)
    print(bills)