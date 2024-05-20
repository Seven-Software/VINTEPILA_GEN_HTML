from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MainWindow(BoxLayout):
    """
    This class represents the main window of the application.

    It inherits from the `BoxLayout` class and provides the layout and functionality
    for the main window UI.

    Attributes:
        - attribute1: Description of attribute1.
        - attribute2: Description of attribute2.

    Methods:
        - method1(): Description of method1.
        - method2(): Description of method2.
    """


class MainApp(App):
    def build(self):
        self.title = "Generate Code Html - Seven Software"
        return MainWindow()


MainApp().run()
