import sys
import threading
import time
import resources_rc

from PyQt5           import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui     import * 
from PyQt5.QtCore    import * 


def homefunc(data):
    data.stackedWidget.setCurrentIndex(0)
    while True:
        time.sleep(5)
        data.homeButton.setEnabled(True)
        if data.poop == True:  # Add your desired condition here
            break  # Break out of the loop when the condition is met




class Ui_go6(object):
    def setupUi(self, go6):
        if go6.objectName():
            go6.setObjectName(u"go6")
        go6.resize(1000, 580)
        go6.setMinimumSize(QSize(1000, 580))
        go6.setMaximumSize(QSize(1000, 580))
        go6.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.centralwidget = QWidget(go6)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 160, 581))
        self.frame.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.DiscordIcon = QLabel(self.frame)
        self.DiscordIcon.setObjectName(u"DiscordIcon")
        self.DiscordIcon.setGeometry(QRect(30, 0, 101, 111))
        self.DiscordIcon.setStyleSheet(u"background-image: url(:/newPrefix/assets/discord.png);\n"
"background-color: rgba(0,0,0,0)")
        self.DiscordIcon.setPixmap(QPixmap(u":/newPrefix/assets/discord.png"))
        self.DiscordIcon.setScaledContents(True)
        self.homeButton = QPushButton(self.frame)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setEnabled(True)
        self.homeButton.setGeometry(QRect(10, 120, 86, 33))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon = QIcon()
        icon.addFile(u"assets/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setFlat(False)
        self.guildButton = QPushButton(self.frame)
        self.guildButton.setObjectName(u"guildButton")
        self.guildButton.setEnabled(True)
        self.guildButton.setGeometry(QRect(10, 160, 134, 33))
        self.guildButton.setFont(font)
        self.guildButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assets/log-out (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.guildButton.setIcon(icon1)
        self.guildButton.setFlat(False)
        self.msgButton = QPushButton(self.frame)
        self.msgButton.setObjectName(u"msgButton")
        self.msgButton.setEnabled(True)
        self.msgButton.setGeometry(QRect(10, 200, 131, 33))
        self.msgButton.setFont(font)
        self.msgButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"assets/message-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.msgButton.setIcon(icon2)
        self.msgButton.setFlat(False)
        self.voiceButton = QPushButton(self.frame)
        self.voiceButton.setObjectName(u"voiceButton")
        self.voiceButton.setEnabled(True)
        self.voiceButton.setGeometry(QRect(10, 240, 140, 33))
        self.voiceButton.setFont(font)
        self.voiceButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"assets/volume-2 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.voiceButton.setIcon(icon3)
        self.voiceButton.setFlat(False)
        self.threadButton = QPushButton(self.frame)
        self.threadButton.setObjectName(u"threadButton")
        self.threadButton.setEnabled(True)
        self.threadButton.setGeometry(QRect(10, 280, 141, 33))
        self.threadButton.setFont(font)
        self.threadButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"assets/cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.threadButton.setIcon(icon4)
        self.threadButton.setFlat(False)
        self.dmButton = QPushButton(self.frame)
        self.dmButton.setObjectName(u"dmButton")
        self.dmButton.setEnabled(True)
        self.dmButton.setGeometry(QRect(10, 320, 124, 33))
        self.dmButton.setFont(font)
        self.dmButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"assets/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dmButton.setIcon(icon5)
        self.dmButton.setFlat(False)
        self.nickButton = QPushButton(self.frame)
        self.nickButton.setObjectName(u"nickButton")
        self.nickButton.setEnabled(True)
        self.nickButton.setGeometry(QRect(10, 360, 131, 33))
        self.nickButton.setFont(font)
        self.nickButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"assets/tag (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nickButton.setIcon(icon6)
        self.nickButton.setFlat(False)
        self.webhookButton = QPushButton(self.frame)
        self.webhookButton.setObjectName(u"webhookButton")
        self.webhookButton.setEnabled(True)
        self.webhookButton.setGeometry(QRect(10, 400, 140, 33))
        self.webhookButton.setFont(font)
        self.webhookButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"assets/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.webhookButton.setIcon(icon7)
        self.webhookButton.setFlat(False)
        self.groupButton = QPushButton(self.frame)
        self.groupButton.setObjectName(u"groupButton")
        self.groupButton.setEnabled(True)
        self.groupButton.setGeometry(QRect(10, 440, 141, 33))
        self.groupButton.setFont(font)
        self.groupButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"assets/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.groupButton.setIcon(icon8)
        self.groupButton.setFlat(False)
        self.aiButton = QPushButton(self.frame)
        self.aiButton.setObjectName(u"aiButton")
        self.aiButton.setEnabled(True)
        self.aiButton.setGeometry(QRect(10, 480, 95, 33))
        self.aiButton.setFont(font)
        self.aiButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"assets/cast.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aiButton.setIcon(icon9)
        self.aiButton.setFlat(False)
        self.utils_infoButton = QPushButton(self.frame)
        self.utils_infoButton.setObjectName(u"utils_infoButton")
        self.utils_infoButton.setEnabled(True)
        self.utils_infoButton.setGeometry(QRect(30, 530, 95, 31))
        self.utils_infoButton.setFont(font)
        self.utils_infoButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #1e2130;\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #9075EF;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"assets/tool (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.utils_infoButton.setIcon(icon10)
        self.utils_infoButton.setFlat(False)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 0, 841, 581))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.loadTokens = QPushButton(self.home_page)
        self.loadTokens.setObjectName(u"loadTokens")
        self.loadTokens.setGeometry(QRect(20, 40, 180, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.loadTokens.setFont(font1)
        self.loadTokens.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.checkTokens = QPushButton(self.home_page)
        self.checkTokens.setObjectName(u"checkTokens")
        self.checkTokens.setGeometry(QRect(20, 80, 180, 31))
        self.checkTokens.setFont(font1)
        self.checkTokens.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.rmInvTok = QPushButton(self.home_page)
        self.rmInvTok.setObjectName(u"rmInvTok")
        self.rmInvTok.setGeometry(QRect(20, 120, 180, 31))
        self.rmInvTok.setFont(font1)
        self.rmInvTok.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.rmInvProxies = QPushButton(self.home_page)
        self.rmInvProxies.setObjectName(u"rmInvProxies")
        self.rmInvProxies.setGeometry(QRect(635, 120, 180, 31))
        self.rmInvProxies.setFont(font1)
        self.rmInvProxies.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.loadProxies = QPushButton(self.home_page)
        self.loadProxies.setObjectName(u"loadProxies")
        self.loadProxies.setGeometry(QRect(635, 40, 180, 31))
        self.loadProxies.setFont(font1)
        self.loadProxies.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.checkProxies = QPushButton(self.home_page)
        self.checkProxies.setObjectName(u"checkProxies")
        self.checkProxies.setGeometry(QRect(635, 80, 180, 31))
        self.checkProxies.setFont(font1)
        self.checkProxies.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.label_5 = QLabel(self.home_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 20, 211, 71))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0)")
        self.label_6 = QLabel(self.home_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 90, 161, 81))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0)")
        self.label_6.setWordWrap(True)
        self.guildInfoFrame_2 = QFrame(self.home_page)
        self.guildInfoFrame_2.setObjectName(u"guildInfoFrame_2")
        self.guildInfoFrame_2.setGeometry(QRect(40, 250, 760, 160))
        self.guildInfoFrame_2.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
"border: 1px solid #8677C3;")
        self.guildInfoFrame_2.setFrameShape(QFrame.StyledPanel)
        self.guildInfoFrame_2.setFrameShadow(QFrame.Raised)
        self.bypassMemVer_3 = QCheckBox(self.guildInfoFrame_2)
        self.bypassMemVer_3.setObjectName(u"bypassMemVer_3")
        self.bypassMemVer_3.setGeometry(QRect(10, 10, 91, 17))
        font4 = QFont()
        font4.setPointSize(10)
        self.bypassMemVer_3.setFont(font4)
        self.bypassMemVer_3.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border: 1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.maxTokensSlider = QSlider(self.guildInfoFrame_2)
        self.maxTokensSlider.setObjectName(u"maxTokensSlider")
        self.maxTokensSlider.setGeometry(QRect(10, 53, 691, 22))
        self.maxTokensSlider.setStyleSheet(u"QSlider {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	border: 0px;\n"
"	background-color: #8677C3;\n"
"	radius: 20px;\n"
"	border-radius: 4px;\n"
"}")
        self.maxTokensSlider.setOrientation(Qt.Horizontal)
        self.label_7 = QLabel(self.guildInfoFrame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 30, 141, 21))
        self.label_7.setStyleSheet(u"border: 0px;\n"
"color: #ffffff;")
        self.label_8 = QLabel(self.guildInfoFrame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 97, 141, 21))
        self.label_8.setStyleSheet(u"border: 0px;\n"
"color: #ffffff;")
        self.maxProxiesSlider = QSlider(self.guildInfoFrame_2)
        self.maxProxiesSlider.setObjectName(u"maxProxiesSlider")
        self.maxProxiesSlider.setGeometry(QRect(10, 120, 691, 22))
        self.maxProxiesSlider.setStyleSheet(u"QSlider {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	border: 0px;\n"
"	background-color: #8677C3;\n"
"	radius: 20px;\n"
"	border-radius: 4px;\n"
"}")
        self.maxProxiesSlider.setOrientation(Qt.Horizontal)
        self.label_9 = QLabel(self.home_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 520, 91, 21))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"border: 0px;\n"
