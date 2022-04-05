import tkinter as tk

def Ask_link(s):
	def Link_get():
		s.append(link.get())
		window.destroy()

	def Link_get_comb(event):
		Link_get()

	window = tk.Tk()
	window.title("Link")
	text = tk.Label(text = "Вводите ссылку на json файл")
	text.pack()
	link = tk.StringVar()
	entry = tk.Entry(width = 50, fg = "blue", textvariable = link)
	entry.pack(fill = tk.X)
	button = tk.Button(text = "OK", width = 10, height = 2, fg = "blue", command = Link_get)
	window.bind('<Return>', Link_get_comb)
	button.pack()
	window.mainloop()
	return s