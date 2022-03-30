import Uplode
import Open
import Link
import Editor
import tkinter as tk

s = []
s = Link.Ask_link(s)
#s = "http://kappa.cs.petrsu.ru/~dimitrov/info_1/test.json"
jsonData = Uplode.fuplode(s[0])
jsonData = Editor.json_editor(jsonData)
print("\n\n")
print(jsonData)