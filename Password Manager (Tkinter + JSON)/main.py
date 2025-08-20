from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = entry_web.get()
    emails = entry_user.get()
    passw = entry_pass.get()

    if len(web) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Oops",message="something empty.")

    else:
        is_ok = messagebox.askyesnocancel(title=web,message=f"These are Details Entered: \nEmail:{emails}\n"
                                                            f" Password:{passw}\n Is It ok to Save?")
        if is_ok:
            with open ("data.txt","a") as data_file:
                data_file.write(f"{web} | {emails} | {passw}\n")
                entry_web.delete(0,END)
                entry_pass.delete(0,END)
                entry_web.focus()
# ---------------------------- UI SETUP ------------------------------- #


window =Tk()
window.title("Password Manger")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock)
canvas.grid(column=1,row=0)

website = Label(text="Website:")
website.grid(column=0,row=1)

email= Label(text="Email/Username:")
email.grid(column=0,row=2)

password1 = Label(text="Password:")
password1.grid(column=0,row=3)

entry_web = Entry(width=35)
entry_web.grid(column=1,row=1,columnspan=2)
entry_web.focus()

entry_user = Entry(width=35,)
entry_user.grid(column=1,row=2,columnspan=2)

entry_user.insert(0,"panchalparthp1919@gmail.com")
entry_pass = Entry(width=21)
entry_pass.grid(column=1,row=3)


generate = Button(text="Generate Password",width=14,command=generate_password)
generate.grid(column=2,row=3)

add = Button(text="Add",width=35,command=save)
add.grid(column=1,row=4,columnspan=2)

window.mainloop()