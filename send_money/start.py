# 定义一个start.py ，启动文件展示最终存款金额
import send_money
import select_money

if __name__ == '__main__':
    send_money.send_money()
    select_money.select_money()
