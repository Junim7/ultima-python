from lzma import MODE_FAST


centavos_5 = int(input('quantidade moedas 0.05 - ')) 
centavos_10 = int(input('quantidade moedas 0.10 - '))
centavos_25 = int(input('quantidade moedas 0.25 -' ))
centavos_50 = int(input('quantidade moedas 0.50 - '))
real_1 = int(input('quantidade moedas 1.00 - '))
resultado = (centavos_5*0.05)+(centavos_10*0.10)+(centavos_25*0.25)+(centavos_50*0.50)+(real_1*1)
print('Total no caixa R$ ',resultado)
