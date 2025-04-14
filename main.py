from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/enchantments")
def enchantments():
    return render_template("enchantments.html")

@app.route("/potions")
def potions():
    return render_template("potions.html")

@app.route("/alev")
def alev():
    return render_template("alev.html")

@app.route("/alevdencehre")
def alevdencehre():
    return render_template("alevdencehre.html")

@app.route("/ateskorumasi")
def ateskorumasi():
    return render_template("ateskorumasi.html")

@app.route("/atkikorumasi")
def atkikorumasi():
    return render_template("atkikorumasi.html")

@app.route("/ayartma")
def ayartma():
    return render_template("ayartma.html")

@app.route("/ayazdayuruyus")
def ayazdayuruyus():
    return render_template("ayazdayuruyus.html")

@app.route("/baglanmalaneti")
def baglanmalaneti():
    return render_template("baglanmalaneti.html")

@app.route("/cokluatis")
def cokluatis():
    return render_template("cokluatis.html")

@app.route("/darbe")
def darbe():
    return render_template("darbe.html")

@app.route("/delme")
def delme():
    return render_template("delme.html")

@app.route("/derinkosucu")
def derinkosucu():
    return render_template("derinkosucu.html")

@app.route("/dikenler")
def dikenler():
    return render_template("dikenler.html")

@app.route("/ganimet")
def ganimet():
    return render_template("ganimet.html")

@app.route("/girdap")
def girdap():
    return render_template("girdap.html")

@app.route("/guc")
def guc():
    return render_template("guc.html")

@app.route("/ipeksidokunus")
def ipeksidokunus():
    return render_template("ipeksidokunus.html")

@app.route("/kaybolmalaneti")
def kaybolmalaneti():
    return render_template("kaybolmalaneti.html")

@app.route("/keskinlik")
def keskinlik():
    return render_template("keskinlik.html")

@app.route("/kirilmazlik")
def kirilmazlik():
    return render_template("kirilmazlik.html")

@app.route("/koruma")
def koruma():
    return render_template("koruma.html")

@app.route("/onarim")
def onarim():
    return render_template("onarim.html")

@app.route("/patlamakorumasi")
def patlamakorumasi():
    return render_template("patlamakorumasi.html")

@app.route("/ruhhizi")
def ruhhizi():
    return render_template("ruhhizi.html")

@app.route("/sadakat")
def sadakat():
    return render_template("sadakat.html")

@app.route("/servet")
def servet():
    return render_template("servet.html")

@app.route("/solungac")
def solungac():
    return render_template("solungac.html")

@app.route("/sonsuzluk")
def sonsuzluk():
    return render_template("sonsuzluk.html")

@app.route("/supurucukenar")
def supurucukenar():
    return render_template("supurucukenar.html")

@app.route("/tuydususu")
def tuydususu():
    return render_template("tuydususu.html")

@app.route("/verimlilik")
def verimlilik():
    return render_template("verimlilik.html")

@app.route("/yildirimyonlendirmesi")
def yildirimyonlendirmesi():
    return render_template("yildirimyonlendirmesi.html")

@app.route("/alev1")
def alev1():
    return render_template("alev1.html")

@app.route("/alevdencehre1")
def alevdencehre1():
    return render_template("alevdencehre1.html")

@app.route("/alevdencehre2")
def alevdencehre2():
    return render_template("alevdencehre2.html")

@app.route("/ateskorumasi1")
def ateskorumasi1():
    return render_template("ateskorumasi1.html")

@app.route("/ateskorumasi2")
def ateskorumasi2():
    return render_template("ateskorumasi2.html")

@app.route("/ateskorumasi3")
def ateskorumasi3():
    return render_template("ateskorumasi3.html")

@app.route("/ateskorumasi4")
def ateskorumasi4():
    return render_template("ateskorumasi4.html")

@app.route("/atkikorumasi1")
def atkikorumasi1():
    return render_template("atkikorumasi1.html")

