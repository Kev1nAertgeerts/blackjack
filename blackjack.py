import random

GETROKKEN_KAARTEN_IEDEREEN = dict()

class Speler:
    def __init__(self,decks=7):
        self.inzet = 50
        self.getrokken_kaarten = []
        self.dealer = []
        self.aantal_decks = decks #meerdere decks

    def add_card_dealer(self):
        kaart = random.randint(1, 13)
        kaart_check = GETROKKEN_KAARTEN_IEDEREEN[kaart]
        if kaart_check < 4*self.aantal_decks:
            GETROKKEN_KAARTEN_IEDEREEN[kaart] = GETROKKEN_KAARTEN_IEDEREEN[kaart]+1
            self.dealer.append(kaart)
            if len(self.dealer)==2:
                print(f"zichtbare kaart dealer: {self.dealer[1]}")
            else:
                print("onzichtbare kaart dealer gedeeld")
        else:
            self.add_card_dealer



    def add_card(self): #voor speler
        kaart = random.randint(1,13)
        kaart_check = GETROKKEN_KAARTEN_IEDEREEN[kaart]
        if kaart_check < 4*self.aantal_decks:
            GETROKKEN_KAARTEN_IEDEREEN[kaart] = GETROKKEN_KAARTEN_IEDEREEN[kaart]+1
            self.getrokken_kaarten.append(kaart)
        else:
            self.add_card()
        print(f"getrokken kaart(en) speler: {self.getrokken_kaarten}")


    def bepaal_inzet(self):
        try:
            self.ingezet = int(input("geef een inzetwaarde: "))
            print(f"speler inzet: {self.ingezet}")
        except:
            print("geen geldige waarde")
            self.bepaal_inzet()


    def create_speler(self):
        for kaart_nummer in range(13):
            GETROKKEN_KAARTEN_IEDEREEN[kaart_nummer+1] = 0
        self.add_card()

            
class Spel:
    def __init__(self):
        self.speler = object()
        self.create_game()
        self.speler_speelt()


    def create_game(self):
        #print("test")
        self.speler = Speler()
        #print(self.speler.inzet)
        self.speler.bepaal_inzet()
        self.speler.create_speler()
        self.speler.add_card_dealer()
        self.speler.add_card()
        #self.speler.getrokken_kaarten = [10,11]
        if sum(self.speler.getrokken_kaarten) == 21:
            print("winnaar")
            self.speler.inzet = self.speler.inzet + (self.speler.ingezet*1.5)
            print(f"nieuwe inzet: {self.speler.inzet}")
        self.speler.add_card_dealer()

    
    def speler_speelt(self):
        extra_kaart = input("wil je nog een kaart? j/n: ")
        if extra_kaart == "j" or extra_kaart == "n":
            if extra_kaart == "j":
                self.speler.add_card()
                self.speler_speelt()
            else:
                self.winnaar() #winnaar wordt berekend
        else:
            print("zeg 'j' of 'n': ")
            self.speler_speelt()


    def winnaar(self):
        print(f"kaarten dealer: {self.speler.dealer}")

        #waarde kaarten bepalen
        som_speler = int()
        som_dealer = int()
        for kaart in self.speler.getrokken_kaarten:
            if kaart < 10:
                som_speler = som_speler + kaart
            else:
                som_speler = som_speler + 10

        for kaart in self.speler.dealer:
            if kaart < 10:
                som_dealer = som_dealer + kaart
            else:
                som_dealer = som_dealer + 10
        
        #speler en dealer vergelijken
        if som_speler > 21:
            print("verloren")
            print(f"geld: {self.speler.inzet-self.speler.ingezet}")
        elif som_dealer > 21:
            print("winnaar")
            print(f"geld = {self.speler.inzet + (self.speler.ingezet*2)}")
        elif som_speler == 21:
            print("winnaar")
            self.speler.inzet = self.speler.inzet + (self.speler.ingezet*1.5)
            print(f"nieuwe inzet: {self.speler.inzet}")
        elif som_speler > som_dealer:
            print("winnaar")
            print(f"geld: {self.speler.inzet+self.speler.ingezet * 2}")
        elif som_dealer > som_speler:
            print("verloren")
            print(f"geld: {self.speler.inzet-self.speler.ingezet}")



    def dealer_speelt(self):
        pass
        

spel = Spel()
print(f"alle getrokken kaarten: {GETROKKEN_KAARTEN_IEDEREEN}")