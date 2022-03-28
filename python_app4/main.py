import Uplode
import Open
import Link
import Editor
import tkinter as tk

s = Link.Ask_link()
s = "http://kappa.cs.petrsu.ru/~dimitrov/info_1/test.json"
jsonData = Uplode.fuplode(s)
jsonData = Editor.json_editor(jsonData)
