# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Xml2Code_qt.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 550)
        MainWindow.setStyleSheet("background-color: rgb(246,245,245);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 421, 551))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab{background-color:#323646;\n"
"            color:white;\n"
"            padding-top:4px;\n"
"            padding-bottom:4px;\n"
"            padding-left:12px;\n"
"            padding-right:12px;\n"
"            margin-right:1px}\n"
"QTabBar::tab::selected{background-color:white;\n"
"                        color:balck;\n"
"                        border-top:2px solid orange;}\n"
"QPushButton#pushButton_gen_1,QPushButton#pushButton_gen_2,QPushButton#pushButton_gen_3{background-color:#323646;\n"
"                        color:white;\n"
"                        border-radius:3px;}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("background-color: rgb(246,245,245);\n"
"")
        self.tab_1.setObjectName("tab_1")
        self.pushButton_src_1 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_src_1.setGeometry(QtCore.QRect(310, 31, 21, 20))
        self.pushButton_src_1.setStyleSheet("image: url(:/newPrefix/timg.jpg);")
        self.pushButton_src_1.setText("")
        self.pushButton_src_1.setObjectName("pushButton_src_1")
        self.lineEdit_tar_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_tar_1.setGeometry(QtCore.QRect(80, 70, 220, 20))
        self.lineEdit_tar_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_tar_1.setObjectName("lineEdit_tar_1")
        self.lineEdit_src_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_src_1.setGeometry(QtCore.QRect(80, 30, 220, 20))
        self.lineEdit_src_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_src_1.setClearButtonEnabled(False)
        self.lineEdit_src_1.setObjectName("lineEdit_src_1")
        self.pushButton_tar_1 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_tar_1.setGeometry(QtCore.QRect(310, 70, 21, 21))
        self.pushButton_tar_1.setStyleSheet("image: url(:/newPrefix/timg.jpg);")
        self.pushButton_tar_1.setText("")
        self.pushButton_tar_1.setObjectName("pushButton_tar_1")
        self.label_pkg_1 = QtWidgets.QLabel(self.tab_1)
        self.label_pkg_1.setGeometry(QtCore.QRect(80, 210, 54, 20))
        self.label_pkg_1.setObjectName("label_pkg_1")
        self.lineEdit_pkg_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_pkg_1.setGeometry(QtCore.QRect(130, 210, 211, 20))
        self.lineEdit_pkg_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_pkg_1.setObjectName("lineEdit_pkg_1")
        self.checkBox_std_1 = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_std_1.setGeometry(QtCore.QRect(80, 110, 171, 20))
        self.checkBox_std_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_std_1.setObjectName("checkBox_std_1")
        self.checkBox_dc_1 = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_dc_1.setGeometry(QtCore.QRect(80, 140, 171, 20))
        self.checkBox_dc_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_dc_1.setObjectName("checkBox_dc_1")
        self.checkBox_lv_1 = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_lv_1.setGeometry(QtCore.QRect(80, 170, 171, 20))
        self.checkBox_lv_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_lv_1.setObjectName("checkBox_lv_1")
        self.progressBar_1 = QtWidgets.QProgressBar(self.tab_1)
        self.progressBar_1.setGeometry(QtCore.QRect(80, 250, 261, 23))
        self.progressBar_1.setStyleSheet("QProgressBar{background-color:#F1E1C7;\n"
"            border-radius:4px;\n"
"            text-align:center;}\n"
"QProgressBar::chunk{background-color:#F9A924;}")
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_1.setObjectName("progressBar_1")
        self.pushButton_gen_1 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_gen_1.setGeometry(QtCore.QRect(140, 470, 131, 23))
        self.pushButton_gen_1.setStyleSheet("background-color: rgb(51,55,71);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_gen_1.setObjectName("pushButton_gen_1")
        self.textBrowser_info_1 = QtWidgets.QTextBrowser(self.tab_1)
        self.textBrowser_info_1.setGeometry(QtCore.QRect(80, 290, 261, 151))
        self.textBrowser_info_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_info_1.setObjectName("textBrowser_info_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color: rgb(246,245,245);")
        self.tab_2.setObjectName("tab_2")
        self.pushButton_src_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_src_2.setGeometry(QtCore.QRect(310, 30, 21, 20))
        self.pushButton_src_2.setStyleSheet("image: url(:/newPrefix/timg.jpg);")
        self.pushButton_src_2.setText("")
        self.pushButton_src_2.setObjectName("pushButton_src_2")
        self.pushButton_tar_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_tar_2.setGeometry(QtCore.QRect(310, 70, 21, 20))
        self.pushButton_tar_2.setStyleSheet("image: url(:/newPrefix/timg.jpg);")
        self.pushButton_tar_2.setText("")
        self.pushButton_tar_2.setObjectName("pushButton_tar_2")
        self.lineEdit_tar_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_tar_2.setGeometry(QtCore.QRect(80, 70, 220, 20))
        self.lineEdit_tar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_tar_2.setObjectName("lineEdit_tar_2")
        self.lineEdit_src_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_src_2.setGeometry(QtCore.QRect(80, 30, 220, 20))
        self.lineEdit_src_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_src_2.setClearButtonEnabled(False)
        self.lineEdit_src_2.setObjectName("lineEdit_src_2")
        self.checkBox_std_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_std_2.setGeometry(QtCore.QRect(80, 110, 171, 20))
        self.checkBox_std_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_std_2.setObjectName("checkBox_std_2")
        self.label_pkg_2 = QtWidgets.QLabel(self.tab_2)
        self.label_pkg_2.setGeometry(QtCore.QRect(80, 140, 54, 20))
        self.label_pkg_2.setObjectName("label_pkg_2")
        self.lineEdit_pkg_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_pkg_2.setGeometry(QtCore.QRect(130, 140, 211, 20))
        self.lineEdit_pkg_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_pkg_2.setObjectName("lineEdit_pkg_2")
        self.comboBox_ftype_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_ftype_2.setGeometry(QtCore.QRect(160, 180, 69, 22))
        self.comboBox_ftype_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_ftype_2.setObjectName("comboBox_ftype_2")
        self.comboBox_ftype_2.addItem("")
        self.comboBox_ftype_2.addItem("")
        self.comboBox_ftype_2.addItem("")
        self.label_ftype_2 = QtWidgets.QLabel(self.tab_2)
        self.label_ftype_2.setGeometry(QtCore.QRect(80, 180, 54, 20))
        self.label_ftype_2.setObjectName("label_ftype_2")
        self.pushButton_gen_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_gen_2.setGeometry(QtCore.QRect(140, 470, 131, 23))
        self.pushButton_gen_2.setStyleSheet("background-color: rgb(51,55,71);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_gen_2.setObjectName("pushButton_gen_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(80, 250, 261, 23))
        self.progressBar_2.setStyleSheet("QProgressBar{background-color:#F1E1C7;\n"
"            border-radius:4px;\n"
"            text-align:center;}\n"
"QProgressBar::chunk{background-color:#F9A924;}")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.textBrowser_info_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_info_2.setGeometry(QtCore.QRect(80, 290, 261, 151))
        self.textBrowser_info_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_info_2.setObjectName("textBrowser_info_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("background-color: rgb(246,245,245);")
        self.tab_3.setObjectName("tab_3")
        self.pushButton_src_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_src_3.setGeometry(QtCore.QRect(310, 40, 21, 20))
        self.pushButton_src_3.setStyleSheet("image: url(:/newPrefix/timg.jpg);")
        self.pushButton_src_3.setText("")
        self.pushButton_src_3.setObjectName("pushButton_src_3")
        self.pushButton_tar_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_tar_3.setGeometry(QtCore.QRect(310, 80, 21, 20))
        self.pushButton_tar_3.setStyleSheet("image: url(:/newPrefix/timg.jpg);")
        self.pushButton_tar_3.setText("")
        self.pushButton_tar_3.setObjectName("pushButton_tar_3")
        self.lineEdit_tar_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_tar_3.setGeometry(QtCore.QRect(80, 80, 220, 20))
        self.lineEdit_tar_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_tar_3.setObjectName("lineEdit_tar_3")
        self.lineEdit_src_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_src_3.setGeometry(QtCore.QRect(80, 40, 220, 20))
        self.lineEdit_src_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_src_3.setClearButtonEnabled(False)
        self.lineEdit_src_3.setObjectName("lineEdit_src_3")
        self.label_pkg_3 = QtWidgets.QLabel(self.tab_3)
        self.label_pkg_3.setGeometry(QtCore.QRect(80, 120, 54, 20))
        self.label_pkg_3.setObjectName("label_pkg_3")
        self.lineEdit_pkg_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_pkg_3.setGeometry(QtCore.QRect(140, 120, 201, 20))
        self.lineEdit_pkg_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_pkg_3.setObjectName("lineEdit_pkg_3")
        self.label_llmatch_3 = QtWidgets.QLabel(self.tab_3)
        self.label_llmatch_3.setGeometry(QtCore.QRect(80, 160, 181, 20))
        self.label_llmatch_3.setObjectName("label_llmatch_3")
        self.label_plmatch_3 = QtWidgets.QLabel(self.tab_3)
        self.label_plmatch_3.setGeometry(QtCore.QRect(80, 220, 131, 20))
        self.label_plmatch_3.setObjectName("label_plmatch_3")
        self.label_paset_3 = QtWidgets.QLabel(self.tab_3)
        self.label_paset_3.setGeometry(QtCore.QRect(80, 280, 111, 20))
        self.label_paset_3.setObjectName("label_paset_3")
        self.label_lcset_3 = QtWidgets.QLabel(self.tab_3)
        self.label_lcset_3.setGeometry(QtCore.QRect(80, 400, 151, 20))
        self.label_lcset_3.setObjectName("label_lcset_3")
        self.label_dcset_3 = QtWidgets.QLabel(self.tab_3)
        self.label_dcset_3.setGeometry(QtCore.QRect(80, 340, 101, 20))
        self.label_dcset_3.setObjectName("label_dcset_3")
        self.lineEdit_llmatch_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_llmatch_3.setGeometry(QtCore.QRect(200, 190, 81, 20))
        self.lineEdit_llmatch_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_llmatch_3.setPlaceholderText("")
        self.lineEdit_llmatch_3.setObjectName("lineEdit_llmatch_3")
        self.comboBox_llmatch_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_llmatch_3.setGeometry(QtCore.QRect(110, 190, 61, 20))
        self.comboBox_llmatch_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_llmatch_3.setObjectName("comboBox_llmatch_3")
        self.comboBox_llmatch_3.addItem("")
        self.comboBox_llmatch_3.addItem("")
        self.lineEdit_plmatch_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_plmatch_3.setGeometry(QtCore.QRect(200, 250, 81, 20))
        self.lineEdit_plmatch_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_plmatch_3.setPlaceholderText("")
        self.lineEdit_plmatch_3.setObjectName("lineEdit_plmatch_3")
        self.lineEdit_paset_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_paset_3.setGeometry(QtCore.QRect(200, 310, 81, 20))
        self.lineEdit_paset_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_paset_3.setPlaceholderText("")
        self.lineEdit_paset_3.setObjectName("lineEdit_paset_3")
        self.lineEdit_lcset_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_lcset_3.setGeometry(QtCore.QRect(200, 430, 81, 20))
        self.lineEdit_lcset_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_lcset_3.setPlaceholderText("")
        self.lineEdit_lcset_3.setObjectName("lineEdit_lcset_3")
        self.lineEdit_dcset_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_dcset_3.setGeometry(QtCore.QRect(200, 370, 81, 20))
        self.lineEdit_dcset_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_dcset_3.setPlaceholderText("")
        self.lineEdit_dcset_3.setObjectName("lineEdit_dcset_3")
        self.comboBox_plmatch_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_plmatch_3.setGeometry(QtCore.QRect(110, 250, 61, 20))
        self.comboBox_plmatch_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_plmatch_3.setObjectName("comboBox_plmatch_3")
        self.comboBox_plmatch_3.addItem("")
        self.comboBox_plmatch_3.addItem("")
        self.comboBox_paset_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_paset_3.setGeometry(QtCore.QRect(110, 310, 61, 20))
        self.comboBox_paset_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_paset_3.setObjectName("comboBox_paset_3")
        self.comboBox_paset_3.addItem("")
        self.comboBox_paset_3.addItem("")
        self.comboBox_lcset_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_lcset_3.setGeometry(QtCore.QRect(110, 370, 61, 20))
        self.comboBox_lcset_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_lcset_3.setObjectName("comboBox_lcset_3")
        self.comboBox_lcset_3.addItem("")
        self.comboBox_lcset_3.addItem("")
        self.comboBox_dcset_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_dcset_3.setGeometry(QtCore.QRect(110, 430, 61, 20))
        self.comboBox_dcset_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_dcset_3.setObjectName("comboBox_dcset_3")
        self.comboBox_dcset_3.addItem("")
        self.comboBox_dcset_3.addItem("")
        self.pushButton_gen_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_gen_3.setGeometry(QtCore.QRect(160, 470, 75, 23))
        self.pushButton_gen_3.setStyleSheet("background-color: rgb(51,55,71);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_gen_3.setObjectName("pushButton_gen_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("background-color: rgb(246,245,245);")
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setStyleSheet("background-color: rgb(246,245,245);")
        self.tab_5.setObjectName("tab_5")
        self.label_info1 = QtWidgets.QLabel(self.tab_5)
        self.label_info1.setGeometry(QtCore.QRect(40, 50, 321, 141))
        self.label_info1.setObjectName("label_info1")
        self.label_info2 = QtWidgets.QLabel(self.tab_5)
        self.label_info2.setGeometry(QtCore.QRect(60, 350, 281, 91))
        self.label_info2.setObjectName("label_info2")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_src_1.clicked.connect(MainWindow.btn_src_1)
        self.pushButton_tar_1.clicked.connect(MainWindow.btn_tar_1)
        self.pushButton_gen_1.clicked.connect(MainWindow.btn_gen_1)
        self.pushButton_src_2.clicked.connect(MainWindow.btn_src_2)
        self.pushButton_tar_2.clicked.connect(MainWindow.btn_tar_2)
        self.pushButton_gen_2.clicked.connect(MainWindow.btn_gen_2)
        self.pushButton_src_3.clicked.connect(MainWindow.btn_src_3)
        self.pushButton_tar_3.clicked.connect(MainWindow.btn_tar_3)
        self.pushButton_gen_3.clicked.connect(MainWindow.btn_gen_3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_tar_1.setPlaceholderText(_translate("MainWindow", "生成文件路径"))
        self.lineEdit_src_1.setPlaceholderText(_translate("MainWindow", "目标文件路径"))
        self.label_pkg_1.setText(_translate("MainWindow", "父包名："))
        self.lineEdit_pkg_1.setPlaceholderText(_translate("MainWindow", "请输入包名"))
        self.checkBox_std_1.setText(_translate("MainWindow", "生成标准控件函数         "))
        self.checkBox_dc_1.setText(_translate("MainWindow", "生成数据类(Data)         "))
        self.checkBox_lv_1.setText(_translate("MainWindow", "ListView适配器类生成     "))
        self.pushButton_gen_1.setText(_translate("MainWindow", "开始生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "整体工程生成"))
        self.lineEdit_tar_2.setPlaceholderText(_translate("MainWindow", "生成文件路径"))
        self.lineEdit_src_2.setPlaceholderText(_translate("MainWindow", "目标文件路径"))
        self.checkBox_std_2.setText(_translate("MainWindow", "生成标准控件函数         "))
        self.label_pkg_2.setText(_translate("MainWindow", "包名："))
        self.lineEdit_pkg_2.setPlaceholderText(_translate("MainWindow", "请输入包名"))
        self.comboBox_ftype_2.setItemText(0, _translate("MainWindow", "页面"))
        self.comboBox_ftype_2.setItemText(1, _translate("MainWindow", "控件集合"))
        self.comboBox_ftype_2.setItemText(2, _translate("MainWindow", "适配器"))
        self.label_ftype_2.setText(_translate("MainWindow", "文件类别："))
        self.pushButton_gen_2.setText(_translate("MainWindow", "开始生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "单页生成"))
        self.lineEdit_tar_3.setPlaceholderText(_translate("MainWindow", "生成文件路径"))
        self.lineEdit_src_3.setPlaceholderText(_translate("MainWindow", "目标文件路径"))
        self.label_pkg_3.setText(_translate("MainWindow", "默认包名："))
        self.lineEdit_pkg_3.setPlaceholderText(_translate("MainWindow", "请输入包名"))
        self.label_llmatch_3.setText(_translate("MainWindow", "ListView适配器Layout名称匹配："))
        self.label_plmatch_3.setText(_translate("MainWindow", "页面布局文件名称匹配："))
        self.label_paset_3.setText(_translate("MainWindow", "页面类别名称设置："))
        self.label_lcset_3.setText(_translate("MainWindow", "ListView适配器名称设置："))
        self.label_dcset_3.setText(_translate("MainWindow", "Data类名称设置："))
        self.comboBox_llmatch_3.setItemText(0, _translate("MainWindow", "前缀"))
        self.comboBox_llmatch_3.setItemText(1, _translate("MainWindow", "后缀"))
        self.comboBox_plmatch_3.setItemText(0, _translate("MainWindow", "前缀"))
        self.comboBox_plmatch_3.setItemText(1, _translate("MainWindow", "后缀"))
        self.comboBox_paset_3.setItemText(0, _translate("MainWindow", "前缀"))
        self.comboBox_paset_3.setItemText(1, _translate("MainWindow", "后缀"))
        self.comboBox_lcset_3.setItemText(0, _translate("MainWindow", "前缀"))
        self.comboBox_lcset_3.setItemText(1, _translate("MainWindow", "后缀"))
        self.comboBox_dcset_3.setItemText(0, _translate("MainWindow", "前缀"))
        self.comboBox_dcset_3.setItemText(1, _translate("MainWindow", "后缀"))
        self.pushButton_gen_3.setText(_translate("MainWindow", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "高级设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "帮助"))
        self.label_info1.setText(_translate("MainWindow", "尊敬的客户：\n"
"\n"
"    感谢您的使用！\n"
"    我们一直专注于软件的快速开发和软件工程的快速构建，为程序员而生是我们的目标。\n"
"    希望我们软件对您有帮助，敬请关注我们的更多产品\n"
"\n"
"\n"
"\n"
"                                软件开发工作室"))
        self.label_info2.setText(_translate("MainWindow", "软件名：Polliwog_v-1.0\n"
"版本：V-1.0\n"
"运行平台：Win1dows\n"
"官网：暂无\n"
"邮箱：cwing.gao@gmail.com"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "关于我们"))

import background_rc
