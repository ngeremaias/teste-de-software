class Calculadora:
    def aplicar_desconto(self, valor_total, percentual):
        if percentual < 0:
            raise ValueError("Desconto não pode ser negativo")
        
        desconto = valor_total * (percentual / 100)
        return valor_total - desconto