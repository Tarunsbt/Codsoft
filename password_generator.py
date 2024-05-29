import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.current_input = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill="both")

        display = tk.Label(display_frame, textvariable=self.result_var, font=("Arial", 24), anchor="e", bg="white", fg="black")
        display.pack(expand=True, fill="both")

        # Buttons
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 0
        col_val = 0
        for button in buttons:
            button_command = lambda x=button: self.on_button_click(x)
            b = tk.Button(buttons_frame, text=button, font=("Arial", 18), command=button_command)
            b.grid(row=row_val, column=col_val, sticky="nsew")

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Make the buttons expand
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
            buttons_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.current_input))
                self.current_input = result
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
                self.current_input = ""
        elif char in "0123456789.+-*/":
            self.current_input += str(char)
            self.result_var.set(self.current_input)
        else:
            self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