@app.route("/atkikorumasi2")
def atkikorumasi2():
    return render_template("atkikorumasi2.html")

@app.route("/atkikorumasi3")
def atkikorumasi3():
    return render_template("atkikorumasi3.html")

@app.route("/atkikorumasi4")
def atkikorumasi4():
    return render_template("atkikorumasi4.html")

@app.route("/ayartma1")
def ayartma1():
    return render_template("ayartma1.html")

@app.route("/ayartma2")
def ayartma2():
    return render_template("ayartma2.html")

@app.route("/ayartma3")
def ayartma3():
    return render_template("ayartma3.html")

@app.route("/ayazdayuruyus1")
def ayazdayuruyus1():
    return render_template("ayazdayuruyus1.html")

@app.route("/ayazdayuruyus2")
def ayazdayuruyus2():
    return render_template("ayazdayuruyus2.html")

@app.route("/baglanmalaneti1")
def baglanmalaneti1():
    return render_template("baglanmalaneti1.html")

@app.route("/cokluatis1")
def cokluatis1():
    return render_template("cokluatis1.html")

@app.route("/darbe1")
def darbe1():
    return render_template("darbe1.html")

@app.route("/darbe2")
def darbe2():
    return render_template("darbe2.html")

@app.route("/darbe3")
def darbe3():
    return render_template("darbe3.html")

@app.route("/darbe4")
def darbe4():
    return render_template("darbe4.html")

@app.route("/darbe5")
def darbe5():
    return render_template("darbe5.html")

@app.route("/delme1")
def delme1():
    return render_template("delme1.html")

@app.route("/delme2")
def delme2():
    return render_template("delme2.html")

@app.route("/delme3")
def delme3():
    return render_template("delme3.html")

@app.route("/delme4")
def delme4():
    return render_template("delme4.html")

@app.route("/derinkosucu1")
def derinkosucu1():
    return render_template("derinkosucu1.html")

@app.route("/derinkosucu2")
def derinkosucu2():
    return render_template("derinkosucu2.html")

@app.route("/derinkosucu3")
def derinkosucu3():
    return render_template("derinkosucu3.html")

@app.route("/dikenler1")
def dikenler1():
    return render_template("dikenler1.html")

@app.route("/dikenler2")
def dikenler2():
    return render_template("dikenler2.html")

@app.route("/dikenler3")
def dikenler3():
    return render_template("dikenler3.html")

@app.route("/ganimet1")
def ganimet1():
    return render_template("ganimet1.html")

@app.route("/ganimet2")
def ganimet2():
    return render_template("ganimet2.html")

@app.route("/ganimet3")
def ganimet3():
    return render_template("ganimet3.html")

@app.route("/girdap1")
def girdap1():
    return render_template("girdap1.html")

@app.route("/girdap2")
def girdap2():
    return render_template("girdap2.html")

@app.route("/girdap3")
def girdap3():
    return render_template("girdap3.html")

@app.route("/guc1")
def guc1():
    return render_template("guc1.html")

@app.route("/guc2")
def guc2():
    return render_template("guc2.html")

@app.route("/guc3")
def guc3():
    return render_template("guc3.html")

@app.route("/guc4")
def guc4():
    return render_template("guc4.html")

@app.route("/guc5")
def guc5():
    return render_template("guc5.html")

@app.route("/ipeksidokunus1")
def ipeksidokunus1():
    return render_template("ipeksidokunus1.html")

@app.route("/kaybolmalaneti1")
def kaybolmalaneti1():
    return render_template("kaybolmalaneti1.html")

@app.route("/keskinlik1")
def keskinlik1():
    return render_template("keskinlik1.html")

@app.route("/keskinlik2")
def keskinlik2():
    return render_template("keskinlik2.html")

@app.route("/keskinlik3")
def keskinlik3():
    return render_template("keskinlik3.html")

