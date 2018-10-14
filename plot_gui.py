# 13/10/2018 13:10:01 

import tkinter as tk

class StockGUI:

    """
    Creates a frame work for our future GUI.
    None of the buttons do anything yet, and it doesn't plot nothing either.
    """

    def __init__(self, parent):
        self.parent = parent
        parent.title("Stock Stalker")

        button_allTime = tk.Button(parent, text="All time") 
        button_thisYear = tk.Button(parent, text='This year')
        button_thisMonth = tk.Button(parent, text='This month')
        button_thisWeek = tk.Button(parent, text='This week')
        button_today = tk.Button(parent, text='Today')

        label_plotStandIn = tk.Label(parent, text="PLOT", fg='red', font=('Courier New','40') )

        button_allTime.grid(row=0, column=0)
        button_thisYear.grid(row=0, column=1)
        button_thisMonth.grid(row=0, column=2)
        button_thisWeek.grid(row=0, column=3)
        button_today.grid(row=0, column=4)

        label_plotStandIn.grid(row=1, columnspan=5, pady=100)

root = tk.Tk()
start = StockGUI(root)
root.mainloop()
