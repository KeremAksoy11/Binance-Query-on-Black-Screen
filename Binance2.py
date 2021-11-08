from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import locale
from urllib3.packages.six import _import_module
locale.setlocale(locale.LC_ALL, 'turkish')
from bs4 import BeautifulSoup
import requests
import os
import csv
import pandas as pd
from bs4 import BeautifulSoup
import pyautogui



sorgu = input("Sorgulamak İstediğiniz Kripto Parayı Giriniz: ")
tekrar_sayisi = int(input("Kaç Tane Kayıt Alsın: "))
dakika = int(input("Kaç Saniye Aralıkla Bir Kayıt Alsın: "))


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
url = "https://www.google.com.tr/"
driver.get(url)
time.sleep(2)

googlegit = driver.find_element_by_name("q")
googlegit.send_keys(sorgu + " Binance")
time.sleep(1)

ara = driver.find_element_by_name("btnK")
ara.click()
time.sleep(1)

giris = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div[1]/div/div[1]/a/h3")
giris.click()
time.sleep(1)

butonukapa = driver.find_element_by_css_selector("body > div.css-1u2nk9f > div.css-f1lu4p > div.css-4rbxuz > svg")
butonukapa.click()
time.sleep(1)

kaç_kere = 1
while True:
    kaç_kere = kaç_kere + 1
    tarihsaat = datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")
    print("Anlık Tarih ve Saaat: " + tarihsaat)
    kripto = driver.find_element_by_class_name("css-1qkv3vk").text
    print("Kripto Paranın İsmi: " + kripto)
    anlikdeger = driver.find_element_by_class_name("showPrice").text
    print(kripto + " Kripto Paranın Anlık Değeri: " + anlikdeger)
    anlikdegertl = driver.find_element_by_class_name("subPrice").text
    print(kripto +" Kripto Paranın Türk Lirasi Cinsinden Değeri: " + anlikdegertl)
    saatlik24 = driver.find_element_by_xpath("//*[@id='__APP']/div/div/div[4]/div/div[1]/div[2]/div/div/div[1]/div[2]/span").text
    print(kripto + " Kripto Paranın 24 Saatlik Değişim Oranı: " + saatlik24)
    enyuksekdeger = driver.find_element_by_xpath("//*[@id='__APP']/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div[2]").text
    print(kripto + " Kripto Paranın 24 Saaattaki En Yüksek Değeri: " + enyuksekdeger)
    endusukdeger = driver.find_element_by_xpath("//*[@id='__APP']/div/div/div[4]/div/div[1]/div[2]/div/div/div[3]/div[2]").text
    print(kripto + " Kripto Paranın 24 Saaattaki En Düşük Değeri: " + endusukdeger)
    hacim = driver.find_element_by_xpath("//*[@id='__APP']/div/div/div[4]/div/div[1]/div[2]/div/div/div[4]/div[2]").text
    print(kripto +" Anlık Hacimi: " + hacim)
    time.sleep(dakika)
    with open("binance1.txt","a+",encoding="utf-8") as file:
        file.write("\nAnlık Tarih ve Saaat: {}\nKripto Paranın İsmi: {}\nKripto Paranın Anlık Değeri: {}\nKripto Paranın Türk Lirasi Cinsinden Değeri: {}\nKripto Paranın 24 Saatlik Değişim Oranı: {}\nKripto Paranın 24 Saaattaki En Yüksek Değeri: {}\nKripto Paranın 24 Saaattaki En Düşük Değeri:{}\nAnlık Hacimi: {}\n".format(tarihsaat,kripto, anlikdeger,anlikdegertl,saatlik24,enyuksekdeger,endusukdeger,hacim))
    
    
    print("Başarıyla Tamamlandı.\n")
    if kaç_kere > tekrar_sayisi:
        print("\nİşlem Başarıyla Gerçekleşti. Tarayıcı 3 Saniye Sonra Kapanacaktır.")
        time.sleep(3)
        driver.quit()
        break

os.startfile("binance1.txt")

    

