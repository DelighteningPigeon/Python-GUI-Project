import random
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import requests
root = Tk()


# MAIN MENU
def main_menu():
    global MainMenu
    global heart
    global apple
    root.title("TIMELESS SOULS CORPORATION")
    root.geometry("760x507")
    root.configure(bg="#ffffff")
    canvas = Canvas(root, bg="#ffffff", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    MainMenu = PhotoImage(file=f"MAIN MENU.png")
    heart = PhotoImage(file=f"heart.png")
    apple = PhotoImage(file=f"apple.png")
    canvas.create_image(0, 0, image=MainMenu, anchor='nw')
    Button(text=" ", height=70, width=80, image=heart, command=login_page).place(x=537, y=194)
    Button(text=" ", height=75, width=85, image=apple, command=register_page).place(x=537, y=349)


def back():
    global login_page
    login_page()


def login_page():
    global username_verify
    global password_verify
    global login_page
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    root.title("SOUL ACTIVATION")
    root.geometry("760x507")
    root.configure(bg="#ffffff")
    canvas = Canvas(root, bg="#ffffff", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    login_page = PhotoImage(file=f"LOGIN.png")
    canvas.create_image(0, 0, image=login_page, anchor='nw')
    Label(root, text="ENTER THE NAME OF YOUR BODY", width=57, height=3, bg="black", fg="white").place(x=176, y=127)
    username_entry1 = Entry(root, textvariable=username_verify, width=50)
    username_entry1.place(x=230, y=180)
    Label(root, text="ENTER THE SECRETS TO YOUR MIND", width=57, height=3, bg="black", fg="white").place(x=176, y=265)
    password_entry1 = Entry(root, textvariable=password_verify, width=50)
    password_entry1.place(x=230, y=318)
    Button(root, text="TO SOUL'S\nMANUAL", width=20, height=6, command=lambda: login(username_entry1.get(), password_entry1.get()), bg="black",
           fg="white").place(x=305, y=366)
    Button(root, text="Back to the\nTimeless Souls", width=17, height=3, command=main_menu).place(x=50, y=400)


def register_page():
    global RegisterPage
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    root.title("SOUL SEARCH")
    root.geometry("760x507")
    root.configure(bg="#ffffff")
    canvas = Canvas(root, bg="#ffffff", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    RegisterPage = PhotoImage(file=f"REGISTER.png")
    canvas.create_image(0, 0, image=RegisterPage, anchor='nw')
    Label(root, text="ENTER THE NAME OF YOUR BODY", width=57, height=3, bg="black", fg="white").place(x=176, y=127)
    username_entry = Entry(root, textvariable=username, width=50)
    username_entry.place(x=230, y=180)
    Label(root, text="ENTER THE SECRETS TO YOUR MIND", width=57, height=3, bg="black", fg="white").place(x=176, y=265)
    password_entry = Entry(root, textvariable=password, width=50)
    password_entry.place(x=230, y=318)
    Button(root, text="Ready for the heart?", width=23, height=3, command=lambda: register(username_entry.get(), password_entry.get()), bg="black",
           fg="white").place(x=295, y=400)
    Button(root, text="Back to the\nTimeless Souls", width=17, height=3, command=back).place(x=50, y=400)


def login(username, password):
    correct = False
    file = open("accounts.txt", "r")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if a == username and b == password:
            correct = True
            break
    file.close()
    if correct:
        tkinter.messagebox.showinfo("Now we take you on a trip young sprite", "See you in your Soul's Manual")
        soul_manual_page()
    else:
        tkinter.messagebox.showerror("Unsuccessful login",
                                     "Wrong username or password, please try again. If you wish to "
                                     "create a new account\nplease proceed to Create Account.")


def register(username, password):
    check = True
    file = open("accounts.txt", "r")
    for i in file:
        a, b = i.split(",")
        if a == username:
            tkinter.messagebox.showwarning("Invalid operation", "Looks like you already have a soul"
                                                                "Take the heart or find a new soul.")
            check = False
    file.close()
    if not check:
        return
    elif username == "" or password == "":
        tkinter.messagebox.showwarning("Invalid operation", "Please try again.")
    else:
        file = open("accounts.txt", "a")
        file.write("\n" + username + "," + password)
        tkinter.messagebox.showinfo("Greetings: {}".format(username),
                                    "\nYour soul have been found\nNow you may take the heart.")
        main_menu()


def soul_manual_page():
    global manual
    root.title("SOUL'S MANUAL")
    root.geometry("760x507")
    root.configure(bg="#ffffff")
    canvas = Canvas(root, bg="#ffffff", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    manual = PhotoImage(file=f"MANUAL.png")
    canvas.create_image(0, 0, image=manual, anchor='nw')
    Button(root, text="Guide My Soul", width=28, height=3, command=sky, bg="black", fg="white").place(x=498, y=394)


def print_quote(quotes, strlist, color1, color2):
    Button(root, text="There you go\nsee you tomorrow.", width=20, height=3, command=exit, bg="#800000",
           fg="white").place(x=303, y=451)
    for quote in quotes:
        strlist.append(quote.text)
    checker = random.randint(0, len(strlist))
    my_label = tkinter.Label(root)
    my_label.config(font=("Helvetica", 10), text=strlist[checker].replace('.', '.\n').replace(',', '\n'), fg=color1,
                    bg=color2)
    my_label.pack()


def feels_quote():
    strlist = []
    html_text = requests.get('https://www.keepinspiring.me/quotes-about-feelings/').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('blockquote', class_='wp-block-quote is-style-large')
    print_quote(quotes, strlist, '#1CC6A0', '#DA2F18')


def sad_quote():
    strlist = []
    html_text = requests.get('https://www.keepinspiring.me/quotes-about-sadness/').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('blockquote', class_='wp-block-quote is-style-large')
    print_quote(quotes, strlist, '#DE8532', '#121090')


def happy_quote():
    strlist = []
    html_text = requests.get('https://www.keepinspiring.me/quotes-about-happiness/').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('blockquote', class_='wp-block-quote is-style-large')
    print_quote(quotes, strlist, '#A524A3', '#65DE17')


def fiery_quote():
    strlist = []
    html_text = requests.get('https://www.keepinspiring.me/hard-work-quotes/').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('blockquote', class_='wp-block-quote is-style-large')
    print_quote(quotes, strlist, '#FE4F09', '#0F8456')


def no_give_up_quote():
    strlist = []
    html_text = requests.get('https://www.keepinspiring.me/quotes-about-not-giving-up-staying-strong/').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('blockquote', class_='wp-block-quote is-style-large')
    print_quote(quotes, strlist, '#F14040', '#24EC2A')


def attitude_quote():
    strlist = []
    html_text = requests.get('https://www.keepinspiring.me/attitude-quotes/').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('blockquote', class_='wp-block-quote is-style-large')
    print_quote(quotes, strlist, '#FE4A22', '#149946')


def self_quote():
    strlist = []
    html_text = requests.get('https://www.keepinspiring.me/quotes-about-being-yourself/').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('blockquote', class_='wp-block-quote is-style-large')
    print_quote(quotes, strlist, '#2C2FF9', '#F9932C')


def improvement_quote():
    strlist = []
    html_text = requests.get('https://www.keepinspiring.me/24-quotes-moving-on-forward-thinking/').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('blockquote', class_='wp-block-quote is-style-large')
    print_quote(quotes, strlist, '#7D3FD3', '#EBDE60')


def sky():
    global sky
    root.title("YOUR JOURNEY")
    root.geometry("760x507")
    canvas = Canvas(root, bg="#2F94F5", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    sky = ImageTk.PhotoImage(Image.open("SKY.jpg"))
    image_store = Label(image=sky)
    image_store.place(x=125, y=80)
    Button(root, text=":)", width=6, height=3, command=work, bg="green", fg="white").place(x=708, y=451)
    Button(root, text=":|", width=6, height=3, command=animal, bg="red", fg="white").place(x=0, y=451)


def work():
    global work
    root.title("YOUR JOURNEY")
    root.geometry("760x507")
    canvas = Canvas(root, bg="#121313", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    work = ImageTk.PhotoImage(Image.open("WORKPLACE.jpg"))
    image_store = Label(image=work).place(x=14, y=10)
    Button(root, text=":)", width=6, height=3, command=ocean, bg="green").place(x=708, y=451)
    Button(root, text=":|", width=6, height=3, command=man, bg="red").place(x=0, y=451)


def animal():
    global animal
    root.title("YOUR JOURNEY")
    root.geometry("760x507")
    canvas = Canvas(root, bg="#E3533E", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    animal = ImageTk.PhotoImage(Image.open("DOGANDCAT.jpg"))
    image_store = Label(image=animal)
    image_store.place(x=73, y=21)
    Button(root, text=":)", width=6, height=3, command=beach, bg="green").place(x=708, y=451)
    Button(root, text=":|", width=6, height=3, command=rain, bg="red").place(x=0, y=451)


def beach():
    global beach
    root.title("YOUR JOURNEY")
    root.geometry("760x507")
    canvas = Canvas(root, bg="#0CDCEE", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    beach = ImageTk.PhotoImage(Image.open("BEACH.jpeg"))
    image_store = Label(image=beach).place(x=68, y=10)
    Button(root, text=":)", width=6, height=3, command=self_quote, bg="green").place(x=708, y=451)
    Button(root, text=":|", width=6, height=3, command=improvement_quote, bg="red").place(x=0, y=451)


def rain():
    global rain
    root.title("YOUR JOURNEY")
    root.geometry("760x507")
    canvas = Canvas(root, bg="#ffffff", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    rain = ImageTk.PhotoImage(Image.open("RAIN.jpg"))
    image_store = Label(image=rain).place(x=0, y=0)
    Button(root, text=":)", width=6, height=3, command=feels_quote, bg="green").place(x=708, y=451)
    Button(root, text=":|", width=6, height=3, command=sad_quote, bg="red").place(x=0, y=451)


def man():
    global man
    root.title("YOUR JOURNEY")
    root.geometry("760x507")
    canvas = Canvas(root, bg="#FFE096", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    man = ImageTk.PhotoImage(Image.open("SUCCESSFULMAN.jpg"))
    image_store = Label(image=man).place(x=65, y=24)
    Button(root, text=":)", width=6, height=3, command=fiery_quote, bg="green").place(x=708, y=451)
    Button(root, text=":|", width=6, height=3, command=no_give_up_quote, bg="red").place(x=0, y=451)


def ocean():
    global ocean
    root.title("YOUR JOURNEY")
    root.geometry("760x507")
    canvas = Canvas(root, bg="#0F3D69", height=507, width=760, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    ocean = ImageTk.PhotoImage(Image.open("OCEAN.jpg"))
    image_store = Label(image=ocean).place(x=65, y=60)
    Button(root, text=":)", width=6, height=3, command=happy_quote, bg="green").place(x=708, y=451)
    Button(root, text=":|", width=6, height=3, command=attitude_quote, bg="red").place(x=0, y=451)


main_menu()

root.mainloop()