"color: #ffffff;\n"
"background-color: rgba(0, 0, 0 ,0)")
        self.label_10 = QLabel(self.home_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(730, 520, 91, 21))
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"border: 0px;\n"
"color: #ffffff;\n"
"background-color: rgba(0, 0, 0 ,0)")
        self.stackedWidget.addWidget(self.home_page)
        self.guildJoin_page = QWidget()
        self.guildJoin_page.setObjectName(u"guildJoin_page")
        self.discInvLineEdit = QLineEdit(self.guildJoin_page)
        self.discInvLineEdit.setObjectName(u"discInvLineEdit")
        self.discInvLineEdit.setGeometry(QRect(20, 50, 411, 31))
        self.discInvLineEdit.setFont(font4)
        self.discInvLineEdit.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.discInvLineEdit.setAlignment(Qt.AlignCenter)
        self.joinButton = QPushButton(self.guildJoin_page)
        self.joinButton.setObjectName(u"joinButton")
        self.joinButton.setGeometry(QRect(440, 50, 125, 31))
        self.joinButton.setFont(font1)
        self.joinButton.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.leaveButton = QPushButton(self.guildJoin_page)
        self.leaveButton.setObjectName(u"leaveButton")
        self.leaveButton.setGeometry(QRect(573, 50, 125, 31))
        self.leaveButton.setFont(font1)
        self.leaveButton.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.doubleSpinBox = QDoubleSpinBox(self.guildJoin_page)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(710, 50, 72, 31))
        self.doubleSpinBox.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.bypassMemVer = QCheckBox(self.guildJoin_page)
        self.bypassMemVer.setObjectName(u"bypassMemVer")
        self.bypassMemVer.setGeometry(QRect(20, 95, 221, 17))
        self.bypassMemVer.setFont(font4)
        self.bypassMemVer.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border: 1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.messageBypass = QPushButton(self.guildJoin_page)
        self.messageBypass.setObjectName(u"messageBypass")
        self.messageBypass.setGeometry(QRect(30, 240, 125, 31))
        font5 = QFont()
        font5.setPointSize(9)
        self.messageBypass.setFont(font5)
        self.messageBypass.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 1px solid #8677C3;\n"
"	border-top-left-radius: 6;\n"
"	border-bottom-left-radius: 6;\n"
"	border-bottom-right-radius: 6;\n"
"	border-top-right-radius: 6;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #8C78F8;\n"
"}")
        self.reactionBypass = QPushButton(self.guildJoin_page)
        self.reactionBypass.setObjectName(u"reactionBypass")
        self.reactionBypass.setGeometry(QRect(155, 240, 125, 31))
        self.reactionBypass.setFont(font5)
        self.reactionBypass.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 1px solid #8677C3;\n"
"	border-top-left-radius: 6;\n"
"	border-bottom-left-radius: 6;\n"
"	border-bottom-right-radius: 6;\n"
"	border-top-right-radius: 6;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #8C78F8;\n"
"}")
        self.buttonBypass = QPushButton(self.guildJoin_page)
        self.buttonBypass.setObjectName(u"buttonBypass")
        self.buttonBypass.setGeometry(QRect(280, 240, 125, 31))
        self.buttonBypass.setFont(font5)
        self.buttonBypass.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 1px solid #8677C3;\n"
"	border-top-left-radius: 6;\n"
"	border-bottom-left-radius: 6;\n"
"	border-bottom-right-radius: 6;\n"
"	border-top-right-radius: 6;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #8C78F8;\n"
"}")
        self.guildInfoFrame = QFrame(self.guildJoin_page)
        self.guildInfoFrame.setObjectName(u"guildInfoFrame")
        self.guildInfoFrame.setGeometry(QRect(30, 270, 760, 160))
        self.guildInfoFrame.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
"border: 1px solid #8677C3;")
        self.guildInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.guildInfoFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.guildInfoFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 20, 221, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #ffffff;\n"
