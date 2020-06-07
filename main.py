from calc_area_circuito import Circuito
from calc_eletroduto import Eletroduto

#Escolhendo a configuração do circuito
print("\nEscolha a configuração do circuito:\n\n")
print('1 - para "3F + N + T"')
print('2 - para "3F + T"')
print('3 - para "2F + T"')
print('4 - para "F + N + T"\n')
esc = int( input('Opção: '))
while (esc!=1 and esc!=2 and esc!=3 and esc!=4):
    print ("Opção inválida!")
    esc = int( input('Opção: '))

#Escolhendo número de cabos por fase/neutro/terra
if (esc==1):
    num_fase = 3*int( input("Entre com o número de cabos por fase: "))
    num_neutro = num_fase/3
    bit_fase = int( input("Entre com a seção do cabo (fases e neutro): "))
    bit_neutro = bit_fase
    num_terra = int( input("Entre com o número de cabos no terra: "))
    bit_terra = int( input("Entre com a seção do cabo terra: ")) 
    
elif (esc==2):
    num_fase = 3*(int( input("Entre com o número de cabos por fase: ")))
    bit_fase = int( input("Entre com a seção do cabo fase: "))
    num_neutro = 0
    bit_neutro = 0
    num_terra = int( input("Entre com o número de cabos no terra: "))
    bit_terra = int( input("Entre com a seção do cabo terra: ")) 

elif (esc==3):
    num_fase = 2*(int( input("Entre com o número de cabos por fase: ")))
    bit_fase = int( input("Entre com a seção do cabo fase: "))
    num_neutro = 0
    bit_neutro = 0
    num_terra = int( input("Entre com o número de cabos no terra: "))
    bit_terra = int( input("Entre com a seção do cabo terra: ")) 
elif (esc==4):
    num_fase = int( input("Entre com o número de cabos por fase: "))
    num_neutro = num_fase
    bit_fase = int( input("Entre com a seção do cabo (fases e neutro): "))
    bit_neutro = bit_fase
    num_terra = int( input("Entre com o número de cabos no terra: "))
    bit_terra = int( input("Entre com a seção do cabo terra: ")) 

circ1 = Circuito(num_fase, bit_fase, num_terra, bit_terra, num_neutro, bit_neutro)
area_circ = circ1.calc_area()
elet1 = Eletroduto(area_circ)
eletrofinal = elet1.calc_eletroduto()
print("O eletroduto escolhido foi: {} mm".format(eletrofinal))