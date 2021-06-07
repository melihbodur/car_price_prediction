import pickle
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import webbrowser
from warnings import filterwarnings
filterwarnings('ignore')
from tkinter import *
from tkinter.ttk import Combobox
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
from PIL import Image, ImageTk



a3_m = pickle.load(open("a3_m","rb"))
a4_m = pickle.load(open("a4_m","rb"))
a6_m = pickle.load(open("a6_m","rb"))
accenb_m = pickle.load(open("accenb_m","rb"))
accent_m = pickle.load(open("accent_m","rb"))
accente_m = pickle.load(open("accente_m","rb"))
auris_m = pickle.load(open("auris_m","rb"))
avensis_m = pickle.load(open("avensis_m","rb"))
bessekiz_m = pickle.load(open("bessekiz_m","rb"))
c4_m = pickle.load(open("c4_m","rb"))
c4_pi_m = pickle.load(open("c4_pi_m","rb"))
civic_m = pickle.load(open("civic_m","rb"))
c5_m = pickle.load(open("c5_m","rb"))
clio_m = pickle.load(open("clio_m","rb"))
corolla_m = pickle.load(open("corolla_m","rb"))
egea_m = pickle.load(open("egea_m","rb"))
elantra_m = pickle.load(open("elantra_m","rb"))
elysee_m = pickle.load(open("elysee_m","rb"))
fabia_m = pickle.load(open("fabia_m","rb"))
fiesta_m = pickle.load(open("fiesta_m","rb"))
fluence_m = pickle.load(open("fluence_m","rb"))
focus_m = pickle.load(open("focus_m","rb"))
golf_m = pickle.load(open("golf_m","rb"))
i20_m = pickle.load(open("i20_m","rb"))
i30_m = pickle.load(open("i30_m","rb"))
jazz_m = pickle.load(open("jazz_m","rb"))
ikiyedi_m = pickle.load(open("ikiyedi_m","rb"))
jetta_m = pickle.load(open("jetta_m","rb"))
linea_m = pickle.load(open("linea_m","rb"))
megane_m = pickle.load(open("megane_m","rb"))
micra_m = pickle.load(open("micra_m","rb"))
mondeo_m = pickle.load(open("mondeo_m","rb"))
octavia_m = pickle.load(open("octavia_m","rb"))
palio_m = pickle.load(open("palio_m","rb"))
passat_m = pickle.load(open("passat_m","rb"))
polo_m = pickle.load(open("polo_m","rb"))
primera_m = pickle.load(open("primera_m","rb"))
S40_m = pickle.load(open("S40_m","rb"))
S60_m = pickle.load(open("S60_m","rb"))
saxo_m = pickle.load(open("saxo_m","rb"))
superB_m = pickle.load(open("superB_m","rb"))
symbol_m = pickle.load(open("symbol_m","rb"))
ücbir_m = pickle.load(open("ücbir_m","rb"))
ücsekiz_m = pickle.load(open("ücsekiz_m","rb"))
ücyedi_m = pickle.load(open("ücyedi_m","rb"))
yaris_m = pickle.load(open("yaris_m","rb"))
dogan_m = pickle.load(open("megane_m","rb"))
Insignia_m = pickle.load(open("Insignia_m","rb"))
vectra_m = pickle.load(open("vectra_m","rb"))
corsa_m = pickle.load(open("corsa_m","rb"))
astra_m = pickle.load(open("astra_m","rb"))
bir_m = pickle.load(open("bir_m","rb"))
iki_m = pickle.load(open("iki_m","rb"))
üc_m = pickle.load(open("üc_m","rb"))
e_m = pickle.load(open("e_m","rb"))
c_m = pickle.load(open("c_m","rb"))

root = Tk()
root.geometry("1500x800")
from PIL import Image, ImageTk
import tkinter as tk

root.configure(background='white')


def benzin():
    global mevkisi

    bölge = mevki_kutu.get()
    if (bölge == "Benzin"):
        mevkisi = 0
    elif (bölge == "Dizel"):
        mevkisi = 1
    elif (bölge == "LPG & Benzin"):
        mevkisi = 2

    return mevkisi


