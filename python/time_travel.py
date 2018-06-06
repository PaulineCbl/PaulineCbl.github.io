a = 2054
if a <= 1900:
     print("Salut visiteur du XIX")
elif a >= 2020:
    print("Salut visiteur du futur")
else:
    print("Salut, en fait t'es contemporain, l'arnaque")

    def greeting(year):
            if year < 1900:
                print("Salut visiteur du XIX")
            elif year >= 1900 and year <= 2020:
                print("Salut, en fait t'es contemporain, l'arnaque")
            else:
                print("Salut, visiteur du futur")
                          