"border: 0px;")
        self.channelID = QLineEdit(self.guildInfoFrame)
        self.channelID.setObjectName(u"channelID")
        self.channelID.setGeometry(QRect(10, 70, 170, 30))
        self.channelID.setFont(font4)
        self.channelID.setStyleSheet(u"color: rgb(101, 98, 99);\n"
"border: 2px solid #8677C3;")
        self.channelID.setAlignment(Qt.AlignCenter)
        self.messageID = QLineEdit(self.guildInfoFrame)
        self.messageID.setObjectName(u"messageID")
        self.messageID.setGeometry(QRect(190, 70, 170, 30))
        self.messageID.setFont(font4)
        self.messageID.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.messageID.setAlignment(Qt.AlignCenter)
        self.emoji = QLineEdit(self.guildInfoFrame)
        self.emoji.setObjectName(u"emoji")
        self.emoji.setGeometry(QRect(370, 70, 170, 30))
        self.emoji.setFont(font4)
        self.emoji.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.emoji.setAlignment(Qt.AlignCenter)
        self.viewReactions = QPushButton(self.guildInfoFrame)
        self.viewReactions.setObjectName(u"viewReactions")
        self.viewReactions.setGeometry(QRect(550, 70, 170, 30))
        self.viewReactions.setFont(font5)
        self.viewReactions.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.stackedWidget.addWidget(self.guildJoin_page)
        self.discInvLineEdit.raise_()
        self.joinButton.raise_()
        self.leaveButton.raise_()
        self.doubleSpinBox.raise_()
        self.bypassMemVer.raise_()
        self.guildInfoFrame.raise_()
        self.messageBypass.raise_()
        self.reactionBypass.raise_()
        self.buttonBypass.raise_()
        self.spam_page = QWidget()
        self.spam_page.setObjectName(u"spam_page")
        self.channelID_spam = QLineEdit(self.spam_page)
        self.channelID_spam.setObjectName(u"channelID_spam")
        self.channelID_spam.setGeometry(QRect(40, 80, 300, 31))
        self.channelID_spam.setFont(font4)
        self.channelID_spam.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.channelID_spam.setAlignment(Qt.AlignCenter)
        self.discInvLineEdit_3 = QLineEdit(self.spam_page)
        self.discInvLineEdit_3.setObjectName(u"discInvLineEdit_3")
        self.discInvLineEdit_3.setGeometry(QRect(350, 80, 300, 31))
        self.discInvLineEdit_3.setFont(font4)
        self.discInvLineEdit_3.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.discInvLineEdit_3.setAlignment(Qt.AlignCenter)
        self.spamButton = QPushButton(self.spam_page)
        self.spamButton.setObjectName(u"spamButton")
        self.spamButton.setGeometry(QRect(660, 80, 140, 31))
        self.spamButton.setFont(font1)
        self.spamButton.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.textEdit_spam = QTextEdit(self.spam_page)
        self.textEdit_spam.setObjectName(u"textEdit_spam")
        self.textEdit_spam.setGeometry(QRect(40, 130, 761, 150))
        self.textEdit_spam.setFont(font5)
        self.textEdit_spam.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.bypassMemVer_2 = QCheckBox(self.spam_page)
        self.bypassMemVer_2.setObjectName(u"bypassMemVer_2")
        self.bypassMemVer_2.setGeometry(QRect(40, 300, 51, 17))
        self.bypassMemVer_2.setFont(font4)
        self.bypassMemVer_2.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.threads_delay = QCheckBox(self.spam_page)
        self.threads_delay.setObjectName(u"threads_delay")
        self.threads_delay.setGeometry(QRect(40, 330, 111, 17))
        self.threads_delay.setFont(font4)
        self.threads_delay.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.jesus_mode = QCheckBox(self.spam_page)
        self.jesus_mode.setObjectName(u"jesus_mode")
        self.jesus_mode.setGeometry(QRect(40, 360, 111, 17))
        self.jesus_mode.setFont(font4)
        self.jesus_mode.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.autoDelete = QCheckBox(self.spam_page)
        self.autoDelete.setObjectName(u"autoDelete")
        self.autoDelete.setGeometry(QRect(190, 300, 111, 17))
        self.autoDelete.setFont(font4)
        self.autoDelete.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.ghostPing = QCheckBox(self.spam_page)
        self.ghostPing.setObjectName(u"ghostPing")
        self.ghostPing.setGeometry(QRect(190, 330, 121, 17))
        self.ghostPing.setFont(font4)
        self.ghostPing.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.multipleMsgs = QCheckBox(self.spam_page)
        self.multipleMsgs.setObjectName(u"multipleMsgs")
        self.multipleMsgs.setGeometry(QRect(190, 360, 111, 17))
        self.multipleMsgs.setFont(font4)
        self.multipleMsgs.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.antiLock = QCheckBox(self.spam_page)
        self.antiLock.setObjectName(u"antiLock")
        self.antiLock.setGeometry(QRect(340, 300, 111, 17))
        self.antiLock.setFont(font4)
        self.antiLock.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.asciiArtTxt = QLineEdit(self.spam_page)
        self.asciiArtTxt.setObjectName(u"asciiArtTxt")
        self.asciiArtTxt.setGeometry(QRect(40, 435, 480, 31))
        self.asciiArtTxt.setFont(font4)
        self.asciiArtTxt.setStyleSheet(u"color: rgb(101, 98, 99);\n"
"border: 2px solid #8677C3;")
        self.asciiArtTxt.setAlignment(Qt.AlignCenter)
        self.insertAscii = QPushButton(self.spam_page)
        self.insertAscii.setObjectName(u"insertAscii")
        self.insertAscii.setGeometry(QRect(530, 435, 270, 31))
        self.insertAscii.setFont(font1)
        self.insertAscii.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.keywordLabel = QLabel(self.spam_page)
        self.keywordLabel.setObjectName(u"keywordLabel")
        self.keywordLabel.setGeometry(QRect(280, 480, 331, 21))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        self.keywordLabel.setFont(font6)
        self.keywordLabel.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.Msg_timeout = QDoubleSpinBox(self.spam_page)
        self.Msg_timeout.setObjectName(u"Msg_timeout")
        self.Msg_timeout.setGeometry(QRect(730, 290, 72, 31))
        self.Msg_timeout.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.label_2 = QLabel(self.spam_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 290, 61, 31))
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.ParseMembers = QPushButton(self.spam_page)
        self.ParseMembers.setObjectName(u"ParseMembers")
        self.ParseMembers.setGeometry(QRect(583, 330, 220, 31))
        self.ParseMembers.setFont(font1)
        self.ParseMembers.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.ParseMembers_2 = QPushButton(self.spam_page)
        self.ParseMembers_2.setObjectName(u"ParseMembers_2")
        self.ParseMembers_2.setGeometry(QRect(40, 390, 760, 31))
        self.ParseMembers_2.setFont(font5)
        self.ParseMembers_2.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.stackedWidget.addWidget(self.spam_page)
        self.voiceSpam_page = QWidget()
        self.voiceSpam_page.setObjectName(u"voiceSpam_page")
        self.guildID = QLineEdit(self.voiceSpam_page)
        self.guildID.setObjectName(u"guildID")
        self.guildID.setGeometry(QRect(120, 80, 300, 31))
        self.guildID.setFont(font4)
        self.guildID.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.guildID.setAlignment(Qt.AlignCenter)
        self.channelID_2 = QLineEdit(self.voiceSpam_page)
        self.channelID_2.setObjectName(u"channelID_2")
        self.channelID_2.setGeometry(QRect(440, 80, 300, 31))
        self.channelID_2.setFont(font4)
        self.channelID_2.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.channelID_2.setAlignment(Qt.AlignCenter)
        self.joinVCButton = QPushButton(self.voiceSpam_page)
        self.joinVCButton.setObjectName(u"joinVCButton")
        self.joinVCButton.setGeometry(QRect(280, 130, 140, 31))
        self.joinVCButton.setFont(font1)
        self.joinVCButton.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.leaveVCButton_2 = QPushButton(self.voiceSpam_page)
        self.leaveVCButton_2.setObjectName(u"leaveVCButton_2")
        self.leaveVCButton_2.setGeometry(QRect(440, 130, 140, 31))
        self.leaveVCButton_2.setFont(font1)
        self.leaveVCButton_2.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.PlayVCButton_3 = QPushButton(self.voiceSpam_page)
        self.PlayVCButton_3.setObjectName(u"PlayVCButton_3")
        self.PlayVCButton_3.setGeometry(QRect(440, 170, 140, 31))
        self.PlayVCButton_3.setFont(font1)
        self.PlayVCButton_3.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.spamJL = QPushButton(self.voiceSpam_page)
        self.spamJL.setObjectName(u"spamJL")
        self.spamJL.setGeometry(QRect(280, 170, 140, 31))
        self.spamJL.setFont(font1)
        self.spamJL.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.startStream = QPushButton(self.voiceSpam_page)
        self.startStream.setObjectName(u"startStream")
        self.startStream.setGeometry(QRect(280, 210, 140, 31))
        self.startStream.setFont(font1)
        self.startStream.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.mutedCheck = QCheckBox(self.voiceSpam_page)
        self.mutedCheck.setObjectName(u"mutedCheck")
        self.mutedCheck.setGeometry(QRect(10, 480, 61, 17))
        self.mutedCheck.setFont(font4)
        self.mutedCheck.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.deathonCheck = QCheckBox(self.voiceSpam_page)
        self.deathonCheck.setObjectName(u"deathonCheck")
        self.deathonCheck.setGeometry(QRect(10, 540, 71, 17))
        self.deathonCheck.setFont(font4)
        self.deathonCheck.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.webcamCheck = QCheckBox(self.voiceSpam_page)
        self.webcamCheck.setObjectName(u"webcamCheck")
        self.webcamCheck.setGeometry(QRect(10, 510, 81, 17))
        self.webcamCheck.setFont(font4)
        self.webcamCheck.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.startWS = QPushButton(self.voiceSpam_page)
        self.startWS.setObjectName(u"startWS")
        self.startWS.setGeometry(QRect(690, 530, 140, 31))
        self.startWS.setFont(font1)
        self.startWS.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.stopStream = QPushButton(self.voiceSpam_page)
        self.stopStream.setObjectName(u"stopStream")
        self.stopStream.setGeometry(QRect(440, 210, 140, 31))
        self.stopStream.setFont(font1)
        self.stopStream.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.stackedWidget.addWidget(self.voiceSpam_page)
        self.threadSpam_page = QWidget()
        self.threadSpam_page.setObjectName(u"threadSpam_page")
        self.keywordLabel_3 = QLabel(self.threadSpam_page)
        self.keywordLabel_3.setObjectName(u"keywordLabel_3")
        self.keywordLabel_3.setGeometry(QRect(280, 480, 331, 21))
        self.keywordLabel_3.setFont(font6)
        self.keywordLabel_3.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.channelID_threadspam = QLineEdit(self.threadSpam_page)
        self.channelID_threadspam.setObjectName(u"channelID_threadspam")
        self.channelID_threadspam.setGeometry(QRect(40, 80, 300, 31))
        self.channelID_threadspam.setFont(font4)
        self.channelID_threadspam.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.channelID_threadspam.setAlignment(Qt.AlignCenter)
        self.insertAscii_2 = QPushButton(self.threadSpam_page)
        self.insertAscii_2.setObjectName(u"insertAscii_2")
        self.insertAscii_2.setGeometry(QRect(530, 435, 270, 31))
        self.insertAscii_2.setFont(font1)
        self.insertAscii_2.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.ghostPing_2 = QCheckBox(self.threadSpam_page)
        self.ghostPing_2.setObjectName(u"ghostPing_2")
        self.ghostPing_2.setGeometry(QRect(190, 330, 121, 17))
        self.ghostPing_2.setFont(font4)
        self.ghostPing_2.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.Msg_timeout_2 = QDoubleSpinBox(self.threadSpam_page)
        self.Msg_timeout_2.setObjectName(u"Msg_timeout_2")
        self.Msg_timeout_2.setGeometry(QRect(730, 290, 72, 31))
        self.Msg_timeout_2.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.bypassMemVer_4 = QCheckBox(self.threadSpam_page)
        self.bypassMemVer_4.setObjectName(u"bypassMemVer_4")
        self.bypassMemVer_4.setGeometry(QRect(40, 300, 51, 17))
        self.bypassMemVer_4.setFont(font4)
        self.bypassMemVer_4.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.autoDelete_2 = QCheckBox(self.threadSpam_page)
        self.autoDelete_2.setObjectName(u"autoDelete_2")
        self.autoDelete_2.setGeometry(QRect(190, 300, 111, 17))
        self.autoDelete_2.setFont(font4)
        self.autoDelete_2.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.TextBox_threadspam = QTextEdit(self.threadSpam_page)
        self.TextBox_threadspam.setObjectName(u"TextBox_threadspam")
        self.TextBox_threadspam.setGeometry(QRect(40, 130, 761, 150))
        self.TextBox_threadspam.setFont(font5)
        self.TextBox_threadspam.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.insertHidePingThreadSpam = QPushButton(self.threadSpam_page)
        self.insertHidePingThreadSpam.setObjectName(u"insertHidePingThreadSpam")
        self.insertHidePingThreadSpam.setGeometry(QRect(40, 390, 760, 31))
        self.insertHidePingThreadSpam.setFont(font5)
        self.insertHidePingThreadSpam.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.ParseMembers_Thread = QPushButton(self.threadSpam_page)
        self.ParseMembers_Thread.setObjectName(u"ParseMembers_Thread")
        self.ParseMembers_Thread.setGeometry(QRect(583, 330, 220, 31))
        self.ParseMembers_Thread.setFont(font1)
        self.ParseMembers_Thread.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.jesus_mode_2 = QCheckBox(self.threadSpam_page)
        self.jesus_mode_2.setObjectName(u"jesus_mode_2")
        self.jesus_mode_2.setGeometry(QRect(40, 360, 111, 17))
        self.jesus_mode_2.setFont(font4)
        self.jesus_mode_2.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.label_3 = QLabel(self.threadSpam_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 290, 61, 31))
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.asciiArtTxt_2 = QLineEdit(self.threadSpam_page)
        self.asciiArtTxt_2.setObjectName(u"asciiArtTxt_2")
        self.asciiArtTxt_2.setGeometry(QRect(40, 435, 480, 31))
        self.asciiArtTxt_2.setFont(font4)
        self.asciiArtTxt_2.setStyleSheet(u"color: rgb(101, 98, 99);\n"
"border: 2px solid #8677C3;")
        self.asciiArtTxt_2.setAlignment(Qt.AlignCenter)
        self.msgRef_threadspam = QLineEdit(self.threadSpam_page)
        self.msgRef_threadspam.setObjectName(u"msgRef_threadspam")
        self.msgRef_threadspam.setGeometry(QRect(350, 80, 300, 31))
        self.msgRef_threadspam.setFont(font4)
        self.msgRef_threadspam.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.msgRef_threadspam.setAlignment(Qt.AlignCenter)
        self.multipleMsgs_2 = QCheckBox(self.threadSpam_page)
        self.multipleMsgs_2.setObjectName(u"multipleMsgs_2")
        self.multipleMsgs_2.setGeometry(QRect(190, 360, 111, 17))
        self.multipleMsgs_2.setFont(font4)
        self.multipleMsgs_2.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.antiLock_2 = QCheckBox(self.threadSpam_page)
        self.antiLock_2.setObjectName(u"antiLock_2")
        self.antiLock_2.setGeometry(QRect(340, 300, 111, 17))
        self.antiLock_2.setFont(font4)
        self.antiLock_2.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.spamButton_threadspam = QPushButton(self.threadSpam_page)
        self.spamButton_threadspam.setObjectName(u"spamButton_threadspam")
        self.spamButton_threadspam.setGeometry(QRect(660, 80, 140, 31))
        self.spamButton_threadspam.setFont(font1)
        self.spamButton_threadspam.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.threads_delay_2 = QCheckBox(self.threadSpam_page)
        self.threads_delay_2.setObjectName(u"threads_delay_2")
        self.threads_delay_2.setGeometry(QRect(40, 330, 111, 17))
        self.threads_delay_2.setFont(font4)
        self.threads_delay_2.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.stackedWidget.addWidget(self.threadSpam_page)
        self.dmSpam_page = QWidget()
        self.dmSpam_page.setObjectName(u"dmSpam_page")
        self.userID = QLineEdit(self.dmSpam_page)
        self.userID.setObjectName(u"userID")
        self.userID.setGeometry(QRect(40, 70, 300, 31))
        self.userID.setFont(font4)
        self.userID.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.userID.setAlignment(Qt.AlignCenter)
        self.msgREf = QLineEdit(self.dmSpam_page)
        self.msgREf.setObjectName(u"msgREf")
        self.msgREf.setGeometry(QRect(350, 70, 300, 31))
        self.msgREf.setFont(font4)
        self.msgREf.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.msgREf.setAlignment(Qt.AlignCenter)
        self.DMspamButton = QPushButton(self.dmSpam_page)
        self.DMspamButton.setObjectName(u"DMspamButton")
        self.DMspamButton.setGeometry(QRect(660, 70, 140, 31))
        self.DMspamButton.setFont(font1)
        self.DMspamButton.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.textEdit_2 = QTextEdit(self.dmSpam_page)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(40, 110, 761, 150))
        self.textEdit_2.setFont(font5)
        self.textEdit_2.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.dm_autoDel = QCheckBox(self.dmSpam_page)
        self.dm_autoDel.setObjectName(u"dm_autoDel")
        self.dm_autoDel.setGeometry(QRect(40, 280, 91, 17))
        self.dm_autoDel.setFont(font4)
        self.dm_autoDel.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.dm_delay = QCheckBox(self.dmSpam_page)
        self.dm_delay.setObjectName(u"dm_delay")
        self.dm_delay.setGeometry(QRect(40, 300, 51, 17))
        self.dm_delay.setFont(font4)
        self.dm_delay.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.dm_autoDel_3 = QCheckBox(self.dmSpam_page)
        self.dm_autoDel_3.setObjectName(u"dm_autoDel_3")
        self.dm_autoDel_3.setGeometry(QRect(140, 300, 121, 17))
        self.dm_autoDel_3.setFont(font4)
        self.dm_autoDel_3.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.dm_multiMsgs = QCheckBox(self.dmSpam_page)
        self.dm_multiMsgs.setObjectName(u"dm_multiMsgs")
        self.dm_multiMsgs.setGeometry(QRect(140, 280, 101, 17))
        self.dm_multiMsgs.setFont(font4)
        self.dm_multiMsgs.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.delFriendReq = QLineEdit(self.dmSpam_page)
        self.delFriendReq.setObjectName(u"delFriendReq")
        self.delFriendReq.setGeometry(QRect(500, 380, 300, 31))
        self.delFriendReq.setFont(font4)
        self.delFriendReq.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.delFriendReq.setAlignment(Qt.AlignCenter)
        self.spamFriendReq_2 = QLineEdit(self.dmSpam_page)
        self.spamFriendReq_2.setObjectName(u"spamFriendReq_2")
        self.spamFriendReq_2.setGeometry(QRect(190, 380, 300, 31))
        self.spamFriendReq_2.setFont(font4)
        self.spamFriendReq_2.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.spamFriendReq_2.setAlignment(Qt.AlignCenter)
        self.insertAscii_dm = QPushButton(self.dmSpam_page)
        self.insertAscii_dm.setObjectName(u"insertAscii_dm")
        self.insertAscii_dm.setGeometry(QRect(530, 485, 270, 31))
        self.insertAscii_dm.setFont(font1)
        self.insertAscii_dm.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.keywordLabel_2 = QLabel(self.dmSpam_page)
        self.keywordLabel_2.setObjectName(u"keywordLabel_2")
        self.keywordLabel_2.setGeometry(QRect(280, 530, 261, 21))
        self.keywordLabel_2.setFont(font6)
        self.keywordLabel_2.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.asciiArtTxt_dm = QLineEdit(self.dmSpam_page)
        self.asciiArtTxt_dm.setObjectName(u"asciiArtTxt_dm")
        self.asciiArtTxt_dm.setGeometry(QRect(40, 485, 480, 31))
        self.asciiArtTxt_dm.setFont(font4)
        self.asciiArtTxt_dm.setStyleSheet(u"color: rgb(101, 98, 99);\n"
"border: 2px solid #8677C3;")
        self.asciiArtTxt_dm.setAlignment(Qt.AlignCenter)
        self.InsertHidePing = QPushButton(self.dmSpam_page)
        self.InsertHidePing.setObjectName(u"InsertHidePing")
        self.InsertHidePing.setGeometry(QRect(40, 440, 760, 31))
        self.InsertHidePing.setFont(font5)
        self.InsertHidePing.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.dm_MsgTimeout = QDoubleSpinBox(self.dmSpam_page)
        self.dm_MsgTimeout.setObjectName(u"dm_MsgTimeout")
        self.dm_MsgTimeout.setGeometry(QRect(730, 280, 72, 31))
        self.dm_MsgTimeout.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.label_4 = QLabel(self.dmSpam_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(660, 280, 61, 31))
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.stackedWidget.addWidget(self.dmSpam_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.msgREf_3 = QLineEdit(self.page_2)
        self.msgREf_3.setObjectName(u"msgREf_3")
        self.msgREf_3.setGeometry(QRect(350, 130, 300, 31))
        self.msgREf_3.setFont(font4)
        self.msgREf_3.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.msgREf_3.setAlignment(Qt.AlignCenter)
        self.nicktxt = QTextEdit(self.page_2)
        self.nicktxt.setObjectName(u"nicktxt")
        self.nicktxt.setGeometry(QRect(40, 170, 761, 150))
        self.nicktxt.setFont(font5)
        self.nicktxt.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.nickspam = QPushButton(self.page_2)
        self.nickspam.setObjectName(u"nickspam")
        self.nickspam.setGeometry(QRect(660, 130, 140, 31))
        self.nickspam.setFont(font1)
        self.nickspam.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.nickname = QLineEdit(self.page_2)
        self.nickname.setObjectName(u"nickname")
        self.nickname.setGeometry(QRect(40, 130, 300, 31))
        self.nickname.setFont(font4)
        self.nickname.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.nickname.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.webhooktxt = QTextEdit(self.page_3)
        self.webhooktxt.setObjectName(u"webhooktxt")
        self.webhooktxt.setGeometry(QRect(40, 170, 761, 150))
        self.webhooktxt.setFont(font5)
        self.webhooktxt.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.webhookSpamStart = QPushButton(self.page_3)
        self.webhookSpamStart.setObjectName(u"webhookSpamStart")
        self.webhookSpamStart.setGeometry(QRect(660, 130, 140, 31))
        self.webhookSpamStart.setFont(font1)
        self.webhookSpamStart.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.webhook2 = QLineEdit(self.page_3)
        self.webhook2.setObjectName(u"webhook2")
        self.webhook2.setGeometry(QRect(350, 130, 300, 31))
        self.webhook2.setFont(font4)
        self.webhook2.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.webhook2.setAlignment(Qt.AlignCenter)
        self.webhook = QLineEdit(self.page_3)
        self.webhook.setObjectName(u"webhook")
        self.webhook.setGeometry(QRect(40, 130, 300, 31))
        self.webhook.setFont(font4)
        self.webhook.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.webhook.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.ghostPing_groupSpam = QCheckBox(self.page_4)
        self.ghostPing_groupSpam.setObjectName(u"ghostPing_groupSpam")
        self.ghostPing_groupSpam.setGeometry(QRect(187, 340, 121, 17))
        self.ghostPing_groupSpam.setFont(font4)
        self.ghostPing_groupSpam.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.antiLock_groupSpam = QCheckBox(self.page_4)
        self.antiLock_groupSpam.setObjectName(u"antiLock_groupSpam")
        self.antiLock_groupSpam.setGeometry(QRect(337, 310, 111, 17))
        self.antiLock_groupSpam.setFont(font4)
        self.antiLock_groupSpam.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.keywordLabel_4 = QLabel(self.page_4)
        self.keywordLabel_4.setObjectName(u"keywordLabel_4")
        self.keywordLabel_4.setGeometry(QRect(277, 490, 331, 21))
        self.keywordLabel_4.setFont(font6)
        self.keywordLabel_4.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.multipleMsgs_groupSpam = QCheckBox(self.page_4)
        self.multipleMsgs_groupSpam.setObjectName(u"multipleMsgs_groupSpam")
        self.multipleMsgs_groupSpam.setGeometry(QRect(187, 370, 111, 17))
        self.multipleMsgs_groupSpam.setFont(font4)
        self.multipleMsgs_groupSpam.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.spamButton__groupSpam = QPushButton(self.page_4)
        self.spamButton__groupSpam.setObjectName(u"spamButton__groupSpam")
        self.spamButton__groupSpam.setGeometry(QRect(657, 90, 140, 31))
        self.spamButton__groupSpam.setFont(font1)
        self.spamButton__groupSpam.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.txt_groupSpam = QTextEdit(self.page_4)
        self.txt_groupSpam.setObjectName(u"txt_groupSpam")
        self.txt_groupSpam.setGeometry(QRect(37, 140, 761, 150))
        self.txt_groupSpam.setFont(font5)
        self.txt_groupSpam.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.autoDelete_groupSpam = QCheckBox(self.page_4)
        self.autoDelete_groupSpam.setObjectName(u"autoDelete_groupSpam")
        self.autoDelete_groupSpam.setGeometry(QRect(187, 310, 111, 17))
        self.autoDelete_groupSpam.setFont(font4)
        self.autoDelete_groupSpam.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.msgRef__groupSpam = QLineEdit(self.page_4)
        self.msgRef__groupSpam.setObjectName(u"msgRef__groupSpam")
        self.msgRef__groupSpam.setGeometry(QRect(347, 90, 300, 31))
        self.msgRef__groupSpam.setFont(font4)
        self.msgRef__groupSpam.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.msgRef__groupSpam.setAlignment(Qt.AlignCenter)
        self.Msg_timeout_groupSpam = QDoubleSpinBox(self.page_4)
        self.Msg_timeout_groupSpam.setObjectName(u"Msg_timeout_groupSpam")
        self.Msg_timeout_groupSpam.setGeometry(QRect(727, 300, 72, 31))
        self.Msg_timeout_groupSpam.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.threads_delay_groupSpam = QCheckBox(self.page_4)
        self.threads_delay_groupSpam.setObjectName(u"threads_delay_groupSpam")
        self.threads_delay_groupSpam.setGeometry(QRect(37, 340, 111, 17))
        self.threads_delay_groupSpam.setFont(font4)
        self.threads_delay_groupSpam.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.ParseMembers_groupSpam = QPushButton(self.page_4)
        self.ParseMembers_groupSpam.setObjectName(u"ParseMembers_groupSpam")
        self.ParseMembers_groupSpam.setGeometry(QRect(580, 340, 220, 31))
        self.ParseMembers_groupSpam.setFont(font1)
        self.ParseMembers_groupSpam.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.insertHidePing_groupSpam = QPushButton(self.page_4)
        self.insertHidePing_groupSpam.setObjectName(u"insertHidePing_groupSpam")
        self.insertHidePing_groupSpam.setGeometry(QRect(37, 400, 760, 31))
        self.insertHidePing_groupSpam.setFont(font5)
        self.insertHidePing_groupSpam.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.jesus_mode_groupSpam = QCheckBox(self.page_4)
        self.jesus_mode_groupSpam.setObjectName(u"jesus_mode_groupSpam")
        self.jesus_mode_groupSpam.setGeometry(QRect(37, 370, 111, 17))
        self.jesus_mode_groupSpam.setFont(font4)
        self.jesus_mode_groupSpam.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.insertAscii__groupSpam = QPushButton(self.page_4)
        self.insertAscii__groupSpam.setObjectName(u"insertAscii__groupSpam")
        self.insertAscii__groupSpam.setGeometry(QRect(527, 445, 270, 31))
        self.insertAscii__groupSpam.setFont(font1)
        self.insertAscii__groupSpam.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(657, 300, 61, 31))
        self.label_13.setFont(font7)
        self.label_13.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.tts_groupSpam = QCheckBox(self.page_4)
        self.tts_groupSpam.setObjectName(u"tts_groupSpam")
        self.tts_groupSpam.setGeometry(QRect(37, 310, 51, 17))
        self.tts_groupSpam.setFont(font4)
        self.tts_groupSpam.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.asciiArtTxt__groupSpam = QLineEdit(self.page_4)
        self.asciiArtTxt__groupSpam.setObjectName(u"asciiArtTxt__groupSpam")
        self.asciiArtTxt__groupSpam.setGeometry(QRect(37, 445, 480, 31))
        self.asciiArtTxt__groupSpam.setFont(font4)
        self.asciiArtTxt__groupSpam.setStyleSheet(u"color: rgb(101, 98, 99);\n"
"border: 2px solid #8677C3;")
        self.asciiArtTxt__groupSpam.setAlignment(Qt.AlignCenter)
        self.groupChannelID = QLineEdit(self.page_4)
        self.groupChannelID.setObjectName(u"groupChannelID")
        self.groupChannelID.setGeometry(QRect(37, 90, 300, 31))
        self.groupChannelID.setFont(font4)
        self.groupChannelID.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.groupChannelID.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.multipleMsgs_AIRAD = QCheckBox(self.page_5)
        self.multipleMsgs_AIRAD.setObjectName(u"multipleMsgs_AIRAD")
        self.multipleMsgs_AIRAD.setGeometry(QRect(187, 370, 111, 17))
        self.multipleMsgs_AIRAD.setFont(font4)
        self.multipleMsgs_AIRAD.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.keywordLabel_5 = QLabel(self.page_5)
        self.keywordLabel_5.setObjectName(u"keywordLabel_5")
        self.keywordLabel_5.setGeometry(QRect(277, 490, 331, 21))
        self.keywordLabel_5.setFont(font6)
        self.keywordLabel_5.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.label_14 = QLabel(self.page_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(657, 300, 61, 31))
        self.label_14.setFont(font7)
        self.label_14.setStyleSheet(u"color: #ffffff;\n"
"background-color: rgba(0, 0, 0, 0) ")
        self.channelID_AIRAD = QLineEdit(self.page_5)
        self.channelID_AIRAD.setObjectName(u"channelID_AIRAD")
        self.channelID_AIRAD.setGeometry(QRect(37, 90, 300, 31))
        self.channelID_AIRAD.setFont(font4)
        self.channelID_AIRAD.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.channelID_AIRAD.setAlignment(Qt.AlignCenter)
        self.ghostPing_AIRAD = QCheckBox(self.page_5)
        self.ghostPing_AIRAD.setObjectName(u"ghostPing_AIRAD")
        self.ghostPing_AIRAD.setGeometry(QRect(187, 340, 121, 17))
        self.ghostPing_AIRAD.setFont(font4)
        self.ghostPing_AIRAD.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.insertAscii__AIRAD = QPushButton(self.page_5)
        self.insertAscii__AIRAD.setObjectName(u"insertAscii__AIRAD")
        self.insertAscii__AIRAD.setGeometry(QRect(527, 445, 270, 31))
        self.insertAscii__AIRAD.setFont(font1)
        self.insertAscii__AIRAD.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.msgRef_AIRAD = QLineEdit(self.page_5)
        self.msgRef_AIRAD.setObjectName(u"msgRef_AIRAD")
        self.msgRef_AIRAD.setGeometry(QRect(347, 90, 300, 31))
        self.msgRef_AIRAD.setFont(font4)
        self.msgRef_AIRAD.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.msgRef_AIRAD.setAlignment(Qt.AlignCenter)
        self.antiLock_AIRAD = QCheckBox(self.page_5)
        self.antiLock_AIRAD.setObjectName(u"antiLock_AIRAD")
        self.antiLock_AIRAD.setGeometry(QRect(337, 310, 111, 17))
        self.antiLock_AIRAD.setFont(font4)
        self.antiLock_AIRAD.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.threads_delay_AIRAD = QCheckBox(self.page_5)
        self.threads_delay_AIRAD.setObjectName(u"threads_delay_AIRAD")
        self.threads_delay_AIRAD.setGeometry(QRect(37, 340, 111, 17))
        self.threads_delay_AIRAD.setFont(font4)
        self.threads_delay_AIRAD.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.Msg_timeout_AIRAD = QDoubleSpinBox(self.page_5)
        self.Msg_timeout_AIRAD.setObjectName(u"Msg_timeout_AIRAD")
        self.Msg_timeout_AIRAD.setGeometry(QRect(727, 300, 72, 31))
        self.Msg_timeout_AIRAD.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.insertHidePing_AIRAD = QPushButton(self.page_5)
        self.insertHidePing_AIRAD.setObjectName(u"insertHidePing_AIRAD")
        self.insertHidePing_AIRAD.setGeometry(QRect(37, 400, 760, 31))
        self.insertHidePing_AIRAD.setFont(font5)
        self.insertHidePing_AIRAD.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.txt_AIRAD = QTextEdit(self.page_5)
        self.txt_AIRAD.setObjectName(u"txt_AIRAD")
        self.txt_AIRAD.setGeometry(QRect(37, 140, 761, 150))
        self.txt_AIRAD.setFont(font5)
        self.txt_AIRAD.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.spamButton_AIRAD = QPushButton(self.page_5)
        self.spamButton_AIRAD.setObjectName(u"spamButton_AIRAD")
        self.spamButton_AIRAD.setGeometry(QRect(657, 90, 140, 31))
        self.spamButton_AIRAD.setFont(font1)
        self.spamButton_AIRAD.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.jesus_mode_AIRAD = QCheckBox(self.page_5)
        self.jesus_mode_AIRAD.setObjectName(u"jesus_mode_AIRAD")
        self.jesus_mode_AIRAD.setGeometry(QRect(37, 370, 111, 17))
        self.jesus_mode_AIRAD.setFont(font4)
        self.jesus_mode_AIRAD.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.tts_AIRAD = QCheckBox(self.page_5)
        self.tts_AIRAD.setObjectName(u"tts_AIRAD")
        self.tts_AIRAD.setGeometry(QRect(37, 310, 51, 17))
        self.tts_AIRAD.setFont(font4)
        self.tts_AIRAD.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.asciiArtTxt__AIRAD = QLineEdit(self.page_5)
        self.asciiArtTxt__AIRAD.setObjectName(u"asciiArtTxt__AIRAD")
        self.asciiArtTxt__AIRAD.setGeometry(QRect(37, 445, 480, 31))
        self.asciiArtTxt__AIRAD.setFont(font4)
        self.asciiArtTxt__AIRAD.setStyleSheet(u"color: rgb(101, 98, 99);\n"
"border: 2px solid #8677C3;")
        self.asciiArtTxt__AIRAD.setAlignment(Qt.AlignCenter)
        self.autoDelete_AIRAD = QCheckBox(self.page_5)
        self.autoDelete_AIRAD.setObjectName(u"autoDelete_AIRAD")
        self.autoDelete_AIRAD.setGeometry(QRect(187, 310, 111, 17))
        self.autoDelete_AIRAD.setFont(font4)
        self.autoDelete_AIRAD.setStyleSheet(u"QCheckBox {\n"
"	color: #ffffff;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border :1px solid #8677C3;\n"
"	border-radius : 4px;\n"
"	background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"	border :1px solid #8677C3;\n"
"	border-radius: 4px;\n"
"	background-color: #8677C3;\n"
"}")
        self.ParseMembers_AIRAD = QPushButton(self.page_5)
        self.ParseMembers_AIRAD.setObjectName(u"ParseMembers_AIRAD")
        self.ParseMembers_AIRAD.setGeometry(QRect(580, 340, 220, 31))
        self.ParseMembers_AIRAD.setFont(font1)
        self.ParseMembers_AIRAD.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.stackedWidget.addWidget(self.page_5)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.textEdit_3 = QTextEdit(self.page)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(50, 110, 430, 370))
        self.textEdit_3.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(520, 110, 270, 220))
        self.frame_2.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.displayPath = QLabel(self.frame_2)
        self.displayPath.setObjectName(u"displayPath")
        self.displayPath.setGeometry(QRect(25, 100, 221, 21))
        self.displayPath.setStyleSheet(u"border: 0px;")
        self.addButton = QLineEdit(self.frame_2)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(25, 170, 221, 31))
        self.addButton.setFont(font4)
        self.addButton.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.addButton.setAlignment(Qt.AlignCenter)
        self.rndIntro = QPushButton(self.frame_2)
        self.rndIntro.setObjectName(u"rndIntro")
        self.rndIntro.setGeometry(QRect(25, 20, 221, 31))
        self.rndIntro.setFont(font1)
        self.rndIntro.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.filePath = QPushButton(self.frame_2)
        self.filePath.setObjectName(u"filePath")
        self.filePath.setGeometry(QRect(25, 60, 221, 31))
        self.filePath.setFont(font1)
        self.filePath.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(520, 340, 270, 140))
        self.frame_3.setStyleSheet(u"color: #ffffff;\n"
"border: 2px solid #8677C3;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 0, 81, 21))
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: #ffffff;\n"
"border: 0px;")
        self.remove_button = QPushButton(self.frame_3)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setGeometry(QRect(30, 90, 221, 31))
        self.remove_button.setFont(font1)
        self.remove_button.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: #ffffff;\n"
