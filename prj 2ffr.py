import random

class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Время учиться")
        self.progress += 0.3
        self.gladness -= 5

    def to_sleep(self):
        print("Время одыхать")
        self.gladness += 3
        self.money -= 25

    def to_chill(self):
        print("Время тусовки")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 30

    def to_work(self):
        print("Работать")
        self.money += 45
        self.gladness -= 4
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Подтяни интелект в другом мире овощь")
            self.alive = False
        elif self.gladness <=0:
            print("Депрессия...")
            self.alive = False
        elif self.progress > 5:
            print("Взрыв реактора головного отделла")
            self.alive = False
        elif self.money <- 0:
            print("Эх кушатс хочется")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2 )}")
        print(f"money = {self.money}")

    def live(self, day):
        day = "День" + str(day) + " из " + self.name + "жизни "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Oxido")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)