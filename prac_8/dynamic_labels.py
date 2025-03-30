from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import (GridLayout)


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob", "Andrew", "Jessica"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list entries and add them to the GUI."""
        layout = self.root.ids.main
        for name in self.names:
            label = Label(text=name)
            layout.add_widget(label)


DynamicLabelsApp().run()
