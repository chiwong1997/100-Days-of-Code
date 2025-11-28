import tkinter

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)

def second_button():
    print("this button does nothing")

window = tkinter.Tk()
window.title("My GUI")
window.minsize(width=1000, height=500)
window.config(padx=20, pady=20) #creates space around the edges of our GUI program

# LABEL

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))


# Two ways to change the text of the label 
#my_label["text"] = "new_text"
my_label.config(text= "New Text")
my_label.config(padx=50, pady=50)
my_label.grid(column=0, row=0)
#my_label.place(x=100, y=200)
#my_label.pack() - pack and grid are not compatible together

# BUTTON

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
#button.pack()

button_2 = tkinter.Button(text="Second Button", command=second_button)
button_2.grid(column=2, row=0)

# ENTRY

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
#input.pack()

window.mainloop()