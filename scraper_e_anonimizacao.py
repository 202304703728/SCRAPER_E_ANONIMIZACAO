# Lê a pré-visualização de uma sentença no banco de jurisprudências
# e faz a supressão dos nomes dos envolvidos
# obs: Foi escolhida a sentença de um processo Convenção de Haia
# sobre Aspectos Civis do Sequestro Internacional de Crianças
# porque normalmente é necessário ocultar os nomes das partes

import requests
from bs4 import BeautifulSoup

try:
    url = 'https://www10.trf2.jus.br/consultas/?movimento=cache&q=cache:383wfQwvqMEJ:sentencasrj.trf2.jus.br/apolo/databucket/idx%3Fcoddoc%3D%26dthrmov%3D2016-10-13%252015:37:00+haia&site=v2_sentencas&client=v2_index&proxystylesheet=v2_index&lr=lang_pt&ie=UTF-8&output=xml_no_dtd&access=p&oe=UTF-8'

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    requisicao = requests.get(url)
    # print(requisicao)

    # Verifica se ocorreu a conexão
    if requisicao.status_code == 200:

        # Salva o texto da sentença
        # print(requisicao.text)
        novo_texto = requisicao.text

        # Guardei o nome das partes que precisam ser omitidos
        # Como eu já sabia quais nomes queria ocultar, coloquei em
        # nomes_para_substituicao, inclusive nomes com grafia diferente, pré-nome e sobrenome
        # Em um sistema processual, bastaria ler os nomes no cadastro das partes
        # e perguntar ao usuário se gostaria de incluir alguma variação dos nomes no array
        nomes_para_substituicao = ["ERICA", "ERICKA", "ERIKA", "KYLE", "02/05/2003", "GEORGE", "RANGEL", "PENNINGTON", "JR.", "MOREIRA", "RANGE", "WILLIAM", "JR"]
        total_nomes_substituicao = len(nomes_para_substituicao)
        caracter_de_substituicao = u'\u220E'+u'\u220E'+u'\u220E'

        # Busca os nomes no texto da sentença e substitui
        for i in range(total_nomes_substituicao):
            if nomes_para_substituicao[i] in requisicao.text or nomes_para_substituicao[i].title() in requisicao.text:
                novo_texto = novo_texto.replace(nomes_para_substituicao[i], caracter_de_substituicao)
                novo_texto = novo_texto.replace(nomes_para_substituicao[i].title(), caracter_de_substituicao)
                # print(novo_texto)

        print(novo_texto)

    else:
        print("Não foi possível estabelecer conexão com a página. Tente mais tarde.")

except:
    # Exceção ampla, mas quis deixar assim mesmo
    print("Algo está errado! Tente novamente.")
