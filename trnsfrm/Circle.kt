class Circle (var x: Int, var y: Int, var r: Int) : Movable, Figure(0)  {
    var color: Int = -1

    lateinit var name: String
    constructor(circle: Circle) : this(circle.x, circle.y, circle.r)


    override fun move(dx: Int, dy: Int) {
        x += dx
        y += dy
        println("Move x = $x and y = $y")
    }

    override fun resize(zoom: Int) {
        r *= zoom
        println("Resize radius = $r")
    }

    override fun rotate(direction: RotateDirection, centerX: Int, centerY: Int) {
        if(centerX==x && centerY==y){
            return
        }
        if(direction==RotateDirection.Clockwise){
            x = y - centerY + centerX.also{ y = -x + centerX + centerY}
        }
        else if(direction==RotateDirection.CounterClockwise){
            x = - y + centerY + centerX.also{ y = x - centerX + centerY}
        }
        println("Rotate x = $x and y = $y")
    }

    override fun area(): Float {
        val p = 3.14;
        return (p*r*r).toFloat()
    }
}

