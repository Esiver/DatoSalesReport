import tkinter as tk


HEIGHT = 400
WIDTH = 400

root = tk.Tk()

def full_anal_butt(entry):
    print('Given file {} for full analysis'.format(entry))
    body_label['text'] = entry
    import cvsreader

def week_anal_butt(entry):
    print('Given file {} for full analysis'.format(entry))
    body_label['text'] = 'Given file {} for week analysis'.format(entry)
    import cvsreader

def day_anal_butt(entry):   
    print(entry)
    body_label['text'] = 'Given file {} for day analysis'.format(entry)
    import cvsreader

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#fff3b0')
canvas.pack()

#background_image = tk.PhotoImage(file='datologo.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(x=0,y=0, relwidth=1, relheight=1)

#header for entries & buttons 
header = tk.Frame(root, bg='#9e2a2b')
header.place( rely=0.05, width=WIDTH, height=HEIGHT/3)

entry = tk.Entry(header, bg='#540b0e', fg='#9e2a2b', font=35)
entry.place(relx=0.4 , rely=0.1, relwidth=0.4, height=HEIGHT/10)

label = tk.Label(header, text='File for Analysis:', bg='#540b0e', fg='#fff3b0')
label.place(relx=0.02, rely=0.1, relwidth=0.35, height=HEIGHT/10)

#Buttons -----------------------------------------------------------------
#FULL
full_button = tk.Button(header, text='Full Analysis', bg='#335c67', fg='#fff3b0',command=lambda: full_anal_butt(entry.get()))
full_button.place(relx=0.02, rely=0.6, width=WIDTH/4, height=HEIGHT/10)

#WEEK
week_button = tk.Button(header, text='Week Analysis', bg='#335c67', fg='#fff3b0',command=lambda: week_anal_butt(entry.get()))
week_button.place(relx=0.3, rely=0.6, width=WIDTH/4, height=HEIGHT/10)

#DAY
full_button = tk.Button(header, text='Day Analysis', bg='#335c67', fg='#fff3b0',command=lambda: day_anal_butt(entry.get()))
full_button.place(relx=0.6, rely=0.6, width=WIDTH/4, height=HEIGHT/10)

#---------------------------------------------------------------------------


body = tk.Frame(root, bg='#9e2a2b')
body.place(rely=0.5, width=WIDTH, height=HEIGHT/4)

body_label = tk.Label(body, text='', bg='#540b0e', fg='#fff3b0')
body_label.place(relx=0.02, rely=0.1, relwidth=0.8, height=HEIGHT/10)


root.mainloop()

