import json 
import requests 

class Carro: 
    def __init__(self, marca, modelo, ano, posicaox, posicaoy):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.posicaox = posicaox
        self.posicaoy = posicaoy
        
    def acelerar(self, incremento=10):
        self.velocidade += incremento
        print(f"{self.modelo} Acelerando... Velocidade Atual: {self.velocidade}")
        
    def frear(self, decremento=10):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} Freando... Velocidade Atual: {self.velocidade}")
        
    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "ano":self.ano,
            "velocidade":self.velocidade,
            "posicaox": self.posicaox,
            "posicaoy": self.posicaoy
        }
        
meu_carro = Carro("Ford", "Mustang", 1969, 10, 20)
    
carro_json = json.dumps(meu_carro.to_dict(), indent=4)

print(carro_json)
        
    
        
