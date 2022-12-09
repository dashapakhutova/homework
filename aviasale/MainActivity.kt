package com.example.aviasale

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.Spinner
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val spinner = findViewById<Spinner>(R.id.spinner)
        ArrayAdapter.createFromResource(this, R.array.City, R.layout.my_selected_item).also { adapter ->
            adapter.setDropDownViewResource(R.layout.my_dropdown_item)
            spinner.adapter = adapter
        }
    }
}
