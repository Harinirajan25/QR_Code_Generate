import qrcode
from tkinter import *

cp = Tk()


cp.title('HAVIRAT')
cp.geometry('700x250')
cp.config(bg='#5D426D')

def generate():
    img = qrcode.make(msg.get())
    type(img)
    img.save(f'{save_name.get()}.png')
    Label(cp, text='File Saved!', bg='#5F4889' , fg='black', font=('Arial Black', 8)).pack()

def show():
    img = qrcode.make(msg.get())
    type(img)
    img.show()

frame = Frame(cp, bg='#C5BADA')
frame.pack(expand=True)

#------------------ENTER THE TEXT OR URL------------------

Label(frame, text='Enter the Text or URL : ', font=('Arial Black', 16),
      bg='#C5BADA').grid(row=0, column=0, sticky='w')

msg = Entry(frame)
msg.grid(row=0, column=1)

#------------------ENTER THE FILE NAME------------------

Label(frame, text='File Name(Save As) : ', font=('Arial Black', 16),
      bg='#C5BADA').grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

#------------------BUTTONS TO SHOW OR SAVE QRCODE------------------

btn = Button(cp, text='Show QR code', bd='5', command=show, width=15)
btn.pack()
btn = Button(cp, text='Save QR code', command=generate, bd='5', width=15)
btn.pack()

cp.mainloo
