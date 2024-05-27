from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory as F


class MainWindow(BoxLayout):
    """
    This class represents the main window of the application.
    """

    data = F.ListProperty([])

    def update_table(self):
        value = self.ids.text_input.text
        self.ids.btn_add_question.disabled = False if value else True

    def add_question(self):
        value = self.ids.text_input.text
        self.ids.text_input.text = ""
        self.ids.btn_add_question.disabled = True
        self.data.append({"text": value})
        self.ids.list_view.data = self.data


class MainApp(App):
    def build(self):
        self.title = "Generate Code Html - Seven Software"
        return MainWindow()


MainApp().run()
