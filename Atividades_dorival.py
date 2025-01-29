"""#1
class ControleRemoto:
    def __init__(self): #toda classe tem a função init , self é o o propió controle remoto
        cor="rosa"
        altura="20cm"
        profundidade="5cm"
        largura="5cm"

#ambos são controles porem podem ter caracteristicas fisícas diferentes
controle_remoto=ControleRemoto() #Criei a primeira instancia(o objeto e
controle_remoto2=ControleRemoto()
"""
#novo
class ControleRemoto:
    def __init__(self, cor , altura,profundidade,largura): #toda classe tem a função init , self é o o propió controle remoto
        """Acima eudisse pra função que toda vez que ela for usada o objeto vai conter essas caracteristicas"""
        self.cor = cor #sem o self ele não vai entender cor como caracteristica
        self.altura = altura
        self.prpfundidade = profundidade
        self.largura = largura
        """Fizemos isso pro python entender que após o . tem a cor assim ela é entendida como característica do controle remoto"""
#ambos são controles porem podem ter caracteristicas fisícas diferentes
controle_remoto=ControleRemoto("rosa","10cm","3cm","6cm") #Criei a primeira instancia(o objeto e
print(controle_remoto.cor)
controle_remoto2=ControleRemoto("roxo","10cm","3cm","6cm")