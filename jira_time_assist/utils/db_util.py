import sqlite3
from jira_time_assist.entities.settings import Settings

settings_create: str = '''
        CREATE TABLE settings (id INTEGER PRIMARY KEY AUTOINCREMENT, url VARCHAR(255), user VARCHAR(255), password VARCHAR(255))
    '''
task_create: str = '''
        CREATE TABLE task (id INTEGER PRIMARY KEY AUTOINCREMENT, ticket VARCHAR(255), description VARCHAR(255), jira_json VARCHAR(10), removed BOOLEAN) 
    '''
time_log_create: str = '''
        CREATE TABLE time_log (id INTEGER PRIMARY KEY AUTOINCREMENT, task_id INTEGER, start_time DATETIME, end_time DATETIME, submitted BOOLEAN)
    '''


def create_connection(path):
    conn = sqlite3.connect(path)
    print("Create Connection " + path)
    return conn


def create_settings(cursor):
    if cursor:
        cursor.execute(settings_create)


def create_task(cursor):
    if cursor:
        cursor.execute(task_create)


def create_time_log(cursor):
    if cursor:
        cursor.execute(time_log_create)


def create_db(path):
    conn = create_connection(path)

    if conn:
        cursor = conn.cursor()
        create_settings(cursor)
        create_task(cursor)
        create_time_log(cursor)
        conn.commit()
        conn.close()
    return conn


def get_settings(conn):
    if conn:
        cursor = conn.cursor()
        sql: str = "SELECT * FROM settings"
        cursor.execute(sql)
        rows = cursor.fetchone()

        settings = None

        if rows:
            settings = Settings(rows[0], rows[1], rows[2], rows[3])
        
        return settings


def save_settings(conn, settings):

    if conn:
        cursor = conn.cursor()
        sql: str = ""

        if settings.get_id():
            sql = "UPDATE settings SET url = ?, user = ?, password = ?"
        else:
            sql = "INSERT INTO settings (url, user, password) VALUES (?,?,?)"

        settings_tuple = (settings.get_url(),
                          settings.get_user(), settings.get_password(), )
                          
        cursor.execute(sql, settings_tuple)
        conn.commit()
