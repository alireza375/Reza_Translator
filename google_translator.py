from tkinter import *
from tkinter import ttk, messagebox
from google_trans_new.google_trans_new import google_translator as trans
from google_trans_new.google_trans_new import LANGUAGES


def getText(text, target):
    translated = trans().translate(text=text, lang_tgt=target)
    print(translated)
    return translated

root = Tk()
root.title("Google Translator 2.0")
root.geometry("1150x400")
root.resizable(False,False)
root.configure(background="white")


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)


def translate_now():
    try:
        text_ = text1.get(1.00, END)
        c2 = combo1.get()
        c3 = combo2.get().lower()
        if(text_):
            for i, j in LANGUAGES.items():
                if(j == c3):
                    lan_ = i
            words = getText(text_, lan_)
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        print(e)
        messagebox.showerror("Google Translator 2.0","Please try again.")

# icon setup
image_icon = PhotoImage(file="./icon.png")
root.iconphoto(False,image_icon)

# bg translate image arrow setup
arrow_image = PhotoImage(file="./images.png")
image_label = Label(root,image=arrow_image,width=217,)
image_label.place(x=460,y=50)


languageV = [lang.upper() for lang in LANGUAGES.values()]
lang1 = LANGUAGES.keys()

# first combobox
combo1 = ttk.Combobox(
    root,
    values=languageV,
    font="Roboto 14",
    state="r"
)
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1 = Label(
    root,
    text="ENGLISH",
    font="segoe 30 bold",
    bg="white",
    width=18,
    bd=5,
    relief = GROOVE
)
label1.place(x=10,y=50)

# first frame
f = Frame(root,bg="Black",bd=5)
f.place(x=10,y=145,height=210,width=440)

text1 = Text(
    f,
    font="Robote 20",
    bg="white",
    relief=GROOVE,
    wrap=WORD
)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# Second combobox
combo2 = ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=800,y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(
    root,
    text="ENGLISH",
    font="segoe 30 bold",
    bg="white",
    width=18,
    bd=5,
    relief = GROOVE
)
label2.place(x=690,y=50)

# Second frame
f1 = Frame(root,bg="Black",bd=5)
f1.place(x=690,y=145,height=210,width=440)

text2 = Text(
    f1,
    font="Robote 20",
    bg="white",
    relief=GROOVE,
    wrap=WORD
)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#translate button
translate = Button(
    root,
    text="Translate",
    font=("Robote", 15),
    activebackground="white",
    width=10,
    height=1,
    cursor="hand2",
    bd=1,bg="black",
    fg="white",
    command=translate_now
)

translate.place(x=515, y=308)

label_change()
root.mainloop()
