import Uplode
import Open
import tkinter as tk

jsonData = Uplode.fuplode()
window = tk.Tk()
text = []
for i in range(5):
	text.append(tk.Label(text = str(i), width = 50))
	text[i].pack()

entry = tk.Entry(width = 50, fg = "blue")
entry.insert(0, "hello")
entry.pack()
button = tk.Button(text = "OK", width = 10, height = 2, fg = "blue")
button.pack()
s = entry.get()
print(s)
window.mainloop()
print(s)