def vites():
    global vitesi

    bölgee = vites_kutu.get()
    if (bölgee == "Düz"):
        vitesi = 0
    elif (bölgee == "Yarı Otomatik"):
        vitesi = 1
    elif (bölgee == "Otomatik"):
        vitesi = 2

    return vitesi


aram = Image.open("aram.png")
aram = aram.resize((60, 40))
aram = ImageTk.PhotoImage(aram)

kredm = Image.open("kredm.png")
kredm = kredm.resize((40, 20))
kredm = ImageTk.PhotoImage(kredm)

sece = Image.open("secc.png")
sece = sece.resize((30, 20))
sece = ImageTk.PhotoImage(sece)

basv = Image.open("basv.png")
basv = basv.resize((45, 20))
basv = ImageTk.PhotoImage(basv)

mdl = StringVar()
yıl = StringVar()
km = StringVar()
mevkisi = Entry(root)
vitesi = Entry(root)
mevkiler = ["Benzin", "Dizel", "LPG & Benzin"]
vitess = ["Düz", "Yarı Otomatik", "Otomatik"]
mevki_kutu = Combobox(root, values=mevkiler)
mevki_kutu.place(x=300, y=160)
vites_kutu = Combobox(root, values=vitess)
vites_kutu.place(x=300, y=240)

Button(root, text="Seç", image=sece, width=25, command=benzin).place(x=445, y=160)
Button(root, text="Seç", image=sece, width=25, command=vites).place(x=445, y=240)
Entry(root, text=mdl, width=25).place(x=300, y=330)
Entry(root, text=yıl, width=25).place(x=300, y=410)
Entry(root, text=km, width=25).place(x=300, y=490)

Label(root, text="Benzin Türü", font=("Helvetica", 10, "bold",), bg="White",
      width=30).place(x=260, y=130)
Label(root, text="Vites Türü", font=("Helvetica", 10, "bold",), bg="White",
      width=30).place(x=260, y=210)
Label(root, text="Motor Gücü", font=("Helvetica", 10, "bold",), bg="White",
      width=30).place(x=260, y=290)
Label(root, text="Üretim Yılı", font=("Helvetica", 10, "bold",), bg="White",
      width=30).place(x=260, y=380)
Label(root, text="Km", font=("Helvetica", 10, "bold",), bg="White",
      width=30).place(x=260, y=460)

Label(root, text="ARABA FİYAT TAHMİNİ", font=("Helvetica", 20, "bold",), bg="White",
      width=30).place(x=130, y=10)


def kredim():
    global kredii

    bölgeee = kredi_kutu.get()
    if (bölgeee == "3 Ay"):
        kredii = "3 Ay"
    elif (bölgeee == "6 Ay"):
        kredii = "6 Ay"
    elif (bölgeee == "9 Ay"):
        kredii = "9 Ay"

    elif (bölgeee == "12 Ay"):
        kredii = "12 Ay"

    elif (bölgeee == "18 Ay"):
        kredii = "18 Ay"

    elif (bölgeee == "24 Ay"):
        kredii = "24 Ay"

    elif (bölgeee == "30 Ay"):
        kredii = "30 Ay"

    elif (bölgeee == "36 Ay"):
        kredii = "36 Ay"
    return kredii


kredii = Entry(root)
kredisi = ["3 Ay", "6 Ay", "9 Ay", "12 Ay", "18 Ay", "24 Ay", "30 Ay", "36 Ay"]
kredi_kutu = Combobox(root, values=kredisi)
kredi_kutu.place(x=1050, y=140)
Button(root, text="Kredi Seç", image=kredm, width=40, command=kredim).place(x=1200, y=135)

kredi_miktarı = StringVar()
Entry(root, text=kredi_miktarı, width=25).place(x=800, y=140)

Label(root, text="Kredi Vadesi", font=("Helvetica", 13, "bold",), bg="White",
      width=20).place(x=1000, y=100)

Label(root, text="Kredi Tutarı", font=("Helvetica", 13, "bold",), bg="White",
      width=20).place(x=800, y=100)

Label(root, text="KREDİ HESAPLA", font=("Helvetica", 20, "bold",), bg="White",
      width=20).place(x=850, y=10)

mmme = Image.open("mavi.png")
mmme = mmme.resize((5, 40000))
mmme = ImageTk.PhotoImage(mmme)
labb = Label(image=mmme).place(x=780, y=0)

