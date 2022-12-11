package com.example.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun onclick(view: View) {
        val intent = Intent(this, GameActivity::class.java)
        val frnum = findViewById<EditText>(R.id.fnum)
        val sndnum = findViewById<EditText>(R.id.snum)

        intent.putExtra("fnum", frnum.text)
        intent.putExtra("snum", sndnum.text)
        startActivity(intent)
    }
}
