import numpy as np

slova = {'a': 'а', 'A': 'А', 'b': 'б', 'B':'Б', 'v': 'в', 'V': 'В', 'g': 'г', 'G': 'Г', 'd': 'д', 'D': 'Д', 'đ': 'ђ', 'Đ':'Ђ','e': 'е', 'E': 'Е', 'ž': 'ж', 'Ž': 'Ж', 'z': 'з', 'Z': 'З', 'i': 'и', 'I':'И','j': 'ј', 'J': 'Ј', 'k': 'к', 'K':'К', 'l': 'л', 'L':'Л', 'lj': 'љ', 'Lj': 'Љ', 'm': 'м', 'M':'М', 'n': 'н', 'N':'Н', 'nj':'њ', 'Nj':'Њ', 'o': 'о', 'O':'О', 'p': 'п', 'P':'П', 'r': 'р', 'R': 'Р', 's': 'с', 'S':'С', 't': 'т', 'T': 'Т', 'ć': 'ћ', 'Ć':'Ћ', 'u': 'у', 'U': 'У', 'f': 'ф', 'F': 'Ф', 'x': 'х', 'X': 'Х', 'h': 'х', 'H': 'Х','c': 'ц', 'C':'Ц', 'č': 'ч', 'Č': 'Ч', 'l': 'л', 'L': 'Л','dž': 'џ', 'Dž':'Џ','š': 'ш', 'Š': 'Ш'}   
skracenice = {'sl': 1, 'itd': 1, 'br': 1, 'dr': 1, 'ul': 1, 'prof': 1, 'srp': 1, 'tkzv': 1, 'сл': 1, 'итд': 1, 'бр': 1, 'др': 1, 'ул': 1, 'проф': 1, 'срп': 1, 'ткзв': 1} 

def invertovanjeRecnika(recnik):
    invertovaniRecnik = dict(map(reversed, recnik.items()))
    return invertovaniRecnik
    
def duzinaFajla(recnik):
    brojLinija = sum(1 for line in open(recnik))
    return brojLinija

def recnik(recnik1, recnik2):
    fajl1 = open(recnik1, 'r')
    fajl2 = open(recnik2, 'r')
    recnik = dict()
    for i in range(duzina_fajla(recnik1)):
        linija1 = fajl1.readline()
        linija2 = fajl2.readline()
        kosaCrta1 = linija1.find('/')
        kosaCrta2 = linija2.find('/')
        linija1 = linija1[:kosaCrta1]
        linija2 = linija2[:kosaCrta2]
        recnik[linija1] = linija2
    fajl1.close()
    fajl2.close()
    return recnik

def snimiRecnik():
    rec = recnik('sr-Latn.dic.txt', 'sr.dic.txt')
    np.save('recnik.npy', rec)

def ucitajRecnik():
    recnik = np.load('recnik.npy', allow_pickle=True).item()
    return recnik