"	border: 2px solid #8677C3;\n"
"    background-color: #8C78F8;\n"
"}")
        self.msgREf_2 = QLineEdit(self.frame_3)
        self.msgREf_2.setObjectName(u"msgREf_2")
        self.msgREf_2.setGeometry(QRect(30, 40, 221, 31))
        self.msgREf_2.setFont(font4)
        self.msgREf_2.setStyleSheet(u"color: #656263;\n"
"border: 2px solid #8677C3;")
        self.msgREf_2.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(530, 100, 51, 21))
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: #ffffff;\n"
"")
        self.tokens_configs = QPushButton(self.page)
        self.tokens_configs.setObjectName(u"tokens_configs")
        self.tokens_configs.setGeometry(QRect(50, 60, 95, 23))
        self.tokens_configs.setFont(font5)
        self.tokens_configs.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 1px solid #8677C3;\n"
"	border-top-left-radius: 6;\n"
"	border-bottom-left-radius: 6;\n"
"	border-bottom-right-radius: 6;\n"
"	border-top-right-radius: 6;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #8C78F8;\n"
"}")
        self.disscraper = QPushButton(self.page)
        self.disscraper.setObjectName(u"disscraper")
        self.disscraper.setGeometry(QRect(160, 60, 95, 23))
        self.disscraper.setFont(font5)
        self.disscraper.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 1px solid #8677C3;\n"
