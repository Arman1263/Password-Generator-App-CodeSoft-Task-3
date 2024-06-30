from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_combine = small_alphabets+capital_alphabets+numbers+special_characters
    password_length = int(length_box.get())

    if choice.get()==1:
        password_field.insert(0, random.sample(small_alphabets, password_length))

    if choice.get()==2:
        password_field.insert(0, random.sample(small_alphabets+capital_alphabets, password_length))

    if choice.get()==3:
        password_field.insert(0, random.sample(all_combine, password_length))

    # password = random.sample(all_combine, password_length)
    # password_field.insert(0, password)


def copy():
    random_password = password_field.get()
    pyperclip.copy(random_password)

root = Tk()
root.config(bg='gray20')

# variables 
choice = IntVar()
Font = ('arial', 13, 'bold')

passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)

# radio button weak, medaium, strong
weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradioButton.grid(pady=5) 

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradioButton.grid(pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradioButton.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid()

# spin box
length_box = Spinbox(root, from_=5, to=15, width=5, font=Font)
length_box.grid(pady=5)

# generate button
generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

# password field
password_field = Entry(root, width=25, bd=2, font=Font)
password_field.grid(pady=5)

# generate Button
copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(pady=5)

root.mainloop()