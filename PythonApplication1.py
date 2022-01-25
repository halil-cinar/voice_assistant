import speech_recognition as sr
dosya=open("name.txt","w")

import time
import webbrowser
from gtts import gTTS
from playsound import playsound
import os
import random
import keyboard
#from subprocess import call
import wikipedia
r=sr.Recognizer()
#ny=wikipedia.page("New York")
import feedparser
locCode="EUR|TR|27350|GAZIANTEP"
#> KITA|ULKE|POSTAKODU|IL

def yaz(sayı):
    #sayı=random.randint(1,10000)
    sayı=str(sayı)
    dosya=open(sayı+".txt","a")
    print("buyrun")
    oynat("buyrun")
    while 1:
        metin1=mikrofon()
        dosya.write(metin1)
        if "okey" in metin1 or "Okey" in metin1:
            print("dosya yolu")
            oynat("dosya yolu")
            print(os.path.abspath(sayı+".txt"))
            break
        



def hava():
    
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode="+locCode)
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    print (parse[2], parse[4], parse[5])
    return (parse)
def mikrofon() :
    with sr.Microphone() as source:
        print("dinleniyor")
        audio=r.listen(source)
        metin=" "
        try:
            metin=r.recognize_google(audio,language="tr-tr")
            print(metin)
            dosya.writelines(metin)
            dosya.writelines("\n")
            
        except:
            #oynat("ses algılama yada dosya hatası")
            time.sleep(0.1)
        return metin
def oynat(string):
   ses= gTTS(string,lang="tr")
   a=random.randint(1,100000)
   file="dosya"+str(a)+".mp3"
   #fil=open(file,"w")
   ses.save(file)
   
   try:
       playsound(file)
   except:
       playsound(file)
   os.remove(file)


while 1:
    if keyboard.is_pressed("+"):
        metin="bilgisayar"
        if metin =="bilgisayar" or metin=="Bilgisayar":
            while 1:
                metin=mikrofon()
                    
                if "Merhaba"in metin or "merhaba"in metin:
                    print("merhabaaaaaa")
                    oynat("merhaba")
                if "nasılsın" in metin or "Nasılsın" in metin:
                    print("iyi sen")
                    oynat("iyi sen")
                if "saat kaç" in metin or "Saat kaç" in metin:
                    print(str(time.strftime("%X")))
                    oynat(str(time.strftime("%X")))
                if "arama yap"in metin or "Arama yap"in metin:
                    print("ne arayayım")
                    oynat("ne istiyon")
                    metinn=mikrofon()
                    while 1:
                        if metinn==" ":
                            metinn=mikrofon()
                        else:
                            break
                    url="https://www.google.com/search?q="+ metinn
                    webbrowser.get().open(url)
                    oynat("bunları buldum")
                if "tamamdır" in metin or "Tamamdır" in metin:
                    break
                if "youtube" in metin or "YouTube" in metin:
                    url="https://www.youtube.com/"
                    webbrowser.get().open(url)
                    oynat("youtube açıyorum")
                if "ses" in metin or"Ses" in metin :
                    if "kıs" in metin or "Kıs" in metin:
                        #call(["amixer", "-D", "pulse", "sset", "Master", "{}%-".format(20)])

                        print("seamsam")
                if "araştır" in metin or "Araştır" in metin:
                    print("ne araştıralım")
                    oynat("ne araştıralım")
                    metinnn=mikrofon()
                    result=(" ")
                    print(metinnn)

                    while 1:
                       if metinnn==" ":
                            metinnn=mikrofon()
                       else:
                            break
                    wikipedia.set_lang("tr")
                    try:
                        result = wikipedia.summary(metinnn, sentences = 5)
                        print(result)
                        oynat(result)
                    except wikipedia.exceptions.DisambiguationError:
                        print("daha ayrıntı")
                        oynat("daha ayrıntı")
                    
                    except:
                        print("lutfen tekrar deneyin")
                        oynat("lutfen tekrar deneyin")
                        result=(" ")
                        #result = wikipedia.summary(metinnn, sentences = 5, results = 5)
                    
                        
                    #sonuc=wikipedia.summary(metinnn,sentences=3)
                if "hava durumu" in metin or "Hava durumu" in metin:
                    durum=hava()
                    durum1=[durum[2],durum[4],durum[5]]
                    durum1=str(durum1)
                    oynat( durum1)
                    
                if "yaz" in metin or "Yaz" in metin:
                    
                    yaz(random.randint(1,100000))

                break

        else:
            continue

    else:
        time.sleep(0.1)

