#Rubikin kuution ratkaisemisajastin.
#Ilman lisätoimia vaativa versio.
#Tehnyt Oskari Hiedanpää 2.10.2019
#Ohjelma antaa ohjeet kuinka sekoittaa kuutio
#Siirrot siis ovat
#R = oikea sivu (myötäpäivään)
#L = vasen sivu
#U = päällä oleva "sivu"
#F = edessä oleva "sivu"
#D = alhaalla olvea "sivu" 
#B = takana oleva "sivu"
#heittomerkki (') tarkoittaa vastapäivään
#(2) kirjaimen perässä tarkoittaa kaksi pyöräytystä
#Ohjelma sitten ottaa aikaa, kun ratkaiset kuution.
#Lopuksi ohjelma antaa nopeimman ajan, hitaimman ajan,
#keskiarvon ja mediaanin.

import time         #ajastin
import random       #satunnainen sekoitus
import statistics   #mediaani

g = 0               #auttaa myöhemmin
ajat = []           #"ajat" lista ennen mitään ajanottoa

def tyhjennys():    #helpompi komento tyhjentämiselle
  print("\n"*49)    #IDLE:ssä ei toimi mikään tyhjennyskomento, joten pitää vain printata paljon rivejä

def sekoitus():     #sekoitus
  print ("Sekoita kuutiosi ohjeiden mukaan\n")
  liikkeet1 = ["R", "R'", "R2", "L", "L'", "L2"]  #Siirrot ovat eri listoissa,
  liikkeet2 = ["U", "U'", "U2", "D", "D'", "D2"]  #jotta samoja ei tulisi peräkkäin
  liikkeet3 = ["F", "F'", "F2", "B", "B'", "B2"]  

  for i in range (0,8):       #Ohjelma tulostaa 8 siirtoa jokaisesta listasta
    a = random.randint(0,5)   #eli yhteensä 24 siirtoa
    print (liikkeet1[a])

    b = random.randint(0,5)
    print (liikkeet2[b])

    c = random.randint(0,5)
    print (liikkeet3[c])

def ajanotto():    #Ajanotto
  h = input ("\nPaina 'enter' aloittaaksesi") #syötettyä tekstiä ei käytetä mihinkään, se on vain tauko, jonka pystyy itse lopettaa
  
  aloitus = time.time() #aloitus on aika jolloin enteriä painettiin ensimmäisen kerran
  tyhjennys()   #tyhjä sivu
  

  i = input ("\nPaina 'enter' lopettaaksesi")
  
  lopetus = time.time() #lopetus on aika jolloin välilyöntiä painetaan uudestaan

  ajat.append(round(lopetus-aloitus, 2))  #lopetus - aloitus = niiden välillä kulunut aika
                             #ohjelma lisää ajan "ajat" listaan


def keskiarvo():  #lopuksi ohjelma tulostaa tarkempaa tietoa ajoista
  print("\n")   #ensiksi ajat laitetaan järjestykseen
  ajat.sort()
  print("Nopein aika")
  print (ajat[0]) #nopein aika on listan ensimmäinen aika
  
  print ("Hitain aika")
  print (ajat[len(ajat)-1]) #hitain aika on listan viimeisin aika
  
  print ("Keskiarvo") #keskiarvo on lukujen keskiarvo
  print (round(sum(ajat)/len(ajat), 2))
  
  print ("Mediaani")  #jos yksi tai kaksi aikaa menee paljon huonommin kuin muut,
  print (statistics.median(ajat)) #on mediaani eli tarkempi "keskiarvo"

  
while True: #nyt päästään itse ohjelmaan
    

    sekoitus()  #sekoitus
    ajanotto()  #ajanotto

    print ("\nAikasi:")
    for luku in ajat: #ratkaisun jälkeen ohjelma tulostaa kaikki ajat
        print(luku)
 
    print("\n"*1)
    c = input("Haluatko\n1. jatkaa\n2. lopettaa\n3. poistaa viimeisimmän ajan?\nOma vastaus: ") #mitä haluat tehdä seuraavaksi
      #jos käyttäjä vastaa, että haluaa jatkaa, silmukka alkaa alusta
    if c == "2" or c == "lopettaa":
      keskiarvo() #jos käyttäjä lopettaa, ohjelma tulostaa tarkemmat tilastot ajoista
      break   #silmukka loppuu
    
    if c == "3" or c == "poistaa":
      ajat.pop()  #käyttäjä voi myös poistaa viimeisimmän ajan, jos siinä meni joku pieleen
      print ("\n")
      d = input("Haluatko\n1. jatkaa\n2. lopettaa?\nOma vastaus: ") #ohjelma kysyy mitä haluat tehdä ajan poistamisen jälkeen
    
      if c == "2" or c == "lopettaa":
        keskiarvo() #tilastot
        break   #lopetus
    tyhjennys() #uusi sivu
