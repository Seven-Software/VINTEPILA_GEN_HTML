from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 522)
        MainWindow.setMinimumSize(QtCore.QSize(784, 522))
        MainWindow.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #310061;\n"
            "    border-radius: 10px;\n"
            "    padding: 5px 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #f00;\n"
            "}\n"
            "\n"
            "QPushButton:disabled  {\n"
            "    background-color: #36271e;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #ff8456;\n"
            "}\n"
            "\n"
            "#tablet{\n"
            "    background-color: #555555;\n"
            "}\n"
            "\n"
            "*{\n"
            '    font: 18pt "DejaVu Sans";\n'
            "    background: black;\n"
            "    color: #fff;\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(784, 522))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tablet = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tablet.setObjectName("tablet")
        self.tablet.setColumnCount(0)
        self.tablet.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tablet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_question = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_question.setObjectName("add_question")
        self.horizontalLayout.addWidget(self.add_question)
        self.remove_question = QtWidgets.QPushButton(parent=self.centralwidget)
        self.remove_question.setEnabled(False)
        self.remove_question.setObjectName("remove_question")
        self.horizontalLayout.addWidget(self.remove_question)
        self.export_html = QtWidgets.QPushButton(parent=self.centralwidget)
        self.export_html.setEnabled(False)
        self.export_html.setObjectName("export_html")
        self.horizontalLayout.addWidget(self.export_html)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.add_question, self.export_html)
        MainWindow.setTabOrder(self.export_html, self.remove_question)
        MainWindow.setTabOrder(self.remove_question, self.tablet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Gerar Html - Seven Software")
        )
        self.label.setText(_translate("MainWindow", "Gerar Html"))
        self.add_question.setText(_translate("MainWindow", "Adicionar"))
        self.remove_question.setText(_translate("MainWindow", "Remover"))
        self.export_html.setText(_translate("MainWindow", "Exportar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
