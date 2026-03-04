# 🏎️ Simulação de Veículo com POO e JSON

Este módulo demonstra como utilizar a Programação Orientada a Objetos em Python para modelar entidades do mundo real e prepará-las para integração com APIs ou sistemas de armazenamento através do formato JSON.

## 🛠️ Funcionalidades

- **Abstração e Encapsulamento**: A classe `Carro` gere propriedades internas como velocidade e coordenadas geográficas (posicaox, posicaoy).
- **Lógica de Movimentação**:
  - `acelerar()`: Incrementa a velocidade do veículo.
  - `frear()`: Reduz a velocidade, garantindo que o valor nunca seja inferior a zero.
- **Serialização de Dados**: Conversão dinâmica de instâncias da classe em dicionários e, posteriormente, em strings JSON formatadas.

## 💻 Exemplo de Uso

```python
# Instanciação de um novo carro
meu_carro = Carro("Ford", "Mustang", 1969, 10, 20)

# Simulação de condução
meu_carro.acelerar(20)
meu_carro.frear(5)

# Exportação para JSON
carro_json = json.dumps(meu_carro.to_dict(), indent=4)
