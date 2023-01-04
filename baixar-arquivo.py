import requests as rq

links = ['https://is5-ssl.mzstatic.com/image/thumb/Music/v4/40/88/bf/4088bf23-e80e-c8c4-d562-258af29900b9/628855005676.jpg/316x316bb.webp',\
'https://f4.bcbits.com/img/a1926305734_10.jpg', 'https://topwar.ru/uploads/posts/2012-08/1345003572_t32_5.jpg']

for i in range(len(links)):
    dicio = {'name': 'imagem', 'id': i}
    nome = dicio['name'] + str(dicio['id'])# + '.png'
    #print (nome)
    url = links[i]
    resposta = rq.get(url, verify=False)
    open(nome, "wb").write(resposta.content)
