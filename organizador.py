# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:16:56 2026

@author: daian
"""

from pathlib import Path

pasta = Path.cwd()
contador = 0

print("ORGANIZADOR DE FICHEIROS")
print("-----------------------")

for ficheiro in pasta.iterdir():
    if ficheiro.is_file():
        contador = contador + 1
        print("Nome:", ficheiro.name)
        print("Extensão:", ficheiro.suffix)
        print("Tamanho:", ficheiro.stat().st_size, "bytes")
        if ficheiro.suffix in [".py", ".txt", ".csv"]:
           print("Ficheiro identificado:", ficheiro.suffix)
print("Total de ficheiros:", contador)
if contador == 0:
    print("A pasta não contém ficheiros.")
        