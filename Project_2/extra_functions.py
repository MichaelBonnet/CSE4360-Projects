from pybricks.parameters import Port, Stop, Color

# Prints the detected color to the console for color sensor debugging
def check_color_sensor(cs):
    while True:
        if cs.color() == Color.BLACK:
            print("BLACK")
        elif cs.color() == Color.BLUE:
            print("BLUE")
        elif cs.color() == Color.GREEN:
            print("GREEN")
        elif cs.color() == Color.YELLOW:
            print("YELLOW")
        elif cs.color() == Color.RED:
            print("RED")
        elif cs.color() == Color.WHITE:
            print("WHITE")
        elif cs.color() == Color.BROWN:
            print("BROWN")
        else:
            print("IMPROPER SENSING")

def check_light_sensor(ls):
    while True:
        print(ls.reflection())
        # elif ls.color() == Color.BLUE:
        #     print("BLUE")
        # elif ls.color() == Color.GREEN:
        #     print("GREEN")
        # elif ls.color() == Color.YELLOW:
        #     print("YELLOW")
        # elif ls.color() == Color.RED:
        #     print("RED")
        # elif ls.color() == Color.WHITE:
        #     print("WHITE")
        # elif ls.color() == Color.BROWN:
        #     print("BROWN")
        # else:
        #     print("IMPROPER SENSING")