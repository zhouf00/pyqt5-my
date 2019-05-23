import sys
import time
import pyqtgraph as pg
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                             QHBoxLayout, QVBoxLayout,QLabel, QComboBox,QPushButton,
                             QDateEdit, QSpacerItem,QFrame, QSizePolicy, QSplitter,
                             QRadioButton, QGroupBox,QCheckBox,QLineEdit, QAction)
from PyQt5.QtCore import Qt, QDate, QRect
from TmpData import *


class Qt_Test_Frame(QMainWindow):

    Items = []

    def __init__(self):
        #super(Qt_Test_Frame, self).__init__(*args, **kw)
        super().__init__()

        # 初始化界面
        self._initUI()

        self.show()

    def _initUI(self):
        self.setWindowTitle("QT图形界面测试")
        self.resize(800, 600)

        wwg = QWidget()

        # 全局布局
        wlayout = QVBoxLayout()
        h1_wlayout = QHBoxLayout()
        h2_wlayout = QHBoxLayout()
        h3_wlayout = QHBoxLayout()
        v4_wlayout = QVBoxLayout()
        v5_wlayout = QVBoxLayout()

        # 第一层
        self._frist_story(h1_wlayout)

        # 第二层
        self._second_story(h2_wlayout)

        # 第三层 左
        self._third_left(v4_wlayout)

        # 第三层 右
        pass

        self.statusBar().showMessage("abc")
        # 加载
        splt = self._my_line()
        splt2 = self._my_line(False)
        wlayout.addSpacing(10)  # 增加布局间距
        wlayout.addLayout(h1_wlayout)
        wlayout.addSpacing(10)  # 增加布局间距
        wlayout.addLayout(h2_wlayout)
        wlayout.addSpacing(10)  # 增加布局间距
        wlayout.addWidget(splt)
        wlayout.addLayout(h3_wlayout)
        wlayout.addWidget(self.statusBar())
        h3_wlayout.addLayout(v4_wlayout, 0)
        h3_wlayout.addWidget(splt2)
        h3_wlayout.addLayout(v5_wlayout, 2)

        #wlayout.setAlignment(Qt.AlignTop)

        wwg.setLayout(wlayout)
        self.setCentralWidget(wwg)

    def _frist_story(self, h1_wlayout):
        self.h1_combox1 = QComboBox(minimumWidth=100)
        self.h1_combox1.addItems(wind_field)
        self.h1_combox2 = QComboBox(minimumWidth=100)
        self.h1_combox3 = QComboBox(minimumWidth=100)
        self.h1_combox3.addItems(wind_blade)
        self.h1_combox4 = QComboBox(minimumWidth=100)
        self.h1_combox4.addItems(signal_type)

        # 行为测试 暂时无法使用
        h1_cb1_action = QAction("风场选择", self)
        h1_cb1_action.setStatusTip("请选择风场")
        self.h1_combox1.addAction(h1_cb1_action)

        h1_wlayout.addItem(QSpacerItem(20, 20))
        h1_wlayout.addWidget(QLabel("风场"),0)
        h1_wlayout.addWidget(self.h1_combox1,0)
        h1_wlayout.addItem(QSpacerItem(40, 20))
        h1_wlayout.addWidget(QLabel("风机"), 0)
        h1_wlayout.addWidget(self.h1_combox2, 0)
        h1_wlayout.addItem(QSpacerItem(40, 20))
        h1_wlayout.addWidget(QLabel("叶片ID"), 0)
        h1_wlayout.addWidget(self.h1_combox3, 0)
        h1_wlayout.addItem(QSpacerItem(40, 20))
        h1_wlayout.addWidget(QLabel("信号类型"), 0)
        h1_wlayout.addWidget(self.h1_combox4, 0)

        h1_wlayout.setAlignment(Qt.AlignLeft)

    def _second_story(self, h2_wlayout):
        self.h2_date1 = QDateEdit(QDate.currentDate())
        self.h2_date1.setCalendarPopup(True)
        self.h2_date2 = QDateEdit(QDate.currentDate())
        self.h2_date2.setCalendarPopup(True)
        self.h2_button = QPushButton("运行")

        h2_wlayout.addItem(QSpacerItem(20, 20))
        h2_wlayout.addWidget(QLabel("起始"),0)
        h2_wlayout.addWidget(self.h2_date1)
        h2_wlayout.addItem(QSpacerItem(50, 20))
        h2_wlayout.addWidget(QLabel("结束"), 0)
        h2_wlayout.addWidget(self.h2_date2)
        h2_wlayout.addItem(QSpacerItem(70, 20))
        h2_wlayout.addWidget(self.h2_button)

        h2_wlayout.setAlignment(Qt.AlignLeft)

        # 事件绑定
        self.h2_button.clicked.connect(lambda: self._print())

    def _third_left(self,v4_wlayout):
        # 分量布局
        v4_group_imf = QGridLayout()
        vbox1 = QGroupBox("分量值")
        self.radio_1 = QRadioButton("分量1")
        self.radio_2 = QRadioButton("分量2")
        self.radio_3 = QRadioButton("分量3")
        self.radio_4 = QRadioButton("分量4")
        self.radio_5 = QRadioButton("分量5")
        self.radio_6 = QRadioButton("分量6")
        self.radio_7 = QRadioButton("分量7")
        self.radio_8 = QRadioButton("分量8")
        self.radio_9 = QRadioButton("分量9")
        self.radio_1.setChecked(True)
        self.radio_val = self.radio_1.text()

        # 优先级布局
        v4_group_prior = QGridLayout()
        vbox2 = QGroupBox("优先级")
        cb1 = QCheckBox("叶片1")
        cb2 = QCheckBox("叶片2")
        cb3 = QCheckBox("叶片3")
        self.v3_lineEdit = QLineEdit()

        # 时间布局
        v4_group_time = QGridLayout()
        vbox3 = QGroupBox("时间选择")
        self.v4_combox1 = QComboBox(minimumWidth=100)

        # 按键
        v4_button = QPushButton("显示图形")

        # 写入网格格布局
        v4_group_imf.addWidget(self.radio_1, 0, 0)
        v4_group_imf.addWidget(self.radio_2, 0, 1)
        v4_group_imf.addWidget(self.radio_3, 1, 0)
        v4_group_imf.addWidget(self.radio_4, 1, 1)
        v4_group_imf.addWidget(self.radio_5, 2, 0)
        v4_group_imf.addWidget(self.radio_6, 2, 1)
        v4_group_imf.addWidget(self.radio_7, 3, 0)
        v4_group_imf.addWidget(self.radio_8, 3, 1)
        v4_group_imf.addWidget(self.radio_9, 4, 0)

        v4_group_prior.addWidget(cb1, 1, 0)
        v4_group_prior.addWidget(cb2, 2, 0)
        v4_group_prior.addWidget(cb3, 3, 0)
        v4_group_prior.addWidget(QLabel("选择是："),4,0)
        v4_group_prior.addWidget(self.v3_lineEdit, 5, 0)

        v4_group_time.addWidget(self.v4_combox1)

        # 写入左侧布局
        vbox1.setLayout(v4_group_imf)
        vbox2.setLayout(v4_group_prior)
        vbox3.setLayout(v4_group_time)
        v4_wlayout.addWidget(vbox1)
        v4_wlayout.addWidget(vbox2)
        v4_wlayout.addWidget(vbox3, 0)
        v4_wlayout.addWidget(v4_button,1)

        # 事件绑定
        self.radio_1.toggled.connect(lambda: self._changestyle(self.radio_1))
        self.radio_2.toggled.connect(lambda: self._changestyle(self.radio_2))
        self.radio_3.toggled.connect(lambda: self._changestyle(self.radio_3))
        self.radio_4.toggled.connect(lambda: self._changestyle(self.radio_4))
        self.radio_5.toggled.connect(lambda: self._changestyle(self.radio_5))
        self.radio_6.toggled.connect(lambda: self._changestyle(self.radio_6))
        self.radio_7.toggled.connect(lambda: self._changestyle(self.radio_7))
        self.radio_8.toggled.connect(lambda: self._changestyle(self.radio_8))
        self.radio_9.toggled.connect(lambda: self._changestyle(self.radio_9))

        cb1.stateChanged.connect(lambda: self._prior_func(cb1))
        cb2.stateChanged.connect(lambda: self._prior_func(cb2))
        cb3.stateChanged.connect(lambda: self._prior_func(cb3))

        v4_button.clicked.connect(lambda: self._show_func())

    def _my_line(self, var=True):
        # var 为True时，为横线，否则为竖线
        line = QFrame(self)
        line_var = QFrame.HLine
        sp_var = Qt.Horizontal
        if not var:
            line_var = QFrame.VLine
            sp_var = Qt.Vertical
        line.setFrameShape(line_var)
        line.setFrameShadow(QFrame.Sunken)
        splitter = QSplitter(sp_var)
        splitter.addWidget(line)
        return splitter

    def _print(self):
        a = self.h1_combox1.currentText()
        b = self.h1_combox2.currentText()
        c = self.h1_combox3.currentText()
        d = self.h1_combox4.currentText()
        e = self.h2_date1.dateTime().toString("yy-MM-dd")
        f = self.h2_date2.dateTime().toString("yy-MM-dd")
        print(a,b,c,d)
        print(e)
        print(f)
        print(self.radio_val)

    def _changestyle(self, btn):
        if btn.isChecked():
            self.radio_val = btn.text()
        #print("%s"%(time.strftime('<%H:%M:%S>', time.localtime())))

    def _prior_func(self, cb):
        # 复选框内容添加
        if cb.isChecked():
            if cb.text() not in self.Items:
                self.Items.append(cb.text())
            shop_cart= ",".join(self.Items)
            self.v3_lineEdit.setText(shop_cart)
        else:
            if cb.text() in self.Items:
                self.Items.remove(cb.text())
            shop_cart = ",".join(self.Items)
            self.v3_lineEdit.setText(shop_cart)

    def _show_func(self):
        print(self.v3_lineEdit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Qt_Test_Frame()
    sys.exit(app.exec_())