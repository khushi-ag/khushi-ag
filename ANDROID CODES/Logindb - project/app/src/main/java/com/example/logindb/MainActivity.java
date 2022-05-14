package com.example.logindb;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    EditText et1,et2;
    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        et1 = findViewById(R.id.et1); //number edit text
        et2 = findViewById(R.id.et2);
        btn = findViewById(R.id.btn1);
        btn.setOnClickListener(MainActivity.this);
        
    }

    @Override
    public void onClick(View view) {

        if(et1.getText().toString().equals("1234") & (et2.getText().toString().equals("1234")))
        {
            Toast.makeText(this, "Login successfull", Toast.LENGTH_SHORT).show();
            Intent i = new Intent(MainActivity.this,SecondActivity.class);
            i.putExtra("name", "Admin!");
            startActivity(i);

        }
        else{
            Toast.makeText(this, "Invalid Password and Uname", Toast.LENGTH_SHORT).show();
        }

    }
}