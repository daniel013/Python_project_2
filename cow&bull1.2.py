"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Daniel Filip
email: danielfilip102@gmail.com
discord: Danko#3595
"""
#-----------------------------------------------------------------------------------------------------#
def generuj():
    """
    Funkce na vygenerování 4místného čísla, pomocí metody random, které bude uživatel hádat
    Podmínky: 
    - Rozmezí od 1000-9999
    """
    import random
    # odělovač + přivítání uživatele
    oddelovac = "-"
    print(oddelovac*40)
    print("Vítej ve hře Cow&Bull")
    print(oddelovac*40)

    # list všech pokusů uživatele
    listPokusu = ['']
    cisloGenerovane = random.randint(1000,9999)
    cisloGenerovane = str(cisloGenerovane)

    return listPokusu, cisloGenerovane

def hadej(listPokusu):
    """
    Funkce hádej požádá uživatele, aby zadal 4 ciferné číslo. zjistí zda má vstup od uživatele 4 cifry a zda se jedná o čísla
    """
    oddelovac = "-"
    cisloUzivatele = input("Zadej číslo od 1000-9999: ")
    # kontrola správného vstupu od uživatele
    if len(cisloUzivatele) != 4 or not cisloUzivatele.isdigit():
        print("Neplatný vstup!")
        quit()
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