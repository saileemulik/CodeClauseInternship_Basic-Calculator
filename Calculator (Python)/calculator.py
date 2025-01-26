import tkinter as tk
def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

def clear_display():
    display.delete(0, tk.END)

def cancel():
    current_text = display.get()
    display.delete(len(current_text)-1, tk.END)

def evaluate_expression():
    expression = display.get() 
    try:
        expression = expression.replace(' ', '')
        num_stack = []
        operator = '+'
        num = 0
        is_float = False  
        decimal_place = 0.1
        for i, char in enumerate(expression):
            if char.isdigit():
                if is_float:
                    num += int(char) * decimal_place
                    decimal_place /= 10
                else:
                    num = num * 10 + int(char)
            elif char == '.':
                is_float = True 
            if char in '+-*/%' or i == len(expression) - 1:
                if not char.isdigit() and char != '.':
                    is_float = False
                    decimal_place = 0.1
                if operator == '+':
                    num_stack.append(num)
                elif operator == '-':
                    num_stack.append(-num)
                elif operator == '*':
                    num_stack[-1] = num_stack[-1] * num
                elif operator == '%':
                    num_stack[-1] = num_stack[-1] % num
                elif operator == '/':
                    if num == 0:
                        num_stack[-1] = "Error: Cannot divide by zero"
                        break
                    num_stack[-1] = num_stack[-1] / num
                num = 0 
                operator = char  
       
        result = sum(num_stack)

        display.delete(0, tk.END)
        display.insert(0, str(result))
        # display.insert(0, tk.END)
        
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error: Invalid Expression")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x500")
root.resizable(True,True)

display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('X', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0),('/', 5, 1), ('.', 5, 2), ('=', 5, 3),
]

for text, row, col in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 14), bg="#4CAF50", fg="white",
                        command=evaluate_expression, height=2, width=5)
    elif text =='C':
        btn = tk.Button(root, text="C", font=("Arial", 14), bg="red", fg="white", command=clear_display, height=2, width=5)
    elif text =='X':
        btn = tk.Button(root, text="X", font=("Arial", 14), bg="red", fg="white", command=cancel, height=2, width=5)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14), bg="#f0f0f0",
                        command=lambda t=text: button_click(t), height=2, width=5)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
# cancel_btn = tk.Button(root, text="X", font=("Arial", 14), bg="red", fg="white", command=cancel, height=2, width=5)
# cancel_btn.grid(row=5, column=2, columnspan=4, pady=5)

# clear_btn = tk.Button(root, text="C", font=("Arial", 14), bg="red", fg="white", command=clear_display, height=2, width=5)
# clear_btn.grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()