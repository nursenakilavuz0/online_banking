import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def update_balance(new_balance):
    #Update the balance and write it to the file
    with open('money.txt', 'w') as file:
        file.write(str(new_balance))

def get_balance():
    #Read the balance from the file
    try:
        with open('money.txt', 'r') as file:
            return float(file.read().strip())
    except FileNotFoundError:
        return 0.0

def deposit():
    #Handle deposit
    amount = float(word8.get().strip())
    current_balance = get_balance()
    new_balance = current_balance + amount
    update_balance(new_balance)
    showinfo(title='Deposit', message=f'{amount} deposited. New balance: {new_balance}')

def withdraw():
    #Handle withdrawal
    amount = float(word8.get().strip())
    current_balance = get_balance()
    if current_balance >= amount:
        new_balance = current_balance - amount
        update_balance(new_balance)
        showinfo(title='Withdraw', message=f'{amount} withdrawn. New balance: {new_balance}')
    else:
        showinfo(title='Withdraw', message='Insufficient funds.')

def open_account_window():
    #Close the current window and open a new window
    global word8
    # Close the current window
    root.destroy()
    
    # Create a new window
    account_window = tk.Tk()
    account_window.geometry("500x400")
    account_window.resizable(False, False)
    account_window.title('BANKING ACCOUNT')

    # Amount entry field
    word8_label = ttk.Label(account_window, text="AMOUNT:")
    word8_label.pack(fill='x', expand=True)

    word8 = tk.StringVar()
    word8_entry = ttk.Entry(account_window, textvariable=word8)
    word8_entry.pack(fill='x', expand=True)

    # Deposit button
    deposit_button = ttk.Button(account_window, text="DEPOSİT", command=deposit)
    deposit_button.pack(padx=10, pady=10, fill='x')

    # Withdraw button
    withdraw_button = ttk.Button(account_window, text="WITHDRAW", command=withdraw)
    withdraw_button.pack(padx=10, pady=10, fill='x')

    # Start the new window
    account_window.mainloop()

def login_clicked():
    #Callback function when the login button is clicked
    num1 = word1.get().strip()
    num2 = word2.get().strip()

    try:
        with open('data.txt', 'r') as file:
            lines = file.readlines()
            file_name = lines[0].strip()
            file_password = lines[1].strip()

        if num1 == file_name and num2 == file_password:
            # Successful login, open the new window
            open_account_window()
        else:
            showinfo(title='RESULT', message='Invalid name or password.')

    except FileNotFoundError:
        showinfo(title='RESULT', message='File not found.')

# Main window
root = tk.Tk()
root.geometry("500x400")
root.resizable(False, False)
root.title('BANKING ACCOUNT')

word1 = tk.StringVar()
word2 = tk.StringVar()

# Sign-in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# Name/Surname entry field
word1_label = ttk.Label(signin, text="NAME/SURNAME:")
word1_label.pack(fill='x', expand=True)

word1_entry = ttk.Entry(signin, textvariable=word1)
word1_entry.pack(fill='x', expand=True)

# Password entry field
word2_label = ttk.Label(signin, text="PASSWORD:")
word2_label.pack(fill='x', expand=True)

word2_entry = ttk.Entry(signin, textvariable=word2, show='*')
word2_entry.pack(fill='x', expand=True)

# Buttons
buttons_frame = ttk.Frame(signin)
buttons_frame.pack(fill='x', expand=True)

login1_button = ttk.Button(buttons_frame, text="LOG IN", command=login_clicked)
login1_button.pack(side=tk.LEFT, expand=True, padx=10)

# Start the main window
root.mainloop()
