import math
import time
print ("Tekijä: Oskari Hiedanpää 16.08.2019.")
print ("Tervetuloa laskimeen")
while True:
  time.sleep(2)
  print ("Haluatko plus-, miinus-, kerto-, jakolaskun tai jonkun muun (=muu)?")
  päätös = input ("Oma vastaus: ")
  if päätös == "plus" or päätös == "pluslasku" or päätös == "pluslaskun" or päätös == "+":
    luku1 = input ("Syötä ensimmäinen luku: ")
    luku2 = input ("Syötä toinen luku: ")
    print (int(luku1)+int(luku2))
  if päätös == "miinus" or päätös == "miinus lasku" or päätös == "miinuslaskun" or päätös == "-":
    luku1 = input ("Syötä ensimmäinen luku: ")
    luku2 = input ("Syötä toinen luku: ")
    print (int(luku1)-int(luku2))
  if päätös == "kerto" or päätös == "kertolasku" or päätös == "kertolaskun" or päätös == "*":
    luku1 = input ("Syötä ensimmäinen luku: ")
    luku2 = input ("Syötä toinen luku: ")
    print (int(luku1)*int(luku2))
  if päätös == "jako" or päätös == "jakolasku" or päätös == "jakolaskun" or päätös == "/":
    luku1 = input ("Syötä ensimmäinen luku: ")
    luku2 = input ("Syötä toinen luku: ")
    print (int(luku1)/int(luku2))
  if päätös == "en" or päätös == "ei":
    print ("Ei sit")
  if päätös == "muu":
    print ("Mitä haluaisit tehdä?")
    päätös3 = input ("Sanan pituus\nPotenssi\nNeliöjuuri\nYmpyrään liittyviä laskuja (=ympyrä)\nYksikkömuunnin\nOma vastaus: ")
    if päätös3 == "sanan pituus" or päätös3 == "Sanan pituus":
      sana = input ("Sana, jonka pituuden haluat tietää: ")
      print ("Sanasi pituus on",len(sana))
    if päätös3 == "potenssi" or päätös3 == "Potenssi":
      luku1 = input ("Syötä ensimmäinen luku: ")
      luku2 = input ("Syötä toinen luku: ")
      print (int(luku1)**int(luku2))
    if päätös3 == "neliöjuuri" or päätös3 == "Neliöjuuri":
      luku3 = input ("Anna numero josta haluat neliöjuuren: ")
      print (math.sqrt(int(luku3)))
    if päätös3 == "ympyrä" or päätös3 == "Ympyrä":
      päätös4 = input ("Kehä\nHalkaisija\nPinta-ala\nOma vastaus: ")
      if päätös4 == "halkaisija" or päätös4 == "Halkaisija":
        kehä = input ("Syötä kehä: ")
        print (int(kehä)/math.pi)
      if päätös4 == "kehä" or päätös4 == "Kehä":
        halkaisija = input ("Syötä halkaisija: ")
        print (math.pi*int(halkaisija))
      if päätös4 == "pinta-ala" or päätös4 == "Pinta-ala":
        säde = input ("Syötä säde: ")
        print (math.pi*int(säde)*(int(säde)))
    if päätös3 == "yksikkömuunnin" or päätös3 == "Yksikkömuunnin":
      päätös5 = input ("1. Tuumat senttimetreiksi\n2. Senttimetrit tuumiksi\n3. Fahrenheitit celsiuksiksi\n4. Celsiukset fahrenheiteiksi\n5. Paunat kiloiksi\n6. Kilot paunoiksi\nValitse numero: ")
      if päätös5 == "1." or päätös5 == "1":
        tuuma = input ("Syötä tuumat: ")
        print (tuuma,"tuumaa on",int(tuuma)*2.54,"senttimetriä")
      if päätös5 == "2." or päätös5 == "2":
        sentti = input ("Syötä senttimetrit: ")
        print (sentti,"senttimetriä on",int(sentti)*0.393700787,"tuumaa")
      if päätös5 == "3." or päätös5 == "3":
        fahrenheit = input ("Syötä fahrenheitit: ")
        print (fahrenheit,"fahrenheittia on",(int(fahrenheit)-32)/1.8,"celsiusta")
      if päätös5 == "4." or päätös5 == "4":
        celsius = input ("Syötä celsiukset: ")
        print (celsius,"celsiusta on",int(celsius)*1.8+32,"fahrenheittia")
      if päätös5 == "5." or päätös5 == "5":
        pauna = input ("Syötä paunat: ")
        print (pauna,"paunaa on",int(pauna)*0.45359237,"kiloa")
      if päätös5 == "6." or päätös5 == "6":
        kilo = input ("Syötä kilot: ")
        print (kilo,"kiloa on",int(kilo)*2.20462262,"paunaa")
  time.sleep(3)
  print ("Kiitos laskimen käytöstä")
  päätös2 = input ("Haluatko uudestaan? ")
  if päätös2 == "ei" or päätös2 == "en":
    print ("Ei sit")
    time.sleep(2)
    exit()
  if päätös2 == "kyllä" or päätös2 == "joo" or päätös2 == "ok":
    x += 1
  else:
    print ("En ymmärtänyt (aloitetaan uudestaan)")
