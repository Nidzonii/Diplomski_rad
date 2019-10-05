# O alatu

Softverski alat baziran na komandnoj liniji koji vrši određene modifikacije odnosno transformacije tekstualnih
datoteka ekstenzije __.txt__ i __.docx__. O samom načinu pokretanja i korišćenja funkcionalnosti samog alata
opširnije možete proćitati u odeljku *Instrukcije*.

# Instalacija 

Potrebno je imati instaliranu verziju >= 3.0  programskog jezika Python 

U okviru programskog jezika Python, potrebno je instalirati sledeće pakete:
__python-docx__ | primer instalacije ukoliko korisnik ima instaliranu komandu pip -> pip install python-docx
__pyspellchecker__ | primer instalacije ukoliko korisnik ima instaliranu komandu pip -> pip install pyspellchecker
__numpy__ | primer instalacije ukoliko korisnik ima instaliranu komandu pip -> pip install numpy

Za konverziju .txt fajlova u pdf potrebno je instalirati sledeće:
__paps__ link -> https://www.systutorials.com/docs/linux/man/1-paps/

Windows:
Za konverziju .docx fajlova u pdf potrebno je ući na sledeću stranicu i skinuti __"OfficeToPDF.exe"__
https://github.com/cognidox/OfficeToPDF/releases/tag/v1.8.22.0
Nakon toga, potrebno je prebaciti skinuti .exe u folder gde se nalaze .py skripte.
Potrebno je imati instaliran Office 2016, 2013, 2010 ili 2007. Za verziju Office 2007 potrebno je instalirati dodatne 
stavke koje se mogu videti u README.md na sledećem linku https://github.com/cognidox/OfficeToPDF#giving-back-to-the-community

Linux: 
Linux koristi LibreOffice za konverziju .docx fajlova u pdf

Za spajanje više pdf fajlova u jedan pdf fajl, potrebno je instalirati __ghostscript__ -> https://www.ghostscript.com/

# Važno obaveštenje

Ovaj softverski alat se bazira na radu sa tekstom i stil teksta ostaje nepromenjen (veličina slova, font, poravnanje, osobine teksta - boldovan, podvučen, iskošen ...) 
Funkcije koje modifikuju ulazni .docx fajl modifikuju tekst dok se ostale stvari kao što su slike ili
tebele gube. Rešenje za taj problem jeste da se modifikovana verzija rada snimi kao različita datoteka gde će se izvršiti odabrana funkcionalnost nad tekstom
a zatim se taj tekst može kopirati u ulazni fajl koji nije izgubio nikakav sadržaj.

# Instrukcije 

Program se koristi pokretanjem skripte diplomski_rad.py. Ukoliko korisnik na svom sistemu ima instaliranu samo verziju >= 3.0 Pythona, program se pokreće
komandom *python diplomksi_rad.py ...* gde tri tačke predstavljaju funkcije koje se mogu primeniti. Ukoliko korisnik ima instalirane obe verzije Pythona
i ukoliko je verzija 2 primarna, pokretanje se vrši komandom *python3 diplomski_rad.py ...*. Pošto funkcije sedam i osam u skripti funkcije.py koriste funkciju dva kao 
uslužnu funkciju, potrebno je ući u skriptu funkcije.py i u navedenim funkcijama podesiti komandu na *python/python3 ...*.

| Instrukcija                |      Objašnjenje instrukcije     |
|:--------------------------|:--------------------------------:|
| python diplomski_rad.py -p | pruža objašnjenje svake funkcije |  
| python diplomski_rad.py -f ime_fajla -1            | Transformiše malo slovo u veliko na početku rečenice odnosno iza tačke |
| python diplomski_rad.py -f ime_fajla -2            | Dodaje razmak između zapete/tačke i reči ukoliko razmak ne postoji     |
| python diplomski_rad.py -f ime_fajla -3            | Uklanja višestruke razmake u tekstu                                    |
| python diplomski_rad.py -f ime_fajla -4 l/latinica | Transformiše sve ćirilične reči u tekstu u latinicu                    |
| python diplomski_rad.py -f ime_fajla -4 ć/ćirilica | Transformiše sve latinične reči u tekstu u ćirilicu                    |
| python diplomski_rad.py -f ime_fajla -5                        | Konvertuje ulazni fajl u pdf                               |
| python diplomski_rad.py -6 ulazni_fajlovi.pdf izlazni_fajl.pdf | Spaja navedene ulazne fajlove u izlazni                    |
| python diplomski_rad.py -f ime_fajla -7 distanca               | Proverava da li u tekstu postoje pogrešno napisane reči - opširnije preko komande -p/pomoć | 
| python diplomksi_rad.py -f ime_fajla -8 brojReči               | Štampa u komandnoj liniji prvih *brojReči* reči koje se najčešće pojavjljuju |
| python diplomski_rad.py -f ime_fajla -8 brojReči -i            | Slično prethodnoj komandi s tim što se prilikom brojanja reči zanemaruju mala i velika slova |
| python diplomski_rad.py -f ime_fajla -9 reč novaReč            | Menja reč novom sekvencom novaReč na prvom pronađenom mestu |
| python diplomski_rad.py -f ime_fajla -9 reč novaReč -i         | Slično prethodnoj komandi s tim što se prilikom zamene sekvence reč zanemaruju mala i velika slova |
| python diplomski_rad.py -f ime_fajla -9 reč novaReč -z         | Menja reč novom sekvencom novaReč na svakom pronađenom mestu |
| python diplomski_rad.py -f ime_fajla -9 reč novaReč -z -i      | Slično prethodnoj komandi s tim što se prilikom zamene sekvence reč zanemaruju mala i velika slova  

Na funkcije koje vrše modifikaciju fajla (funckije -1, -2, -3, -4, -7, -9), mogu se primeniti sve nabrojane funkcije u tabeli sa dodatkom -o/--izlaz imeNovogFajla.
Ime novog fajla se navodi bez ekstenzije.

Primer: python diplomski_rad.py -f demo.docx -1 -o demo_izlaz 
