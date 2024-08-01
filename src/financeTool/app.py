import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, LEFT
from toga.colors import RED, BLUE, GREEN, LIGHTBLUE, LIGHTGREEN, ORANGE, WHITE

class ExpenseManager(toga.App):
    def startup(self):
        # Initialize the main window
        self.main_window = toga.MainWindow(title="Login")
        self.setup_login_window()

    def setup_login_window(self):
        # Create login box
        login_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20, background_color=LIGHTBLUE))
        username_input = toga.TextInput(placeholder="Username", style=Pack(flex=1, padding=(0, 5), width=200, background_color=WHITE))
        password_input = toga.PasswordInput(placeholder="Password", style=Pack(flex=1, padding=(0, 5), width=200, background_color=WHITE))
        login_button = toga.Button('Login', on_press=lambda btn: self.login_handler(username_input, password_input), 
                                   style=Pack(padding=5, font_size=16, width=100, background_color=LIGHTGREEN))

        # Add components to the login box
        login_box.add(username_input)
        login_box.add(password_input)
        login_box.add(login_button)

        # Set as the content of the main window
        self.main_window.content = login_box
        self.main_window.show()

    def login_handler(self, username_input, password_input):
        # Validate credentials
        username = username_input.value
        password = password_input.value
        if username == 'admin' and password == 'password':
            # Setup main window content on successful login
            self.setup_main_window()
        else:
            # Show error dialog on login failure
            self.main_window.error_dialog('Login Failed', 'Invalid username or password. Please try again.')

    def setup_main_window(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20, background_color=LIGHTBLUE))

        # Etykieta powitalna
        hello_label = toga.Label(
            'Shared Expense Manager',
            style=Pack(padding=(0, 10), font_size=24, text_align=CENTER, color=BLUE)
        )

        # Pola tekstowe do dodawania znajomych i rachunków
        self.friend_name_input = toga.TextInput(placeholder="Friend's Name",
                                                style=Pack(flex=1, padding=(0, 5), width=200, background_color=WHITE))
        self.expense_description_input = toga.TextInput(placeholder='Expense Description',
                                                        style=Pack(flex=1, padding=(0, 5), width=200,
                                                                   background_color=WHITE))
        self.expense_amount_input = toga.NumberInput(
            style=Pack(flex=1, padding=(0, 5), width=200, background_color=WHITE))
        self.friend_selection = toga.Selection(items=[],
                                               style=Pack(flex=1, padding=(0, 5), width=200, background_color=WHITE))
        self.filter_friend_selection = toga.Selection(items=['All'], style=Pack(flex=1, padding=(0, 5), width=200,
                                                                                background_color=WHITE))

        # Przycisk do dodawania znajomego
        add_friend_button = toga.Button(
            'Add Friend',
            on_press=self.add_friend_handler,
            style=Pack(padding=5, font_size=16, width=100, background_color=LIGHTGREEN)
        )

        # Przycisk do dodawania rachunku
        add_expense_button = toga.Button(
            'Add Expense',
            on_press=self.add_expense_handler,
            style=Pack(padding=5, font_size=16, width=100, background_color=ORANGE)
        )

        # Przycisk do edycji znajomego
        edit_friend_button = toga.Button(
            'Edit Friend',
            on_press=self.edit_friend_handler,
            style=Pack(padding=5, font_size=16, width=100, background_color=LIGHTGREEN)
        )

        # Przycisk do edycji rachunku
        edit_expense_button = toga.Button(
            'Edit Expense',
            on_press=self.edit_expense_handler,
            style=Pack(padding=5, font_size=16, width=100, background_color=ORANGE)
        )

        # Przycisk do dzielenia kosztów
        split_expenses_button = toga.Button(
            'Split Expenses',
            on_press=self.split_expenses_handler,
            style=Pack(padding=5, font_size=16, width=150, background_color=GREEN)
        )

        # Przycisk do resetowania aplikacji
        reset_button = toga.Button(
            'Reset',
            on_press=self.reset_handler,
            style=Pack(padding=5, font_size=16, width=100, background_color=RED)
        )

        # Przycisk do generowania raportu
        report_button = toga.Button(
            'Generate Report',
            on_press=self.generate_report_handler,
            style=Pack(padding=5, font_size=16, width=150, background_color=BLUE)
        )

        # Przycisk do wysyłania przypomnień o długach
        reminder_button = toga.Button(
            'Send Reminders',
            on_press=self.send_reminders_handler,
            style=Pack(padding=5, font_size=16, width=150, background_color=ORANGE)
        )

        # Układ elementów w poziomym pudełku
        input_box = toga.Box(style=Pack(direction=ROW, alignment=LEFT, padding=(5, 10)))
        input_box.add(self.friend_name_input)
        input_box.add(add_friend_button)
        input_box.add(edit_friend_button)

        expense_box = toga.Box(style=Pack(direction=ROW, alignment=LEFT, padding=(5, 10)))
        expense_box.add(self.expense_description_input)
        expense_box.add(self.expense_amount_input)
        expense_box.add(self.friend_selection)
        expense_box.add(add_expense_button)
        expense_box.add(edit_expense_button)

        action_box = toga.Box(style=Pack(direction=ROW, alignment=LEFT, padding=(5, 10)))
        action_box.add(split_expenses_button)
        action_box.add(report_button)
        action_box.add(reset_button)
        action_box.add(reminder_button)

        filter_box = toga.Box(style=Pack(direction=ROW, alignment=LEFT, padding=(5, 10)))
        filter_box.add(toga.Label('Filter by Friend:', style=Pack(padding=(0, 5), color=WHITE)))
        filter_box.add(self.filter_friend_selection)

        # Widżet tabeli do wyświetlania znajomych i rachunków
        self.friend_table = toga.Table(
            headings=['Friend Name', 'Actions'],
            data=[],
            style=Pack(padding=5, width=500, height=200, background_color=WHITE)
        )

        self.expense_table = toga.Table(
            headings=['Description', 'Amount', 'Friend', 'Actions'],
            data=[],
            style=Pack(padding=5, width=500, height=200, background_color=WHITE)
        )

        # Etykieta do wyświetlania sumarycznego kosztu
        self.total_label = toga.Label(
            'Total: $0.00',
            style=Pack(padding=(10, 0), font_size=20, text_align=CENTER, color=RED)
        )

        # Dodanie widżetów do głównego pudełka
        main_box.add(hello_label)
        main_box.add(input_box)
        main_box.add(expense_box)
        main_box.add(filter_box)
        main_box.add(action_box)
        main_box.add(self.friend_table)
        main_box.add(self.expense_table)
        main_box.add(self.total_label)

        # Ustawienie zawartości głównego okna
        # Update the existing main window's content and title
        self.main_window.content = main_box
        self.main_window.title = "Expense Manager"

    def add_friend_handler(self, widget):
        # Obsługa dodawania znajomego
        friend_name = self.friend_name_input.value
        if friend_name:
            self.friend_selection.items.append(friend_name)
            self.filter_friend_selection.items.append(friend_name)
            remove_button = toga.Button('Remove', on_press=self.remove_friend_handler,
                                        style=Pack(background_color=RED, color=WHITE))
            self.friend_table.data.append((friend_name, remove_button))
            self.friend_name_input.value = ''
            self.show_message('Friend Added', f'{friend_name} has been added.')

    def edit_friend_handler(self, widget):
        # Obsługa edycji znajomego
        selected = self.friend_table.selection
        if selected:
            new_name = self.friend_name_input.value
            if new_name:
                # Update friend name in friend_table and friend_selection
                old_name = selected.friend_name
                selected.friend_name = new_name
                self.friend_selection.items[self.friend_selection.items.index(old_name)] = new_name
                self.filter_friend_selection.items[self.filter_friend_selection.items.index(old_name)] = new_name

                # Update friend name in expenses
                for row in self.expense_table.data:
                    if row.friend == old_name:
                        row.friend = new_name

                self.show_message('Friend Edited', f'{new_name} has been updated.')

    def remove_friend_handler(self, widget):
        # Obsługa usuwania znajomego
        selected = self.friend_table.selection
        if selected:
            self.friend_selection.items.remove(selected.friend_name)
            self.filter_friend_selection.items.remove(selected.friend_name)
            self.friend_table.data.remove(selected)
            self.show_message('Friend Removed', f'{selected.friend_name} has been removed.')

    def add_expense_handler(self, widget):
        # Obsługa dodawania rachunku
        description = self.expense_description_input.value
        amount = self.expense_amount_input.value
        friend = self.friend_selection.value
        if description and amount and friend:
            remove_button = toga.Button('Remove', on_press=self.remove_expense_handler,
                                        style=Pack(background_color=RED, color=WHITE))
            self.expense_table.data.append((description, f"${amount:.2f}", friend, remove_button))
            self.expense_description_input.value = ''
            self.expense_amount_input.value = 0
            self.update_total()
            self.show_message('Expense Added',
                              f'Expense "{description}" of amount ${amount:.2f} has been added for {friend}.')

    def edit_expense_handler(self, widget):
        # Obsługa edycji rachunku
        selected = self.expense_table.selection
        if selected:
            new_description = self.expense_description_input.value
            new_amount = self.expense_amount_input.value
            new_friend = self.friend_selection.value
            if new_description and new_amount and new_friend:
                selected.description = new_description
                selected.amount = f"${new_amount:.2f}"
                selected.friend = new_friend
                self.update_total()
                self.show_message('Expense Edited',
                                  f'Expense "{new_description}" of amount ${new_amount:.2f} has been updated for {new_friend}.')

    def remove_expense_handler(self, widget):
        # Obsługa usuwania rachunku
        selected = self.expense_table.selection
        if selected:
            self.expense_table.data.remove(selected)
            self.update_total()
            self.show_message('Expense Removed',
                              f'Expense "{selected.description}" of amount {selected.amount} for {selected.friend} has been removed.')

    def update_total(self):
        # Aktualizacja sumarycznego kosztu
        total = sum(float(row.amount[1:]) for row in self.expense_table.data)
        self.total_label.text = f"Total: ${total:.2f}"

    def split_expenses_handler(self, widget):
        # Dzielenie kosztów
        friend_expenses = {friend: 0 for friend in self.friend_selection.items}
        print("Initial friend_expenses:", friend_expenses)

        for row in self.expense_table.data:
            friend_name = row.friend
            amount = float(row.amount[1:])
            print(f"Processing row: friend={friend_name}, amount={amount}")
            if friend_name not in friend_expenses:
                friend_expenses[friend_name] = 0
            friend_expenses[friend_name] += amount
            print("Updated friend_expenses:", friend_expenses)

        # Przesunięcie pętli do przodu o tyle ile jest wpisanych osób
        start_index = len(self.friend_selection.items)

        split_message = "Expense Split Report:\n\n"
        split_message += "Friends:\n"
        for index, (friend, amount) in enumerate(friend_expenses.items(), start=start_index):
            split_message += f"{friend}: ${amount:.2f}\n"
            print(f"Friend: {friend}, Amount: ${amount:.2f}")

        self.show_message('Split Expenses', split_message)

    def reset_handler(self, widget):
        # Resetowanie aplikacji
        self.friend_table.data.clear()
        self.expense_table.data.clear()
        self.friend_selection.items.clear()
        self.filter_friend_selection.items = ['All']
        self.update_total()
        self.show_message('Reset', 'All data has been reset.')

    def generate_report_handler(self, widget):
        # Generowanie raportu
        report = "Expense Report:\n\n"
        report += "Friends:\n"
        for friend in self.friend_table.data:
            report += f"- {friend.friend_name}\n"
        report += "\nExpenses:\n"
        for expense in self.expense_table.data:
            report += f"- {expense.description}: {expense.amount} (for {expense.friend})\n"
        report += f"\nTotal Expenses: {self.total_label.text}"

        with open('expense_report.txt', 'w') as file:
            file.write(report)

        self.show_message('Expense Report',
                          f'The expense report has been generated and saved as expense_report.txt.\n\n{report}')

    def send_reminders_handler(self, widget):
        # Wysyłanie przypomnień o długach
        friend_expenses = {friend: 0 for friend in self.friend_selection.items}
        for row in self.expense_table.data:
            friend_name = row.friend
            amount = float(row.amount[1:])
            if friend_name not in friend_expenses:
                friend_expenses[friend_name] = 0
            friend_expenses[friend_name] += amount

        reminder_message = "Debt reminders sent as follows:\n\n"
        for friend, amount in friend_expenses.items():
            if amount > 0:
                reminder_message += f"Reminder sent to {friend} for ${amount:.2f}\n"

        self.show_message('Debt Reminders', reminder_message)

    def show_message(self, title, message):
        # Wyświetlanie komunikatu
        self.main_window.info_dialog(title, message)

    

def main():
    return ExpenseManager(formal_name='Expense Manager', app_id='org.beeware.expensemanager')

if __name__ == '__main__':
    main().main_loop()
