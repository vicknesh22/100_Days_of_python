import tkinter

# Creating Window object from tkinter module with TK() class
window = tkinter.Tk()

# Window sizing
window.title("GUI Window")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.pack()

# updating the existing label

my_label["text"] = "New Label"
my_label.config(text="Second Label")


# Creating a new button
# clicking
def clicking():
    new_text = entry.get()
    my_label.config(text=new_text)


# button
button = tkinter.Button(text="ClickMe", command=clicking)
button.pack()

# Entry
entry = tkinter.Entry(width=17)
entry.pack()
entry.get()
if my_label["text"] == "I Got Clicked":
    my_label["text"] = input
entry.get()

# this code below keep the tkinter window open all the time ( in a loop)
window.mainloop()
