import tkinter as tk
def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = round(eval(entry.get()),2)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Maths Error")
     
    elif text == "D":
        entry.delete(len(entry.get())-1)
    elif text=="C":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END, text)
root = tk.Tk()
root.title("Calc by Khushi Pandey")
root.geometry("300x565")
root.configure(bg="pink")
root.resizable(False, False)
entry = tk.Entry(root, font=("Helvetica", 30), justify="right",background="pink",fg="#FFFFFF")
entry.pack(fill=tk.BOTH, ipadx=5, ipady=5, padx=10, pady=10)
button_color = "#FFFFFF"
button_font = ("Helvetica", 20)
button_active_bg = "#03C988"

button_frame = tk.Frame(root,background="#EEEEEE")
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'D', '0', '.', '+',
    '(',')','C', '=',
     
]

row, col = 1, 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=button_font, bg=button_color, relief=tk.GROOVE,
                       activebackground=button_active_bg)
    button.grid(row=row, column=col, padx=12, pady=12, sticky="nsew")
    button.bind("<Button-1>", on_click)

    col += 1
    if col > 3:
        col = 0
        row += 1
for r in range(1, 5):
    button_frame.rowconfigure(r, weight=2)
for c in range(4):
    button_frame.columnconfigure(c, weight=2)
root.mainloop()
