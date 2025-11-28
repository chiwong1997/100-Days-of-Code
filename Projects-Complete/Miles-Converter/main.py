import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

# Label 1 - Miles
l1=tkinter.Label(text="Miles")
l1.grid(column=3, row=1)

# Label 2 - is equal to
l2=tkinter.Label(text="is equal to")
l2.grid(column=1, row=2)

# Label 3 - conversion in KM
l3=tkinter.Label(text="0")
l3.grid(column=2, row=2)

# Label 4 - Km
l4=tkinter.Label(text="Km")
l4.grid(column=3, row=2)

# Entry - Miles to convert
entry=tkinter.Entry(width=10)
entry.insert(index=0, string="0")
entry.grid(column=2,row=1)

def convert_miles():
    print("Miles converted!")
    miles = float(entry.get())
    km = int(round(miles*1.60934, 0))
    print(km)
    l3.config(text=f"{km}")

# Button - Calculate
button=tkinter.Button(text="Calculate", command=convert_miles)
button.grid(column=2,row=3)




window.mainloop()