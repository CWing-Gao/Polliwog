# -*-coding:utf-8-*-

import sys,subprocess,time,glob
from os import path
from Xml2Code_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from checker import *

class m_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)       
        self.setWindowTitle("Polliwog_v-1.0")
    def btn_src_1(self):
        path=QFileDialog.getExistingDirectory(self,"choose directory","C:/")
        if path!='':
            self.ui.lineEdit_src_1.setText(path)
    
    def btn_src_2(self):
        path,_ = QFileDialog.getOpenFileName(self,"open file dialog","C:/","xml files(*.xml)")
        if path!='':
            self.ui.lineEdit_src_2.setText(path)
    
    def btn_src_3(self):
        path,_ = QFileDialog.getOpenFileName(self,"open file dialog","C:/","xml files(*.xml)")
        if path!='':
            self.ui.lineEdit_src_3.setText(path)
    
    def btn_tar_1(self):
        path=QFileDialog.getExistingDirectory(self,"choose directory","C:/")
        if path!='':
            self.ui.lineEdit_tar_1.setText(path)
    
    def btn_tar_2(self):
        path=QFileDialog.getExistingDirectory(self,"choose directory","C:/") 
        if path!='':
            self.ui.lineEdit_tar_2.setText(path)
    
    def btn_tar_3(self):
        path=QFileDialog.getExistingDirectory(self,"choose directory","C:/")    
        if path!='':
            self.ui.lineEdit_tar_3.setText(path)
    
    def btn_gen_1(self):
        page=1
        # check source file which is necessary for gennerate code
        msg=check_source()
        if msg:
            self.show_info(msg,page)
            return
        
        global app
        
        # get data from ui input
        src=self.ui.lineEdit_src_1.text()     
        tar=self.ui.lineEdit_tar_1.text()   
        if_gen_stdfunc='true' if self.ui.checkBox_std_2.isChecked() else 'false'       
        pkg_name=self.ui.lineEdit_pkg_1.text()
        
        # check path
        msg=check_project(src,tar)
        if msg:
            self.show_info(msg,page)
            return
        
        # necessary preprocess for data got
        src=path.abspath(src)
        tar=path.abspath(tar)        
        if pkg_name=='':
            pkg_name='null'
            
        # generate xml files' name
        files=glob.glob(src+'/*.xml')
        
        self.show_info('开始生成：',page)
        
        length=len(files)
        for i,file in enumerate(files,start=1):
            
            file_tar_base=(path.basename(file))[:-3]+'java'
            file_tar=path.join(tar,file_tar_base)
            
            # generate code
            command='xml2code.exe "'+file+'" '+pkg_name+' null '+if_gen_stdfunc+' "'+file_tar+'"'
            flag=subprocess.Popen(command, shell=False)
            
            if flag==-1:
                self.ui.textBrowser_info_1.append('error raised when generating codes!')
                self.ui.progressBar_1.setValue(0)
                app.processEvents()
                return
            
            # update process bar
            pss=int(i/length*100)
            self.ui.textBrowser_info_1.append('%d'%(pss)+'% -> '+file_tar_base)
            self.ui.progressBar_1.setValue(pss)
            app.processEvents()
            
        self.append_info('生成完毕!',page)            
            
    
    def btn_gen_2(self):
        page=2
        
        # check source file which is necessary for gennerate code
        msg=check_source()
        if msg:
            self.show_info(msg,page)
            return
                
        global app
        
        # get data from ui input
        src=self.ui.lineEdit_src_2.text()     
        tar=self.ui.lineEdit_tar_2.text()
        if_gen_stdfunc='true' if self.ui.checkBox_std_2.isChecked() else 'false'      
        pkg_name=self.ui.lineEdit_pkg_2.text()
        
        # check path
        msg=check_single(src,tar)
        if msg:
            self.show_info(msg,page)
            return        
        
        # necessary preprocess for data got
        src=path.abspath(src)
        tar=path.abspath(tar)
        if pkg_name=='':
            pkg_name='null'    
        
        # generate xml file's name
        file_tar=path.join(tar,(path.basename(src))[:-3]+'java')  
        
        self.show_info('开始生成：',page)
        
        # generate code
        command='xml2code.exe "'+src+'" '+pkg_name+' null '+if_gen_stdfunc+' "'+file_tar+'"'
        flag=subprocess.Popen(command, shell=True)
            
        if flag==-1:
            self.ui.textBrowser_info_2.append('error raised when generating codes!')
            return
        elif flag==0:
            # update process bar
            for i in range(1,6):
                self.ui.progressBar_2.setValue(20*i)
                time.sleep(0.02)
        self.append_info('生成完毕!',page)   
    
    def btn_gen_3(self):
        pass
    
    def show_info(self,msg,page):
        global app
        if page==1:
            self.ui.textBrowser_info_1.clear
            self.ui.textBrowser_info_1.append(msg)
        else:
            self.ui.textBrowser_info_2.clear
            self.ui.textBrowser_info_2.append(msg)
        app.processEvents()      
        
    def append_info(self,info,page):
        global app
        if page==1:
            self.ui.textBrowser_info_1.append(info)
        else:
            self.ui.textBrowser_info_2.append(info)
        app.processEvents()        
           
app=QApplication(sys.argv)
main_window = m_MainWindow()
main_window.show()
sys.exit(app.exec_())