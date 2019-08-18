from uuid import uuid4 as gid, UUID
from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
import os

# spajanje na bazu
db = Database()

# ukoliko želiš da se svaki puta briše baza
#if os.path.exists("database.sqlite"):
#  os.remove("database.sqlite")

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

class Student(db.Entity):
    jmbag_studenta = PrimaryKey(str)
    oznaka_studenta = Required(str)  
    ime_studenta = Required(str)
    prezime_studenta = Required(str)
    email_studenta = Required(str, unique=True)
    lozinka_studenta = Required(str)
    fakultet = Required(str)

class Profesor(db.Entity):
    oib_profesora = PrimaryKey(str)
    oznaka_profesora = Required(str) 
    ime_profesora = Required(str)
    prezime_profesora = Required(str)
    email_profesora = Required(str, unique=True)
    lozinka_profesora = Required(str)
    fakultet = Required(str)

class Novosti(db.Entity):
    id = PrimaryKey(int, auto=True)
    naziv_novosti = Required(str)
    datum_novosti = Required(str)
    tekst_novosti = Required(str)

class Datoteka(db.Entity):
    id = PrimaryKey(int, auto=True)
    src_datoteke = Optional(str)
    kolegij = Set("Kolegij")
    repozitorij = Set("Repozitorij")

class Kolegij(db.Entity):
    id = PrimaryKey(int, auto=True) 
    ime_kolegija = Required(str) 
    literatura_kolegija = Required(str) 
    obaveze_kolegija = Required(str) 
    napomena_kolegija = Required(str) 
    datoteka = Optional(Datoteka)

class Repozitorij(db.Entity):
    id = PrimaryKey(int, auto=True) 
    ime_kolegija_rep = Required(str) 
    tekst_kolegija_rep = Required(str)
    datoteka = Optional(Datoteka)

class Kalendar(db.Entity):
    id = PrimaryKey(int, auto=True)
    naziv_kolegija = Required(str)
    datum_ispita = Required(str)
    vrijeme_ispita = Required(str)
    opis_ispita = Required(str)

     
# automatsko generiranje tablica u bazi
db.generate_mapping(check_tables=True, create_tables=True)
print("Tablice su kreirane! :)")

