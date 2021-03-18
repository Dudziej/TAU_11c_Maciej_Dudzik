Niestety operując na cudzej stronie większość klas i nazw
elementów są zmienne dlatego niektóre testy stwierdzą że Element 
o owej nazwie nie istnieje.

X-Kom:
 
Scenariusz 1:

        Testujemy czy strona po wyszukaniu produktu
        wyświetla odpowiednią ilość produktów.
        W tym celu znajdujemy classname searchbara,
        wpisujemy w niego "msa" i sprawdzamy czy pojawił
        się jeden produkt.

Scenariusz 2:
    
    Testujemy czy strona po niepoprawnym wpisaniu danych logowania
    wyświetli błąd. W tym celu znajdujemy guzik konta, klikamy go,
    znajdujemy 2 inputy od hasła i emailu wpisujemy niepopranwe dane,
    i sprawdzamy czy pojawi sie error.

Scenariusz 3:

    Testujemy czy po kliknięciu w produkt możemy zobaczyć jego cene.
    W tym celu znajdujemy guzik, "laptopy i komputery" > laptopy i notebooki
    pierwszy produkt i sprawdzamy czy cena istnieje.

Zalando:

Scenariusz 1:

    Testujemy czy popup "Zapomniałeś hasła?" istnieje,
    w tym celu klikamy w guzik konta, wpisujemy dane logowania
    i klikamy guzik zapomniałem hasła, jeśli popup wyskoczy 
    test wykona się poprawnie.

Scenariusz 2:

    Testujemy czy w zakładce pomoc, pojawi się na dole formularz
    z zapisem do newslettera, szukamy guzika pomoc, po czym poszukujemy
    danego elementu na stronie.

Scenariusz 3:

    Testujemy czy po wyszukaniu słowa w wyszukiwarce wyskoczy nam dana
    ilość produktów, w tym celu szukamy input boxa, wpisujemy słowo "dhl"
    oraz sprawdzamy czy element zliczający produkty istnieje.

    