car2 = Image.open("carrrr.jpg")
car2 = car2.resize((300, 190))
car2 = ImageTk.PhotoImage(car2)
labb = Label(image=car2).place(x=230, y=580)

# ing
ing = Image.open("ingg.png")
ing = ing.resize((110, 40))
ing = ImageTk.PhotoImage(ing)
labb = Label(image=ing).place(x=800, y=250)

# iiş
işi = Image.open("işbn.png")
işi = işi.resize((110, 40))
işi = ImageTk.PhotoImage(işi)
labb = Label(image=işi).place(x=800, y=350)

# iyapı
yap = Image.open("yapım3.jpg")
yap = yap.resize((110, 40))
yap = ImageTk.PhotoImage(yap)
labb = Label(image=yap).place(x=800, y=450)

gar = Image.open("gari2.jpg")
gar = gar.resize((110, 40))
gar = ImageTk.PhotoImage(gar)
labb = Label(image=gar).place(x=800, y=550)

zir = Image.open("zir4.jpg")
zir = zir.resize((110, 40))
zir = ImageTk.PhotoImage(zir)
labb = Label(image=zir).place(x=800, y=650)

Label(root, text="Faiz Oranı", font=("Helvetica", 10, "bold",), bg="White",
      width=15).place(x=950, y=200)
Label(root, text="Aylık Taksit", font=("Helvetica", 10, "bold",), bg="White",
      width=15).place(x=1100, y=200)
Label(root, text="Toplam Ödeme", font=("Helvetica", 10, "bold",), bg="White",
      width=15).place(x=1250, y=200)


def kredi():
    browser = webdriver.Chrome("C:\Selenium\chromedriver", chrome_options=chrome_options)
    browser.get("https://www.hangikredi.com/kredi/ihtiyac-kredisi")
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/div/div/div[1]/div/input") \
        .send_keys(kredi_miktarı.get())

    select = Select(browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/div/div/div[2]/div/select"))
    select.select_by_visible_text(kredii)
    time.sleep(0.5)
    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/div/div/div[3]/a").click()

    ing_faiz = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/p").text
    ing_aylık_taksit = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]/div[4]/div/p").text
    ing_toplam = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]/div[5]/div/p").text
    ing_başvurr = browser.find_element_by_xpath(
        '/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]/div[6]/div/a[1]').get_attribute('href')

    iş_faiz = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/p").text
    iş_aylık_taksit = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[3]/div/p").text
    iş_toplam = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[4]/div/p").text
    iş_başvurr = browser.find_element_by_xpath(
        '/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[5]/div/a[1]').get_attribute('href')

    yapı_faiz = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/p").text
    yapı_aylık_taksit = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[3]/div/p").text
    yapı_toplam = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[4]/div/p").text
    yapı_başvurr = browser.find_element_by_xpath(
        '/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[5]/div/a[1]').get_attribute('href')

    garanti_faiz = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/p").text
    garanti_aylık_taksit = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[4]/div/p").text
    garanti_toplam = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[5]/div/p").text
    garanti_başvurr = browser.find_element_by_xpath(
        '/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[6]/div/a[1]').get_attribute('href')

    ziraat_faiz = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div[2]/div/p").text
    ziraat_aylık_taksit = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div[3]/div/p").text
    ziraat_toplam = browser.find_element_by_xpath(
        "/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div[4]/div/p").text
    ziraat_başvurr = browser.find_element_by_xpath(
        '/html/body/div[7]/div[1]/div/div/div[1]/div[1]/div[5]/div/div[3]/div/div/div[2]/div[5]/div/a').get_attribute(
        'href')

    Label(root, text=ing_faiz, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=950, y=250)
    Label(root, text=ing_aylık_taksit, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1100, y=250)
    Label(root, text=ing_toplam, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1250, y=250)

    Label(root, text=iş_faiz, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=950, y=350)
    Label(root, text=iş_aylık_taksit, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1100, y=350)
    Label(root, text=iş_toplam, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1250, y=350)

    Label(root, text=yapı_faiz, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=950, y=450)
    Label(root, text=yapı_aylık_taksit, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1100, y=450)
    Label(root, text=garanti_toplam, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1250, y=450)

    Label(root, text=garanti_faiz, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=950, y=550)
    Label(root, text=garanti_aylık_taksit, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1100, y=550)
    Label(root, text=garanti_toplam, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1250, y=550)

    Label(root, text=ziraat_faiz, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=950, y=650)
    Label(root, text=ziraat_aylık_taksit, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1100, y=650)
    Label(root, text=ziraat_toplam, font=("Helvetica", 10, "bold",), bg="White",
          width=15).place(x=1250, y=650)

    def ing_baş():
        url = "{}".format(
            "https://www.ing.com.tr/tr/sizin-icin/krediler/ihtiyac-kredisi-basvuru-formu?utm_source=hangikredi&utm_medium=karsilastirma&utm_campaign=ihtiyac_kredisi5&utm_content=ihtiyackredisi_62439938")
        webbrowser.open_new_tab(url)

    button = Button(root, text='    BAŞVUR    ', width=40, image=basv, command=ing_baş)
    button.place(x=1400, y=250)

    def iş_baş():
        url = "{}".format(
            "https://www.isbank.com.tr/internet/MainPageEnter.aspx?src=BKTP_HizliKrediBasvuruAnasayfa&channel=WebSitesi&site=HNGSNET-21")
        webbrowser.open_new_tab(url)

    button = Button(root, text='    BAŞVUR    ', width=40, image=basv, command=iş_baş)
    button.place(x=1400, y=350)

    def yapı_baş():
        url = "{}".format(
            "https://www.yapikredi.com.tr/basvuru-merkezi/bireysel-ihtiyac-kredisi/?utm_source=hangikredi&utm_medium=cpc&utm_campaign=bik_web")
        webbrowser.open_new_tab(url)

    button = Button(root, text='    BAŞVUR    ', image=basv, width=40, command=yapı_baş)
    button.place(x=1400, y=450)

    def garanti_baş():
        url = "{}".format(
            "https://www.garantibbva.com.tr/hizli-kredi?cid=oth:afl:oth:hangikredi-ihtiyac-kredisi-listeleme:ihtiyac-kredisi:62439939::::::oth:::#calcContent=UID27eca7f")
        webbrowser.open_new_tab(url)

    button = Button(root, text='    BAŞVUR    ', image=basv, width=40, command=garanti_baş)
    button.place(x=1400, y=550)

    def ziraat_baş():
        url = "{}".format(ziraat_başvurr)
        webbrowser.open_new_tab(url)

    button = Button(root, text='    BAŞVUR    ', image=basv, width=40, command=ziraat_baş)
    button.place(x=1400, y=650)


