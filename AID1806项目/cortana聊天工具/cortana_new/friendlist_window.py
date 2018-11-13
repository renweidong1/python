
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Form(object):
    def __init__(self):
        super(Ui_Form,self).__init__()
        # self.setupUi()

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(350, 800)
        self.move(0,0)
        icon = QIcon()
        icon.addPixmap(QPixmap("./static/images/logo.png"),QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)


        # 设置背景图片
        palette = QPalette()
        palette.setBrush(Form.backgroundRole(), QBrush(QPixmap('./static/images/friend.jpg')))
        Form.setPalette(palette)
        Form.setAutoFillBackground(True)

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.bt_search = QToolButton(Form)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("./static/images/search.ico"), QIcon.Normal, QIcon.Off)
        self.bt_search.setIcon(icon1)
        self.bt_search.setIconSize(QSize(32, 32))
        self.bt_search.setAutoRaise(True)
        self.bt_search.setObjectName("bt_search")
        self.horizontalLayout.addWidget(self.bt_search)

        self.bt_adduser = QToolButton(Form)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./static/images/adduser.ico"), QIcon.Normal, QIcon.Off)
        self.bt_adduser.setIcon(icon2)
        self.bt_adduser.setIconSize(QSize(32, 32))
        self.bt_adduser.setAutoRaise(True)
        self.bt_adduser.setObjectName("bt_adduser")
        self.horizontalLayout.addWidget(self.bt_adduser)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QTreeWidget(Form)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "联系人"))
        self.bt_search.setToolTip(_translate("Form", "查找联系人"))
        self.bt_search.setWhatsThis(_translate("Form", "查找联系人"))
        self.bt_search.setText(_translate("Form", "..."))
        self.bt_adduser.setToolTip(_translate("Form", "新增好友"))
        self.bt_adduser.setWhatsThis(_translate("Form", "新增好友"))
        self.bt_adduser.setText(_translate("Form", "..."))
        self.treeWidget.setWhatsThis(_translate("Form", "我的好友"))


