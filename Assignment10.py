import tkinter as tk
import webbrowser as wb

root = tk.Tk()

# Entry 
entry = tk.Entry(root, font=("Century Schoolbook", 40), width=30)
entry.grid(row=0, column=0)


l1 = tk.Label(root, font=("Century Schoolbook", 30))
l1.grid(row=1, column=0)

#display
def display():
    search = entry.get()
    print(search)
    if search:
        l1.config(text="Navigating to RetailerHub")

        wb.open(f"https://www.retailerhub.in/={search}")
    else:
        print("Enter Something")

#search button
search_button = tk.Button(root, text="Search", font=("Century Schoolbook", 30),bg="red", activebackground="orange", command=display)
search_button.grid(row=4, column=0)

#close button
close_button = tk.Button(root, text="Close", font=("Century Schoolbook", 30),bg="blue", activebackground="pink", command=root.destroy)
close_button.grid(row=5, column=0)

root.mainloop()