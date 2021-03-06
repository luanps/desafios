#DESCRIÇÃO DA SOLUÇÃO PROPOSTA:
1. Manipulação de Strings:
desenvolvido em Python 3, a função breaklines.py lê da entrada padrão
o texto a ser formatado, a quantidade de caracteres maxima permitida 
por linha e opcionalmente a indentacao do texto.
desta forma a chamada para função se dá conforme exemplo a seguir:

```
python3 breakLines.py input.txt 40
```
e para texto indentado:

```
python3 breakLines.py input.txt 40 -i 1
```

2. Crawling data:
desenvolvido em Python 3, a função crawlReddit.py lê da entrada padrão
subreddits separados por ";" e busca threads no portal 
[reddit](http://reddit.com) que possuam menos de 24 horas de postagem e
 mais de 5000 upvotes.

Exemplo de execução:

```
python3 crawlReddit.py 'cats;dogs;brazil'
```

Adicionalmente pode-se enviar a lista acima para o 
[Telegram](https://web.telegram.org/) mediante a seguinte chamada:

```
python3 crawlReddit.py 'cats;dogs;brazil' -id $123
```

substituindo o parâmetro $123 pelo respectivo chat_id do usuário Telegram.


# Desafios IDwall

Aqui estão os desafios para a primeira fase de testes de candidatos da IDwall.
Escolha em qual linguagem irá implementar (a não ser que um de nossos colaboradores lhe instrua a utilizar uma linguagem específica).

Não há diferença de testes para diferentes níveis de profissionais, porém o teste será avaliado com diferentes critérios, dependendo do perfil da vaga.

1. [Manipulação de strings](https://github.com/idwall/desafios/tree/master/strings)
2. [Crawlers](https://github.com/idwall/desafios/tree/master/crawlers)

## Como entregar estes desafios
Você deve forkar este projeto e fazer o *push* no seu próprio repositório e enviar o link para _jobs@idwall.co_ ou para o email do recrutador, junto com seu LinkedIn atualizado.

A implementação deve ficar na pasta correspondente ao desafio. Fique à vontade para adicionar qualquer tipo de conteúdo que julgue útil ao projeto, alterar/acrescentar um README com instruções de como executá-lo, etc.

**Obs.**:
- Você não deve fazer um Pull Request para este projeto!
- Utilizar as versões mais atuais da linguagem que escolher para desenvolver (JavaScript ES6+; Java 8; Python 3, etc).

### Extras

- Descreva o processo de resolução dos desafios;
- Descreva como utilizar a sua solução;
- Tratamento de erros e exceções. Fica a seu critério quais casos deseja tratar e como serão tratados;
- Testes unitários ou de integração;
- Use o Docker.

## Carreira IDwall

Caso queira mais detalhes de como trabalhamos, quais são nossos valores e ideais, confira a página [Carreira IDwall](https://idwall.co/carreira) e mesmo que seu perfil não esteja listado nas vagas em aberto, lhe encorajamos a mandar seu CV! Valorizamos bons profissionais sempre e gostamos de manter contato com gente boa.

Boas implementações! 🎉
