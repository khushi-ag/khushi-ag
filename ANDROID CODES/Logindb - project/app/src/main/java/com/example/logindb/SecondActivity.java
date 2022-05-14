package com.example.logindb;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextClock;
import android.widget.TextView;
import android.widget.Toast;

public class SecondActivity extends AppCompatActivity implements View.OnClickListener {

    TextView tv1;
    Button btn1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        tv1 = findViewById(R.id.tv1);
        btn1 = findViewById(R.id.btn2);
        btn1.setOnClickListener(SecondActivity.this);

        Bundle reci = getIntent().getExtras();
        String n = reci.getString("name");
        Log.d("reci data: ", reci.toString());
        Toast.makeText(this, "Second Activity", Toast.LENGTH_SHORT).show();
        tv1.setText("WELCOME - "+ n);
    }

    @Override
    public void onClick(View view) {
        Toast.makeText(this, "Allow to PARSE.", Toast.LENGTH_SHORT).show();
        Intent i = new Intent(SecondActivity.this, ThirdActivity.class);
        startActivity(i);
    }
}