#coding:utf-8

import sys
import festival

print("talking")
festival.execCommand("(voice_el_diphone)")
string = unicode("Hola mundo, esta es una prueba del criticon, con una canción", "ascii")
festival.sayText(string)
