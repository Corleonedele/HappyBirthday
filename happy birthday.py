from tkinter import *
from tkinter import messagebox

root = Tk()
root.title = ('To JIAJIA')
root.geometry('750x250')

btn01 = Button(root, bg='pink')
btn01['text'] = 'One'
btn01.pack(side='left', padx='5')

btn02 = Button(root)
btn02['text'] = 'Two'
btn02['bg'] = 'pink'
btn02.pack(side='left', padx='5')

btn03 = Button(root)
btn03['text'] = 'Three'
btn03['bg'] = 'pink'
btn03.pack(side='left', padx='5')

btn04 = Button(root)
btn04['text'] = 'four'
btn04['bg'] = 'pink'
btn04.pack(side='left', padx='5')

btnQ = Button(root, text='Quit', command=root.destroy)
btnQ['bg'] = 'pink'
btnQ.pack(side='left', padx='5')

photo = PhotoImage(file='1.gif')
lab01 = Label(root, text='To you', image=photo)
lab01.pack()

def birthWord1(e):
    messagebox.showinfo('Massage', "Happy birthday JIAJIA")

def birthWord2(e):
    messagebox.showinfo('Massage', "I'm so lucky to meet you and I'm really really like you")

def birthWord3(e):
    messagebox.showinfo('Massage', "I will nerver never be able to get enough of you")

def birthWord4(e):
    messagebox.showinfo('Massage', "Thank you hope happiness is always with you!")

btn01.bind('<Button-1>',birthWord1)
btn02.bind('<Button-1>',birthWord2)
btn03.bind('<Button-1>',birthWord3)
btn04.bind('<Button-1>',birthWord4)

root.mainloop()