if __name__ == "__main__":
    with db_session() as s:
        a = Student(jmbag_studenta="0303068581", oznaka_studenta="S", ime_studenta="Iva", prezime_studenta="Sabolek", email_studenta="isabolek@unipu.hr", lozinka_studenta="iva123", fakultet="FIPU")
        b = Student(jmbag_studenta="0303068582", oznaka_studenta="S", ime_studenta="Monika", prezime_studenta="Lenić", email_studenta="mlenic@unipu.hr", lozinka_studenta="monika123", fakultet="FIPU")
        c = Student(jmbag_studenta="0303068583", oznaka_studenta="S", ime_studenta="Simona", prezime_studenta="Jurić", email_studenta="sjuric@unipu.hr", lozinka_studenta="simona123", fakultet="FIPU")
        
        d = Profesor(oib_profesora="1234567890", oznaka_profesora="P", ime_profesora="Nikola", prezime_profesora="Tanković", email_profesora="ntankovic@unipu.hr", lozinka_profesora="nikola123", fakultet="FIPU")
        e = Profesor(oib_profesora="3456789012", oznaka_profesora="P", ime_profesora="Tihomir", prezime_profesora="Orehovački", email_profesora="torehovacki@unipu.hr", lozinka_profesora="tiho123", fakultet="FIPU")
        
        k = Novosti(id="1", naziv_novosti="Poziv na Svečanu promociju diplomanata FIPU-a (14.6.2019.)", datum_novosti="06/14/2019", tekst_novosti="Čast nam je pozvati vas na promociju prvostupnika i magistara Fakulteta informatike u Puli koja će se održati u petak 14. lipnja 2019. u 12 sati u dvorani Pula (zgrada FET-a, Preradovićeva I/1). Dekan izv. prof. dr. sc. Giorgio Sinković. Rektor prof. dr. sc. Alfio Barbieri. Za dodatne informacije možete se obratiti djelatniku Ureda za studente i obrazovne programe: https://www.unipu.hr/vladimir.gnip")
        l = Novosti(id="2", naziv_novosti="Fakultet informatike u Puli na Danima komunikacije 2019", datum_novosti="06/03/2019", tekst_novosti="Studenti i nastavnici FIPU-a posjetili su konferenciju Dani komunikacije 2019 koja se i ove godine održala u atraktivnom rovinjskom Hotelu Lone. Naglasak koneferencije ove godine bio je na mogućnostima unaprjeđenja poslovanja i marketinške komunikacije apliciranjem suvremenih tehnologija umjetne inteligencije (engl. artificial intelligence - AI).")
        nn = Novosti(id="3", naziv_novosti="Poziv za studente: Prijavi se na Case Study Competition i osvoji vrijedne nagrade", datum_novosti="03/12/2019", tekst_novosti="Case Study Competition je natjecanje u rješavanju poslovnih slučajeva zadanih od strane poduzeća. Prijave su od 4.-17. ožujka, a rješenja se mogu predati online putem do 14. travnja. Natjecatelji mogu osvojiti vrijedne novčane nagrade u iznosu 10.000, 5.000 i 3.000 kuna. Poduzeća nude i mogućnost prakse, studentskog posla te brojne druge dodatne nagrade (poput vikend putovanja za pobjednički tim, poklon paketa, te VIP ulaznica za festival Ultra). Osim brojnih nagrada studenti na ovom natjecanju stječu vrijedno iskustvo i znanje te priliku da se predstave poslodavcu.Studenti se za natjecanje prijavljuju na web stranici natjecanja (https://www.estudent.hr/category/natjecanja/case-study-competition/#prijavi-se_tab) te u timovima od 2-4 člana mogu prijaviti čak 2 poslovna slučaja.Poduzeća koja sudjeluju ove godine su: Ina, Heineken, Loreal, Pliva, Helen Doron, Zagrebačka banka i Privredna banka Zagreb. Više o ovogodišnjim poslovnim slučajevima može se pronaći također na stranicama natjecanja.")

        lj= Kolegij(id="1", ime_kolegija="Dinamičke web aplikacije", literatura_kolegija="1) Gaston C. Hillar: Hands-On RESTful Python Web Services, Packt Publishing Ltd, 2018. 2) Daniel Gaspar, Jack Stouffer: Mastering Flask Web Development, Packt Publishing Ltd, 2018. 3) Marijn Haverbeke: Eloquent JavaScript, 3rd Edition, No Starch Press, 2019. 4) Olga Filipova: Learning Vue.js 2, Packt Publishing Ltd, 2016. 5) David Beazley, Brian K. Jones: Python Cookbook, O'Reilly Media, Inc., 2013.", obaveze_kolegija="Obaveza 	Udio u ocjeni Pohađanje nastave 	10% Projekt 	50% + 10% bonus Kontrolne zadaće10% Usmeni ispit 30% + 10% bonus", napomena_kolegija="Napomena: bodove iz nastave i kontrolnih zadaća moguće je nadoknaditi projektom. Studenti koji su ovaj kolegij odslušali ranije (ak. god. 2017/18. ili ranije) materijale mogu pronaći na arhivi e-učenja: http://ag2017-2018.e-ucenje.unipu.hr/. Ispit će se odviti na isti način kao i ranije, ali ne preko studlamp-a, nego će se poslužitelj dobiti u trenutku izvođenja ispita. Zadaci za vježbanje zajedno sa SQL skriptama dostupni su i na https://www.dropbox.com/s/gfn37c3jxoz2rup/IspitiVje%C5%BEbanje.zip?dl=0 Studenti koji su kolegij upisali ak. god. 2018./19. raditi će po novom programu.")
        m = Kolegij(id="2", ime_kolegija="Programsko inženjerstvo", literatura_kolegija="1) Manger, R.: Softversko inženjerstvo, nadopunjeno drugo izdanje skripte. Prirodoslovno Matematički Fakultet Sveučilišta u Zagrebu (2013) 2) Sommerville, I.: Software Engineering, 10th Edition. Pearson Education, Boston (2015) 3) Edd Dumbill, Mono: A Developer’s Notebook (2004) 4) Mono, službena dokumentacija, http://www.mono-project.com/docs/ 5) Charles Petzold, .NET Book Zero (2007)", obaveze_kolegija="Obaveza 	Udio u ocjeni Pohađanje nastave 	0% Seminarski rad 	20% Projekt 	80%", napomena_kolegija="Napomena: za dobivanje potpisa i pristupanje ispitu potrebno je sudjelovati na barem 80% nastavnih sati (predavanja i vježbe zasebno). ")
        n = Kolegij(id="3", ime_kolegija="Informatički praktikum 2", literatura_kolegija="- Uvod u Oracle ADF - ADF Business Components Task Flows – osnovni koncepti i upotreba - Izrada web stranica i fragmenata -  ADF komponente za izradu web i mobile aplikacija - Podjela i izrada projektnih zadataka - Prezentacije projektnih rješenja", obaveze_kolegija="Da položi kolegij, student/studentica mora: - ostvariti vise od 12,5 bodova od mogućih 25 (25%) na svakom od tri testa provjere znanja i - dobiti zadovoljavajuću timsku ocjenu projektnog zadatka (više od 12,5 od mogucih 25 ). Za redovite studente uvjet prijavljivanja konačnog ispita i sudjelovanje u prezentaciji projektnog rješenja, ostvaren minimalan broj bodova na sva tri testa.  U slučaju neispunjavanja navedenog uvjeta, smatra se da student nije ispunio svoje obaveze na kolegiju, te ne može pristupati ispitu, odnosno prezentaciji projektnog rješenja tima. Za izvanredne studente, na ispitnom roku se organizira polaganje svih testova, te nema uvjeta za izlazak na ispit i prezentaciju projektnog rješenja.", napomena_kolegija="Voditelji timova, mogu korigirati timsku ocjenu za svakog člana svog tima, na temelju njegovog doprinosa i sudjelovanja u izradi rješenja. Nakon prezentacije, voditelji timova su dužni dostaviti projektnu dokumentaciju na e-učenje kolegija. Konačna ocjena se formira zbrojem ostvarenih bodova testova i projektnog rješenja.")
        nj= Kolegij(id="4", ime_kolegija="Operacijska istraživanja", literatura_kolegija="1) Hillier, F.S., Lieberman, G.J. (1986.) Introduction to Operations Research, Holden-Day Inc, Oakland 2) Neralić, L. (2003.) Uvod u matematičko programiranje 1, Element, Zagreb 3) Anderson, D.R., Sweeney, D.J., Williams, T. A. (1994.) An Introduction to Management Science, West Publishing Company 4) Chiang, A.C. (1994.) Osnovne metode matematičke ekonomije, Mate, Zagreb 5) Martić, Lj. (1966.)  Matematičke metode za ekonomske analize II, Narodne novine, Zagreb", obaveze_kolegija="Ispit iz kolegija održava se na način da studenti najprije riješe tri zadatka kao uvjet za pristup usmenom dijelu ispita (nema klasičnog pismenog dijela ispita). Zadatke je potrebno zatražiti od nositelja kolegija na e-mail vbolj@unipu.hr tjedan dana prije termina ispita. ", napomena_kolegija="Usmeni dio ispita održava se u tjednu u kojem je termin ispta na ISVU portalu, a obavijest o terminu usmenog dijela biti će na stranicama fakulteta.")
        o = Kolegij(id="5", ime_kolegija="Upravljački informacijski sustavi", literatura_kolegija="Obvezna:  1. Čerić, V. i drugi: Informacijska tehnologija u poslovanju, Element, Zagreb, 2004. 2. Turban&Aronson&Liang&Sharda: Decision Support and Business Intelligence Systems, Pearson International Edition, 2007. 3. Tutban& Leider& McLean&Wetherbe: Information Technology for Management , John Wiley &Sons, 2007 4. Panian i ostali: Poslovna inteligencija: Studija slučajeva iz  hrv. prakse, Narodne novine, 2007, Zagreb", obaveze_kolegija="Da položi kolegij student/studentica mora: 1. Položiti oba kolokvija s minimalno 13 bodova  2. Uspješno riješiti dvije vježbe 3. Pristupiti usmenom ispitu", napomena_kolegija="Predmet ima ukupno 5 ECTS bodova. Bodovi kolokvija i vježbi se zbrajaju. Rad studenta se prati i ocjenjuje tijekom cijelog semestra kako slijedi: 1. Kolokvij I-  25% 2. Kolokvij II-  25% 3. Vježba 1: PowerPivot  - 20%,  4. Vježba 2: Rudarenje po podacima - 15%,  5. Usmeni ispit - 15%.")
        p = Kolegij(id="6", ime_kolegija="Modeliranje i simulacija", literatura_kolegija="Obvezna:1) [Panian, Ćurko] Poslovni informacijski sustavi  2) [Varga, Strugar] Informacijski sustavi u poslovanju    Izborna: 1) [Sterman] Business Dynamics 2) [Laguna] Business process modelling simulation and design 3) [Guttag] Introduction to Computation and Programming using Python 4) [Ross] Simulation", obaveze_kolegija="Da položi kolegij, student/studentica mora: 1. prisustvovatipredavanjima i vježbama -najmanje 70%, pripremati se za nastavu svakog tjedna utvrđivanjem i ponavljanjem gradiva iznijetog na predavanjima proteklog tjedna, aktivno se uključiti u nastavni proces rješavanjem zadataka, odgovorima na postavljena pitanja, sudjelovanjem u diskusiji i sl.Student ima pravo prisustvovanje na nastavi zamijeniti aktivnim sudjelovanjem u izvanučioničnoj nastavi (zadaci, konkretni praktični primjeri, kratke rasprave i sl.). 2. Izraditi projektprema uputama nastavnika i predati u roku koji utvrdi predmetni nastavnik ili asistent te izvršiti njegovu prezentaciju prema dogovoru s predmetnim nastavnikom/asistentom. Izradom i prezentacijom projektnog zadatka student ostvaruje do max. 20% uspješnosti.3. pristupiti i položiti usmeni ispit koji obuhvaća sadržaj kolegija. Položenim ispitom smatra se ispit na kojem je student ostvario najmanje 50% od ukupnog broja bodova", napomena_kolegija="Konačna ocjena iz predmeta izvodi se iz ukupno ostvarenog postotka uspješnosti naispitu, projektnog zadatka te pohađanja i/ili aktivnosti u nastavi")
        r = Kolegij(id="7", ime_kolegija="Poslovni informacijski sustavi", literatura_kolegija="Obvezna:1) [Panian, Ćurko] Poslovni informacijski sustavi  2) [Varga, Strugar] Informacijski sustavi u poslovanju    Izborna: 1) [Baltzan] Business Driven Information Systems 2) [Curtis, Cobham] Business Information Systems 3) [Cadle] Developing Information Systems 4) [Provost, Fawcett] Data Science for Business", obaveze_kolegija="Da položi kolegij, student/studentica mora: 1. prisustvovati predavanjima i vježbama -najmanje 70%, pripremati se za nastavu svakog tjedna utvrđivanjem i ponavljanjem gradiva iznijetog na predavanjima proteklog tjedna, aktivno se uključiti u nastavni proces rješavanjem zadataka, odgovorima na postavljena pitanja, sudjelovanjem u diskusiji i sl. Student ima pravo prisustvovanje na nastavi zamijeniti aktivnim sudjelovanjem u izvanučioničnoj nastavi (zadaci, konkretni praktični primjeri, kratke rasprave i sl.). Prisustvom student ostvaruje max. 10% uspješnosti.  2. Izraditi referat/projekt prema uputama nastavnika i predati u roku koji utvrdi predmetni nastavnik ili asistent te izvršiti njegovu prezentaciju prema dogovoru s predmetnim nastavnikom/asistentom. Izradom i prezentacijom projektnog zadatka student ostvaruje do max. 40% uspješnosti. 3. pristupiti i položiti usmeniispit koji obuhvaća sadržaj kolegija. Položenim ispitom smatra se ispit na kojem je student ostvario najmanje 50% od ukupnog broja bodova.", napomena_kolegija="Konačna ocjena iz predmeta izvodi se iz ukupno ostvarenog postotka uspješnosti na ispitu, iz referata/projektnog zadatkate pohađanja i/ili aktivnosti u nastavi")
        
        s = Repozitorij(id="10", ime_kolegija_rep="Dinamičke web aplikacije", tekst_kolegija_rep="DWA, pitanja sa dosadasnjih rokova, ako netko zna odgovor na zadnja tri neka napise u komentarima :) DWA-prava skripta.docx")
        t = Repozitorij(id="11", ime_kolegija_rep="Programsko inženjerstvo", tekst_kolegija_rep="Programsko, pitanja sa dosadasnjih rokova, ako netko zna odgovor na zadnja tri neka napise u komentarima :) PROGRAMSKO-prava skripta.docx")
        u = Repozitorij(id="12", ime_kolegija_rep="Informatički praktikum 2", tekst_kolegija_rep="Praktikum, pitanja sa dosadasnjih rokova, ako netko zna odgovor na zadnja tri neka napise u komentarima :) Praktikum-prava skripta.docx")
        v = Repozitorij(id="13", ime_kolegija_rep="Operacijska istraživanja", tekst_kolegija_rep="Evo riješeni zadaci za ta tri zadatka :) OI-zadaci.docx")
        z = Repozitorij(id="14", ime_kolegija_rep="Upravljački informacijski sustavi", tekst_kolegija_rep="Treba napisat word dokument u kojem zapravo vodimo dnevnik prakse,sve što smo radili. Dnevnik_prakse.docx")
        q = Repozitorij(id="15", ime_kolegija_rep="Modeliranje i simulacija", tekst_kolegija_rep="MIS, pitanja sa dosadasnjih rokova, ako netko zna odgovor na zadnja tri neka napise u komentarima :) MIS-prava skripta.docx")
        x = Repozitorij(id="16", ime_kolegija_rep="Poslovni informacijski sustavi", tekst_kolegija_rep="PIS, pitanja sa dosadasnjih rokova, ako netko zna odgovor na zadnja tri neka napise u komentarima :) PIS-prava skripta.docx")

        mmm = Kalendar(id="12", naziv_kolegija="DWA", datum_ispita="06/14/2019", vrijeme_ispita="14/10", opis_ispita="Ispit se odrzava")