import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operation"

    result_label.config(text=f"Result: {result}")

# Create main window
window = tk.Tk()
window.title("Simple Calculator By Parth Patil")

# Entry widgets for user input
entry_num1 = tk.Entry(window, width=20)
entry_num1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

entry_num2 = tk.Entry(window, width=20)
entry_num2.grid(row=0, column=5, columnspan=4, padx=10, pady=10)

# Buttons for each operation
add_button = tk.Button(window, text="+", command=lambda: operation_var.set("+"))
add_button.grid(row=1, column=0, padx=5, pady=5)

subtract_button = tk.Button(window, text="-", command=lambda: operation_var.set("-"))
subtract_button.grid(row=1, column=1, padx=5, pady=5)

multiply_button = tk.Button(window, text="*", command=lambda: operation_var.set("*"))
multiply_button.grid(row=1, column=2, padx=5, pady=5)

divide_button = tk.Button(window, text="/", command=lambda: operation_var.set("/"))
divide_button.grid(row=1, column=3, padx=5, pady=5)

# Button to perform calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=4, pady=10)

# Label to display result
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=3, column=0, columnspan=4, pady=10)

# Variable to store the selected operation
operation_var = tk.StringVar(window)
operation_var.set("+")  # default operation

# Start the main loop
window.mainloop()
