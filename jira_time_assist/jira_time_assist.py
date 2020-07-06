import os
from jira_time_assist.screens.main_screen import MainApp
from jira_time_assist.utils import db_util


def init_db():
    path: str = "jira_time_assist/jira_time_assist.db3"
    conn = None

    if not os.path.exists(path):
        conn = db_util.create_db(path)
    else:
        conn = db_util.create_connection(path)

    return conn


class JiraTimeAssistant:

    @staticmethod
    def run():
        init_db()
        main_app = MainApp()
        main_app.run()
