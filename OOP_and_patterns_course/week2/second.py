import pygame
import random
import math

SCREEN_DIM = (800, 600)


# Методы для работы с векторами

class Vec2d:
    """Makes interactions with two vectors in 2D"""

    def __sub__(self, vector1, vector2):  # разность двух векторов
        return vector1[0] - vector2[0], vector1[1] - vector2[1]

    def __add__(self, vector1, vector2):  # сумма двух векторов
        return vector1[0] + vector2[0], vector1[1] + vector2[1]

    def __len__(self, vector1):  # длинна вектора
        return math.sqrt(vector1[0] * vector1[0] + vector1[1] * vector1[1])

    def __mul__(self, vector, number):  # умножение вектора на число
        return vector[0] * number, vector[1] * number

    def scal_mul(self, vector1, vector2):  # скалярное умножение векторов
        return vector1[0] * vector1[0] + vector1[1] * vector2[1]

    # создание вектора по началу (x) и концу (y) направленного отрезка
    def create_vector_by_parallelogram_rule(self, vector1, vector2):
        return self.__sub__(vector2, vector1)

    def int_pair(self, vector):
        return tuple((int(vector[0]), int(vector[1])))


class Polyline:
    """Polyline"""
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, point):
        self.points.append(point)

    def add_speed(self, speed):
        self.speeds.append(speed)

    # Персчитывание координат опорных точек
    def set_points(self):
        for p in range(len(self.points)):
            vector = Vec2d()
            self.points[p] = vector.__add__(self.points[p], self.speeds[p])
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (- self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])

    # "Отрисовка" точек

    def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color, (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)


class GetPoints:

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1

        if deg == 0:
            return points[0]

        vector = Vec2d()

        first_component = vector.__mul__(points[deg], alpha)
        second_component = vector.__mul__(self.get_point(points, alpha, deg - 1), (1 - alpha))

        return vector.__add__(first_component, second_component)

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

# Сглаживание ломаной


class Knot(Polyline):

    def add_point_speed_and_recalculate_coord(self, point, speed, steps):
        """
        Each time when we add some point or recalculate them - this function calls get_knot
        """
        polyline.add_point(point)
        polyline.add_speed(speed)
        polyline.set_points()
        res = knot.get_knot(polyline.points, steps)
        return res

    def get_knot(self, points, count):
        if len(points) < 3:
            return []

        res = []
        getpoint = GetPoints()
        vector = Vec2d()

        for i in range(-2, len(points) - 2):
            ptn = []
            calculated_vector1 = vector.__add__(points[i], points[i + 1])
            ptn.append(vector.__mul__(calculated_vector1, 0.5))
            ptn.append(points[i + 1])
            calculated_vector2 = vector.__add__(points[i + 1], points[i + 2])
            ptn.append(vector.__mul__(calculated_vector2, 0.5))

            res.extend(getpoint.get_points(ptn, count))

        return res


class Helper:

    # Отрисовка справки
    def draw_help(self):
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(steps), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# Основная программа
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    show_help = False
    pause = True
    action_bool = False

    polyline = Polyline()
    knot = Knot()
    helper = Helper()

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    polyline.points = []
                    polyline.speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                action_bool = True
                calculated_speed = (random.random() * 2, random.random() * 2)
                action = knot.add_point_speed_and_recalculate_coord(event.pos, calculated_speed, steps)


        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        if action_bool:
            polyline.draw_points(polyline.points)
            polyline.draw_points(action, "line", 3, color)


        if show_help:
            helper.draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
