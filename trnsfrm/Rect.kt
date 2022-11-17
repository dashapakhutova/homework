class Rect(var x: Int, var y: Int, var width: Int, var height: Int) : Movable, Figure(0) {

    var color: Int = -1

    lateinit var name: String
    constructor(rect: Rect) : this(rect.x, rect.y, rect.width, rect.height)

    override fun move(dx: Int, dy: Int) {
        x += dx
        y += dy
        println("Move x = $x and y = $y")
    }

    override fun resize(zoom: Int) {
        width *= zoom
        height *= zoom
        println("Resize width = $width and height = $height")
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
        return (width*height).toFloat()
    }

}