@app.route("/keskinlik4")
def keskinlik4():
    return render_template("keskinlik4.html")

@app.route("/keskinlik5")
def keskinlik5():
    return render_template("keskinlik5.html")

@app.route("/kirilmazlik1")
def kirilmazlik1():
    return render_template("kirilmazlik1.html")

@app.route("/kirilmazlik2")
def kirilmazlik2():
    return render_template("kirilmazlik2.html")

@app.route("/kirilmazlik3")
def kirilmazlik3():
    return render_template("kirilmazlik3.html")

@app.route("/koruma1")
def koruma1():
    return render_template("koruma1.html")

@app.route("/koruma2")
def koruma2():
    return render_template("koruma2.html")

@app.route("/koruma3")
def koruma3():
    return render_template("koruma3.html")

@app.route("/koruma4")
def koruma4():
    return render_template("koruma4.html")

@app.route("/patlamakorumasi1")
def patlamakorumasi1():
    return render_template("patlamakorumasi1.html")

@app.route("/patlamakorumasi2")
def patlamakorumasi2():
    return render_template("patlamakorumasi2.html")

@app.route("/patlamakorumasi3")
def patlamakorumasi3():
    return render_template("patlamakorumasi3.html")

@app.route("/patlamakorumasi4")
def patlamakorumasi4():
    return render_template("patlamakorumasi4.html")

@app.route("/ruhhizi1")
def ruhhizi1():
    return render_template("ruhhizi1.html")

@app.route("/ruhhizi2")
def ruhhizi2():
    return render_template("ruhhizi2.html")

@app.route("/ruhhizi3")
def ruhhizi3():
    return render_template("ruhhizi3.html")

@app.route("/sadakat1")
def sadakat1():
    return render_template("sadakat1.html")

@app.route("/sadakat2")
def sadakat2():
    return render_template("sadakat2.html")

@app.route("/sadakat3")
def sadakat3():
    return render_template("sadakat3.html")

@app.route("/servet1")
def servet1():
    return render_template("servet1.html")

@app.route("/servet2")
def servet2():
    return render_template("servet2.html")

@app.route("/servet3")
def servet3():
    return render_template("servet3.html")

@app.route("/solungac1")
def solungac1():
    return render_template("solungac1.html")

@app.route("/solungac2")
def solungac2():
    return render_template("solungac2.html")

@app.route("/solungac3")
def solungac3():
    return render_template("solungac3.html")

@app.route("/sonsuzluk1")
def sonsuzluk1():
    return render_template("sonsuzluk1.html")

@app.route("/supurucukenar1")
def supurucukenar1():
    return render_template("supurucukenar1.html")

@app.route("/supurucukenar2")
def supurucukenar2():
    return render_template("supurucukenar2.html")

@app.route("/supurucukenar3")
def supurucukenar3():
    return render_template("supurucukenar3.html")

@app.route("/tuydususu1")
def tuydususu1():
    return render_template("tuydususu1.html")

@app.route("/tuydususu2")
def tuydususu2():
    return render_template("tuydususu2.html")

@app.route("/tuydususu3")
def tuydususu3():
    return render_template("tuydususu3.html")

@app.route("/tuydususu4")
def tuydususu4():
    return render_template("tuydususu4.html")

@app.route("/verimlilik1")
def verimlilik1():
    return render_template("verimlilik1.html")

@app.route("/verimlilik2")
def verimlilik2():
    return render_template("verimlilik2.html")

@app.route("/verimlilik3")
def verimlilik3():
    return render_template("verimlilik3.html")

@app.route("/verimlilik4")
def verimlilik4():
    return render_template("verimlilik4.html")

@app.route("/verimlilik5")
def verimlilik5():
    return render_template("verimlilik5.html")

@app.route("/yildirimyonlendirmesi1")
def yildirimyonlendirmesi1():
    return render_template("yildirimyonlendirmesi1.html")

app.run(debug=True)