import argparse
import sys
from funkcije import *

parser = argparse.ArgumentParser(description='Softverski alat kojim se ulazni tekstualni fajl ekstenzije .txt/.docx transformiše u željeni izlaz', add_help=False)
pomoc = parser.add_argument_group('pomoć')
pomoc.add_argument("-p", "--pomoć", action='store_true', help="Pruža objašnjenje svake funkcije")
flegovi = parser.add_argument_group('flegovi')
flegovi.add_argument("-i", "--ignoriši", action="store_true", help="Kada se pozove kao argument, velika i mala slova će se posmatrati isto. Može se upariti sa funkcijama -8/--osam, -9/--devet")
flegovi.add_argument("-z", "--zameni_sve", action="store_true", help="Omogućava da se svako/prvo pojavljivanje specificirane reči u tekstu zameni novom sekvencom. Ukoliko se navede kao argument, zameniće se svako pojavljivanje navedene sekvence - u suprotnom će se zameniti samo prva pronađena sekvenca. Može se upariti samo sa funkcijom -9/--devet")
flegovi.add_argument("-o", "--izlaz", type=str, help="Izlaz će biti novi fajl. Potrebno je navesti ime izlaznog fajla bez navođenja ekstenzije jer će ekstenzija biti jednaka ekstenziji ulaznog fajla. Može se primeniti na svaku funkciju koja vrši modifikaciju fajla - ne može se prmeniti na funkcije -5/--pet, -6/--šest, -8/--osam")
funkcije = parser.add_argument_group('funkcije')
funkcije.add_argument("-f", "--fajl", type=str, help='Naziv ulaznog fajla')
funkcije.add_argument("-1", "--jedan", action='store_true', help="Transformacija malih slova u velika gde god je to potrebno - početak rečenice, posle tačke")
funkcije.add_argument("-2", "--dva", action='store_true', help="Nakon svakog zareza, ukoliko nema razmaka, dodati ga kao i nakon tačke") 
funkcije.add_argument("-3", "--tri", action='store_true', help="Ukloniti duple ili višestruke razmake između dve reči")
funkcije.add_argument("-4", "--četiri", type=str, help="Transformacija iz latinice u ćirilicu i obrnuto. Kao argument se navodi pismo u koje je potrebno izvršiti konverziju teksta - l/latinica za latinično pismo, ć/ćirilica za ćirilično pismo")
funkcije.add_argument("-5", "--pet", action='store_true', help="Eksportovanje fajla u pdf")
funkcije.add_argument("-6", "--šest", nargs='*', help="Mogućnost spajanja više pdf fajlova u jedan pdf fajl - poslednje navedeni pdf fajl predstavlja izlaz")
funkcije.add_argument("-7", "--sedam", type=int, help="Najbliže pronađena reč. Kao argument se navodi distanca (broj slova koja se razlikuju između pogrešno napisane reči i nove, predložene reči) na osnovu koje će se tražiti odgovarajuće reči za pogrešno unesenu reč.")
funkcije.add_argument("-8", "--osam", type=int, help="Reči koje se najčešće pojavljuju u tekstu - kao paramter se unosi broj 'n' kojim se ispisuje prvih 'n' najčešće upotrebljenih reči u tekstualnom fajlu. Ovu funkcionalnost moguće je kombinovati uz fleg -i/--ignoriši")
funkcije.add_argument("-9", "--devet", nargs=2, help="Pronađi prvo pojavljivanje unesene sekvence i zameni drugim unosom | Pronađi svako pojavljivanje unesene sekvence i zameni drugim unosom. Navode se dva parametra. Prvi treba da bude sekvenca koju želimo da zamenimo, zatim se unosi nova sekvenca kojom želimo da zamenimo navedenu. Ukoliko je potrebno zameniti svako pojavljivanje sekvence, unosi se fleg -z. Ukoliko nije bitno da li je navedena sekvenca koju je potrebno zameniti sačinjena od malih odnosno velikih slova, unosi se i fleg -i")
args, nepoznatiArgumenti = parser.parse_known_args()

if args.pomoć:
    parser.print_help()
    sys.exit(0)

