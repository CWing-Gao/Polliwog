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

      package cwing;	//工程包

      //基础包含
      import android.os.Handler;
      import android.os.Message;
      import android.support.v7.app.ActionBar;
      import android.support.v7.app.AppCompatActivity;

      //布局控件类包含
      import android.widget.Button;


      public class PageName implements View.OnClickListener, {
          AppCompatActivity parent=null;	//父活动
          MainActivity.MainHandler mainHandler=null;		//核心句柄处理器
         //检测到的所有控件声明,格式：
      //		privat 控件类 控件类名+名字=null;
          private Button buttonName=null;

          //构造方法
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

#### Adapter 
      public class AdapterHomeList extends ArrayAdapter<ContentCourseItem> {

          private int resourceId;
          private AppCompatActivity parent=null;
          private List<ContentCourseItem> list;
          Main.MainHandler mainHandler=null;


          public AdapterHomeList(@NonNull Context context, @LayoutRes int resource, List<ContentCourseItem> objects,Main.MainHandler handler) {
              super(context, resource, objects);
              this.parent=(AppCompatActivity) context;
              Log.d("resourceId", resource + "");
              this.resourceId = resource;
              this.list=objects;
              this.mainHandler=handler;
          }


          @Override
          public View getView(int position, @Nullable final View convertView, @NonNull ViewGroup parent) {
              Log.d("resourceId", resourceId + "");
              View view = LayoutInflater.from(getContext()).inflate(resourceId, parent, false);

              ContentCourseItem content=(ContentCourseItem) getItem(position);

              ImageView image1=(ImageView) view.findViewById(R.id.image_1);
              TextView textName1=(TextView) view.findViewById(R.id.text_name_1);
              TextView textTeacher1=(TextView) view.findViewById(R.id.text_teacher_1);
              TextView textType1=(TextView) view.findViewById(R.id.text_type_1);



              image1.setImageBitmap(content.image_1);
              textName1.setText(content.name_1);
              textTeacher1.setText(content.teacher_1);
              textType1.setText(content.type_1);

              ImageView image2=(ImageView) view.findViewById(R.id.image_2);
              TextView textName2=(TextView) view.findViewById(R.id.text_name_2);
              TextView textTeacher2=(TextView) view.findViewById(R.id.text_teacher_2);
              TextView textType2=(TextView) view.findViewById(R.id.text_type_2);

              image2.setImageBitmap(content.image_2);
              textName2.setText(content.name_2);
              textTeacher2.setText(content.teacher_2);
              textType2.setText(content.type_2);


              LinearLayout linearLayout1=(LinearLayout) view.findViewById(R.id.linear_1);
              LinearLayout linearLayout2=(LinearLayout) view.findViewById(R.id.linear_2);

              linearLayout1.setOnClickListener(new View.OnClickListener() {
                  @Override
                  public void onClick(View view) {
                      Message msg=new Message();
                      msg.what= Msg.ACTION_INTO_COURSE;
                      mainHandler.sendMessage(msg);

                  }
              });

              linearLayout2.setOnClickListener(new View.OnClickListener() {
                  @Override
                  public void onClick(View view) {
                      Message msg=new Message();
                      msg.what= Msg.ACTION_INTO_COURSE;
                      mainHandler.sendMessage(msg);
                  }
              });

              return view;
          }
      }

### identify schedules of widget (You can expand it)



