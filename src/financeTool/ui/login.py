# import toga
# from toga.style import Pack
# from toga.style.pack import COLUMN, CENTER
# from toga.colors import  LIGHTBLUE, LIGHTGREEN, WHITE
# def build_main_box():
#     # Create login box
#     login_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20, background_color=LIGHTBLUE))
#     username_input = toga.TextInput(placeholder="Username", style=Pack(flex=1, padding=(0, 5), width=200, background_color=WHITE))
#     password_input = toga.PasswordInput(placeholder="Password", style=Pack(flex=1, padding=(0, 5), width=200, background_color=WHITE))
#     login_button = toga.Button('Login', on_press=lambda btn: login_handler(username_input, password_input), 
#                                 style=Pack(padding=5, font_size=16, width=100, background_color=LIGHTGREEN))

#     # Add components to the login box
#     login_box.add(username_input)
#     login_box.add(password_input)
#     login_box.add(login_button)
#     return login_box

# def login_handler(username_input, password_input):
#     # Validate credentials
#     username = username_input.value
#     password = password_input.value
#     if username == 'admin' and password == 'password':
#         # Setup main window content on successful login
#         self.setup_main_window()
#     else:
#         # Show error dialog on login failure
#         self.main_window.error_dialog('Login Failed', 'Invalid username or password. Please try again.')

    