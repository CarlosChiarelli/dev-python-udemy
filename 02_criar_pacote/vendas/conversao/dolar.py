"""Converte para dólar."""

from vendas.formatacao.preco import real


def conv_dolar(valor):
    """Função converte dólar para real."""
    return real(valor * 5)
