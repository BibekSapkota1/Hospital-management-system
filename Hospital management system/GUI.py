from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from tkinter import *
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == 'admin' and password == '123':
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror('Error', 'Incorrect username or password.')

def main_window():
    # main window
    window = Tk()
    window.title('Hospital Management System')

    # Add your GUI elements and functionality here
    window.mainloop()

# login window
login_window = Tk()
login_window.title('Login')

# username label and entry
username_label = Label(login_window, text='Username:')
username_label.pack()
username_entry = Entry(login_window)
username_entry.pack()

# password label and entry
password_label = Label(login_window, text='Password:')
password_label.pack()
password_entry = Entry(login_window, show='*')
password_entry.pack()

#login button
login_button = Button(login_window, text='Login', command=login)
login_button.pack()

#login window
login_window.mainloop()