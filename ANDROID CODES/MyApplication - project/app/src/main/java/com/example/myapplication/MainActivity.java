package com.example.myapplication;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.content.DialogInterface;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.os.Bundle;
import android.util.Log;
import android.view.ContextMenu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Button b1,b2,b3;
    TextView tv1;
    ListView lv1;
    Student []arr = {};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tv1 = findViewById(R.id.tv1);
        registerForContextMenu(tv1);

        b1 = findViewById(R.id.btn);
        b2 = findViewById(R.id.btn2);
        b3 = findViewById(R.id.btn3);
        lv1 = findViewById(R.id.lv1);
        b1.setOnClickListener(MainActivity.this);
        b2.setOnClickListener(MainActivity.this);
        b3.setOnClickListener(MainActivity.this);

    }

    @Override
    public void onClick(View view) {

//        Intent i = new Intent(MainActivity.this, Sec.class);
//        i.putExtra("name","khushi");
//        startActivity(i);
//
//        Bundle reci = getIntent().getExtras();
//        reci.toString();
        switch(view.getId()) {
            case R.id.btn:
                alert();
                break;

            case R.id.btn2:
                parse();
                break;

            case R.id.btn3:
                db();
                break;
        }
    }

    private void db()
    {
        DBHelper helper = new DBHelper(MainActivity.this,DBHelper.dbname,null,1);
//insert record
//        SQLiteDatabase db = helper.getWritableDatabase();
//        ContentValues val = new ContentValues();
//        val.put("id","v01");
//        val.put("name","qwerty");
//
//        long insertStatus = db.insert("ka",null,val);
//        if(insertStatus != -1)
//        {
//            Toast.makeText(MainActivity.this, "record inserted...", Toast.LENGTH_SHORT).show();
//        }
//        else
//        {
//            Toast.makeText(MainActivity.this, "record not inserted..", Toast.LENGTH_SHORT).show();
//        }
//        db.close();

//select query:
        SQLiteDatabase db = helper.getReadableDatabase();
        String[] col = {"id","name"};
        Cursor record = db.query("ka",col,null,null,null,null,null);

        while(record.moveToNext())
        {
            Log.d("id",record.getString(0));
            Log.d("name",record.getString(1));
        }
//not complusory to store in the stud
//        Stud s1 = new Stud();
//        s1.setId(record.getString(0));
//        s1.setName(record.getString(1));
        db.close();


//update
//        SQLiteDatabase db = helper.getReadableDatabase();
//        ContentValues val = new ContentValues();
//        val.put("name","ytrewq");
//        int updt = db.update("ka",val,null,null);
//        if(updt != -1)
//        {
//            Toast.makeText(MainActivity.this, "updatedd records", Toast.LENGTH_SHORT).show();
//        }
//        else
//        {
//            Toast.makeText(MainActivity.this, "not updated", Toast.LENGTH_SHORT).show();
//        }
//
//        db.close();

// delete

//        SQLiteDatabase db = helper.getReadableDatabase();
//        int d = db.delete("ka",null,null);
//        if(d != -1)
//        {
//            Toast.makeText(MainActivity.this, "record deleted", Toast.LENGTH_SHORT).show();
//        }
//        else
//        {
//            Toast.makeText(MainActivity.this, "record not deleted", Toast.LENGTH_SHORT).show();
//        }
//
//        db.close();

    }

    private void parse() {

        String jsondata = "{\n" +
                "\t{\n" +
                "\t\t\"id\":\"z01\",\n" +
                "\t\t\"name\": \"gff\"\n" +
                "\t},\n" +
                "\t{\n" +
                "\t\t\"id\":\"z02\",\n" +
                "\t\t\"name\": \"hff\"\n" +
                "\t}\n" +
                "}";

        try {
            JSONObject obj = new JSONObject(jsondata);
            Log.d("json data: ",obj.toString());
            arr = new Student[jsondata.length()-1];
            Toast.makeText(this, "parsing...", Toast.LENGTH_SHORT).show();

            //take loop for multi values..
            for(int i =0; i< obj.length()-1; i++)
            {
                Student s1 = new Student();
                JSONObject o1 = new JSONObject(String.valueOf(i));
                Log.d("new object value: ",o1.toString());

                s1.setId(o1.getJSONObject("id").toString());
                s1.setName(o1.getJSONObject("name").toString());

                arr[i] = s1;
            }

        } catch (JSONException e) {
            e.printStackTrace();
        }

        lv1.setAdapter(new BaseAdapter() {
            @Override
            public int getCount() {
                return arr.length;
            }

            @Override
            public Object getItem(int i) {
                return arr[i];
            }

            @Override
            public long getItemId(int i) {
                return 0;
            }

            @Override
            public View getView(int i, View view, ViewGroup viewGroup) {

                LinearLayout ll = (LinearLayout) getLayoutInflater().inflate(R.layout.jsonlist,null);
                TextView tv1 = ll.findViewById(R.id.tv1);
                TextView tv2 = ll.findViewById(R.id.tv2);
                TextView tv3 = ll.findViewById(R.id.tv3);
                TextView tv4 = ll.findViewById(R.id.tv4);

                tv1.setText(arr[i].getId());
                tv2.setText(arr[i].getName());

                return ll;
            }
        });


    }

    private void alert() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setMessage("heyya!!").setPositiveButton("hi", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                Toast.makeText(MainActivity.this, "You know each other...", Toast.LENGTH_SHORT).show();
            }
        }).setNegativeButton("who are you?", null);

        AlertDialog alert = builder.create();
        alert.show();
    }

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        super.onCreateContextMenu(menu, v, menuInfo);

        MenuInflater m = new MenuInflater(MainActivity.this);
        m.inflate(R.menu.menulist,menu);
    }

    @Override
    public boolean onContextItemSelected(@NonNull MenuItem item) {

        switch(item.getItemId())
        {
            case R.id.item1:
                System.exit(0);
        }

        return super.onContextItemSelected(item);
    }
}