"	border-top-left-radius: 6;\n"
"	border-bottom-left-radius: 6;\n"
"	border-bottom-right-radius: 6;\n"
"	border-top-right-radius: 6;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #8C78F8;\n"
"}")
        self.tool_configs = QPushButton(self.page)
        self.tool_configs.setObjectName(u"tool_configs")
        self.tool_configs.setGeometry(QRect(270, 60, 95, 23))
        self.tool_configs.setFont(font5)
        self.tool_configs.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 1px solid #8677C3;\n"
"	border-top-left-radius: 6;\n"
"	border-bottom-left-radius: 6;\n"
"	border-bottom-right-radius: 6;\n"
"	border-top-right-radius: 6;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #8C78F8;\n"
"}")
        self.ds_scripting = QPushButton(self.page)
        self.ds_scripting.setObjectName(u"ds_scripting")
        self.ds_scripting.setGeometry(QRect(380, 60, 95, 23))
        self.ds_scripting.setFont(font5)
        self.ds_scripting.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 1px solid #8677C3;\n"
"	border-top-left-radius: 6;\n"
"	border-bottom-left-radius: 6;\n"
"	border-bottom-right-radius: 6;\n"
"	border-top-right-radius: 6;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #8C78F8;\n"
"}")
        self.custom_tags = QPushButton(self.page)
        self.custom_tags.setObjectName(u"custom_tags")
        self.custom_tags.setGeometry(QRect(490, 60, 95, 23))
        self.custom_tags.setFont(font5)
        self.custom_tags.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	border: 1px solid #8677C3;\n"
