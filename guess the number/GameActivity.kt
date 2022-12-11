package com.example.myapplication

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class GameActivity : AppCompatActivity(){
    var fnum: Int = 0
    var snum: Int = 100
    var mean: Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_game)
        val question = findViewById<TextView>(R.id.truenum)

        fnum = intent.getIntExtra("fnum", 0)
        snum = intent.getIntExtra("snum", 100)
        Log.d("mytag", "fnum = " + fnum)
        Log.d("mytag", "snum = " + snum)
        mean = (fnum + snum) / 2
        "Является ли ваше число меньше, чем $mean?".also { question.text = it }

        fun yesorno(view: View) {
            when (view.id) {
                R.id.y -> {
                    snum = mean
                    mean = (fnum + snum) /2
                    question.text = "Является ли ваше число меньше, чем $mean?"
                }
                R.id.no ->{
                    fnum = mean
                    mean = (fnum + snum) /2
                    question.text = "Является ли ваше число меньше, чем $mean?"
                }
            }
            if (snum - 1 == fnum){
                question.text = "Твое число $fnum"
            }
        }


    }
}
