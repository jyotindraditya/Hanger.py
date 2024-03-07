from tkinter import *
import random
from string import ascii_uppercase
from tkinter import messagebox

def random_pair():
    pairs= {"UBISOFT": PhotoImage(file="objects/ubisoftimg.png"), "METALLICA": PhotoImage(file="objects/metallicaimg.png"),
            "PYTHON": PhotoImage(file="objects/pythonimg.png"), "BATMAN": PhotoImage(file="objects/batmanimg.png"),
            "BLENDER": PhotoImage(file="objects/blenderimg.png"), "TWITCH": PhotoImage(file="objects/twitchimg.png"),
            "GITHUB": PhotoImage(file="objects/githubimg.png"), "QUEEN": PhotoImage(file="objects/queenimg.png")}
    rword = random.choice(list(pairs.keys()))
    rimage = pairs[rword]
    return rword, rimage

def new_game():
    global the_word
    global total_guesses
    total_guesses=0
    global rword, rimage
    rword, rimage = random_pair()
    image_stick()
    hanglabel.configure(image=hanged[0])
    the_word=" ".join(rword)
    letters_l.set(" ".join("_"*len(rword)))

def image_stick():
    f2=Frame(m, width=50, height=50)
    Label(f2, image=rimage).grid(row=0, column=0)
    f2.grid(row=1, column=10, columnspan=6, padx=0, pady=20)

def guess(letter):
    global total_guesses
    if total_guesses<11:
        txt=list(the_word)
        guessed=list(letters_l.get())
        if the_word.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                    letters_l.set("".join(guessed))
                    if letters_l.get()==the_word:
                        messagebox.showinfo("Hangman", "You guessed it! \nNot too shabby for a grownup")
                        new_game()
        else:
            total_guesses+=1
            hanglabel.config(image=hanged[total_guesses])
            if total_guesses==11:
                hanglabel.configure(image=hanged[12])
                messagebox.showwarning("Hangman", "Game over \nYou're not the sharpest tool in the shed")
                new_game()

m= Tk()
m.title('Hangman')
m.geometry("1700x900")
backg=PhotoImage(file="killer(0).png")
wall=Label(m, image=backg)
wall.place(x=0,y=0)
t = Label(text="    HANGMAN    ", font="comicsansms 30 bold", borderwidth=3, bg="white", fg="black", relief=SUNKEN)
t.grid(row=0, column=10)

#icon
m.iconbitmap("yoshi.ico")

letters_l= StringVar()
Label(m, textvariable=letters_l, font="comicsansms 25 bold").grid(row=3, column=10, pady=50)

#keyboard
n=0
for c in ascii_uppercase:
    Button(m, text=c, command=lambda c=c: guess(c), font="Helvetica 20", width=3).grid(row=5+n//9, column=n%9)
    n=n+1
Button(m, text="Quit", command=m.quit, font="Helvetica 15", width=3).grid(row=7, column=8)

#Hangedman gallery
hanged = [PhotoImage(file="hanged/hang0.png"), PhotoImage(file="hanged/hang1.png"), PhotoImage(file="hanged/hang2.png"),
          PhotoImage(file="hanged/hang3.png"), PhotoImage(file="hanged/hang4.png"), PhotoImage(file="hanged/hang5.png"),
          PhotoImage(file="hanged/hang6.png"), PhotoImage(file="hanged/hang7.png"), PhotoImage(file="hanged/hang8.png"),
          PhotoImage(file="hanged/hang9.png"), PhotoImage(file="hanged/hang10.png"), PhotoImage(file="hanged/hang11.png"),
          PhotoImage(file="hanged/tarot12.png")]

hanglabel=Label(m, bg="black")
hanglabel.grid(row=1, column=0, columnspan=6, padx=3)
hanglabel.configure(image=hanged[0])

new_game()

m.mainloop()
