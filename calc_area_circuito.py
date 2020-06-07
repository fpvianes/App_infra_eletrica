class Circuito:
    'Classe dos circuitos'
    'O método calcArea retorna o valor float em mm quadrados da área do circuito'
    'Quando passar o num de fases passar o numero total, por exemplo 3x4x240 deve-se passar 12'

    def __init__(self, num_fases, bit_fases, num_terra, bit_terra, num_neutro = 0, bit_neutro = 0):
        self.num_fases = num_fases
        self.bit_fases = bit_fases
        self.num_neutro = num_neutro
        self.bit_neutro = bit_neutro
        self.num_terra = num_terra
        self.bit_terra = bit_terra
    
    def calc_area (self):
        dados_cabos = {240:27 ,185:24 ,150:21.5 ,120:19.5 ,95:18 ,70:16 ,50:14 ,35:12 ,25:10.5 ,16:8.6 ,10:7.6 ,6:6.4 ,4:5.8 ,2.5:5.4 }
        self.area_fases = self.num_fases*(3.1415*((dados_cabos[self.bit_fases]/2)**2))
        if self.bit_neutro != 0:
            self.area_neutro = self.num_neutro*(3.1415*((dados_cabos[self.bit_neutro]/2)**2))
        else:
            self.area_neutro = 0
        self.area_terra = self.num_terra*(3.1415*((dados_cabos[self.bit_terra]/2)**2))
        
        self.area_circ = self.area_fases + self.area_neutro + self.area_terra

        return self.area_circ

if (__name__ == "__main__"):
    circ1 = Circuito(3,240,1,120,1,240)
    print(circ1.calc_area())