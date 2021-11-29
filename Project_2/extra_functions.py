# Prints the detected color to the console for color sensor debugging
def check_color_sensor():
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