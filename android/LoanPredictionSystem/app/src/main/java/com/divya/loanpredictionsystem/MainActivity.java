package com.divya.loanpredictionsystem;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.text.InputFilter;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.android.volley.VolleyError;
import org.json.JSONException;
import org.json.JSONObject;
public class MainActivity extends AppCompatActivity
{
    RadioGroup Gender,Married,Education,SelfEmployed;
    EditText ApplicantIncome,LoanAmountTerm,CreditHistory;
    String ApplicantIncomestr,LoanAmountTermstr,CreditHistorystr,gender,married,education,selfemployed;
    TextView res;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Gender=findViewById(R.id.radiogender);
        Married=findViewById(R.id.radiomarried);
        Education=findViewById(R.id.radioeducation);
        SelfEmployed=findViewById(R.id.radioselfemployed);

        ApplicantIncome=findViewById(R.id.editapplincome);
        LoanAmountTerm=findViewById(R.id.editloanamount);
        CreditHistory=findViewById(R.id.editcredithistory);

        res= findViewById(R.id.response);
        ApplicantIncome.setFilters(new InputFilter[]{new MinMaxFilter(this,0.0,41667.0)});
        LoanAmountTerm.setFilters(new InputFilter[]{new MinMaxFilter(this,12.0,480.0)});
        CreditHistory.setFilters(new InputFilter[]{new MinMaxFilter(this,0.0,1.0)});
    }
    public void submitndvalidate(View view)
    {
        ApplicantIncomestr=ApplicantIncome.getText().toString();
        LoanAmountTermstr=LoanAmountTerm.getText().toString();
        CreditHistorystr=CreditHistory.getText().toString();

        int GenderId=Gender.getCheckedRadioButtonId();
        RadioButton Genderradiobtn=findViewById(GenderId);

        int MarriedId=Married.getCheckedRadioButtonId();
        RadioButton Marriedradiobtn=findViewById(MarriedId);

        int EducationId=Education.getCheckedRadioButtonId();
        RadioButton Educationradiobtn=findViewById(EducationId);

        int SelfEmployedId=SelfEmployed.getCheckedRadioButtonId();
        RadioButton SelfEmployedradiobtn=findViewById(SelfEmployedId);

        if(GenderId==-1){
            Toast.makeText(this, "Nothing selected,please choose any of the above in Gender", Toast.LENGTH_SHORT).show();
        }
        else{
            gender=Genderradiobtn.getText().toString();
        }

        if(MarriedId==-1){
            Toast.makeText(this, "Nothing selected,please choose any of the above in Married", Toast.LENGTH_SHORT).show();
        }
        else{
            married=Marriedradiobtn.getText().toString();
        }
        if(EducationId==-1){
            Toast.makeText(this, "Nothing selected,please choose any of the above in Education", Toast.LENGTH_SHORT).show();
        }
        else{
            education=Educationradiobtn.getText().toString();
        }
        if(SelfEmployedId==-1){
            Toast.makeText(this, "Nothing selected,please choose any of the above in Self Employed", Toast.LENGTH_SHORT).show();
        }
        else{
            selfemployed=SelfEmployedradiobtn.getText().toString();
        }

        if(!TextUtils.isEmpty(ApplicantIncomestr)&&(!TextUtils.isEmpty(LoanAmountTermstr)&&(!TextUtils.isEmpty(CreditHistorystr)))) {
            RequestQueue requestQueue = Volley.newRequestQueue(this);
            final String url = "";
            JSONObject postParams = new JSONObject();
            try {
                postParams.put("Gender", gender);
                postParams.put("Married", married);
                postParams.put("Education", education);
                postParams.put("Self_Employed", selfemployed);
                postParams.put("CoapplicantIncome", ApplicantIncomestr);
                postParams.put("Loan_Amount_Term", LoanAmountTermstr);
                postParams.put("Credit_History", CreditHistorystr);
            } catch (JSONException e)
            {
                e.printStackTrace();
            }

            JsonObjectRequest jsonObjectRequest=new JsonObjectRequest(Request.Method.POST, url, postParams, new Response.Listener<JSONObject>() {
                @Override
                public void onResponse(JSONObject response) {
                    Log.i("On Response", "onResponse: " + response.toString());
                    res.setText(response.toString());
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    Log.i("On Error",error.toString());
                    Toast.makeText(MainActivity.this, ""+error.toString(), Toast.LENGTH_SHORT).show();
                }
            });
            requestQueue.add(jsonObjectRequest);

        }
        else
        {
            Toast.makeText(this, "check if all the details are given correct", Toast.LENGTH_SHORT).show();
        }
    }
}