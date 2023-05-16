"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Daniel Filip
email: danielfilip102@gmail.com
discord: Danko#3595
"""
#-----------------------------------------------------------------------------------------------------#
import random

def duplicita(cisloGenerovane):
    """
    Funkce duplicita zjistí, zda v generovaném čísle je duplicita
    Pokud ano, vratí False a bude se generovat nové číslo, dokud nebude duplicitní
    
    """
    listCisel =[int(i) for i in str(cisloGenerovane)]
    if len(listCisel) == len(set(listCisel)):
        return True
    else:
        return False

def generuj():
    """
    Funkce na vygenerování 4místného čísla
    číslo generované Pomocí metody random, které bude uživatel hádat
    Podmínky: 
    - Rozmezí od 1000-9999
    """
    
    # odělovač + přivítání uživatele
    oddelovac = "-"
    print(oddelovac*40)
    print(f"Vítej ve hře Cow&Bull \nTvým ukolem je uhádnout 4-místné čislo, které sme pro tebe generovali")
    print(oddelovac*40)

    # list všech pokusů uživatele
    listPokusu = ['']

    while True:
        cisloGenerovane = random.randint(1000,9999)
        if duplicita(cisloGenerovane):
            #return cisloGenerovane
        
    
            cisloGenerovane = str(cisloGenerovane)

            return listPokusu, cisloGenerovane

def hadej(listPokusu):
    """
    Funkce hádej požádá uživatele, aby zadal 4 ciferné číslo.
    Zjistí zda má vstup od uživatele 4 cifry a zda se jedná o čísla a zda nezačíná "0"
    """
    oddelovac = "-"
    cisloUzivatele = input("Zadej číslo od 1000-9999: ")
    # kontrola správného vstupu od uživatele(delka 4, nesmí obsahovat písmeno a nesmí začínat 0)
    while len(cisloUzivatele) != 4 or not cisloUzivatele.isdigit() or cisloUzivatele.startswith("0"):
        print("Neplatný vstup!")
        print(oddelovac*40)
        cisloUzivatele = input("Zadej číslo od 1000-9999: ")
        
        #quit()
    # přidání čísla do listu 
    listPokusu.append(cisloUzivatele)

    return listPokusu

def porovnej(cisloUzivatele, cisloGenerovane):
    """
    Funkce porovnej porovná náhodně generované číslo s číslem, které hádá uživatel
    Je třeba si udělat proměnné cow a bull 
  
    """
    # potřebné proměnné cow a bull
    cow = 0
    bull = 0

    # for na procházení pozic čísla uživatele a výpočet počtu cow a bull
    for i in range(len(cisloUzivatele)):
        if cisloUzivatele[i] == cisloGenerovane[i]:
            bull += 1
        if cisloUzivatele[i] in cisloGenerovane:
            cow += 1 
    cow = cow - bull

    return cow, bull

def main():
    
    oddelovac = "-"
    listPokusu, cisloGenerovane = generuj()
    # zjistí zda číslo v listu na poslední pozici se nerozvá číslu generovanému
    while listPokusu[-1] != cisloGenerovane:
        listPokusu = hadej(listPokusu)
        cow, bull = porovnej(listPokusu[-1], cisloGenerovane)
        # print s rozdělením množné a jednotné číslo
        print(f"{bull} bull{('s'[:bull^1])}, {cow} cow{('s'[:cow^1])}".format(bull, cow))
        # vypis generovaného čísla pouze pro ověření funkce(jinak bych to hádal dlouho :D)
        #print(cisloGenerovane)
        print(oddelovac*40)
    print("Blahopřeji!")
    print(f"zvládl si to za {len(listPokusu)} pokus{('ů'[:len(listPokusu)^1])}".format(len(listPokusu)))
              
if __name__ == "__main__":
    main()