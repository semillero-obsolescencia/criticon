#!/usr/bin/python

import sys, os
import random
from nlgen.cfg import read_cfg

class GeneradorFrases:
  def __init__(self, rating_scale=5.0):
    self.rating_scale = rating_scale
    self.cfg_pos = ""
    self.cfg_neu = ""
    self.cfg_neg = ""
    self.load_cfgs()
    self.rating = self.rating_scale/2;
    self.permutaciones = []
    self.frase = ""

  def load_cfgs(self):
    path_pos = 'data/positivo/' + random.choice(os.listdir('data/positivo'))
    path_neu = 'data/neutral/' + random.choice(os.listdir('data/neutral'))
    path_neg = 'data/negativo/' + random.choice(os.listdir('data/negativo'))
    file_pos = open(path_pos, "r").read()
    file_neu = open(path_neu, "r").read()
    file_neg = open(path_neg, "r").read()
    self.cfg_pos = read_cfg(file_pos.strip())
    self.cfg_neu = read_cfg(file_neu.strip())
    self.cfg_neg = read_cfg(file_neg.strip())

  def generar(self, rating):
    self.rating = rating
    #genera el rating aleatoriamente
    #self.rating = random.uniform(0.0, 5.1)

    # rating bajo, frase negativa
    if self.rating < (self.rating_scale / 3):
      print("frase negativa")
      self.permutaciones = self.cfg_neg.permutation_values("SENTENCE")

      # rating medio, frase neutral
    elif self.rating > self.rating_scale/3 and self.rating < (self.rating_scale/3)*2:
      print("frase neutral")
      self.permutaciones = self.cfg_neu.permutation_values("SENTENCE")

    # rating alto, frase positiva
    elif self.rating > (self.rating_scale/3)*2:
      print("frase positiva")
      self.permutaciones = self.cfg_pos.permutation_values("SENTENCE")

    self.frases = [" ".join( frase ) for frase in set(self.permutaciones) ]
    self.frase = random.choice(self.frases)
    print("Frase: %s" % self.frase)
    print("Rating: %s" % self.rating)
    return self.frase

  def autogenerar(self):
    self.rating = random.uniform(0.0, self.rating_scale)
    result = self.generar(self.rating)
    return result


