package com.example.expay;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class  SignUp<mAuth> extends AppCompatActivity {
    EditText emailId,password_2;
    Button btn_sign_up;
    private FirebaseAuth mAuth;
    FirebaseDatabase db = FirebaseDatabase.getInstance();
    DatabaseReference ref;
    int Max = 0;

    private Object User;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_up);
        super. onStart(); {
            mAuth = FirebaseAuth.getInstance();
            super.onStart();
            // Check if user is signed in (non-null) and update UI accordingly.
            FirebaseUser currentUser = mAuth.getCurrentUser();
        }

        mAuth = FirebaseAuth.getInstance();
        emailId = findViewById(R.id.email_type_1);
        password_2 = findViewById(R.id.pwd_type_1);
        btn_sign_up = findViewById(R.id.btn_sign_up);


        btn_sign_up.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
              System.out.println(emailId.getText().toString().trim());
                System.out.println(password_2.getText().toString().trim());
                String useremail = emailId.getText().toString().trim();
                String password = password_2.getText().toString().trim();


                mAuth.createUserWithEmailAndPassword(useremail,password)
                        .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                            @Override
                            public void onComplete(@NonNull Task<AuthResult> task) {
                                Intent intent = new Intent(SignUp.this, Reg.class);
                                startActivity(intent);

                            }
                        });


            }

        });


    }
}