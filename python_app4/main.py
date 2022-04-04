import Uplode
#import Data_proc
import Link
import Editor
import Error
import tkinter as tk

while True:
	s = []
	s = Link.Ask_link(s)
	tepes = []
	#s = "http://kappa.cs.petrsu.ru/~dimitrov/info_1/test.json"
	jsonData = Uplode.fuplode(s[0])
	if jsonData != None:
		jsonData = Editor.json_editor(jsonData)
		break
	else:
		Error.Error_message_box()

