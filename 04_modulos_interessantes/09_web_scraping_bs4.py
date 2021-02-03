import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

# serão pegos os endereços "class" do elemento no css
# abaixo é um retângulo inteiro (uma pergunta)
for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')  # dentro do retângulo
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')

    print(data.text, titulo.text, votos.text, sep='\t')
