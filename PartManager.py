from tkinter import *

# Create window object
app = Tk()

# Part
part_text  = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer
customer_text  = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text  = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 14))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# Price
Price_text  = StringVar()
Price_label = Label(app, text='Price', font=('bold', 14), pady=20)
Price_label.grid(row=1, column=2, sticky=W)
Price_entry = Entry(app, textvariable=Price_text)
Price_entry.grid(row=1, column=3)

app.title('Part Manager')
app.geometry('700x350')

# Start program
app.mainloop()
