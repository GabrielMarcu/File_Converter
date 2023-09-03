# Scrieti o aplicatie care salveaza textul dintr-un fisier text intr-un fisier .csv, dar si invers .csv -> .txt.
# Input-ul va fi dat de utilizator ca o cale catre fisierul text/csv
import os.path
import sys

path = input("path: ")
ext = os.path.splitext(path)[1]
if ext == '.csv':
    pass
elif ext == '.txt':
    pass
else:
    print(f"Not implemented for file type {ext}")
