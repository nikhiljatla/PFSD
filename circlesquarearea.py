from Area.circle import circlearea
from Area.square import squarearea

class Mainclass(circlearea,squarearea):
    def __init__(self):
        super().sarea(int(input("Square:")))
        super().carea(int(input("Circle:")))
    def cm(self):
        print("This Is MainClass")

obj=Mainclass()
for numb in range(1,5):
    if numb==2:
        pass
    else:
        print("Present Number={}".format(numb))