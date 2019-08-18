from flask import Flask, Response, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS
from domain import Student1, Novosti1, Kolegij1, Repozitorij1, Profesor1,Kalendar1


app = Flask(__name__)
CORS(app)



@app.route("/")
def home():
    r = Response(status=200)
    r.set_data("Ovo je početna stranica.")
    return r

# studenti 

@app.route("/studenti", methods=["GET"])
def ispisi_studente():
    studenti = Student1.ispisi()
    return jsonify({"data": studenti})

@app.route("/studenti/<jmbag>", methods=["GET"])
def ispisi_studenta(jmbag):
    jmbag = str(jmbag)
    student = Student1.ispisi_studenta(jmbag)
    return jsonify(student)

@app.route("/studenti", methods=["POST"])
def dodaj_studenta():
    status, greske = Student1.dodaj(request.get_json())
    if status:
        return Response("Novi student je dodan.", status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
    return r

@app.route('/studenti/<jmbag_studenta>', methods = ['DELETE'])
def obrisi_studenta(jmbag_studenta):
    student_jmbag = str(jmbag_studenta)
    stu = Student1.obrisi(student_jmbag)
    return jsonify(stu)


# prijava

@app.route("/prijava1/<email>/<lozinka>", methods = ['GET'])
def prijava_studenta(email, lozinka):
    email = str(email)
    lozinka = str(lozinka)
    prijava = Student1.prijava1(email, lozinka)
    return jsonify(prijava)

@app.route("/prijava2/<email>/<lozinka>", methods = ['GET'])
def prijava_profesora(email, lozinka):
    email = str(email)
    lozinka = str(lozinka)
    prijava = Profesor1.prijava2(email, lozinka)
    return jsonify(prijava)



# profesori

@app.route("/profesori", methods=["GET"])
def ispisi_profesore():
    profesori = Profesor1.ispisi()
    return jsonify({"data": profesori})

@app.route("/profesori", methods=["POST"])
def dodaj_profesora():
    status, greske = Profesor1.dodaj(request.get_json())
    if status:
        return Response("Novi profesor je dodan.", status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
    return r

@app.route('/profesori/<oib_profesora>', methods = ['DELETE'])
def obrisi_profesora(oib_profesora):
    profesor_oib = str(oib_profesora)
    pro = Profesor1.obrisi(profesor_oib)
    return jsonify(pro)

# popis kolegija

@app.route("/popis_kolegija", methods=["GET"])
def ispisi_sve_kolegije():
    kolegij = Kolegij1.ispisi()
    return jsonify({"data": kolegij})

@app.route("/popis_kolegija", methods=["POST"])
def dodaj_novi_kolegij():
    status, greske = Kolegij1.dodaj(request.get_json())
    if status:
        return Response("Novi kolegij je dodan.", status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        print(greske)
    return r

@app.route('/popis_kolegija/<id_kolegija>', methods = ['DELETE'])
def obrisi_kolegij(id_kolegija):
    kolegij_id = str(id_kolegija)
    kol = Kolegij1.obrisi(kolegij_id)
    return jsonify(kol)

@app.route('/popis_kolegija/<ime_kolegija>', methods = ['GET'])
def ispisi_kolegij(ime_kolegija):
    kolegij_id = str(ime_kolegija)
    pkolegij = Kolegij1.ispisi_kolegij(kolegij_id)
    return jsonify(pkolegij)

'''unutar novog kolegija da se doda sve unutra, isto tako da se unutar već postojećeg kolegija doda neka nova stavka'''

# popis repozitorija

@app.route("/popis_repozitorija", methods=["GET"])
def ispisi_sve_kolegije_repozitorija():
    repozitorij = Repozitorij1.ispisi()
    return jsonify({"data": repozitorij})

@app.route("/popis_repozitorija", methods=["POST"])
def dodaj_novi_repozitorij():
    status, greske = Repozitorij1.dodaj(request.get_json())
    if status:
        return Response("Kolegij je dodan u repozitorij.", status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
    return r

@app.route('/popis_repozitorija/<id_kolegija_rep>', methods = ['DELETE'])
def obrisi_kolegij_repozitorija(id_kolegija_rep):
    repozitorij_id = str(id_kolegija_rep)
    rep = Repozitorij1.obrisi(repozitorij_id)
    return jsonify(rep)

@app.route('/popis_repozitorija/<ime_kolegija_rep>', methods = ['GET'])
def ispisi_kolegij_repozitorija(ime_kolegija_rep):
    repozitorij_id = str(ime_kolegija_rep)
    prepozitorij = Repozitorij1.ispisi_repozitorij(repozitorij_id)
    return jsonify(prepozitorij)


# novosti

@app.route("/novosti", methods=["GET"])
def ispisi_sve_novosti():
    novosti = Novosti1.ispisi()
    return jsonify({"data": novosti})

@app.route("/novosti", methods=["POST"])
def dodaj_novost():
    status, greske = Novosti1.dodaj(request.get_json())
    if status:
        return Response("Novost je dodana.", status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        print(greske)
    return r

@app.route('/novosti/<id_novosti>', methods = ['DELETE'])
def obrisi_novost(id_novosti):
    novost_id = str(id_novosti)
    nov = Novosti1.obrisi(novost_id)
    return jsonify(nov)

@app.route('/novosti/<id_novosti>', methods = ['GET'])
def ispisi_jednu_novost(id_novosti):
    novost_id = str(id_novosti)
    novosti = Novosti1.ispisi_novost(novost_id).to_dict()
    return jsonify(novosti)

#kalendar
@app.route("/kalendar", methods=["GET"])
def ispisi_sve_ispite():
    kalendar = Kalendar1.ispisi()
    return jsonify({"data": kalendar})
    
@app.route("/kalendar", methods=["POST"])
def dodaj_ispit():
    status, greske = Kalendar1.dodaj(request.get_json())
    if status:
        return Response("Ispit je dodan.", status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        print(greske)
    return r
    
@app.route('/kalendar/<id_kalendar>', methods = ['DELETE'])
def obrisi_ispit(id_kalendar):
    kalendar_id = str(id_kalendar)
    nov = Kalendar1.obrisi(kalendar_id)
    return jsonify(nov)
    
@app.route('/kalendar/<id_kalendar>', methods = ['GET'])
def ispisi_jedan_ispit(id_kalendar):
    kalendar_id = str(id_kalendar)
    kalendar = Kalendar1.ispisi_ispit(kalendar_id).to_dict()
    return jsonify(kalendar)


if __name__ == "__main__":
    app.run(debug=True)
