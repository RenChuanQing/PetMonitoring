from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QImage, QPixmap
import cv2
import sys
from PIL import Image
from PyQt5.QtWidgets import *
from aip import AipImageClassify
import win32gui
import win32con
import win32clipboard
import os
import threading
import time
from login import *
import json
import win32api


"""def test(self):
    path = './photo'  # 输入文件夹地址
    files = os.listdir(path)  # 读入文件夹
    num_png = len(files)  # 统计文件夹中的文件个数
    # 输出所有文件名
    print("所有文件名:")
    for file in files:
        print(file)
        self.lineEdit.append(file)
        if (type in self.Picture(file)):
            self.sendmsg(name, "警告有宠物闯入")
            break"""

# 主界面
class Ui_MainWindow(QtWidgets.QMainWindow):
    global type, bool, t1, name, path
    name = '乐乐'
    bool = 1
    type = '女孩'
    path = os.path.join(os.getcwd(),"photo").replace("\\","/")
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.buttondeclick()

    # 主界面布局
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(900, 600)
        Dialog.setMinimumSize(QtCore.QSize(900, 600))
        Dialog.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        Dialog.setFont(font)
        Dialog.setToolTip("")
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(
            "#Dialog{border-image: url(background1.png);}\n"
            "\n"
            "QLabel{border:5px;}\n"
            "QLabel::hover {\n"
            "border:0px;}\n"
            "\n"
            "QMenuBar{border-color:transparent;}\n"
            "QToolButton[objectName=pushButton_doIt]{\n"
            "border:5px;}\n"
            "\n"
            "QScrollBar:vertical{\n"
            "background:transparent;\n"
            "padding:2px;\n"
            "border-radius:4px;\n"
            "max-width:8px;}\n"
            "\n"
            "QScrollBar::handle:vertical{\n"
            "background:#9acd32;\n"
            "min-height:8px;\n"
            "border-radius:4px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical:hover{\n"
            "background:#9eb764;}\n"
            "\n"
            "QScrollBar::handle:vertical:pressed{\n"
            "background:#9eb764;\n"
            "}\n"
            "QScrollBar::add-page:vertical{\n"
            "background:none;\n"
            "}\n"
            "                               \n"
            "QScrollBar::sub-page:vertical{\n"
            "background:none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical{\n"
            "background:none;}\n"
            "                                 \n"
            "QScrollBar::sub-line:vertical{\n"
            "background:none;\n"
            "}\n"
            "QScrollArea{\n"
            "border:0px;\n"
            "}\n"
            "\n"
            "QScrollBar:horizontal{\n"
            "background:transparent;\n"
            "padding:0px;\n"
            "border-radius:4px;\n"
            "max-height:6px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal{\n"
            "background:#9acd32;\n"
            "min-width:8px;\n"
            "border-radius:4px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal:hover{\n"
            "background:#9eb764;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed{\n"
            "background:#9eb764;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:horizontal{\n"
            "background:none;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-page:horizontal{\n"
            "background:none;\n"
            "}\n"
            "QScrollBar::add-line:horizontal{\n"
            "background:none;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:horizontal{\n"
            "background:none;\n"
            "}\n"
            "QToolButton::hover{\n"
            "border:0px;\n"
            "} ")

        Dialog.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.pushButton = QtWidgets.QToolButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton.setPalette(palette)
        # self.pushButton.setStyleSheet("border-image: url(image/1.svg);")
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QToolButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 80, 150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_2.setPalette(palette)
        # self.pushButton_2.setStyleSheet("border-image: url(image/2.svg);")
        self.pushButton_2.setObjectName("pushButton_2")

        # 摄像头1
        width = 610
        height = 275
        background_color = "background-color: rgb(255, 255, 255);"
        self.label_display = QtWidgets.QLabel(Dialog)
        self.label_display.setGeometry(QtCore.QRect(230, 40, width, height))
        self.label_display.setMinimumSize(QtCore.QSize(width, height))
        self.label_display.setMaximumSize(QtCore.QSize(width, height))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_display.setFont(font)
        self.label_display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_display.setStyleSheet(background_color)
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 150, 60, 20))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(550, 150, 60, 20))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label")


        self.lineEdit = QtWidgets.QTextBrowser(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 330, 800, 230))
        self.lineEdit.setStyleSheet("border-image: url(ss/black.jpg);")
        self.lineEdit.setObjectName("lineEdit")


        self.pushButton_3 = QtWidgets.QToolButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 130, 150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_3.setPalette(palette)
        # self.pushButton_3.setStyleSheet("border-image: url(image/4.svg);")
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton_4 = QtWidgets.QToolButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 180, 150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_4.setPalette(palette)
        # self.pushButton_4.setStyleSheet("border-image: url(image/5.svg);")
        self.pushButton_4.setObjectName("pushButton_4")


        self.pushButton_5 = QtWidgets.QToolButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 230, 150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_5.setPalette(palette)
        # self.pushButton_5.setStyleSheet("border-image: url(image/6.svg);")
        self.pushButton_5.setObjectName("pushButton_5")


        self.pushButton_6 = QtWidgets.QToolButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 280, 150, 40))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # 主界面渲染
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "宠物监控系统2.0"))
        self.pushButton.setText(_translate("Dialog", "开启摄像头"))
        self.pushButton_2.setText(_translate("Dialog", "宠物类型"))
        self.label.setText(_translate("Dialog", "监控摄像头"))
        # self.label_2.setText(_translate("Dialog","摄像头2"))
        self.pushButton_3.setText(_translate("Dialog", "选择联系人"))
        self.pushButton_4.setText(_translate("Dialog", "开启实时监控"))
        self.pushButton_5.setText(_translate("Dialog", "分析照片"))
        self.pushButton_6.setText(_translate("Dialog", "测试消息"))

    # 点击事件
    def buttondeclick(self):
        self.pushButton.clicked.connect(self.camera)
        self.pushButton_2.clicked.connect(self.petType)
        self.pushButton_3.clicked.connect(self.contacts)
        self.pushButton_4.clicked.connect(self.realmonitor)
        self.pushButton_5.clicked.connect(self.analysePhoto)
        self.pushButton_6.clicked.connect(lambda:self.sendmsg(name,"验证信息勿回"))

    # 读取图片or文件
    def get_file_content(slef,filePath):
        with open(filePath, 'rb') as fp:
            read = fp.read()
            return read

    # 图像识别
    def Picture(self, image1):
        """ 你的 APPID AK SK """
        """APP_ID = '23390095'
        API_KEY = '0KlDGMvrSTMI7vst9WBWGO7x'
        SECRET_KEY = 'jP3bSbS3yw0XgvbboXHRVD2Q0RX53XvZ'"""
        APP_ID = '24223153'
        API_KEY = 'lTmwiZiMWpZfrY9xaOophnB8'
        SECRET_KEY = 'v86CV91FbY3YLGRVnThQQ3eBm7dYwuAG'
        client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
        # 获取当前文件路径
        current_path = os.path.abspath(__file__)
        # 获取当前文件的父目录
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        image2 = father_path + '/photo/' + image1
        image = self.get_file_content(image2)
        """ 调用通用物体识别 """
        client.advancedGeneral(image)
        """ 如果有可选参数 """
        options = {}
        options["baike_num"] = 5
        """ 带参数调用通用物体识别 """
        lst = client.advancedGeneral(image, options)
        n = lst['result_num']
        result = []
        s = ""
        confidence = ""
        print(lst.values())
        for ab in range(0,n):
            result.append(lst['result'][ab]['keyword'])
            s += lst['result'][ab]['keyword']+"  "
            confidence += str(lst['result'][ab]['score'])+"  "
        print("图中对象包括")
        print(result)
        self.lineEdit.append("图中对象包括"+s)
        self.lineEdit.append("置信度分别为："+confidence)
        # print(lst['result'][0]['keyword'] + '\n' + lst['result'][0]['baike_info']['description'])
        # self.lineEdit.append(lst['result'][0]['keyword'] + '\n' + lst['result'][0]['baike_info']['description'])
        return result

    # 分析照片
    def analysePhoto (self):
        path = './photo'  # 输入文件夹地址
        files = os.listdir(path)  # 读入文件夹
        num_png = len(files)  # 统计文件夹中的文件个数
        # 输出所有文件名
        print("所有文件名:")
        for file in files:
            print(file)
            self.lineEdit.append(file)
            if (type in self.Picture(file)):
                self.sendmsg(name,"警告有宠物闯入")
                break

    # 输入宠物类型
    def petType(self, event):  # 输入：文本
        global type
        # 第三个参数表示显示类型，可选，有正常（QLineEdit.Normal）、密碼（ QLineEdit. Password）、不显示（ QLineEdit. NoEcho）三种情况
        type, ok = QInputDialog.getText(None, "输入宠物类型", "这是提示输入如狗，猫\n\n请输入类型:", QLineEdit.Normal, "")
        print(type)
        self.lineEdit.append('宠物类型：' + type)

    # 输入联系人昵称
    def contacts(self, event):  # 输入：文本
        # 第三个参数表示显示类型，可选，有正常（QLineEdit.Normal）、密碼（ QLineEdit. Password）、不显示（ QLineEdit. NoEcho）三种情况
        value, ok = QInputDialog.getText(None, "输入联系人名称", "这是提示输入QQ昵称\n\n请输入昵称:", QLineEdit.Normal, "")
        global name
        name = value
        self.lineEdit.append('联系人昵称：' + name)

    # 开启摄像头
    def CatchUsbVideo(slef, window_name):
        # cv2.namedWindow(window_name)  # 该方法是写入打开时视频框的名称
        # 捕捉摄像头
        cap = cv2.VideoCapture(0)  # camera_idx 的参数是0代表是打开笔记本的内置摄像头，也可以写上自己录制的视频路径
        while cap.isOpened():  # 判断摄像头是否打开，打开的话就是返回的是True
            ok, frame = cap.read()  # 读取一帧数据，该方法返回两个参数，第一个参数是布尔值，frame就是每一帧的图像，是个三维矩阵，当输入的是一个是视频文件，读完ok==flase
            if not ok:  # 如果读取帧数不是正确的则ok就是Flase则该语句就会执行
                slef.lineEdit.append("摄像头开启失败")
                break
            # 显示图像
            # cv2.imshow(window_name, frame)  # 该方法就是现实该图像
            show = cv2.resize(frame, (400, 270))  # 这里设置尺寸，最好设置和你的label一样，或者偏小几个数值
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 这个要不要都行，相当于重新渲染了一下
            showImage = QImage(show.data, show.shape[1], show.shape[0],
                               QImage.Format_RGB888)  # 这个比较重要，需要创建这个image对象用于承载图像
            slef.label_display.setPixmap(QPixmap.fromImage(showImage))
            c = cv2.waitKey(1)
            if c == 27:
                slef.lineEdit.append("按ESC退出")
                print("esc")
                # 通过esc键退出摄像
                cap.release()
                cv2.destroyAllWindows()
                slef.lineEdit.append("退出摄像头成功")
                break
            if c == ord('s'):  # s退出视频
                cv2.imwrite("image2.jpg", frame)
                cv2.destroyAllWindows()
                slef.lineEdit.append("图片保存成功")
                break
                # 释放摄像头并销毁所有窗口
        cap.release()
        cv2.destroyAllWindows()

        # 开启摄像头监控

    # 开启摄像头槽函数
    def camera(self):
        self.CatchUsbVideo("FaceRect")

    # 开启实时监控槽函数
    def realmonitor(self):
        self.monitoring("FaceRect")

    # 开启实时监控
    def monitoring(slef, window_name):
        global cap,frame
        # cv2.namedWindow(window_name)  # 该方法是写入打开时视频框的名称
        # 捕捉摄像头
        cap = cv2.VideoCapture(0)  # camera_idx 的参数是0代表是打开笔记本的内置摄像头，也可以写上自己录制的视频路径
        # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        t=1
        i=0
        global b
        b = 1
        c = cv2.waitKey(1)
        while cap.isOpened():  # 判断摄像头是否打开，打开的话就是返回的是True
            ok, frame = cap.read()  # 读取一帧数据，该方法返回两个参数，第一个参数是布尔值，frame就是每一帧的图像，是个三维矩阵，当输入的是一个是视频文件，读完ok==flase
            if not ok:  # 如果读取帧数不是正确的则ok就是Flase则该语句就会执行
                slef.lineEdit.append("摄像头开启失败")
                break
            # 显示图像
            # cv2.imshow(window_name, frame)  # 该方法就是现实该图像
            if c == 27:
                # 通过esc键退出摄像
                cv2.destroyAllWindows()
                slef.lineEdit.append("退出摄像头成功")
                break

            if t == 1 and i < 30:#设置拍摄照片
                time.sleep(2)  # 休眠一秒 可通过这个设置拍摄间隔，类似帧。设置间隔时间
                cv2.waitKey(1)
                ige = 'photo/' + str(i) + '.jpg'
                ig = str(i) + '.jpg'
                cv2.imwrite(ige, frame)
                cv2.destroyAllWindows()
                slef.lineEdit.append("图片保存成功"+time.strftime('%Y-%m-%d %H:%M:%S'))
                b = slef.SS(ig)
                i = i + 1
                # slef.heart_beat()
                # 释放摄像头并销毁所有窗口
            # if b == 0:  # 识别后关闭 B==0，不关闭把 break注释了
            #     print("b==0关闭摄像头")
            #     break
        print("跳出循环")
        cap.release()
        cv2.destroyAllWindows()

    # 获取消息信息
    def setText(self,msg):  # 把要发送的消息复制到剪贴板
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, msg)
        win32clipboard.CloseClipboard()

    # 识别到宠物后发送消息
    def SS(self, image):
        a = 1
        if (type in self.Picture(image)):
            self.sendmsg(name, "警告有宠物闯入")
            print("发送成功")
            self.lineEdit.append("消息发送成功")
            a = 0
            return a
        return a

        # 定时器
        def heart_beat(self):
            print("进入定时器")
            ok, frame1 = cap.read()
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            global exec_count
            exec_count += 1  # 15秒后停止定时器
            if exec_count < 4:
                i = str(exec_count)
                ige = 'photo/image' + i + '.jpg'
                cv2.imwrite(ige, frame1)
                cv2.destroyAllWindows()
                self.lineEdit.append("图片保存成功")
                threading.Timer(1, self.heart_beat).start()

    # 获取QQ弹框
    def sendmsg(self, friendName, msg):  # 给好友发送消息
        self.setText(msg)
        hwndQQ = win32gui.FindWindow(None, friendName)  # 找到名字为'王三'的窗口
        print('friendName: '+friendName)
        if hwndQQ == 0:
            print('未找到qq对话框')
            return
        win32gui.SendMessage(hwndQQ, win32con.WM_PASTE, 0, 0)
        win32gui.SendMessage(hwndQQ, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        self.lineEdit.append('发送消息: '+msg)
