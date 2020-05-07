class Circuito:
    'Classe dos circuitos'
    
    'O método calcArea retorna o valor em mm quadrados da área do circuito'

    def __init__(self, numFases, bitFases, numTerra, bitTerra, numNeutro = 0, bitNeutro = 0):
        self.numFases = numFases
        self.bitFases = bitFases
        self.numNeutro = numNeutro
        self.bitNeutro = bitNeutro
        self.numTerra = numTerra
        self.bitTerra = bitTerra
    
    def calcArea (self):
        dadosCabos = {240:27 ,185:24 ,150:21.5 ,120:19.5 ,95:18 ,70:16 ,50:14 ,35:12 ,25:10.5 ,16:8.6 ,10:7.6 ,6:6.4 ,4:5.8 ,2.5:5.4 }
        self.areaFases = self.numFases*(3.1415*((dadosCabos[self.bitFases]/2)**2))
        if self.bitNeutro != 0:
            self.areaNeutro = self.numNeutro*(3.1415*((dadosCabos[self.bitNeutro]/2)**2))
        else:
            self.areaNeutro = 0
        self.areaTerra = self.numTerra*(3.1415*((dadosCabos[self.bitTerra]/2)**2))
        
        self.areaCirc = self.areaFases + self.areaNeutro + self.areaTerra

        return self.areaCirc