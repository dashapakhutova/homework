class Square (var x: Int, var y: Int, var width: Int) : Movable, Figure(0)  {

    var color: Int = -1

    lateinit var name: String
    constructor(square: Square) : this(square.x, square.y, square.width)

    override fun move(dx: Int, dy: Int) {
        x += dx
        y += dy
    }

    override fun resize(zoom: Int) {
        width *= zoom
        println("Resize width = $width")
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
        return (width*width).toFloat()
    }

}