package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun isNumInt(s: String): Boolean {
        return try {
            s.toInt()
            true
        } catch (e: NumberFormatException) {
            false
        }
    }

    fun isNumFl(s: String): Boolean {
        return try {
            s.toFloat()
            true
        } catch (e: NumberFormatException) {
            false
        }
    }
    fun onClick(v: View) {
        val etA = findViewById<EditText>(R.id.numA);
        val etB = findViewById<EditText>(R.id.numB);
        val tvSum = findViewById<TextView>(R.id.sum);

        val strA = etA.text.toString();
        val strB = etB.text.toString();

        if (!strA.isNullOrBlank() && !strB.isNullOrBlank()) {
            if(isNumInt(strA) && isNumInt(strB)) {
                val sum = strA.toInt() + strB.toInt();
                val strSum = sum.toString();
                tvSum.text = strSum
            }
            else if(isNumFl(strA) && isNumFl(strB)) {
                val sum = strA.toFloat() + strB.toFloat();
                val strSum = sum.toString();
                tvSum.text = strSum
            }
            else {
                tvSum.text = "is not a number"
            }
        }
        else {
            tvSum.text = "ooppss!";
        }


    }
}