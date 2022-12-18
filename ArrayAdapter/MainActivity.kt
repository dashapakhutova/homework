package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import android.widget.EditText
import android.widget.ListView
import java.util.*

class MainActivity : AppCompatActivity() {
    var people = mutableListOf<String>()
    var snPeople = mutableListOf<String>("Pakhutova", "Chumachenko", "Malanova", "Ramazanova")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val lvPeople = findViewById<ListView>(R.id.people_list)
        val adapter = ArrayAdapter<String>(this, R.layout.item, people)
        lvPeople.adapter = adapter
    }

    fun onClickForAdd(view: View) {
        val add_name = findViewById<EditText>(R.id.names)
        val rnd = snPeople.random()
        people.add(add_name.text.toString() + ' ' + rnd)
        val lvPeople = findViewById<ListView>(R.id.people_list)
        val adapter = ArrayAdapter<String>(this, R.layout.item, people)
        lvPeople.adapter = adapter
    }
}
