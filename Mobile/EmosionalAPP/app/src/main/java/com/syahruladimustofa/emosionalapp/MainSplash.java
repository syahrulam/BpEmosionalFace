package com.syahruladimustofa.emosionalapp;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;

import androidx.appcompat.app.AppCompatActivity;

public class MainSplash extends AppCompatActivity {
    Handler h = new Handler();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_splash);
        h.postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent i = new Intent(MainSplash.this, MainMenu.class);
                startActivity(i);
                finish();
            }
        }, 2000);
    }
}