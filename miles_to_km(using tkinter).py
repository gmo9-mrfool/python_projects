from tkinter import *

window = Tk()
# window.minsize(width=100, height=10)
window.title("Mile to km converter")


def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    kilometer_result_label.config(text=f"{km}")


# Entry
miles_input = Entry()
miles_input.grid(column=1, row=0)
# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid()

window.mainloop()
