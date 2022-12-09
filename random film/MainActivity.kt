package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.TextView
import org.w3c.dom.Text
import java.util.*

class MainActivity : AppCompatActivity() {
    lateinit var movies: Array<String>;
    var previous_film = emptyArray<Int>();

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        movies = resources.getStringArray(R.array.list_of_films)
        for (i in movies.indices) {
            previous_film += 0
        }
    }

    fun onClickForShow(view: View) {
        val text_view = findViewById<TextView>(R.id.films)
        for (i in movies.indices) {
            if (i == movies.size - 1) {
                text_view.text = "Films are over"
            }
            if (previous_film[Random().nextInt(movies.size)] == 0) {
                text_view.text = movies[Random().nextInt(movies.size)]
                previous_film[Random().nextInt(movies.size)] = 1
                break
            }
        }
    }
    fun onClickForClear(view: View) {
        val text_view = findViewById<TextView>(R.id.films)
        for (i in movies.indices) {
            previous_film[i] = 0
        }
        text_view.text = "Films cleared"
    }


}
