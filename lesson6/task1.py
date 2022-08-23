import time
from turtle import Turtle

GREEN = "green"

YELLOW = "yellow"

RED = "red"


class Trafficlight:
    __turtle = Turtle()
    __actions = {
        RED: lambda tl: tl.__turn_on_and_wait(tl.__red_light, tl.__color, 1),
        YELLOW: lambda tl: tl.__turn_on_and_wait(tl.__yellow_light, tl.__color, 1),
        GREEN: lambda tl: tl.__turn_on_and_wait(tl.__green_light, tl.__color, 1)
    }

    def __init__(self, panel_color):
        super().__init__()
        self.__prev_color = None
        self.__color = None
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
        if color not in (RED, YELLOW, GREEN):
            raise Exception(f"Некорректный цвет: {color}")
        elif self.__color == RED and color != YELLOW \
                or self.__color == GREEN and color != YELLOW \
                or self.__color == YELLOW and self.__prev_color == GREEN and color != RED \
                or self.__color == YELLOW and self.__prev_color == RED and color != GREEN:
            raise Exception("Некорректная последовательность")
        else:
            self.__prev_color = self.__color
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
    trafficlight.color(RED)
    trafficlight.running()
    trafficlight.color(YELLOW)
    trafficlight.running()
    trafficlight.color(GREEN)
    trafficlight.running()
    trafficlight.color(YELLOW)
    trafficlight.running()
