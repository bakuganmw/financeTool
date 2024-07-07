import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, LEFT


class HelloWorld(toga.App):
    def startup(self):
        # Główne okno aplikacji
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

        # Etykieta
        hello_label = toga.Label(
            'Hello, World!',
            style=Pack(padding=(0, 10), font_size=24, text_align=CENTER)
        )

        # Pole tekstowe
        self.text_input = toga.TextInput(style=Pack(flex=1, padding=(0, 5), width=200))

        # Przycisk
        button = toga.Button(
            'Click me!',
            on_press=self.button_handler,
            style=Pack(padding=5, font_size=16, width=100)
        )

        # Suwak
        self.slider = toga.Slider(
            range=(0, 100),
            value=50,
            style=Pack(padding=5, width=200)
        )

        # Pole wyboru (Switch)
        self.checkbox = toga.Switch(
            'Toggle me!',
            style=Pack(padding=5, font_size=16)
        )

        # Układ elementów w poziomym pudełku
        input_box = toga.Box(style=Pack(direction=ROW, alignment=LEFT, padding=(5, 10)))
        input_box.add(self.text_input)
        input_box.add(button)

        # Dodanie widżetów do głównego pudełka
        main_box.add(hello_label)
        main_box.add(input_box)
        main_box.add(self.slider)
        main_box.add(self.checkbox)

        # Ustawienie zawartości głównego okna
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def button_handler(self, widget):
        # Obsługa kliknięcia przycisku
        print("Button clicked!")
        print(f"Text input value: {self.text_input.value}")
        print(f"Slider value: {self.slider.value}")
        print(f"Checkbox state: {'On' if self.checkbox.value else 'Off'}")


def main():
    return HelloWorld(formal_name='Hello World', app_id='org.beeware.helloworld')


if __name__ == '__main__':
    main().main_loop()
