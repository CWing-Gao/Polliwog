# Polliwog v-1.0
A tool of android demo rapid generation for college student.   
   
**Designer: Xiangyu Gao  
Developer: Shengzhong Tang, Yifan Zhu  
Assistant：Liangyan Mo, Mengjiao He**  
(Email:cwing.gao@gmail.com / 302787376@qq.com)  
*We welcome you to join us，and perfect and Perfect and extend this tool software together.*

  
## Overview   
Polliwog is a set of framework and auxiliary software of rapid developing Android App Demo for college students or other non-professional groups with a certain computer foundation. This auxiliary software need be combined with Android Studio (From Google) software. It can realize the automatic generation from visual interface development to Java code. The automatic generation part is mainly a fixed form of code part, which is most suitable for user-oriented application-oriented App Demo development. Users can adjust automatically generated content , format according to their needs and modify our framework to suit their own development needs.

There is only one set of development framework design at present, and we will provide more design framework and more personalized assistant software to meet more needs of App demo development in the subsequent version update iteration process.

  
  
## Detailed introduction  


### Framework introduction

### Introduction of auxiliary software


## Appendix

### The generation paradigm for Java code  

#### PageClass

'''java   
package cwing;

import android.os.Handler;
import android.os.Message;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;


import android.widget.Button;


public class PageName implements View.OnClickListener, {
    AppCompatActivity parent=null;
    MainActivity.MainHandler mainHandler=null;	

    private Button buttonName=null;
    
public PageGet(AppCompatActivity parent, Handler mainHandler){
        this.parent= parent;
       this.mainHandler=( MainActivity.MainHandler)mainHandler;
    }



    public void setUI() {
        parent.setContentView(R.layout.page_name);
        ActionBar actionBar = parent.getSupportActionBar();
        actionBar.hide();
    }

    public void loadControl() {
        buttonName=(Button) parent.findViewById(R.id.butt_back);
    }



    @Override
    public void onClick(View view) {		//控件专有函数
        Message msg=new Message();
        switch (view.getId()){
            case R.id.butt_back:
                break;
        }

    }

    void memoryClear()
    {
    }

    public void onClose() {
        return false;
    }
}   
'''


