from tkinter import *

# init the window
import entrypoints

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=600, height=300)
window.config(padx=50, pady=100)

# Adding labels
welcome = Label(text="Welcome, Enter the Mile", font=("Arial", 18, "italic"))
welcome.grid(column=0, row=0)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

mile = Label(text="in Miles", font=("Arial", 18, "italic"))
mile.grid(column=2, row=0)

equal_to = Label(text="is equal to ", font=("Arial", 18, "italic"))
equal_to.grid(column=0, row=2)

km = Label(text="KM ", font=("Arial", 18, "italic"))
km.grid(column=2, row=2)

km_conv = Label(text="0", font=("Arial", 18, "italic"))
km_conv.grid(column=1, row=2)


# calculate

def conversion():
    mile_value = float(mile_input.get())
    result = str(mile_value * 1.609344)
    km_conv.config(text=result)


# calc button

calc_button = Button(text="Calculate", command=conversion)
calc_button.grid(column=1, row=3)

## adding loop to end
window.mainloop()
