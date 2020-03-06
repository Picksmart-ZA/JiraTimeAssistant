import os
import sys
from PyQt5 import QtWidgets
from jira_time_assist.utils import db_util
from jira_time_assist.screens import UIMain


def init_db():

    if not os.path.exists("jira_time_assist.db3"):
        db_util.create_db()


class JiraTimeAssistant:

    @staticmethod
    def run():
        init_db()
        app = QtWidgets.QApplication(sys.argv)
        ex = UIMain.UiMainWindow()
        w = QtWidgets.QMainWindow()
        ex.setup_ui(w)
        w.show()
        sys.exit(app.exec_())

