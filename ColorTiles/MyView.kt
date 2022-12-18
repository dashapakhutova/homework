package com.example.myapplication
import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.os.Bundle
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.widget.Toast
import java.util.*

class MyView(context: Context?) : View(context){
    val p = Paint();
    val r = Random()
    var layoutWidth = -1; var layoutHeight = -1
    val tiles = Array(4) { BooleanArray(4) { r.nextBoolean() } }
    val padding = 10
    lateinit var tilesRect: Array<Array<Rect>>
    var centerX = 50f
    val rect = Rect(0.1f, 0.1f, 0.1f, 0.1f)
    var centerY = 50f
    var w = 100
    var h = 100
    val num_rect = 16
    var even = false

    fun win(): Boolean {
        var sum = 0
        for (i in tiles) {
            for (j in i) {
                if (j) {
                    sum += 1
                }
            }
        }

        if(sum == 0 || sum == num_rect)
            return true
        return false
    }

    override fun onDraw(canvas: Canvas?) {
        p.setColor(Color.RED);
        canvas?.apply {
            var left = 0
            var top = 0
            var inX = 0
            var inY = 0

            for (i in 0..3) {
                if (i*210+100<centerX && (i+1)*210+100>centerX)
                    inY = i
                if (i*210+100<centerY && (i+1)*210+100>centerY)
                    inX = i
            }

            if (even == true) {
                for (k in 0..3) {
                    tiles[inX][k] = !(tiles[inX][k])
                    tiles[k][inY] = !(tiles[k][inY])
                }
                tiles[inX][inY] = !(tiles[inX][inY])
            }

            left = 100
            top = 100

            if (win()) {
                context.apply {Toast.makeText(context, "Вы победили!", Toast.LENGTH_SHORT).show();}
                for (i in 0..3) {
                    for (j in 0..3) {
                        tiles[i][j]=r.nextBoolean()
                        if (tiles[i][j] == true)
                            p.setColor(Color.YELLOW)
                        else
                            p.setColor(Color.RED)

                        drawRect(left.toFloat(), top.toFloat(), (left + w).toFloat(), (top + h).toFloat(), p)
                        left = left + w + padding
                    }
                    left = 100
                    top = top + w + padding
                }
            }
            else {
                for (i in 0..3) {
                    for (j in 0..3) {
                        if (tiles[i][j] == true)
                            p.setColor(Color.YELLOW)
                        else
                            p.setColor(Color.RED)
                        drawRect(left.toFloat(), top.toFloat(), (left + w).toFloat(), (top + h).toFloat(), p)
                        left = left + w + padding
                    }
                    left = 100
                    top = top + width + padding
                }
            }
        }
    }
    override fun onTouchEvent(event: MotionEvent?): Boolean {
        event?.apply {
            if(event.action == MotionEvent.ACTION_DOWN)
            {
                centerX = x;
                centerY = y
                even=true
            }
            else
                even=false

        }
        invalidate()

        return true
    }
}
