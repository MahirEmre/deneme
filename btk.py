""""
print(9**(1/3))
print((9**1)/3)
print(9**1/3)

a=5+2
print(a)

b=a+a
print(b)


print(a)
a=1
print(a)

gelir=1000
vergi_orani=0.27

toplam_vergi=gelir*vergi_orani
print(toplam_vergi,"TL")

print(type(gelir))
print(type(vergi_orani))

#kullanıcının gelirini ve vergi oranını alınız ve 2 değişkene kaydediniz
#ekrana toplam geliri ve toplam vergiyi yazınız

isim=input()
print("Merhaba",isim)
print(type(isim))


sayi=5
sayi=str(sayi)
print(type(sayi))

#print(sayi+5)
print(sayi + "5")
print(int(sayi)+5)


yas=input("yasinizi giriniz")
yas=int(yas)
yas=("dogum tarihiniz",2022-yas)


#kullanıcıdan gelirini ve vergi oranını alınız ve 2 değişkene kaydediniz
#ekrana toplam gelir ve vergiyi giriniz


örnek çıktı:

gelirinizi giriniz:1000
vergi oranını giriniz:0.27
toplam gelir:1000
toplam vergi:270


gelir=input("geliri giriniz:   ")
float(gelir)

yuzde=input("vergi yüzdesini giriniz:   ")
float(yuzde)

vergi=float(gelir)*float(yuzde)
int(vergi)

print("vergi:  ",int(vergi))


ornek_bool = True
print(ornek_bool , type(ornek_bool))
#bool = Doğru ya da yanlışı ölçmek demektir


#karşılaştırma operatörleri örnek 

print(3+5==7) #3+5 7'ye eşit mi?  - false 
print(4!=3) #4 3'e eit değildir   - true 
print(3>2)#3 2'den büyüktür  - true 
print(4<8) #4 8'den küçüktür  -true 
print(9>=12) #9 12'ye eşit ya da büyüktür -false
print(17<=33) #17 33'e eşit ya da küçüktür - true


dogumTarihi=input("doğum tarhini giriniz : ")
dogumTarihi=int(dogumTarihi)
yas=2022-dogumTarihi
print("YAŞ" , yas)

if yas<7:
    print("okula gidemezsiniz")
elif yas <= 7:
    print("ilkokula gidersiniz ")
elif yas <= 11:
    print("ortaokula gidersiniz")
elif yas <= 15:
    print("liseye gidersiniz")
elif yas <= 18:
    print("liseye gidersiniz")



for sayı in range(10):  #10a kadar 0dan başlar 10 dahil değil
    #print(sayı)
    #print(sayı+1) #sayıya 1 ekler


print(list(range(0,100,2)))#0dan 100e kadar 2şer 2şer 100 dahil değil 


for sayi in range(100):
    if sayi % 2 == 0: #0dan 100e kadar 2şer 2şer 100 dahil değil üstün aynısı
        print(sayi)


text="hello world"
#i=harf demek

for i in text:
    print(text) #karakter sayısı kadar (boşluk dahil) texti basar 

düzenklenecek
text="hello world"
for i in text:
    if i =="a":
        sayac+= harf
print(sayac)



a=0
while a < 10:
    a+=1
    if a == 5:
        continue # bulana kadar devam break yazılsaydı bi kaçtane yazar bitirirdi
    print(a)


fact=1
for i in range(1,30):
    fact=fact*i
    print(fact)


ilk=("bilişim")
son=("kurumu") 

toplam=str(ilk )+str(son)

print(toplam)


a="ali"

sonuç=a*4
print(sonuç)



sayı=int(input("SAYIYI GİRİNİZ"  ))
for i in range(sayı,0 ,):
    print("*" +1)


sayi=int(input("Sayıyı Girin : "))
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi," Asal Sayı Değildir.")
           break
   else:
       print(sayi," Asal Sayıdır.")
 
else:
   print(sayi," Asal Sayı Değildir.")

print(1)
if 3 < 5:
    print(2)
    print(3)
else:
    print(4)
print(5)

s="Merhaba Ben Ahmet"
#s=[0:7]
#s=s[:]
#s=s[0:7:2]
#s=s[::-1]
#s=s[len(s):-1:-1] bak

s=s.upper()

k="Merhaba Ben Ahmet"

for i in k:
    print(i)


#dictinoary verisinin en büyük valuenun keyini bul

dict_sehir={
    "Ankara" : 6,
    "Çanakkale" : 17,
    "Adana" : 1,
    "xxxx" : 20,
    "Düzce" : 81,

}

max=0
for i in dict_sehir.values():
    if(max > i):
        max=i

for i in dict_sehir.keys():
    if(dict_sehir[i]==max):
        print(i)



def indirim(fiyat , indirim_yuzdesi = 20):
    fiyat = fiyat - (fiyat * indirim_yuzdesi) //100
    return fiyat

print(indirim(400, ))

print(indirim(indirim_yuzdesi = 50 , fiyat = 400))



import random

random_number = random.randint(1, 10)
print(random_number)

# 1 ile 10 arasında random sayı atama

import random

random_numbers = []

for i in range(10):
  random_number = random.randint(1, 10)
  random_numbers.append(random_number)

print(random_numbers)

# 1 ile 10 arasında random sayı atama ve bunları listeleme



import random

random_number = random.randint(1, 6)

if random_number == 1:
  print("⚀")
elif random_number == 2:
  print("⚁")
elif random_number == 3:
  print("⚂")
elif random_number == 4:
  print("⚃")
elif random_number == 5:
  print("⚄")
else:
  print("⚅")

# zar atma ve ekrana zar yansıtma

import random

fixed_number = 3

while True:
  print(fixed_number)

# hileli zar atışı 

"""



