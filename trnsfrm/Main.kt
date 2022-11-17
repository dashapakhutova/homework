fun main() {
    val f: Movable = Rect(3,2,1,1)
    println(f.move(1,1))
    val f1: Figure = Rect(0,0,2,1)
    print("area = ")
    println(f1.area())
    val f2: Transforming = Circle(1,0,5)
    println(f2.rotate(RotateDirection.Clockwise,0, 0))
    val f3: Transforming = Square(1,0,4)
    println(f3.resize(2))
}
