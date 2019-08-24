from flask import jsonify
from pony.orm import Database, db_session, select
from uuid import uuid4 as gid, UUID
from model import Student, Novosti, Kolegij, Repozitorij, Profesor, Kalendar


class Student1:
    @db_session()
    def ispisi():
        q = select(s for s in Student)
        data = [x.to_dict() for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s = Student(**s)
            return True, None
        except Exception as e:
            return False, str(e)
            
    @db_session
    def obrisi(jmbag_studenta):
        Student[jmbag_studenta].delete()
        return "Student je obrisan."

    @db_session
    def prijava1(email, lozinka):
        student = Student.get(email_studenta = email)
        if student:
            student =  student.to_dict()
            if student["lozinka_studenta"]==lozinka:
                return student
            else:
                return "Kriva lozinka"
        else:
            return "Korisnik ne postoji"


class Profesor1:
    @db_session()
    def ispisi():
        q = select(s for s in Profesor)
        data = [x.to_dict() for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s = Profesor(**s)
            return True, None
        except Exception as e:
            return False, str(e)

    @db_session
    def obrisi(oib_profesora):
        Profesor[oib_profesora].delete()
        return "Profesor je obrisan."

    @db_session
    def prijava2(email, lozinka):
        profesor = Profesor.get(email_profesora = email)
        if profesor:
            profesor =  profesor.to_dict()
            if profesor["lozinka_profesora"]==lozinka:
                return profesor
            else:
                return "Kriva lozinka"
        else:
            return "Korisnik ne postoji"


class Kolegij1:
    @db_session()
    def ispisi():
        r = select(p for p in Kolegij)
        data = [x.to_dict() for x in r]
        return data
        
    @db_session
    def dodaj(s):
        try:
            s = Kolegij(**s)
            return True, None
        except Exception as e:
            return False, str(e)

    @db_session
    def obrisi(id_kolegija):
        Kolegij[id_kolegija].delete()        
        return "Kolegij je obrisan."

    @db_session
    def ispisi_kolegij(ime_kolegija):
        kolegij = Kolegij.get(ime_kolegija=ime_kolegija)
        return kolegij

class Repozitorij1:
    @db_session()
    def ispisi():
        r = select(p for p in Repozitorij)
        data = [x.to_dict() for x in r]
        return data

    @db_session
    def dodaj(s):
        try:
            s = Repozitorij(**s)
            return True, None
        except Exception as e:
            return False, str(e)

    @db_session
    def obrisi(id_kolegija_rep):
        Repozitorij[id_kolegija_rep].delete()
        return "Repozitorij je obrisan."

    @db_session
    def ispisi_repozitorij(ime_kolegija_rep):
        repozitorij = Repozitorij.get(ime_kolegija_rep=ime_kolegija_rep)
        return repozitorij


class Novosti1:
    @db_session()
    def ispisi():
        n = select(o for o in Novosti)
        data = [x.to_dict() for x in n]
        return data

    @db_session
    def dodaj(s):
        try:
            s = Novosti(**s)
            return True, None
        except Exception as e:
            return False, str(e)

    @db_session
    def obrisi(id_novosti):
        Novosti[id_novosti].delete()
        return "Novost je obrisana."

    @db_session
    def ispisi_novost(id_novosti):
        novost = Novosti.get(id_novosti=id_novosti)
        return novost

class Kalendar1:
    @db_session()
    def ispisi():
        n = select(o for o in Kalendar)
        data = [x.to_dict() for x in n]
        return data
    
    @db_session
    def dodaj(s):
        try:
            s = Kalendar(**s)
            return True, None
        except Exception as e:
            return False, str(e)
    
    @db_session
    def obrisi(id_kalendar):
        Kalendar[id_kalendar].delete()
        return "Ispit je obrisan."
    
    @db_session
    def ispisi_ispit(id_kalendar):
        kal = Kalendar.get(id_kalendar=id_kalendar)
        return kal

    
