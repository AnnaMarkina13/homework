import time
from turtle import Turtle


class Trafficlight:
    __turtle = Turtle()
    __actions = {
        "red": lambda tl: tl.__turn_on_and_wait(tl.__red_light, tl.__color, 7),
        "yellow": lambda tl: tl.__turn_on_and_wait(tl.__yellow_light, tl.__color, 2),
        "green": lambda tl: tl.__turn_on_and_wait(tl.__green_light, tl.__color, 7)
    }

    def __init__(self, panel_color):
        super().__init__()
        self.__color = "red"
        self.__init_panel(panel_color)
        self.__red_light = self.__light(40)
        self.__yellow_light = self.__light(0)
        self.__green_light = self.__light(-40)

    def __init_panel(self, color):
        self.__turtle.color(color)
        self.__turtle.pensize(5)
        self.__turtle.hideturtle()
        self.__turtle.penup()
        self.__turtle.setposition(-30, 60)
        self.__turtle.pendown()
        for i in range(2):
            self.__turtle.forward(60)
            self.__turtle.right(90)
            self.__turtle.forward(120)
            self.__turtle.right(90)

    def color(self, color):
        if color not in ("red", "yellow", "green"):
            print(f"Некорректный цвет: {color}")
        else:
            self.__color = color

    def running(self):
        self.__actions[self.__color](self)

    @staticmethod
    def __turn_on_and_wait(light, color, secs):
        light.color(color)
        time.sleep(secs)
        light.color("grey")

    @staticmethod
    def __light(pos_y):
        light = Turtle()
        light.shape("circle")
        light.color("grey")
        light.penup()
        light.setposition(0, pos_y)
        return light


trafficlight = Trafficlight("purple")
while True:
    trafficlight.color("red")
    trafficlight.running()
    trafficlight.color("yellow")
    trafficlight.running()
    trafficlight.color("green")
    trafficlight.running()
    trafficlight.color("yellow")
    trafficlight.running()