if args.pomoć and (args.fajl or args.jedan or args.dva or args.tri or args.četiri or args.pet or args.šest or args.sedam or args.osam or args.devet or nepoznatiArgumenti):
    parser.print_help()
    sys.exit(0)

if not args.fajl and (args.jedan or args.dva or args.tri or args.četiri or args.pet or args.sedam or args.osam or args.devet):
    print("Izabrana funkcija se mora primeniti na ulaznom fajlu!")
    sys.exit(0)

if args.fajl and args.izlaz and (args.pet or args.šest or args.osam):
    print("Izabrani fleg -о/--izlaz se ne može primeniti uz izabranu funkciju")
    sys.exit(0)

if args.fajl and args.zameni_sve and not args.devet:
    print("Izabrani fleg -z/--zamena se ne može primeniti uz izabranu funkciju")
    sys.exit(0)

if args.fajl and args.ignoriši and not(args.osam or args.devet):
    print("Izabrani fleg -i/--ignoriši se može primeniti uz funkcije -8/--osam i -9/--devet")
    sys.exit(0)

if not args.pomoć and nepoznatiArgumenti:
    if len(nepoznatiArgumenti) > 1:
        print("Uneli ste nepostojeće komande: " + str(nepoznatiArgumenti))
    else:
        print("Uneli ste nepostojeću komandu: " + str(nepoznatiArgumenti))
    sys.exit(0)

if args.fajl and args.jedan and args.izlaz:
    funkcija_jedan(args.fajl, args.izlaz)
elif args.fajl and args.jedan:
    funkcija_jedan(args.fajl, args.fajl)

if args.fajl and args.dva and args.izlaz:
    funkcija_dva(args.fajl, args.izlaz)
elif args.fajl and args.dva:
    funkcija_dva(args.fajl, args.fajl)

if args.fajl and args.tri and args.izlaz:
    funkcija_tri(args.fajl, args.izlaz)
elif args.fajl and args.tri:
    funkcija_tri(args.fajl, args.fajl)
    
if args.fajl and args.četiri and args.izlaz:
    unos = args.četiri
    while unos.upper() != 'L' and unos.upper() != 'LATINICA' and unos.upper() != 'Ć' and unos.upper() != 'ĆIRILICA':
        print('Unos: l/latinica ili ć/ćirilica')
        unos = input('l/latinica|ć/ćirilica: ') 
    funkcija_cetiri(args.fajl, unos, args.izlaz)
elif args.fajl and args.četiri:
    unos = args.četiri
    while unos.upper() != 'L' and unos.upper() != 'LATINICA' and unos.upper() != 'Ć' and unos.upper() != 'ĆIRILICA':
        print('Unos: l/latinica ili ć/ćirilica')
        unos = input('l/latinica|ć/ćirilica: ') 
    funkcija_cetiri(args.fajl, unos, args.fajl)

if args.fajl and args.pet:
    funkcija_pet(args.fajl)

if args.šest:
    funkcija_sest(args.šest)

if args.fajl and args.sedam and args.izlaz:
    funkcija_sedam(args.fajl, args.sedam, args.izlaz)
elif args.fajl and args.sedam:
    funkcija_sedam(args.fajl, args.sedam, args.fajl)

if args.fajl and args.osam:
    fleg = 'ne'
    if args.ignoriši:
        fleg = 'da'
    funkcija_osam(args.fajl, args.osam, fleg)

if args.fajl and args.devet and args.izlaz:
    fleg_zameni_sve = 'prvo'
    fleg_i = 'ne'
    if args.zameni_sve:
        fleg_zameni_sve = 'svako'
    if args.ignoriši:
        fleg.i = 'da'
    funkcija_devet(args.fajl, args.devet, fleg_zameni_sve, fleg_i, args.izlaz)
elif args.fajl and args.devet:
    fleg_zameni_sve = 'prvo'
    fleg_i = 'ne'
    if args.zameni_sve:
        fleg_zameni_sve = 'svako'
    if args.ignoriši:
        fleg_i = 'da'
    funkcija_devet(args.fajl, args.devet, fleg_zameni_sve, fleg_i, args.fajl)

