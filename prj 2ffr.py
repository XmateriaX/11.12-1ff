import random

class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Время учиться")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("Время одыхать")
        self.gladness += 3

    def to_chill(self):
        print("Время тусовки")
        self.gladness += 5
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

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2 )}")

    def live(self, day):
        day = "День" + str(day) + " из " + self.name + "жизни "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Oxido")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)