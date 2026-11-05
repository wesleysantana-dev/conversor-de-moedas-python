Conversor de Moedas --Dólar para Real-- (Mostra quantos dólares você compra com um valor em reais)

Programa em Python que busca a cotação do dólar em uma API pública e converte um valor em reais para dólares. O código usa programação orientada a objetos, com uma classe que guarda a cotação e faz a conversão.

Exemplo de execução:
--- CONVERSOR DE MOEDAS  ---
Dólar hoje (venda): R$ 5.49
Digite o valor em R$ para converter: 1200
Com R$ 1200.00 você compra US$ 218.50

-- O valor muda todo dia, porque vem da API no momento da consulta.

## O que o programa faz
-Consulta a cotação atual do dólar na AwesomeAPI
-Mostra a cotação de venda do dia
-Converte um valor em reais para dólares
-Trata erros: se a API não responder, mostra uma mensagem e encerra sem travar
## Como o código está organizado
- ConversorMoedas é uma classe, o modelo que reúne os dados e as ações da conversão
- buscar_cotacao() consulta a API e guarda o valor de venda em self.venda
- converter() usa esse valor para calcular a conversão
- test_conversor.py contém os testes, que simulam a resposta da API e não precisam de internet
## Como rodar
1.Ter o Python 3 instalado
2.Instalar a biblioteca de requisições: pip install requests
3.No terminal, rodar: python conversor.py
## Como rodar os testes
1.Instalar o pytest: pip install pytest
2.Na pasta do projeto, rodar: python -m pytest -v
## O que estou aprendendo com este projeto
-Programação orientada a objetos: classes, objetos e self
-Consumir uma API pública com a biblioteca requests
-Tratar erros com try e except
-Escrever testes automatizados com pytest e unittest.mock
## Próximos passos
Guardar o histórico de conversões em um banco SQLite
Permitir escolher outras moedas além do dólar
