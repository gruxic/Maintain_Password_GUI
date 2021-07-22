import random
import string
from tkinter import *
from tkinter import messagebox,PhotoImage
import json
import pyperclip
YELLOW = "#f7f5dd"


# ----------------------------------------PASSWORD GENERATOR--------------------#
def passcode(size, d, u, s):
    digits = list(string.digits)
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    symbols = list(string.punctuation)
    comb8 = lower_case
    comb2 = digits + lower_case + upper_case
    comb3 = digits + lower_case + symbols
    comb4 = digits + lower_case
    comb5 = lower_case + upper_case + symbols
    comb6 = lower_case + upper_case
    comb7 = lower_case + symbols
    comb1 = digits + lower_case + upper_case + symbols

    r_digit = random.choice(digits)
    r_lcase = random.choice(lower_case)
    r_ucase = random.choice(upper_case)
    r_symb = random.choice(symbols)

    # CASE 1
    if d is True & u is True & s is True:
        temp_pass = r_digit + r_lcase + r_symb + r_ucase
        for n in range(size - 4):
            temp_pass = temp_pass + random.choice(comb1)
        temp_pass_l = list(temp_pass)

        password = sorted(temp_pass_l, key=lambda k: random.random())
        f_password = ''
        for char in password:
            f_password = f_password + char
        return f_password

    # CASE 2
    elif (d is True) and (u is True) and (s is False):
        temp_pass = str(r_digit) + str(r_lcase) + str(r_ucase)
        for n in range(size - 3):
            temp_pass = temp_pass + str(random.choice(comb2))
        temp_pass_l = list(temp_pass)

        password = sorted(temp_pass_l, key=lambda k: random.random())
        f_password = ''
        for char in password:
            f_password = f_password + char
        return f_password

    # CASE 3
    elif (d == True) & (u == False) & (s == True):
        temp_pass = r_digit + r_lcase + r_symb
        for n in range(size - 3):
            temp_pass = temp_pass + random.choice(comb3)
        temp_pass_l = list(temp_pass)

        password = sorted(temp_pass_l, key=lambda k: random.random())
        f_password = ''
        for char in password:
            f_password = f_password + char
        return f_password

    # CASE 4
    elif ((d == True) & (u == False) & (s == False)):
        temp_pass = str(r_digit) + r_lcase
        for n in range(size - 2):
            temp_pass = temp_pass + str(random.choice(comb4))
        temp_pass_l = list(temp_pass)

        password = sorted(temp_pass_l, key=lambda k: random.random())
        f_password = ''
        for char in password:
            f_password = f_password + char
        return f_password

        # CASE 5
    # CASE 5
    elif ((d == False) & (u == True) & (s == True)):
        temp_pass = r_lcase + r_symb + r_ucase
        for n in range(size - 3):
            temp_pass = temp_pass + random.choice(comb5)
        temp_pass_l = list(temp_pass)

        password = sorted(temp_pass_l, key=lambda k: random.random())
        f_password = ''
        for char in password:
            f_password = f_password + char
        return f_password


    # CASE 6
    elif ((d == False) & (u == True) & (s == False)):
        temp_pass = r_lcase + r_ucase
        for n in range(size - 2):
            temp_pass = temp_pass + random.choice(comb6)
        temp_pass_l = list(temp_pass)

        password = sorted(temp_pass_l, key=lambda k: random.random())
        f_password = ''
        for char in password:
            f_password = f_password + char
        return f_password

    # CASE 7
    elif ((d == False) & (u == False) & (s == True)):
        temp_pass = r_lcase + r_symb
        for n in range(size - 2):
            temp_pass = temp_pass + random.choice(comb7)
        temp_pass_l = list(temp_pass)

        password = sorted(temp_pass_l, key=lambda k: random.random())
        f_password = ''
        for char in password:
            f_password = f_password + char
        return f_password

    # CASE 8
    elif ((d == False) & (u == False) & (s == False)):

        temp_pass = r_lcase
        for n in range(size - 1):
            temp_pass = temp_pass + str(random.choice(comb8))
        temp_pass_l = list(temp_pass)

        password = sorted(temp_pass_l, key=lambda k: random.random())
        f_password = ''
        for char in password:
            f_password = f_password + char
        return f_password

# ----------------------------------------SEARCH PASSWORDS--------------------#
def search_pass(web):
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            mail_data=data[web]["email"]
            password_data= data[web]["password"]
            messagebox.showinfo(title="CREDENTIALS", message=f"\n     {web}"
                                                             f"\n email: {mail_data}"
                                                             f"\n password: {password_data}")

        except:
            messagebox.showinfo(title="ERROR",message="Credentials not found\n")

# ---------------------------------------- SAVE PASSWORD--------------------#

def save_pass():
    is_ok= FALSE
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="ERROR", message="Please make sure you haven't left any fields empty!")

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the credentials you've entered:\n\nEmail: {email}"
                                               f"\nPassword: {password}"
                                               f"\n\nProceed to save it?")
        if(is_ok==True):
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ----------------------------------------UI SETUP--------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
# Load an image in the script
img = PhotoImage(file="lock.png")


canvas.create_image(125, 100, image=img)
canvas.grid(column=1, row=0)
# Website label
label_website = Label(text="Website:", bg=YELLOW)
label_website.grid(column=0, row=1)
# Email/Username label
label_mail = Label(text="Username/Email:", bg=YELLOW)
label_mail.grid(column=0, row=2)
# Password label
label_password = Label(text="Password:", bg=YELLOW)
label_password.grid(column=0, row=3)

# Entries
website = StringVar(window)
email = StringVar(window)
password = StringVar(window)
website_entry = Entry(window, textvariable=website, width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(window, textvariable=email, width=30)
email_entry.grid(column=1, row=2)
password_entry = Entry(window, width=21, textvariable=password)
password_entry.grid(column=1, row=3)

# add_button
add_button = Button(window, text="Add", width=40, command=save_pass)
add_button.grid(row=4, column=1, columnspan=4)
# generate button
gen_button = Button(window, width=10, text="GENERATE", command=lambda: password.set(
    passcode(8, True, True, False)))
gen_button.grid(row=3, column=2)
#SEARCH BUTTON
search_button = Button(window, text="Search", width=15, command=lambda: search_pass(website.get()))
search_button.grid(row=1,column=2)


# ---------------------------------------- END--------------------#

window.mainloop()
