from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONVERSION_FACTOR = 1.60934


class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = float(value) * CONVERSION_FACTOR if value.replace('.', '', 1).isdigit() else 0.0
        self.root.ids.output_label.text = f"{result:.3f}"

    def handle_increment(self, increment):
        """ handle increment, output result to input widget"""
        input_number = self.root.ids.input_number.text
        if input_number.replace('.', '', 1).isdigit():
            new_value = str(float(input_number) + increment)
            self.root.ids.input_number.text = new_value if '.' in input_number else new_value.rstrip('.0')
        else:
            self.root.ids.input_number.text = str(increment)


if __name__ == "__main__":
    ConvertMilesKmApp().run()
