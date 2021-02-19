"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def talk(self):
        print("叫")

    def run(self):
        print("跑")


class Cat(Animal):
    def __init__(self, name, color, age, gender):
        self.hair = "短毛"
        super().__init__(name, color, age, gender)

    def cat_new_method(self):
        print("捉老鼠")

    def cat_call(self):
        print("喵喵叫")


if __name__ == '__main__':
    cat = Cat("huanghuang", "yellow", 2, "male")
    cat.cat_new_method()
    cat.cat_call()
    cat.run()
    print(cat.hair)
