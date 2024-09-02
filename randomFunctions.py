import main


def slide1(event, entry, slider):
    num = entry.get() # Get whatever is entered in the entry
    if num.isdigit(): # Checks if it is an integer
        num = int(num) # Convert string to integer
        # Change the values on the scale
        slider.set(num) # Why no if statement?? Automatically snaps to the max or min value
        # Optional at the bottom if you also want the value in the entry changed:
        # on_change(None)

def on_change(event, entry, slider): # Change the value of entry
    entry.delete(0, END)
    slider.insert(0, main.entry1.get())

