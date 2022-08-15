from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_cond = [random.choice(letters) for char in range(random.randint(8, 10))]
    symbol_cond = [random.choice(symbols) for sym in range(random.randint(2, 4))]
    num_cond = [random.choice(numbers) for num in range(random.randint(2, 4))]

    password_list = letters_cond + symbol_cond + num_cond
    random.shuffle(password_list)
    password = "".join(password_list)
    # print(f"Your password is: {password}")
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(web, email, password):
    with open(file="pass.txt", mode="a") as pass_file:
        pass_file.write(f"\n{web} | {email} | {password}")
        pass_file.close()


def add_click():
    website_value = website_entry.get()
    email_value = Email_entry.get()
    pass_value = pass_entry.get()
    if website_value == "" or email_value == "" or pass_value == "":
        empty = messagebox.showinfo(title="Incorect", message="Hey!, Please enter the required fields")
        print(website_entry, pass_value)
    else:
        confirmation = messagebox.askokcancel(title=website_value,
                                              message=f"These are the details entered: \nEmail: {email_value} \nPassword: {pass_value} \nis this ok to save? ")

    if confirmation:
        save(web=website_value, email=email_value, password=pass_value)
        website_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password-Manager")
window.config(width=400, height=400, bg="white")
window.config(padx=20, pady=20)
window.config()

### loading image ###
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_pad = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_pad)
canvas.grid(column=1, row=1)

# square overlay
# canvas.create_rectangle(0, 0, 200, 200, outline="black")
# canvas.grid(column=0, row=1)

# label layout

website_label = Label(text="Website: ", bg="white", justify=LEFT, font=("Arial", 12, "bold"))
website_label.grid(column=0, row=4)

email_label = Label(text="Email/Username: ", bg="white", font=("Arial", 12, "bold"))
email_label.grid(column=0, row=5)

pass_label = Label(text="Password: ", bg="white", font=("Arial", 12, "bold"))
pass_label.grid(column=0, row=6)

# Entry layout

website_entry = Entry(width=36)

website_entry.focus()
website_entry.grid(column=1, row=4, columnspan=2)

Email_entry = Entry(width=36)
Email_entry.insert(0, "vicknesh@gmail.com")

Email_entry.grid(column=1, row=5, columnspan=2)

pass_entry = Entry(width=23)

pass_entry.grid(column=1, row=6)

# button layout

gen_but = Button(width=12, text="GeneratePassword", bg="white", font=("Arial", 8, "bold"), command=gen_pass)
gen_but.grid(column=2, row=6)

add_but = Button(width=30, text="Add", bg="white", font=("Arial", 12, "bold"), command=add_click)
add_but.grid(column=1, row=7, columnspan=2)

######## to loop the window ######
window.mainloop()
