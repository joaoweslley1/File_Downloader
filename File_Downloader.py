import requests

#armazena os links que contem os arquivos que serão baixados
#adicionar em 'links' os links para baixar os arquivos no formato de string
links = ['link1.com', 'link2.com', 'link3.com']

#baixa todos os links contidos na variável links
for i in range(len(links)):
    
    #gera o nome dos arquivos dinamicamente
    #alterar 'name' para nome padrão desejado (exemplo: 'imagem', 'video')
    dicio = {'name': 'nome padrao do arquivo', 'id': i+1}

    #concatena o nome ao id do arquivo baixado | permite adicionar a extensão do arquivo (video0 | imagem3.png)
    nome = dicio['name'] + str(dicio['id'])# + '.png'
    
    url = links[i]
    resposta = requests.get(url, verify=False)
    open(nome, "wb").write(resposta.content)
