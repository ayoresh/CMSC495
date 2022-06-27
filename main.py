from tkinter import *
import MortgageCalculator as mc
import CompTool as ct

root = Tk()
root.title('CMSC 495 Captsone Project')
root.geometry("500x400")

def calculator():
    mc.runcalc()


def price():
    ct.__init__()

my_label_frame = LabelFrame(root, text="Please Choose a Tool Below")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# Button
my_button1 = Button(my_label_frame, text="Mortgage Calculator", command=calculator)
my_button1.pack(padx=10, pady=10)

my_button2 = Button(my_label_frame, text="Comp Tool", command=price)
my_button2.pack(pady=20)



root.mainloop()