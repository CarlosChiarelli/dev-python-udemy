# Roteiro para planejamento da API

Alguns ponto devem estar respondidos na faze de **planejamento** antes de iniciar o desenvolvimento propriamente dito.

Abaixo a respostas e parâmetros são baseados no case abordado (01_requisitos_das_apis.pdf). Para cada requisito será gerado uma especificação.

Cada item (sub-título) abaixo deve ser adicionado a um card/tarefa do Jira/Trello (plataformas de gestão).


## 2) Especificação tela de login

1. Qual é o path?

R: Path é a URL que vai acessar a API.

Parâmetro: /login POST


2. Quais são os parâmetros do request?

R: Exemplo "/user/1" significa que quero acessar usuário com id 1. É preciso deixar claro que existe esse parâmetro que é do tipo path.

Parâmetro: (não há)


3. Qual é o formato da resposta?

R: Json, xml, texto puto, etc.

Parâmetro: JSON


4. Qual é o formato do request?

R: Qual o formato aceito para submeter o request.

Parâmetro: JSON


5. Qual é o request body (corpo da requisição)?

Parâmetro: email e password


6. Qual é o response body (corpo da resposta)?

Parâmetro: token, id, email, firstName e lastName


7. Qual é o status da resposta para operação sucesso?

Parâmetro: 200 - ok


8. Qual é a resposta para operação de erro no request?

Parâmetro: 400 - Dados request enviados incorretos


9. Qual é a resposta para operação de erro de regra de negócio?

R: Exemplo que pode haver mais de uma resposta para regra de negócio.

Parâmetro 1: 401 - password incorreto
Parâmetro 2: 404 - usuário não encontrado


10. Qual é a resposta para operação de erro no servidor?

Parâmetro: 500 - Erro no servidor


## 1) Especificação tela de registro da conta

1. Qual é o path?

/accounts GET (recuperar registros)
/accounts POST (salvar registro)
/accounts/{id} GET
/accounts/{id} PUT (editar registro)
/accounts/{id} DELETE (deletar registro)


2. Quais são os parâmetros do request?

toker JWT HEADER (json web token)
{id} accounts PATH, quando necessário

3. Qual é o formato da resposta?

JSON


4. Qual é o formato do request?

JSON


5. Qual é o request body (corpo da requisição)?

firstName, lastName, email, phoneNumber, password, dateBirth e gender


6. Qual é o response body (corpo da resposta)?

id, firstName, lastName, email, phoneNumber, dateBirth e gender


7. Qual é o status da resposta para operação sucesso?

200 - ok GET
201 - Criado POST
202 - Aceito PUT
204 - Sem conteúdo DELETE

8. Qual é a resposta para operação de erro no request?

400 - Dados request enviados incorretos


9. Qual é a resposta para operação de erro de regra de negócio?

401 - Token inválido, inexistente ou expirado
404 - Recurso {id} não encontrado


10. Qual é a resposta para operação de erro no servidor?

500 - Erro no servidor


## 3) Especificação acompanhamento do crescimento infantil

1. Qual é o path?

/progress GET
/progress POST
/progress/{id} GET
/progress/{id} PUT
/progress/{id} DELETE


2. Quais são os parâmetros do request?

toker JWT HEADER
{id} progress PATH quando necessário


3. Qual é o formato da resposta?

JSON


4. Qual é o formato do request?

JSON


5. Qual é o request body (corpo da requisição)?

height, weight, headCircumference, dateProgress e account(id, email, firstName, lastName, dateBirth, gender)


6. Qual é o response body (corpo da resposta)?

id, height, weight, headCircumference, dateProgress e account(id, email, firstName, lastName, dateBirth, gender)


7. Qual é o status da resposta para operação sucesso?

200 - ok GET
201 - Criado POST
202 - Aceito PUT
204 - Sem conteúdo DELETE


8. Qual é a resposta para operação de erro no request?

400 - Dados request enviados incorretos


9. Qual é a resposta para operação de erro de regra de negócio?

401 - Token inválido, inexistente ou expirado
404 - Recurso {id} não encontrado


10. Qual é a resposta para operação de erro no servidor?

500 - Erro no servidor


## 4) Especificação relatório de crescimento infantil

1. Qual é o path?

/accounts/{email}/progress GET


2. Quais são os parâmetros do request?

toker JWT HEADER
{email} accounts PATH


3. Qual é o formato da resposta?

JSON


4. Qual é o formato do request?

JSON


5. Qual é o request body (corpo da requisição)?

vazio (nenhuma informação relevante)


6. Qual é o response body (corpo da resposta)?

height, weight, headCircumference, dateProgress


7. Qual é o status da resposta para operação sucesso?

200 - ok


8. Qual é a resposta para operação de erro no request?

400 - Dados request enviados incorretos


9. Qual é a resposta para operação de erro de regra de negócio?

401 - Token inválido, inexistente ou expirado
404 - Recurso {email} não encontrado


10. Qual é a resposta para operação de erro no servidor?

500 - Erro no servidor


# Próximo passo

Feito o planejamento é necessário escrever as especificações da API, ou seja, pegar tudo que está no planejamento e criá-las de fato.

Inicia-se conhecendo a especificação OpenAPI, seguindo do Swagger Edit e Swagger UI.
