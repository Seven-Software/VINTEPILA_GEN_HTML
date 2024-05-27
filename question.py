from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 452)
        Form.setMinimumSize(QtCore.QSize(559, 452))
        Form.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #310061;\n"
            "    border-radius: 10px;\n"
            "    padding: 5px 10px;\n"
            "    color: #fff; \n"
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
            ".QLineEdit{\n"
            "    background-color: #555555;\n"
            "}\n"
            "\n"
            "*{\n"
            '    font: 18pt "DejaVu Sans";\n'
            "    background: black;\n"
            "    color: #fff;\n"
            "}"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.question = QtWidgets.QLineEdit(parent=self.widget)
        self.question.setText("")
        self.question.setObjectName("question")
        self.verticalLayout_2.addWidget(self.question)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ask = QtWidgets.QLineEdit(parent=self.widget)
        self.ask.setClearButtonEnabled(True)
        self.ask.setObjectName("ask")
        self.horizontalLayout_2.addWidget(self.ask)
        self.btn_add_ask = QtWidgets.QPushButton(parent=self.widget)
        self.btn_add_ask.setObjectName("btn_add_ask")
        self.horizontalLayout_2.addWidget(self.btn_add_ask)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tablet = QtWidgets.QTableWidget(parent=self.widget)
        self.tablet.setObjectName("tablet")
        self.tablet.setColumnCount(0)
        self.tablet.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tablet)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.insert_ask = QtWidgets.QPushButton(parent=Form)
        self.insert_ask.setObjectName("insert_ask")
        self.horizontalLayout.addWidget(self.insert_ask)
        self.cancel = QtWidgets.QPushButton(parent=Form)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.cancel.clicked.connect(Form.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.question, self.ask)
        Form.setTabOrder(self.ask, self.btn_add_ask)
        Form.setTabOrder(self.btn_add_ask, self.insert_ask)
        Form.setTabOrder(self.insert_ask, self.tablet)
        Form.setTabOrder(self.tablet, self.cancel)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Questões - Seven Sofware"))
        self.label.setText(_translate("Form", "Questões"))
        self.question.setStatusTip(_translate("Form", "Informe a questão"))
        self.question.setPlaceholderText(_translate("Form", "Informe a questão"))
        self.ask.setPlaceholderText(_translate("Form", "Informe uma alternativa"))
        self.btn_add_ask.setText(_translate("Form", "Adicionar"))
        self.insert_ask.setText(_translate("Form", "Registrar"))
        self.cancel.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
