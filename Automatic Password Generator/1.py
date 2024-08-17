from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
from PIL import ImageTk, Image
from PIL import Image
from IPython.display import display  


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    nl=" "
    for i in range(0,randint(6, 10)):
        l=choice(letters)
        nl+=l 

    nn=" "
    for i in range(0, randint(4, 9)):
        n=choice(numbers)
        nn+=n

    ns=" "
    for i in range(0, randint(4, 9)):
        s=choice(symbols)
        ns+=s

    g=list(nl+nn+ns)
    v=sample(g,len(g))

    c1="".join(v)

    pas_e.delete(0, END)
    pas_e.insert(END, c1)
    pas_e.clipboard_append(pas_e.get())
    pyperclip.copy(c1)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = w_e.get().capitalize()
    email = em_e.get()
    password = pas_e.get()
    d = {
        website :
            {
            "email" : email,
            "password" : password, 
        }
    }
    if len(website) != 0 and len(email) != 0 and len(password) != 0 :
        try:
            with open('Data.json', mode='r') as data:
                od = json.load(data)
                od.update(d)
        except FileNotFoundError:
            with open('Data.json', mode='w') as data:
                json.dump(d, data, indent=4)
        else:
            with open('Data.json', mode='w') as data:
                json.dump(od, data, indent=4)

        w_e.delete(0, END)
        pas_e.delete(0, END)
        messagebox.showinfo(title='Password Manager', message="Successfully Saved")

    else:
        messagebox.showwarning(title="Oops", message="Don't leave any field emty!")

# ---------------------------- SEARCH FROM DATABASE ------------------------------- #

def find():
    website = w_e.get().capitalize()
    if len(website) == 0 :
        messagebox.showerror(title='Opps', message='Please fill the Website to find the Password!')
        return None
    try:
        with open('Data.json', mode='r') as data:
            f = json.load(data)

    except FileNotFoundError:
        messagebox.showinfo(title='Opps', message=f'Data for {website} does not exist!')
    
    else:
        if website in f:
            messagebox.showinfo(title=website, message=f'Email/Username : {f[f"{website}"]["email"]}\n\nPassword : {f[f"{website}"]["password"]}')
        elif website not in f:
            messagebox.showerror(title='Opps', message=f'Data for {website} does not exist!')

# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title('Password Manager')
w.config(pady=70, padx=70)

fo =  font=['Merriweather', 14, 'normal']

canv = Canvas(width=500, height=300)
canv.grid(column=2, row=1)

pic = ImageTk.PhotoImage(Image.open("mini.jpg"))
canv.create_image(250, 100, image=pic)

web = Label(text='Website   :', font=fo)
web.grid(column=1, row=2, sticky='e', padx=7)
w_e = Entry(width=39, font=fo)
w_e.grid(row=2, column=2, columnspan=2, pady=7)
w_e.focus()

em = Label(text='Email/Username   :', font=fo)
em.grid(column=1, row=3, padx=7)
em_e = Entry(width=39, font=fo)
em_e.grid(column=2, row=3, columnspan=2, pady=7)
em_e.insert(0, 'example@gmail.com')

pas = Label(text='Password   :', font=fo)
pas.grid(column=1, row=4, sticky='e', padx=7, pady=7)
pas_e = Entry(width=39, font=fo)
pas_e.place(x=265, y=400)

gen = Button(text="Generate One", command=generate, font=['Merriweather', 10, 'normal'])
gen.place(x=645, y=400)

add = Button(text='Add', width=42, command=save, font=['Merriweather', 10, 'normal'])
add.grid(column=2, row=5, columnspan=1, pady=7, padx=5)
re = Button(text='Retrive', width=10, command=find, font=['Merriweather', 10, 'normal'])
re.grid(column=3, row=5)
w.mainloop()