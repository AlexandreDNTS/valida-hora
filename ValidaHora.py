def ValidaHora(Tempo):
    hora,minuto = map(int,Tempo.split(':'))

    if minuto < 0 or minuto > 59 or hora < 0 or hora >23:
        return False
    elif minuto >= 0 and hora <= 0 or minuto == 0 and hora>0 or minuto > 0 and hora>0:
        return True
t = input("hora(hora:minuto ): ")
tv = ValidaHora(t)

if tv == True:
    print('hora correta')
elif tv== False:
    print('hora incorreta')
