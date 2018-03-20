#!/usr/bin/python

import sys, os
import random
from nlgen.cfg import read_cfg

nombre_archivo = "example_art_es.nlcfg"
archivo = open(nombre_archivo, "r").read()
config = read_cfg(archivo.strip())
permutaciones = config.permutation_values("SENTENCE")
frases = [" ".join( frase ) for frase in set(permutaciones) ]
frase = random.choice(frases)
print(frase)
