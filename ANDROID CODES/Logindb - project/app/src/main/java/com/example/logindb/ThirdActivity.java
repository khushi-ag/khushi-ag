package com.example.logindb;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class ThirdActivity extends AppCompatActivity {

    Student []arr = {};
    ListView lv1;
    TextView tvmenu;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_third);

        Bundle reci = getIntent().getExtras();
        Toast.makeText(this, "Third Activity.", Toast.LENGTH_SHORT).show();

        lv1 = findViewById(R.id.lv1);
        tvmenu = findViewById(R.id.tvmenu);
        // this will apply context menu into textview
        registerForContextMenu(tvmenu);

        String jdata = "{\n" +
                "\t{\n" +
                "\t\t\"id\":\"Z01\",\n" +
                "\t\t\"name\":{\n" +
                "\t\t\t\"fname\":\"ff\",\n" +
                "\t\t\t\"mname\":\"mm\",\n" +
                "\t\t\t\"lname\":\"ll\"\n" +
                "\t\t},\n" +
                "\t\t\"dob\":{\n" +
                "\t\t\t\"month\":\"may\",\n" +
                "\t\t\t\"date\":\"10\",\n" +
                "\t\t\t\"year\":\"2001\"\n" +
                "\t\t}\n" +
                "\t},\n" +
                "\n" +
                "\t{\n" +
                "\t\t\"id\":\"Z02\",\n" +
                "\t\t\"name\":{\n" +
                "\t\t\t\"fname\":\"ff2\",\n" +
                "\t\t\t\"mname\":\"mm2\",\n" +
                "\t\t\t\"lname\":\"ll2\"\n" +
                "\t\t},\n" +
                "\t\t\"dob\":{\n" +
                "\t\t\t\"month\":\"july\",\n" +
                "\t\t\t\"date\":\"20\",\n" +
                "\t\t\t\"year\":\"2001\"\n" +
                "\t\t}\n" +
                "\t}\n" +
                "}";

        try {
            JSONObject o1 = new JSONObject(jdata);
            arr = new Student[jdata.length()-1];

            for (int i=0; i < o1.length()-1 ; i++)
            {
                JSONObject idObj = o1.getJSONObject(String.valueOf(i));
                Student s1 = new Student();
                s1.setId(idObj.getJSONObject("id").toString());
                
                JSONObject nameObj = o1.getJSONObject("name");
                s1.setFname(nameObj.getJSONObject("fname").toString());
                s1.setMidname(nameObj.getJSONObject("mname").toString());
                s1.setLname(nameObj.getJSONObject("lname").toString());

                JSONObject dobObj = o1.getJSONObject("dob");
                s1.setMonth(dobObj.getJSONObject("month").toString());
                s1.setDt(dobObj.getJSONObject("dt").toString());
                s1.setYr(dobObj.getJSONObject("year").toString());

                arr[i]= s1;
            }

        }
        catch (JSONException e) {
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
//create new xml file in layout.
                LinearLayout ll = (LinearLayout) getLayoutInflater().inflate(R.layout.listviewdisp,null);
                TextView tv1 = ll.findViewById(R.id.tv1);
                TextView tv2 = ll.findViewById(R.id.tv2);
                TextView tv3 = ll.findViewById(R.id.tv3);
                TextView tv4 = ll.findViewById(R.id.tv4);
                TextView tv5 = ll.findViewById(R.id.tv5);
                TextView tv6 = ll.findViewById(R.id.tv6);
                TextView tv7 = ll.findViewById(R.id.tv7);

                tv1.setText(arr[i].getId());
                tv2.setText(arr[i].getFname());
                tv3.setText(arr[i].getMidname());
                tv4.setText(arr[i].getLname());
                tv5.setText(arr[i].getMonth());
                tv6.setText(arr[i].getDt());
                tv7.setText(arr[i].getYr());

                return ll;
            }
        });
    }

//SIMPLE menu code... file in res>menu>mennu.xml

//    @Override
//    public boolean onCreateOptionsMenu(Menu menu) {
//        MenuInflater m = getMenuInflater();
//        m.inflate(R.menu.mennu, menu);
//        return true;
//    }
//
//    @Override
//    public boolean onOptionsItemSelected(MenuItem item) {
//
//        switch (item.getItemId())
//        {
//            case R.id.item1:
//                Toast.makeText(this, "ITEM 1 PRESSED", Toast.LENGTH_SHORT).show();
//                break;
//
//            case R.id.item2:
//                Toast.makeText(this, "ITEM 2 PRESSED", Toast.LENGTH_SHORT).show();
//                break;
//
//            case R.id.item3:
//                Toast.makeText(this, "ITEM 3 PRESSED", Toast.LENGTH_SHORT).show();
//                break;
//
//            case R.id.subitem1:
//                Toast.makeText(this, "SUB- ITEM 1 PRESSED", Toast.LENGTH_SHORT).show();
//                break;
//
//            case R.id.subitem2:
//                Toast.makeText(this, "SUB- ITEM 2 PRESSED", Toast.LENGTH_SHORT).show();
//                break;
//        }
//        return super.onOptionsItemSelected(item);
//    }

//CONTEXT MENU(Long click menu) on txtview- tvmenu...before that use registerForContextMenu(tvmenu);
    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        super.onCreateContextMenu(menu, v, menuInfo);

        MenuInflater m = getMenuInflater();
        m.inflate(R.menu.mennu,menu);
    }
//create a xml file for menu item.
    @Override
    public boolean onContextItemSelected(MenuItem item) {

        switch (item.getItemId())
        {
            case R.id.item1:
 //it will finish the application(current)
                Toast.makeText(this, "ITEM 1 PRESSED", Toast.LENGTH_SHORT).show();
                finish();
                break;

            case R.id.item2:
//                Toast.makeText(this, "ITEM 2 PRESSED", Toast.LENGTH_SHORT).show();
//it will pop-up dialog box
// builder.setMessage(msg).setPositiveButton(msg,listener).setNegativeButton(msg,listener);

                AlertDialog.Builder builder = new AlertDialog.Builder(ThirdActivity.this);
                builder.setMessage("Are you sure??").setPositiveButton("OK", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        Toast.makeText(ThirdActivity.this, "ITEM 2 PRESSED", Toast.LENGTH_SHORT).show();
                    }
                }).setNegativeButton("CANCEL",null);

                AlertDialog alert = builder.create();
                alert.show();

                break;

            case R.id.item3:
                Toast.makeText(this, "ITEM 3 PRESSED", Toast.LENGTH_SHORT).show();
                break;

            case R.id.subitem1:
                Toast.makeText(this, "SUB- ITEM 1 PRESSED", Toast.LENGTH_SHORT).show();
                break;

            case R.id.subitem2:
                Toast.makeText(this, "SUB- ITEM 2 PRESSED", Toast.LENGTH_SHORT).show();
                break;
        }
        return super.onOptionsItemSelected(item);
    }
}











