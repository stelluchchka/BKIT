from oop import Circle
from oop import Square
from oop import Rectangle
import cowsay

if __name__ == "__main__":

    a = Rectangle.Rectangle(6, 6, 'blue', 'pryamougolnik')
    b = Circle.Circle(6, 'green', 'krug')
    c = Square.Square(6, 'red', 'kvadrat')

    cowsay.trex(str(a)+'\n'+str(b)+'\n'+str(c))
