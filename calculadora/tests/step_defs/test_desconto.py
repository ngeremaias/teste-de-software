import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.calculadora import Calculadora

# 1. Localiza o arquivo Gherkin
scenarios('desconto.feature')

# 2. Fixture para compartilhar a calculadora entre os passos
@pytest.fixture
def calc():
    return Calculadora()

# 3. Definições dos Passos (Step Defs)

@given('que eu tenho uma calculadora de descontos', target_fixture='calc_app')
def step_given_calc(calc):
    return calc

@when(parsers.parse('eu aplico um desconto de {pct:d}% em uma compra de {total:d} reais'), target_fixture='resultado')
def step_when_aplicar(calc_app, pct, total):
    return calc_app.aplicar_desconto(total, pct)

@then(parsers.parse('o valor final deve ser {valor_esperado:d} reais'))
def step_then_validar(resultado, valor_esperado):
    assert resultado == valor_esperado