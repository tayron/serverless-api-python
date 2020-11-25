# API Serverless

## Descrição
Exemplo de uma API Serverless usando Serverless Framework e deploy no AWS utilizando os serviços:
- AWS Lambda
- API Gateway
- DynamoDB

## Tutorial seguido
- https://solvimm.com/blog/como-construir-sua-primeira-api-na-nuvem-com-o-serverless-framework
- https://solvimm.com/blog/como-adicionar-uma-chave-de-autorizacao-de-api-com-o-serverless-framework
- https://solvimm.com/blog/como-usar-variaveis-com-o-serverless-framework
- https://solvimm.com/blog/integracao-de-api-com-dynamodb-utilizando-o-serverless-framework

## Comandos

#### Comando para gravar credencial localmente da AWS:
```
serverless config credentials \
--provider aws \
--key apiKeyAqui \
--secret chaveSecretaAqui \
--profile my-aws-profile
```

#### Comando para realizar deploy:

##### Dependências
- ```npm install serverless-iam-roles-per-function```

Para fazer deploy e manter o stage padrão: **dev**
```serverless deploy --aws-profile my-aws-profile```

Para fazer deploy e alterar o stage padrão: **dev** para **prod**
```serverless deploy --aws-profile my-aws-profile --stage prod```

O resultado do comando será algo parecido com 
```
....
Serverless: Stack update finished...
Service Information
service: api-python-hello-world
stage: dev
region: us-east-1
stack: api-python-hello-world-dev
resources: 16
api keys:
  myKey: CCJZsdfgzrbxi0shwR8e2Yasdfaz0bOG6A5hlJc7Ui
endpoints:
  GET - https://aaa.execute-api.aa-aa-1.amazonaws.com/dev/api/python/hello-world
functions:
  hello: api-python-hello-world-dev-hello
layers:
  None
```

Chave da API se encontra na reposta
```
api keys:
  myKey: CCJZsdfgzrbxi0shwR8e2Yasdfaz0bOG6A5hlJc7Ui
```

Chave da API deve ser passado no header da requisição:

```x-api-key: CCJZsdfgzrbxi0shwR8e2Yasdfaz0bOG6A5hlJc7Ui```

#### Comando para remover api em produção:

```serverless remove --aws-profile my-aws-profile --stage dev```

## Requisição

### Exemplo de requisição na API para exibir o Helo World:

```
curl --request GET \
  --url https://7cq8ind2me.execute-api.us-east-1.amazonaws.com/dev/api/python/hello-world \
  --header 'x-api-key: CCJZsdfgzrbxi0shwR8e2Yasdfaz0bOG6A5hlJc7Ui'
```

### Exemplo de requisição na API para listar todos os contatos:
```
curl -X GET
-H "x-api-key: CCJZsdfgzrbxi0shwR8e2Yasdfaz0bOG6A5hlJc7Ui" \
https://8nncm9w4p5.execute-api.us-east-1.amazonaws.com/dev/contact
```

### Exemplo de requisição na API para cadastrar um contato:
```
curl -X POST
-H "x-api-key: CCJZsdfgzrbxi0shwR8e2Yasdfaz0bOG6A5hlJc7Ui" \
-H "Content-Type: application/json" \
-d '{"name":"Lina Nathan", "phone":"90000-0000"}' \
https://8nncm9w4p5.execute-api.us-east-1.amazonaws.com/dev/contact
```

### Exemplo de requisição na API para excluir um contato:
```
curl -X DELETE
-H "x-api-key: CCJZsdfgzrbxi0shwR8e2Yasdfaz0bOG6A5hlJc7Ui" \
-H "Content-Type: application/json" \
-d '{"id":"29a64dab-b77a-4b5f-9e82-222950c3b5ff"}' \
https://8nncm9w4p5.execute-api.us-east-1.amazonaws.com/dev/contact
```