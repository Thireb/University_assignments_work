package com.example.thirebscalcpart2;


import android.os.Bundle;
import android.text.InputFilter;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_0,btn_Add,btn_Sub,btn_Mul,btn_Div,btn_calc,btn_clear;
    EditText ed1;

    double Value1;
    double Value2;
    double Value3;

    boolean mAddition, mSubtract, mMultiplication, mDivision ;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn_0 = (Button) findViewById(R.id.btn_0);
        btn_1 = (Button) findViewById(R.id.btn_1);
        btn_2 = (Button) findViewById(R.id.btn_2);
        btn_3 = (Button) findViewById(R.id.btn_3);
        btn_4 = (Button) findViewById(R.id.btn_4);
        btn_5 = (Button) findViewById(R.id.btn_5);
        btn_6 = (Button) findViewById(R.id.btn_6);
        btn_7 = (Button) findViewById(R.id.btn_7);
        btn_8 = (Button) findViewById(R.id.btn_8);
        btn_9 = (Button) findViewById(R.id.btn_9);
        btn_Add = (Button) findViewById(R.id.btn_Add);
        btn_Div = (Button) findViewById(R.id.btn_Div);
        btn_Sub = (Button) findViewById(R.id.btn_Sub);
        btn_Mul = (Button) findViewById(R.id.btn_Mul);
        btn_calc = (Button) findViewById(R.id.btn_calc);

        btn_clear = (Button) findViewById(R.id.btn_clear);
        ed1 = (EditText) findViewById(R.id.edText1);

        btn_0.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"0");
                }
            }
        });

        btn_1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"1");
                }
            }
        });

        btn_2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"2");
                }
            }
        });

        btn_3.setOnClickListener(new View.OnClickListener() {
            @Override

            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"3");
                }
            }
        });

        btn_4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"4");
                }
            }
        });

        btn_5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"5");
                }
            }
        });

        btn_6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"6");
                }
            }
        });

        btn_7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"7");
                }
            }
        });

        btn_8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"8");
                }
            }
        });

        btn_9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if (ed1.getText().length()<1 ){
                    ed1.setText(ed1.getText()+"9");
                }
            }
        });


        btn_Add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if (ed1 == null){
                    ed1.setText("");
                }else
                {

                    Value1 = Double.parseDouble(ed1.getText().toString());

                    mAddition = true;
                    ed1.setText(null);
                }

            }
        });

        btn_Sub.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Value1 = Float.parseFloat(ed1.getText() + "");
                mSubtract = true ;
                ed1.setText(null);
            }
        });

        btn_Mul.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Value1 = Float.parseFloat(ed1.getText() + "");
                mMultiplication = true ;
                ed1.setText(null);
            }
        });

        btn_Div.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Value1 = Float.parseFloat(ed1.getText()+"");
                mDivision = true ;
                ed1.setText(null);
            }
        });

        btn_calc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Value2 = Double.parseDouble(ed1.getText().toString());

                if (mAddition == true){
                    Value3 = Value1 + Value2;
                    ed1.setText(Value3 +"");
                    mAddition=false;
                }


                if (mSubtract == true){
                    Value3 = Value1 - Value2;
                    ed1.setText(Value3 +"");
                    mSubtract=false;
                }

                if (mMultiplication == true){
                    Value3 = Value1 * Value2;
                    ed1.setText(Value3 + "");
                    mMultiplication=false;
                }

                if (mDivision == true){
                    Value3 = Value1 / Value2;
                    ed1.setText(Value3+"");
                    mDivision=false;
                }
            }
        });

        btn_clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ed1.setText("");
            }
        });
    }

}