"	border-top-left-radius: 6;\n"
"	border-bottom-left-radius: 6;\n"
"	border-bottom-right-radius: 6;\n"
"	border-top-right-radius: 6;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    color: rgb(255, 255, 255);\n"
"    border-top-left-radius: 6;\n"
"    border-bottom-left-radius: 6;\n"
"    border-bottom-right-radius: 6;\n"
"    border-top-right-radius: 6;\n"
"    background-color: #8C78F8;\n"
"}")
        self.stackedWidget.addWidget(self.page)
        go6.setCentralWidget(self.centralwidget)

        self.retranslateUi(go6)

        self.stackedWidget.setCurrentIndex(0)
        self.poop = False

        QMetaObject.connectSlotsByName(go6)
        self.homeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.guildButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.msgButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.voiceButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.threadButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.dmButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.nickButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.webhookButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.groupButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))
        self.aiButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.utils_infoButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(10))



    def retranslateUi(self, go6):
        go6.setWindowTitle(QCoreApplication.translate("go6", u"go6", None))
        self.DiscordIcon.setText("")
        self.homeButton.setText(QCoreApplication.translate("go6", u"  Home", None))
        self.guildButton.setText(QCoreApplication.translate("go6", u" Guild Manager", None))
        self.msgButton.setText(QCoreApplication.translate("go6", u"Msg Spammer", None))
        self.voiceButton.setText(QCoreApplication.translate("go6", u"Voice Spammer", None))
        self.threadButton.setText(QCoreApplication.translate("go6", u"Thread Spamer", None))
        self.dmButton.setText(QCoreApplication.translate("go6", u"DM Spammer", None))
        self.nickButton.setText(QCoreApplication.translate("go6", u"Nick Spammer", None))
        self.webhookButton.setText(QCoreApplication.translate("go6", u"Webhook Spam", None))
        self.groupButton.setText(QCoreApplication.translate("go6", u"Group Spammer", None))
        self.aiButton.setText(QCoreApplication.translate("go6", u"AI Raider", None))
        self.utils_infoButton.setText(QCoreApplication.translate("go6", u"Utils - Info", None))
        self.loadTokens.setText(QCoreApplication.translate("go6", u"Load Tokens", None))
        self.checkTokens.setText(QCoreApplication.translate("go6", u"Check Tokens", None))
        self.rmInvTok.setText(QCoreApplication.translate("go6", u"Remove Invalid Tokens", None))
        self.rmInvProxies.setText(QCoreApplication.translate("go6", u"Remove Invalid Proxies", None))
        self.loadProxies.setText(QCoreApplication.translate("go6", u"Load Proxies", None))
        self.checkProxies.setText(QCoreApplication.translate("go6", u"Check Proxies", None))
        self.label_5.setText(QCoreApplication.translate("go6", u"Demon Spammer", None))
        self.label_6.setText(QCoreApplication.translate("go6", u"<html><head/><body><p>Remember sandwich slaved away, so all these sizes are exact</p></body></html>", None))
        self.bypassMemVer_3.setText(QCoreApplication.translate("go6", u"Use Proxies", None))
        self.label_7.setText(QCoreApplication.translate("go6", u"Max tokens to use:", None))
        self.label_8.setText(QCoreApplication.translate("go6", u"Max proxies to use:", None))
        self.label_9.setText(QCoreApplication.translate("go6", u"Total Tokens: 0", None))
        self.label_10.setText(QCoreApplication.translate("go6", u"Total Proxies: 0", None))
