import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = tk.Tk()
window.title('Text Editor')
window.resizable(width=False, height=False)

# I need a frame to fill the left side of the screen
# I need a text space
# I need a save button and storage for notes
# I need a see notes button to view all the notes
# I need a delete button to delete a note
window.columnconfigure(0, minsize=150)
window.columnconfigure(1, minsize=250)
window.rowconfigure(0, minsize=100)

def open_file():
    filepath = askopenfilename(
        filetypes[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_box.delete("1.0", tk.END)
    with open(filepath, moe="r", encoding="utf-8") as input_file:
        text= input_file.read()
        text_box.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension = ".tx",
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = text_box.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor -{filepath}")

text_box = tk.Text(master=window, bg='beige', fg='blue')
text_box.grid(row=0, column=1, sticky='nsew')

widget_frm = tk.Frame(master=window, bg='brown')
widget_frm.grid(row=0, column=0, sticky='nsew')

save_button = tk.Button(master=widget_frm, text='Save Note', command=save_file)
save_button.pack(fill=tk.X)

open_button = tk.Button(master=widget_frm, text='Open Note', command=open_file)
open_button.pack(fill=tk.X, pady=5)


window.mainloop()