Button(root, text="Ara", image=aram, width=55, height=30, command=kredi).place(x=1400, y=100)

# butonlar

but = Image.open("tahmn.png")
but = but.resize((67, 20))
but = ImageTk.PhotoImage(but)


# 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333


def golf_s():
    global wol

    bölgeeee = ara_kutu.get()
    if (bölgeeee == "Polo"):
        wol = polo_m
    elif (bölgeeee == "Passat"):
        wol = passat_m
    elif (bölgeeee == "Jetta"):
        wol = jetta_m

    elif (bölgeeee == "Golf"):
        wol = golf_m

    return wol


wol = Entry(root)
wol_lis = ["Polo", "Passat", "Jetta", "Golf"]
ara_kutu = Combobox(root, values=wol_lis)
ara_kutu.place(x=10, y=60)

# wolswogen
vols = Image.open("wolsv.png")
vols = vols.resize((60, 40))
vols_l = ImageTk.PhotoImage(vols)
labb = Button(image=vols_l, command=golf_s).place(x=10, y=10)


def golf():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = wol.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", image=but, width=60, command=golf).place(x=160, y=57)
# 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

# Renould
ren = Image.open("renoult.jpg")
ren = ren.resize((60, 40))
photo = ImageTk.PhotoImage(ren)


def reno():
    global ren

    bölgeeee = ren_kutu.get()
    if (bölgeeee == "Clio"):
        ren = clio_m
    elif (bölgeeee == "Fluence"):
        ren = fluence_m
    elif (bölgeeee == "Megane"):
        ren = megane_m

    elif (bölgeeee == "Symbol"):
        ren = symbol_m

    return ren


