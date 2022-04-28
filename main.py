from tkinter import *

def convert_miles():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=convert_miles)
calculate_btn.grid(column=1, row=2)

window.mainloop()