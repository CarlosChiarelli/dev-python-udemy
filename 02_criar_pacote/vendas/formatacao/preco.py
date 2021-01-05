"""Faz a formatação do preço."""


def real(valor):
    """Formata a moeda BR."""
    return f'R$ {valor:.2f}'.replace('.', ',')
