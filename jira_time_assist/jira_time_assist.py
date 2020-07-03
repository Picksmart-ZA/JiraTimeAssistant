import os
from jira_time_assist.utils import db_util


def init_db():

    if not os.path.exists("jira_time_assist/jira_time_assist.db3"):
        db_util.create_db()


class JiraTimeAssistant:

    @staticmethod
    def run():
        init_db()

