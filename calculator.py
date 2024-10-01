from  tkinter import*
x = Tk()

w = StringVar(x)
e = Entry(x, fg = "white", bg = "black", textvariable = w)
e.pack(pady = 50)

for i in ("789/", "456*", "123-", "0.+%"):
    f = Frame(x)
    f.pack()
    for i in i:
        Button(f, text=i, fg = "white", bg = "grey", borderwidth = 6, width = 2, command = lambda w =w, i = i:w.set(w.get()+i)).pack(side = LEFT, pady=5)

f = Frame(x)
f.pack()

#f2 = Frame(x)