#if QT_CONFIG(whatsthis)
        self.discInvLineEdit.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.discInvLineEdit.setText(QCoreApplication.translate("go6", u"discord.gg/invitecode", None))
        self.joinButton.setText(QCoreApplication.translate("go6", u"Join", None))
        self.leaveButton.setText(QCoreApplication.translate("go6", u"Leave", None))
        self.bypassMemVer.setText(QCoreApplication.translate("go6", u"Bypass Membership Verification", None))
        self.messageBypass.setText(QCoreApplication.translate("go6", u"MessageBypass", None))
        self.reactionBypass.setText(QCoreApplication.translate("go6", u"ReactionBypass", None))
        self.buttonBypass.setText(QCoreApplication.translate("go6", u"ButtonBypass", None))
        self.label.setText(QCoreApplication.translate("go6", u"Add <option> verification bypass", None))
#if QT_CONFIG(whatsthis)
        self.channelID.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.channelID.setText(QCoreApplication.translate("go6", u"Channel ID", None))
#if QT_CONFIG(whatsthis)
        self.messageID.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.messageID.setText(QCoreApplication.translate("go6", u"Message ID", None))
#if QT_CONFIG(whatsthis)
        self.emoji.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.emoji.setText(QCoreApplication.translate("go6", u"Emoji", None))
        self.viewReactions.setText(QCoreApplication.translate("go6", u"View Reactions", None))
#if QT_CONFIG(whatsthis)
        self.channelID_spam.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.channelID_spam.setText(QCoreApplication.translate("go6", u"Channel ID", None))
#if QT_CONFIG(whatsthis)
        self.discInvLineEdit_3.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.discInvLineEdit_3.setText(QCoreApplication.translate("go6", u"Message Reference ( optional )", None))
        self.spamButton.setText(QCoreApplication.translate("go6", u"Spam", None))
        self.textEdit_spam.setHtml(QCoreApplication.translate("go6", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">@everyone</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">:fire: ** Ui by sandy sandwich &lt;&lt;&lt; pog&gt;&gt; :fire:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">hi kian</span></p></body></html>", None))
        self.bypassMemVer_2.setText(QCoreApplication.translate("go6", u"TTS", None))
        self.threads_delay.setText(QCoreApplication.translate("go6", u"Threads Delay", None))
        self.jesus_mode.setText(QCoreApplication.translate("go6", u"Jesus Mode", None))
        self.autoDelete.setText(QCoreApplication.translate("go6", u"Auto Delete", None))
        self.ghostPing.setText(QCoreApplication.translate("go6", u"Ghost Ping ( v2 )", None))
        self.multipleMsgs.setText(QCoreApplication.translate("go6", u"Multiple Msgs", None))
        self.antiLock.setText(QCoreApplication.translate("go6", u"Anti Lock", None))
#if QT_CONFIG(whatsthis)
        self.asciiArtTxt.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.asciiArtTxt.setText(QCoreApplication.translate("go6", u"Ascii art text", None))
        self.insertAscii.setText(QCoreApplication.translate("go6", u"Insert ascii art", None))
        self.keywordLabel.setText(QCoreApplication.translate("go6", u"Keywords: [num], [random], [lag], [mtag], [poon]", None))
        self.label_2.setText(QCoreApplication.translate("go6", u"Timeout:", None))
        self.ParseMembers.setText(QCoreApplication.translate("go6", u"Parse Members", None))
        self.ParseMembers_2.setText(QCoreApplication.translate("go6", u"Insert \"hide ping\" text ( it's also a lag message )", None))
#if QT_CONFIG(whatsthis)
        self.guildID.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.guildID.setText(QCoreApplication.translate("go6", u"Guild ID", None))
#if QT_CONFIG(whatsthis)
        self.channelID_2.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.channelID_2.setText(QCoreApplication.translate("go6", u"Channel ID", None))
        self.joinVCButton.setText(QCoreApplication.translate("go6", u"Join", None))
        self.leaveVCButton_2.setText(QCoreApplication.translate("go6", u"Leave", None))
        self.PlayVCButton_3.setText(QCoreApplication.translate("go6", u"Play", None))
        self.spamJL.setText(QCoreApplication.translate("go6", u"Spam Join - Leave", None))
        self.startStream.setText(QCoreApplication.translate("go6", u"Start Stream", None))
        self.mutedCheck.setText(QCoreApplication.translate("go6", u"Muted", None))
        self.deathonCheck.setText(QCoreApplication.translate("go6", u"Deathon", None))
        self.webcamCheck.setText(QCoreApplication.translate("go6", u"Webcam", None))
        self.startWS.setText(QCoreApplication.translate("go6", u"Start WS", None))
        self.stopStream.setText(QCoreApplication.translate("go6", u"Stop Stream", None))
        self.keywordLabel_3.setText(QCoreApplication.translate("go6", u"Keywords: [num], [random], [lag], [mtag], [poon]", None))
#if QT_CONFIG(whatsthis)
        self.channelID_threadspam.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.channelID_threadspam.setText(QCoreApplication.translate("go6", u"Channel ID", None))
        self.insertAscii_2.setText(QCoreApplication.translate("go6", u"Insert ascii art", None))
        self.ghostPing_2.setText(QCoreApplication.translate("go6", u"Ghost Ping ( v2 )", None))
        self.bypassMemVer_4.setText(QCoreApplication.translate("go6", u"TTS", None))
        self.autoDelete_2.setText(QCoreApplication.translate("go6", u"Auto Delete", None))
        self.TextBox_threadspam.setHtml(QCoreApplication.translate("go6", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">@everyone</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">:fire: ** Ui by sandy sandwich &lt;&lt;&lt; pog&gt;&gt; :fire:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">hi kian</span></p></body></html>", None))
        self.insertHidePingThreadSpam.setText(QCoreApplication.translate("go6", u"Insert \"hide ping\" text ( it's also a lag message )", None))
        self.ParseMembers_Thread.setText(QCoreApplication.translate("go6", u"Parse Members", None))
        self.jesus_mode_2.setText(QCoreApplication.translate("go6", u"Jesus Mode", None))
        self.label_3.setText(QCoreApplication.translate("go6", u"Timeout:", None))
#if QT_CONFIG(whatsthis)
        self.asciiArtTxt_2.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.asciiArtTxt_2.setText(QCoreApplication.translate("go6", u"Ascii art text", None))
#if QT_CONFIG(whatsthis)
        self.msgRef_threadspam.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.msgRef_threadspam.setText(QCoreApplication.translate("go6", u"Message Reference ( optional )", None))
        self.multipleMsgs_2.setText(QCoreApplication.translate("go6", u"Multiple Msgs", None))
        self.antiLock_2.setText(QCoreApplication.translate("go6", u"Anti Lock", None))
        self.spamButton_threadspam.setText(QCoreApplication.translate("go6", u"Spam", None))
        self.threads_delay_2.setText(QCoreApplication.translate("go6", u"Threads Delay", None))
