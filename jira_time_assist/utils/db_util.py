import sqlite3

settings_create: str = '''
        CREATE TABLE settings (url VARCHAR(255), user VARCHAR(255), password VARCHAR(255))
    '''
task_create: str = '''
        CREATE TABLE task (id INTEGER, ticket VARCHAR(255), description VARCHAR(255), jira_json VARCHAR(10), removed BOOLEAN) 
    '''
time_log_create: str = '''
        CREATE TABLE time_log (id INTEGER, task_id INTEGER, start_time DATETIME, end_time DATETIME, submitted BOOLEAN)
    '''


def create_settings(cursor):
    if cursor:
        cursor.execute(settings_create)


def create_task(cursor):
    if cursor:
        cursor.execute(task_create)


def create_time_log(cursor):
    if cursor:
        cursor.execute(time_log_create)


def create_db():
    conn = sqlite3.connect("jira_time_assist/jira_time_assist.db3")

    if conn:
        cursor = conn.cursor()
        create_settings(cursor)
        create_task(cursor)
        create_time_log(cursor)
        conn.commit()
        conn.close()


def get_settings(cursor):
    sql: str = "SELECT * FROM settings"
    print(cursor.execute(sql))
