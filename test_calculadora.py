import pytest
from calculadora import Calculadora

@pytest.mark.parametrize("n1,n2,esperado",[(1,2,3),(0,0,0),(-1,1,0)])
def test_soma(n1,n2,esperado):
    assert Calculadora.soma(n1,n2) == esperado, "Houve um erro na soma!"

@pytest.mark.parametrize("n1,n2,esperado",[(2,2,0),(4,3,1),(0,0,0)])
def test_sub(n1,n2,esperado):
    assert Calculadora.subtracao(n1,n2) == esperado, "Houve um erro na subtração!"

@pytest.mark.parametrize("n1,n2,esperado",[(2,2,4),(1,1,1),(0,0,0)])
def test_mult(n1,n2,esperado):
    assert Calculadora.multiplicacao(n1,n2) == esperado, "Houve um erro na multiplicação!"


@pytest.mark.parametrize("n1,n2,esperado",[(4,2,2),(3,0,0),(1,1,1)])
def test_div(n1,n2,esperado):
    assert Calculadora.divisao(n1,n2) == esperado, "Houve um erro na divisão!"    