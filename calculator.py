import tkinter as tk


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        output_label.config(text='Result'+str(result))
    except Exception as e:
        output_label.config(text='Error:'+str(e))


window = tk.Tk()
window.title("Arithmatic Calculator")
entry = tk.Entry(window, width=30)
entry.pack()
calculate_button = tk.Button(window, text='Calculate', command=calculate)
calculate_button.pack()
output_label = tk.Label(window, text='')
output_label.pack()
window.mainloop()