# O alatu

Softverski alat baziran na komandnoj liniji koji nudi određene funkcionalnosti za rad sa tekstualnim
fajlovima ekstenzije __.txt__ i __.docx__. O samom načinu pokretanja i korišćenja funkcionalnosti ovog alata
opširnije možete pročitati u odeljku *Instrukcije*.

# Instalacija 

Potrebno je imati instaliranu verziju >= 3.0  programskog jezika Python 

U okviru programskog jezika Python, potrebno je instalirati sledeće pakete (u zagradi su date verzije korišćene u .py skriptama):
__python-docx__ (verzija 0.8.10) | __pyspellchecker__ (verzija 0.5.2) | __numpy__ (1.16.4). Sve navedene biblioteke se mogu instalirati uz pomoć pip komande.

Za konverziju .txt fajla u .pdf format i za spajanje više .pdf fajlova u jednu, potrebno je instalirati: 

__paps__ -> https://www.systutorials.com/docs/linux/man/1-paps/ 

__ghostscript__ (verzija 9.27)-> https://www.ghostscript.com/

Za konverziju .docx fajlova u .pdf format:

Windows:
__OfficeToPDF.exe__ -> Potrebno je ući na sledeću stranicu i skinuti __"OfficeToPDF.exe"__
https://github.com/cognidox/OfficeToPDF/releases/tag/v1.8.22.0.
Nakon toga, potrebno je prebaciti navedeni .exe u folder gde se nalaze .py skripte.
Potrebno je imati instaliran Office 2016, 2013, 2010 ili 2007. Za verziju Office 2007 potrebno je instalirati dodatne 
stavke koje se mogu videti u README.md na sledećem linku https://github.com/cognidox/OfficeToPDF#giving-back-to-the-community

Linux: 
Linux koristi __LibreOffice__ za konverziju .docx fajlova u .pdf

# Važno obaveštenje

Glavna svrha ovog sotfverskog alata jeste obrada teksta tj. njegovo modifikovanje. Prilikom modifikacije ulaznog fajla, stil teksta ostaje nepromenjen (veličina slova, font, poravnanje, osobine teksta - boldovan, podvučen, iskošen ...) 
Ukoliko se primenjuju funkcije koje modifikuju tekst na .docx fajlove, stvari kao što su slike ili
tebele će se izgubiti. Rešenje za taj problem jeste da se modifikovana verzija rada snimi kao različiti fajl gde će se izvršiti odabrana funkcionalnost nad tekstom a zatim se taj tekst može kopirati u ulazni fajl koji nije izgubio nikakav sadržaj.

# Instrukcije 

Program se koristi pokretanjem skripte diplomski_rad.py. Ukoliko korisnik na svom sistemu ima instaliranu samo verziju >= 3.0 programskog jezika Python, program se pokreće
komandom *python diplomksi_rad.py ...* gde tri tačke predstavljaju funkcije koje se mogu primeniti. Ukoliko korisnik ima instalirane obe verzije Pythona
i ukoliko je verzija 2 primarna, pokretanje se vrši komandom *python3 diplomski_rad.py ...*. Pošto funkcije sedam i osam u skripti funkcije.py koriste funkciju dva kao 
uslužnu funkciju a funkcija sedam koristi i funkciju jedan kao uslužnu, potrebno je ući u skriptu funkcije.py i u navedenim funkcijama podesiti komandu na *python/python3 ...*.

| Instrukcija                                                    |      Objašnjenje instrukcije     |
|:---------------------------------------------------------------|:--------------------------------:|
| python diplomski_rad.py -p                                     | Pruža objašnjenje svake funkcije |  
| python diplomski_rad.py -f ime_fajla -1                        | Transformiše malo slovo u veliko na početku rečenice odnosno iza tačke |
| python diplomski_rad.py -f ime_fajla -2                        | Dodaje razmak između zapete/tačke i reči ukoliko razmak ne postoji     |
| python diplomski_rad.py -f ime_fajla -3                        | Uklanja višestruke razmake u tekstu                                    |
| python diplomski_rad.py -f ime_fajla -4 l/latinica             | Transformiše sve ćirilične reči u tekstu u latinicu                    |
| python diplomski_rad.py -f ime_fajla -4 ć/ćirilica             | Transformiše sve latinične reči u tekstu u ćirilicu                    |
| python diplomski_rad.py -f ime_fajla -5                        | Konvertuje ulazni fajl u .pdf                               |
| python diplomski_rad.py -6 ulazni_fajlovi.pdf izlazni_fajl.pdf | Spaja navedene ulazne fajlove u izlazni .pdf format                   |
| python diplomski_rad.py -f ime_fajla -7 distanca               | Proverava da li u tekstu postoje pogrešno napisane reči - opširnije preko komande -p/--pomoć | 
| python diplomksi_rad.py -f ime_fajla -8 brojReči               | Štampa u komandnoj liniji prvih *brojReči* reči koje se najčešće pojavjljuju |
| python diplomski_rad.py -f ime_fajla -8 brojReči -i            | Slično prethodnoj komandi s tim što se prilikom brojanja učestanosti reči zanemaruju mala i velika slova |
| python diplomski_rad.py -f ime_fajla -9 reč novaReč            | Menja reč novom sekvencom novaReč na prvom pronađenom mestu |
| python diplomski_rad.py -f ime_fajla -9 reč novaReč -i         | Slično prethodnoj komandi s tim što se prilikom zamene sekvence reč zanemaruju mala i velika slova |
| python diplomski_rad.py -f ime_fajla -9 reč novaReč -z         | Menja reč novom sekvencom novaReč na svakom pronađenom mestu |
| python diplomski_rad.py -f ime_fajla -9 reč novaReč -z -i      | Slično prethodnoj komandi s tim što se prilikom zamene sekvence reč zanemaruju mala i velika slova  

Na funkcije koje vrše modifikaciju fajla (funckije -1, -2, -3, -4, -7, -9), može se primeniti fleg -o/--izlaz imeNovogFajla.
Ime novog fajla se navodi bez ekstenzije.

Primer: python diplomski_rad.py -f demo.docx -1 -o demo_izlaz 