labb = Button(image=photo, command=reno).place(x=10, y=100)
ren = Entry(root)
ren_lis = ["Clio", "Fluence", "Symbol", "Megane"]
ren_kutu = Combobox(root, values=ren_lis)
ren_kutu.place(x=10, y=150)


def ren_u():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = ren.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=ren_u).place(x=160, y=147)

# RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR


# Volwo
vol = Image.open("volkoy.jpg")
vol = vol.resize((60, 40))
vol_p = ImageTk.PhotoImage(vol)


def vol():
    global volv

    bölgeeee = voll_kutu.get()
    if (bölgeeee == "S40"):
        volv = S40_m
    elif (bölgeeee == "S60"):
        volv = S60_m

    return volv


labb = Button(image=vol_p, command=vol).place(x=10, y=190)

volv = Entry(root)
vol_lis = ["S40", "S60"]
voll_kutu = Combobox(root, values=vol_lis)
voll_kutu.place(x=10, y=240)


def volve():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = volv.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=volve).place(x=160, y=237)

# Toyoto
toy = Image.open("toyo.jpg")
toy = toy.resize((60, 40))
toy_p = ImageTk.PhotoImage(toy)


def toy():
    global toyo

    bölgeeee = toy_kutu.get()
    if (bölgeeee == "Auris"):
        toyo = auris_m
    elif (bölgeeee == "Avensis"):
        toyo = avensis_m
    elif (bölgeeee == "Corolla"):
        toyo = corolla_m

    elif (bölgeeee == "Yaris"):
        toyo = yaris_m

    return toyo


labb = Button(image=toy_p, command=toy).place(x=10, y=290)

toyo = Entry(root)
toyo_lis = ["Auris", "Avensis", "Corolla", "Yaris"]
toy_kutu = Combobox(root, values=toyo_lis)
toy_kutu.place(x=10, y=340)


def toy_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = toyo.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=toy_t).place(x=160, y=337)

# RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR


# tofaş
tofa = Image.open("tofi.jpg")
tofa = tofa.resize((60, 40))
tofa_p = ImageTk.PhotoImage(tofa)


def tof():
    global tofa

    bölgeeee = tof_kutu.get()
    if (bölgeeee == "Doğan"):
        tofa = dogan_m
    elif (bölgeeee == "Kartal"):
        tofa = kartal_m

    return tofa


labb = Button(image=tofa_p, command=tof).place(x=10, y=390)

tofa = Entry(root)
tof_lis = ["Doğan", "Kartal"]
tof_kutu = Combobox(root, values=tof_lis)
tof_kutu.place(x=10, y=440)


def tof_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = tofa.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=tof_t).place(x=160, y=437)

# skoda
skod = Image.open("skod.jpg")
skod = skod.resize((60, 40))
skod_p = ImageTk.PhotoImage(skod)


def skod():
    global skoda

    bölgeeee = skod_kutu.get()
    if (bölgeeee == "Octavia"):
        skoda = octavia_m
    elif (bölgeeee == "SuperB"):
        skoda = superB_m
    elif (bölgeeee == "Fabia"):
        skoda = fabia_m

    return skoda


labb = Button(image=skod_p, command=skod).place(x=10, y=490)

skoda = Entry(root)
skod_lis = ["Octavia", "SuperB", "Fabia"]
skod_kutu = Combobox(root, values=skod_lis)
skod_kutu.place(x=10, y=540)


def skoda_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = skoda.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=skoda_t).place(x=160, y=537)

# pejo pejo
reno = Image.open("pegou.jpg")
reno = reno.resize((60, 40))
reno_p = ImageTk.PhotoImage(reno)


def rennoo():
    global renou

    bölgeeee = renou_kutu.get()
    if (bölgeeee == "508"):
        renou = bessekiz_m
    elif (bölgeeee == "207"):
        renou = ikiyedi_m
    elif (bölgeeee == "307"):
        renou = ücyedi_m

    elif (bölgeeee == "308"):
        renou = ücsekiz_m

    elif (bölgeeee == "301"):
        renou = ücbir_m

    return renou


labb = Button(image=reno_p, command=rennoo).place(x=10, y=590)

renou = Entry(root)
renou_lis = ["508", "207", "307", "308", "301"]
renou_kutu = Combobox(root, values=renou_lis)
renou_kutu.place(x=10, y=640)


