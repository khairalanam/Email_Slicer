import tkinter as tk
import tkinter.messagebox

def slice():
    email = entry_1.get()
    username = ''
    domain = ''

    for i in range(0, len(email)):
        if i < email.find('@'):
            username += email[i]
            continue
        elif email[i] == '@':
            continue
        else:
            domain += email[i]
            continue

    result.configure(text = f"The username is {username} \n The domain name is {domain}")
    
window = tk.Tk()
window.title("Email Slicer by Khair")
window.geometry("500x500")
window.resizable(0,0)

label_1 = tk.Label(window, text = "Email Slicer", font = ("Verdana", 25, "bold underline"), anchor = "center")
label_1.pack()

label_2 = tk.Label(window, text = "Enter the email to slice:", font = ("TImes", 20), anchor = "center")
label_2.pack(pady = 10)

entry_1 = tk.Entry(window, text = "Enter", width = 40)
entry_1.pack(pady = 10)

button_1 = tk.Button(window, text = "Slice", anchor = "e", command = slice)
button_1.place(x = 240, y = 140)

result = tk.Label(window, text = ' ', font = ("Times", 25, "bold"))
result.pack(pady = 40)

window.mainloop()
