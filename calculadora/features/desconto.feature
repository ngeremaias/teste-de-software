# language: pt
Funcionalidade: Cálculo de Desconto

  Cenário: Aplicar desconto padrão em uma compra
    Dado que eu tenho uma calculadora de descontos
    Quando eu aplico um desconto de 10% em uma compra de 100 reais
    Então o valor final deve ser 90 reais