def renou_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = renou.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=renou_t).place(x=160, y=637)

# opel
opel = Image.open("opel.jpg")
opel = opel.resize((60, 40))
opel_p = ImageTk.PhotoImage(opel)


def opell():
    global opel1

    bölgeeee = opel_kutu.get()
    if (bölgeeee == "Astra"):
        opel1 = astra_m
    elif (bölgeeee == "Vectra"):
        opel1 = vectra_m
    elif (bölgeeee == "Corsa"):
        opel1 = corsa_m

    elif (bölgeeee == "Insignia"):
        opel1 = Insignia_m

    return opel1


labb = Button(image=opel_p, command=opell).place(x=10, y=690)

opel1 = Entry(root)
opel_lis = ["Astra", "Vectra", "Corsa", "Insignia"]
opel_kutu = Combobox(root, values=opel_lis)
opel_kutu.place(x=10, y=740)


def opel_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = opel1.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=opel_t).place(x=160, y=737)

# mercedes
merc = Image.open("nissan_ll.jpg")
merc = merc.resize((60, 40))
merc_p = ImageTk.PhotoImage(merc)


def nissan():
    global merce

    bölgeeee = mer_kutu.get()
    if (bölgeeee == "Micra"):
        merce = micra_m
    elif (bölgeeee == "Primera"):
        merce = primera_m

    return merce


labb = Button(image=merc_p, command=nissan).place(x=550, y=10)

merce = Entry(root)
mer_lis = ["Micra", "Primera"]
mer_kutu = Combobox(root, values=mer_lis)
mer_kutu.place(x=550, y=60)


def merc_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = merce.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=merc_t).place(x=700, y=56)

hyn = Image.open("hyn.jpg")
hyn = hyn.resize((60, 40))
hyn_p = ImageTk.PhotoImage(hyn)


def hyndee():
    global hyndai

    bölgeeee = mhy_kutu.get()
    if (bölgeeee == "Accent"):
        hyndai = accent_m
    elif (bölgeeee == "Accent Blue"):
        hyndai = accenb_m
    elif (bölgeeee == "Accent Era"):
        hyndai = accente_m

    elif (bölgeeee == "i20"):
        hyndai = i20_m

    elif (bölgeeee == "i30"):
        hyndai = i30_m

    elif (bölgeeee == "Elantra"):
        hyndai = elantra_m

    return hyndai


labb = Button(image=hyn_p, command=hyndee).place(x=550, y=100)

hyndai = Entry(root)
hy_lis = ["Accent", "Accent Blue", "Accent Era", "i20", "i30", "Elantra"]
mhy_kutu = Combobox(root, values=hy_lis)
mhy_kutu.place(x=550, y=150)


def hyn_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = hyndai.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=hyn_t).place(x=700, y=146)

# honda
hon = Image.open("honda.jpg")
hon = hon.resize((60, 40))
hon_p = ImageTk.PhotoImage(hon)


def hondae():
    global hondaa

    bölgeeee = hon_kutu.get()
    if (bölgeeee == "Civic"):
        hondaa = civic_m

    elif (bölgeeee == "Jazz"):
        hondaa = jazz_m

    return hondaa


labb = Button(image=hon_p, command=hondae).place(x=550, y=190)

hondaa = Entry(root)
hon_lis = ["Civic", "Jazz"]
hon_kutu = Combobox(root, values=hon_lis)
hon_kutu.place(x=550, y=240)


def hondam():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = hondaa.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=530)


Button(root, text="Tahmin Et", width=60, image=but, command=hondam).place(x=700, y=236)

# Fiat
fiat = Image.open("fiat.jpg")
fiat = fiat.resize((60, 40))
fiat_p = ImageTk.PhotoImage(fiat)


def fiat2():
    global fiatt

    bölgeeee = fiat_kutu.get()
    if (bölgeeee == "Egea"):
        fiatt = egea_m
    elif (bölgeeee == "Palio"):
        fiatt = palio_m
    elif (bölgeeee == "Linea"):
        fiatt = linea_m

    return fiatt


labb = Button(image=fiat_p, command=fiat2).place(x=550, y=290)

