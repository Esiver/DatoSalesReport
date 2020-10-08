import tkinter as tk


HEIGHT = 400
WIDTH = 400

root = tk.Tk()

def button1(Entry):
    print(Entry)
    body_label['text'] = Entry
    import cvsreader

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#fff3b0')
canvas.pack()

#background_image = tk.PhotoImage(file='datologo.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(x=0,y=0, relwidth=1, relheight=1)

header = tk.Frame(root, bg='#9e2a2b')
header.place( rely=0.1, width=WIDTH, height=HEIGHT/5)

entry = tk.Entry(header, bg='#540b0e', fg='#9e2a2b', font=35)
entry.place(relx=0.4 , rely=0.1, relwidth=0.4, height=HEIGHT/10)

button = tk.Button(header, text='Get', bg='#335c67', fg='#fff3b0',command=lambda: button1(entry.get()))
button.place(relx=0.83, rely=0.1, width=WIDTH/8, height=HEIGHT/10)

label = tk.Label(header, text='Input filename:', bg='#540b0e', fg='#fff3b0')
label.place(relx=0.02, rely=0.1, relwidth=0.35, height=HEIGHT/10)

body = tk.Frame(root, bg='#9e2a2b')
body.place(rely=0.5, width=WIDTH, height=HEIGHT/3)

body_label = tk.Label(body, text='', bg='#540b0e', fg='#fff3b0')
body_label.place(relx=0.02, rely=0.1, relwidth=0.35, height=HEIGHT/10)


root.mainloop()

