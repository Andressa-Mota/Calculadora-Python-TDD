import pytest
from calculadora import Calculadora

@pytest.mark.parametrize("n1,n1,esperado",[(1,2,3),(0,0,0),(-1,1,0)])
def test_soma(n1,n2,esperado):
    assert Calculadora.soma(n1,n2) == esperado