fiatt = Entry(root)
fiat_lis = ["Egea", "Palio", "Linea"]
fiat_kutu = Combobox(root, values=fiat_lis)
fiat_kutu.place(x=550, y=340)


def fiat_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = fiatt.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=520)


Button(root, text="Tahmin Et", width=60, image=but, command=fiat_t).place(x=700, y=336)

##Ford
ford = Image.open("ford.jpg")
ford = ford.resize((60, 40))
ford_p = ImageTk.PhotoImage(ford)


def ford2():
    global fordd

    bölgeeee = ford_kutu.get()
    if (bölgeeee == "Focus"):
        fordd = focus_m
    elif (bölgeeee == "Fiesta"):
        fordd = fiesta_m
    elif (bölgeeee == "Mondeo"):
        fordd = mondeo_m

    return fordd


labb = Button(image=ford_p, command=ford2).place(x=550, y=390)

fordd = Entry(root)
ford_lis = ["Focus", "Fiesta", "Mondeo"]
ford_kutu = Combobox(root, values=ford_lis)
ford_kutu.place(x=550, y=440)


def ford_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = fordd.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=520)


Button(root, text="Tahmin Et", width=60, image=but, command=ford_t).place(x=700, y=436)

# citroen
citro = Image.open("cici.png")
citro = citro.resize((60, 40))
citro_p = ImageTk.PhotoImage(citro)


def cit():
    global cittr

    bölgeeee = cit_kutu.get()
    if (bölgeeee == "C4"):
        cittr = c4_m
    elif (bölgeeee == "C5"):
        cittr = c5_m
    elif (bölgeeee == "C4 Grand Picasso"):
        cittr = c4_pi_m

    elif (bölgeeee == "Saxo"):
        cittr = saxo_m

    elif (bölgeeee == "C-Elysee"):
        cittr = elysee_m

    return cittr


labb = Button(image=citro_p, command=cit).place(x=550, y=490)

cittr = Entry(root)
cit_lis = ["C4", "C5", "C4 Grand Picasso", "Saxo", "C-Elysee"]
cit_kutu = Combobox(root, values=cit_lis)
cit_kutu.place(x=550, y=540)


def cit_t():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = cittr.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=520)


Button(root, text="Tahmin Et", width=60, image=but, command=cit_t).place(x=700, y=536)

# BMWW
bmw = Image.open("bmw.jpg")
bmw = bmw.resize((60, 40))
bmw_p = ImageTk.PhotoImage(bmw)


def bmww():
    global bmw2

    bölgeeee = bmw_kutu.get()
    if (bölgeeee == "1 Serisi"):
        bmw2 = bir_m
    elif (bölgeeee == "2 Serisi"):
        bmw2 = iki_m
    elif (bölgeeee == "3 Serisi"):
        bmw2 = üc_m

    return bmw2


labb = Button(image=bmw_p, command=bmww).place(x=550, y=590)
bmw2 = Entry(root)
bmw_lis = ["1 Serisi", "2 Serisi", "3 Serisi"]
bmw_kutu = Combobox(root, values=bmw_lis)
bmw_kutu.place(x=550, y=640)


def bmw_2():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = bmw2.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=520)


Button(root, text="Tahmin Et", width=60, image=but, command=bmw_2).place(x=700, y=636)

# audi
audi = Image.open("audi.jpg")
audi = audi.resize((60, 40))
audi_p = ImageTk.PhotoImage(audi)


def audi2():
    global audii

    bölgeeee = aud_kutu.get()
    if (bölgeeee == "A3"):
        audii = a3_m
    elif (bölgeeee == "A4"):
        audii = a4_m
    elif (bölgeeee == "A6"):
        audii = a6_m

    return audii


labb = Button(image=audi_p, command=audi2).place(x=550, y=690)
audii = Entry(root)
aud_lis = ["A3", "A4", "A6"]
aud_kutu = Combobox(root, values=aud_lis)
aud_kutu.place(x=550, y=740)


def aud_2():
    X_test = [float(mdl.get()), int(yıl.get()), (mevkisi), (vitesi), float(km.get())]

    y_pred = audi.predict([X_test, ])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="white", relief="solid", width=20).place(x=270, y=520)


Button(root, text="Tahmin Et", width=60, image=but, command=aud_2).place(x=700, y=736)

root.resizable(0, 0)
root.mainloop()