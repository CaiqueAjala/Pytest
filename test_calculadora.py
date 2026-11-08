import pytest
from Calculadora import fatorial, adicao

def test_fatorial_correto():
    # O fatorial de 5 deve ser 120 (este teste vai falhar no código atual)
    assert fatorial(5) == 120

def test_fatorial_zero():
    # O fatorial de 0 deve ser 1
    assert fatorial(0) == 1

def test_adicao_valores_simples():
    # Testando se a adição soma corretamente sem duplicar
    assert adicao(2, 3) == 5