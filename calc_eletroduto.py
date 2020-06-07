class Eletroduto:
    'Eletroduto como infra'
    'O método calc_eletroduto retorna o valor do diametro do eletroduto escolhido, caso o eletroduto seja maior que 4"'
    'o valor de retorno será 0'

    def __init__(self, area_circuito):
        self.area_circuito = area_circuito

    def calc_eletroduto(self):
        self.area_eletroduto = [176.71, 314.15, 490.86, 804.22, 1256.6, 1963.44, 3318.21, 5026.4, 7853.75]
        self.esc=0
        self.taxa_ocup_geral = [0,0,0,0,0,0,0,0,0]
        for i in range(0,9):
            self.taxa_ocup_geral[i] = self.area_circuito/self.area_eletroduto[i]
            if self.taxa_ocup_geral[i]>0.4:
                self.tx = self.taxa_ocup_geral[i]
                self.esc = i+1
        self.esc_eletroduto = [15,20,25,32,40,50,65,80,100]
        if self.esc == 9:
            return 0
        else:
            return self.esc_eletroduto[self.esc]

if(__name__=="__main__"):
    elet = Eletroduto(2588.7923)
    print (elet.calc_eletroduto())