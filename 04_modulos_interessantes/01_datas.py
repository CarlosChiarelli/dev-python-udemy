from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange

setlocale(LC_ALL, '')
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
ultimo_dia_mes = mdays[mes_atual]

# sábado, 13 de julho de 2019
formatacao1 = dt.strftime('%A, %d de %B de %Y')
# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1, formatacao2)

# obter o último dia do mês
print(mes_atual, mdays[mes_atual])

# PARA ANO BISSEXTO
dia_semana, ultimo_dia_fev20 = monthrange(2020, 2)
dia_semana, ultimo_dia_fev21 = monthrange(2021, 2)
# Saída: 29 (último dia de fevereiro de 2020)
print(ultimo_dia_fev20, ultimo_dia_fev21)