#if QT_CONFIG(whatsthis)
        self.userID.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.userID.setText(QCoreApplication.translate("go6", u"User ID", None))
#if QT_CONFIG(whatsthis)
        self.msgREf.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.msgREf.setText(QCoreApplication.translate("go6", u"Message Reference ( optional )", None))
        self.DMspamButton.setText(QCoreApplication.translate("go6", u"Spam", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("go6", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">heyo hope your dms are exploding rn lmao</span></p></body></html>", None))
        self.dm_autoDel.setText(QCoreApplication.translate("go6", u"Auto Delete", None))
        self.dm_delay.setText(QCoreApplication.translate("go6", u"Delay", None))
        self.dm_autoDel_3.setText(QCoreApplication.translate("go6", u"Token Threading", None))
        self.dm_multiMsgs.setText(QCoreApplication.translate("go6", u"Multiple Msgs", None))
#if QT_CONFIG(whatsthis)
        self.delFriendReq.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.delFriendReq.setText(QCoreApplication.translate("go6", u"Delete Friend Request", None))
#if QT_CONFIG(whatsthis)
        self.spamFriendReq_2.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.spamFriendReq_2.setText(QCoreApplication.translate("go6", u"Spam Friend Request", None))
        self.insertAscii_dm.setText(QCoreApplication.translate("go6", u"Insert ascii art", None))
        self.keywordLabel_2.setText(QCoreApplication.translate("go6", u"Keywords: [num], [random], [lag], [mtag]", None))
#if QT_CONFIG(whatsthis)
        self.asciiArtTxt_dm.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.asciiArtTxt_dm.setText(QCoreApplication.translate("go6", u"Ascii art text", None))
        self.InsertHidePing.setText(QCoreApplication.translate("go6", u"Insert \"hide ping\" text ( it's also a lag message )", None))
        self.label_4.setText(QCoreApplication.translate("go6", u"Timeout:", None))
#if QT_CONFIG(whatsthis)
        self.msgREf_3.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.msgREf_3.setText(QCoreApplication.translate("go6", u"Nickname", None))
        self.nicktxt.setHtml(QCoreApplication.translate("go6", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">text</span></p></body></html>", None))
        self.nickspam.setText(QCoreApplication.translate("go6", u"Spam", None))
#if QT_CONFIG(whatsthis)
        self.nickname.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.nickname.setText(QCoreApplication.translate("go6", u"Nickname", None))
        self.webhooktxt.setHtml(QCoreApplication.translate("go6", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">@everyone<br />yooo public webhook nice</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">wsg :fire:</span></p></body></html>", None))
        self.webhookSpamStart.setText(QCoreApplication.translate("go6", u"Spam", None))
#if QT_CONFIG(whatsthis)
        self.webhook2.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.webhook2.setText(QCoreApplication.translate("go6", u"Webhook", None))
#if QT_CONFIG(whatsthis)
        self.webhook.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.webhook.setText(QCoreApplication.translate("go6", u"Webhook", None))
        self.ghostPing_groupSpam.setText(QCoreApplication.translate("go6", u"Ghost Ping ( v2 )", None))
        self.antiLock_groupSpam.setText(QCoreApplication.translate("go6", u"Anti Lock", None))
        self.keywordLabel_4.setText(QCoreApplication.translate("go6", u"Keywords: [num], [random], [lag], [mtag], [poon]", None))
        self.multipleMsgs_groupSpam.setText(QCoreApplication.translate("go6", u"Multiple Msgs", None))
        self.spamButton__groupSpam.setText(QCoreApplication.translate("go6", u"Spam", None))
        self.txt_groupSpam.setHtml(QCoreApplication.translate("go6", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">@everyone</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">:fire: ** Ui by sandy sandwich &lt;&lt;&lt; pog&gt;&gt; :fire:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">hi kian</span></p></body></html>", None))
        self.autoDelete_groupSpam.setText(QCoreApplication.translate("go6", u"Auto Delete", None))
#if QT_CONFIG(whatsthis)
        self.msgRef__groupSpam.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.msgRef__groupSpam.setText(QCoreApplication.translate("go6", u"Message Reference ( optional )", None))
        self.threads_delay_groupSpam.setText(QCoreApplication.translate("go6", u"Threads Delay", None))
        self.ParseMembers_groupSpam.setText(QCoreApplication.translate("go6", u"Parse Members", None))
        self.insertHidePing_groupSpam.setText(QCoreApplication.translate("go6", u"Insert \"hide ping\" text ( it's also a lag message )", None))
        self.jesus_mode_groupSpam.setText(QCoreApplication.translate("go6", u"Jesus Mode", None))
        self.insertAscii__groupSpam.setText(QCoreApplication.translate("go6", u"Insert ascii art", None))
        self.label_13.setText(QCoreApplication.translate("go6", u"Timeout:", None))
        self.tts_groupSpam.setText(QCoreApplication.translate("go6", u"TTS", None))
#if QT_CONFIG(whatsthis)
        self.asciiArtTxt__groupSpam.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.asciiArtTxt__groupSpam.setText(QCoreApplication.translate("go6", u"Ascii art text", None))
#if QT_CONFIG(whatsthis)
        self.groupChannelID.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupChannelID.setText(QCoreApplication.translate("go6", u"Group Channel ID", None))
        self.multipleMsgs_AIRAD.setText(QCoreApplication.translate("go6", u"Multiple Msgs", None))
        self.keywordLabel_5.setText(QCoreApplication.translate("go6", u"Keywords: [num], [random], [lag], [mtag], [poon]", None))
        self.label_14.setText(QCoreApplication.translate("go6", u"Timeout:", None))
#if QT_CONFIG(whatsthis)
        self.channelID_AIRAD.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.channelID_AIRAD.setText(QCoreApplication.translate("go6", u"Channel ID", None))
        self.ghostPing_AIRAD.setText(QCoreApplication.translate("go6", u"Ghost Ping ( v2 )", None))
        self.insertAscii__AIRAD.setText(QCoreApplication.translate("go6", u"Insert ascii art", None))
#if QT_CONFIG(whatsthis)
        self.msgRef_AIRAD.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.msgRef_AIRAD.setText(QCoreApplication.translate("go6", u"Message Reference ( optional )", None))
        self.antiLock_AIRAD.setText(QCoreApplication.translate("go6", u"Anti Lock", None))
        self.threads_delay_AIRAD.setText(QCoreApplication.translate("go6", u"Threads Delay", None))
        self.insertHidePing_AIRAD.setText(QCoreApplication.translate("go6", u"Insert \"hide ping\" text ( it's also a lag message )", None))
        self.txt_AIRAD.setHtml(QCoreApplication.translate("go6", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">@everyone</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">:fire: ** Ui by sandy sandwich &lt;&lt;&lt; pog&gt;&gt; :fire:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">hi kian</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; m"
                        "argin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">ai reader? wtf is this xd</span></p></body></html>", None))
        self.spamButton_AIRAD.setText(QCoreApplication.translate("go6", u"Spam", None))
        self.jesus_mode_AIRAD.setText(QCoreApplication.translate("go6", u"Jesus Mode", None))
        self.tts_AIRAD.setText(QCoreApplication.translate("go6", u"TTS", None))
#if QT_CONFIG(whatsthis)
        self.asciiArtTxt__AIRAD.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.asciiArtTxt__AIRAD.setText(QCoreApplication.translate("go6", u"Ascii art text", None))
        self.autoDelete_AIRAD.setText(QCoreApplication.translate("go6", u"Auto Delete", None))
        self.ParseMembers_AIRAD.setText(QCoreApplication.translate("go6", u"Parse Members", None))
        self.displayPath.setText(QCoreApplication.translate("go6", u"<html><head/><body><p>file path display</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.addButton.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.addButton.setText(QCoreApplication.translate("go6", u"Add", None))
        self.rndIntro.setText(QCoreApplication.translate("go6", u"Random Intro", None))
        self.filePath.setText(QCoreApplication.translate("go6", u"Select File Path", None))
        self.label_12.setText(QCoreApplication.translate("go6", u"Remove Tag", None))
        self.remove_button.setText(QCoreApplication.translate("go6", u"Remove", None))
#if QT_CONFIG(whatsthis)
        self.msgREf_2.setWhatsThis(QCoreApplication.translate("go6", u"<html><head/><body><p align=\"center\"><br/>discord.gg/invitecode</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.msgREf_2.setText(QCoreApplication.translate("go6", u"TAG Name", None))
        self.label_11.setText(QCoreApplication.translate("go6", u"Add Tag", None))
        self.tokens_configs.setText(QCoreApplication.translate("go6", u"Tokens Configs", None))
        self.disscraper.setText(QCoreApplication.translate("go6", u"Disboard Scraper", None))
        self.tool_configs.setText(QCoreApplication.translate("go6", u"Tool Configs", None))
        self.ds_scripting.setText(QCoreApplication.translate("go6", u"DS-Scripting", None))
        self.custom_tags.setText(QCoreApplication.translate("go6", u"Custom Tags", None))
    # retranslateUi



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_go6()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())