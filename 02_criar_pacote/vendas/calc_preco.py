"""Faz operações com os preços."""

from vendas.formatacao.preco import real


def aumento(valor, formata=False):
    """Aumenta o preço."""
    calc = valor * 1.05
    calc = real(calc) if formata else calc

    return calc


def diminui(valor, formata=False):
    """Diminui o preço."""
    calc = valor * .95
    calc = real(calc) if formata else calc

    return calc
