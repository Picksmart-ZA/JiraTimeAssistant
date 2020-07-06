import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from jira_time_assist.utils import db_util
from jira_time_assist.entities.settings import Settings
from jira_time_assist import jira_time_assist

kivy.require("1.11.1")


class SettingsPopup(Popup):
    __settings = None

    url_text_input = ObjectProperty()
    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()

    def set_settings(self, settings):
        self.__settings = settings

        if settings:
            self.url_text_input.text = settings.get_url()
            self.username_text_input.text = settings.get_user()
            self.password_text_input.text = settings.get_password()

    def save_settings(self):
        conn = jira_time_assist.init_db()

        settings_id = None

        if self.__settings:
            settings_id = self.__settings.get_id()

        settings = Settings(settings_id, self.url_text_input.text,
                            self.username_text_input.text, self.password_text_input.text)
        db_util.save_settings(conn, settings)


class MainScreen(BoxLayout):
    __settings = None

    def init_settings(self):
        conn = jira_time_assist.init_db()
        self.__settings = db_util.get_settings(conn)

    # Opens Popup when called
    def open_popup(self):
        settings_popup = SettingsPopup()
        settings_popup.set_settings(self.__settings)
        settings_popup.open()


class MainApp(App):

    def build(self):
        Window.clearcolor = (.3, .3, .3, 1)
        main_screen = MainScreen()
        main_screen.init_settings()
        return main_screen
