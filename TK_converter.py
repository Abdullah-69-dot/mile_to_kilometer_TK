import tkinter
window = tkinter.Tk()
window.title("My Gui")
(window.minsize(width=500,height=300))
label = tkinter.Label(text="Convert to miles", font=("Arial",15,"bold"))
label.pack(padx = 250 ,pady = 20)
ENTRY = tkinter.Entry(width=10)
ENTRY.place(x=260,y=60)
label = tkinter.Label(text="miles", font=("Arial",10,"bold"))
label.place(x=340,y=60)
label1 = tkinter.Label(text="The reult is 0 km", font=("Arial",10,"bold"))
label1.place(x=254 , y=90)
def result():

    miles = int(ENTRY.get())*1.5
    label1.config(text=f"The result is: {miles} km")
bot = tkinter.Button(text="Convert",command=result,width=20)
bot.place(x=280 , y=130)





















window.mainloop()