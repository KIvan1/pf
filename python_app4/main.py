import Uplode
import Open
import Link
import Editor
import Error
import tkinter as tk

while True:
	s = []
	s = Link.Ask_link(s)
#s = "http://kappa.cs.petrsu.ru/~dimitrov/info_1/test.json"
	jsonData = Uplode.fuplode(s[0])
	if jsonData != None:
		print(type(jsonData["ticketit_admin"]))
		jsonData = Editor.json_editor(jsonData)
		print("\n\n")
		print(type(jsonData["ticketit_admin"]))
		break
	else:
		Error.Error_message_box()

