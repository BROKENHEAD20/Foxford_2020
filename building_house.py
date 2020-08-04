from graphics import *

win_width = 600
win_height = 500

def main():
    global win, house_elements
    win = GraphWin("Picture", win_width, win_height)
    house_elements = draw_house(win_width//3, win_height*2//3, 150, 200)
    # cursor_point = win.getMouse()
    # win.close()

def draw_house(x0, y0, width, height):
    """
    :param x0: центральная нижняя точка дома
    :param y0: центральная нижняя точка дома
    :param width: ширина
    :param height: высота
    :return: Список нарисованных объектов
    """
    foundation_height = int(height * 0.1)
    walls_height = int(0.5 * height)
    walls_width = int(0.9 * width)
    roof_height = height - walls_height
    window_height = width // 3
    window_width = walls_height // 3

    foundation = draw_foundation(x0,y0, width, foundation_height)
    walls = draw_walls(x0, y0 - foundation_height, walls_width, walls_height)
    house_window = draw_window(x0, y0 - foundation_height - walls_height //3, window_height, window_width)
    roof = draw_roof(x0, y0 - foundation_height -walls_height, width, roof_height)
    return foundation + roof + walls + house_window

def draw_foundation(x0, y0, width, height):
    """
Функция рисует фундамент
    :param x0: Центрльная точка основания
    :param y0: Центральная точка основания
    :param width: Ширина
    :param height: Высота
    :return:
    """
    foundation = Rectangle(Point(x0 - width//2, y0 - height), Point(x0 + width//2, y0))
    foundation.setWidth(3)
    foundation.setFill("Brown")
    foundation.draw(win)
    return[foundation]

def draw_walls(x0, y0, width, height):
    """
Функция рисует стены
    :param x0: Центральная нижняя точка стен
    :param y0: Центральная нижняя точка стен
    :param width: Ширина
    :param height: Высота
    :return:
    """
    walls = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    walls.setWidth(3)
    walls.setFill("gray")
    walls.draw(win)
    return[walls]

def draw_window(x0, y0, width, height):
    """
Функция рисует окно
    :param x0: Центральная нижняя точка окна
    :param y0: Центральная нижняя точка окна
    :param width: Ширина
    :param height: Высота
    :return:
    """
    window = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    window.setWidth(3)
    window.setFill("yellow")
    window.draw(win)
    return[window]

def draw_roof(x0, y0, width, height):
    """
Функция рисует крышу
    :param x0: Центральная нижння точка крыши
    :param y0: Центарльная нижняя точка крыши
    :param width: Ширина
    :param height: Высота
    :return:
    """
    coordinates = [(x0-width//2, y0), (x0, y0-height), (x0+width//2, y0)]
    points = [Point(x, y) for x, y in coordinates]
    roof = Polygon(points)
    roof.setWidth(3)
    roof.setFill("darkred")
    roof.draw(win)
    return[roof]

main()

