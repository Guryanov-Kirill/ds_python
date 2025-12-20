name = len(str(input('введите имя')))
surname = len(str(input('введите фамилию')))
otch = len(str(input('введите отчество')))
summa = int(input('введите сумму'))
coins = [name, surname, otch]
exchange = [False]*(summa + 1)
exchange[0] = '0'
for coin in coins:
    for i in range(coin, summa + 1):
        if exchange[i - coin] != False:
            if exchange[i] == False:
                if i % coin == 0:
                    exchange[i] = f"{coin}*{i // coin}"
                else:
                    exchange[i] = f"{coin}*{i//coin}+{exchange[i - coin]}"
            if exchange[summa] != False:
                print(exchange[summa])
if exchange[summa] != False:
    print(exchange[summa])
else:
    print("-42!")