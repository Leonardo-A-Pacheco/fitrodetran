import requests
from bs4 import BeautifulSoup

def extrair_links(url):
    try:
        # Faz a solicitação HTTP
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se há erros na solicitação

        # Analisa o HTML da página
        soup = BeautifulSoup(resposta.text, 'html.parser')

        # Encontrar todos os links na página
        links = [link.get('href') for link in soup.find_all('a') if link.get('href') is not None]

        return links
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []

# URL da página
url = 'https://www.detran.pr.gov.br/servicos/Motorista/Reciclagem/Agendar-curso-de-reciclagem-ybrzPqN4'

# Extrai e imprime todos os links da página
links_encontrados = extrair_links(url)
for link in links_encontrados:
    print(link)
