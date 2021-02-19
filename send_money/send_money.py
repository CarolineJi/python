# 定义发工资模块 send_money，用来增加收入计算
import money

salary = int(input("salary:"))


def send_money():
    print("发工资啦")
    money.saved_money_sum = money.saved_money + salary
