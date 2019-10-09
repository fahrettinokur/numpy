# -*- coding: utf-8 -*-

#Bu kısımda Recognizer'ımızı r diye çağırıyoruz.
import speech_recognition as sr
r = sr.Recognizer()

#Burada ise cihaza bağlı olan mikrofondan veri almaya başlıyor,
#daha doğrusu mikrofonu dinlemeye başlıyor.
with sr.Microphone() as source:
     print("Birşeyler Söyle!")
     audio = r.listen(source)

#Bir ses sinyali geldiği anda onu google recognizer'ı ile tanımaya çalışıyor.
#Burada birçok seçeneğimiz var, Bing, Yandex vs. ama google en iyi çalışanı diyebilirim.

#Tanıdıktan sonra eğer dediğiniz şey boş bir ses değilse, yani tıkırtı vs. Dediğiniz geri döndürecek.
data = ""
try:
   data = r.recognize_google(audio,language="tr-tr")
 #  data          ​= data.lower()
   print("Bunu Söyledin :" + data)
except sr.UnknownValueError:
       print("Ne dediğini anlamadım")