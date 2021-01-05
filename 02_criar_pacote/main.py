"""Arquivo principal."""

from vendas import calc_preco
from vendas.calc_preco import diminui
import vendas.formatacao.preco as formata

print(calc_preco.aumento(valor=100, formata=True))

print(diminui(valor=100))

print(formata.real(20))
