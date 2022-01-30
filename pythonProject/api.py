from tkinter import *


def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "sorry there is no WORD like that please again"
    output.insert(END, definition)


window = Tk()
window.title("WORD DEFINITION")
window.configure(background="black")

photo1 = PhotoImage(file="twitter.jpg")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

Label(window, text="Enter the word you would like a definition for:", bg="black", fg="white", font="none 12 bold").grid(
    row=1, column=0, sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

Button(window, text="Submit", width=6, command=click).grid(row=3, column=0, sticky=W)

Label(window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

output = Text(window, width=75, height=6, wrap=WORD, bg="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

my_compdictionary = {
    'algorithm': 'step by step instructions to complete a task', 'bug': 'piece of code that cause a program to fail'
}

Label(window, text="click to exit", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)


def close_window():
    window.destroy()
    exit()


Button(window, text="exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)

window.mainloop()

"""root=Tk()
root.title("emmy LONDALA")
root.geometry("700x690")
root.config(bg="black")
photo1 = PhotoImage(file="twitter.jpg")
Label (root, image=photo1, bg="black").grid(row=0, column=0, sticky=E)



root.mainloop()"""
