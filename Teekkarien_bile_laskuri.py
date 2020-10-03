teekkarit = input("Montako teekkaria juhliin on tulossa?\n")
teekkarit = int(teekkarit)
eimakkaraa = input("Moniko heista ei syo makkaraa?\n")
eimakkaraa = int(eimakkaraa)
eikaljaa = input("Moniko heista ei juo kaljaa?\n")
eikaljaa = int(eikaljaa)

makkaraa = (teekkarit - eimakkaraa) * 3
maissintahkaa = eimakkaraa * 3
kaljaa = (teekkarit - eikaljaa) * 4
cola = eikaljaa * 4

print("Juhliin tarvitaan" , makkaraa , "makkaraa,\n" , maissintahkaa , "maissintahkaa,\n" , kaljaa ," kaljapulloa ja\n" , cola , "Cola-pulloa.")
