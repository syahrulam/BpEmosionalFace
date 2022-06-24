package com.syahruladimustofa.emosionalapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class MainMenu extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu);
    }
    public void klasifikasii(View view) {
        Intent intent = new Intent(MainMenu.this,MainActivity.class);
        startActivity(intent);
    }
    public void tentangg(View view) {
        Intent intent = new Intent(MainMenu.this,MainTentang.class);
        startActivity(intent);
    }
}