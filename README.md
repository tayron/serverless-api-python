# API Serverless

## Descrição
Exemplo de uma API Serverless usando Serverless Framework e deploy no AWS utilizando os serviços:
- AWS Lambda
- API Gateway

## Tutorial seguido
- https://solvimm.com/blog/como-construir-sua-primeira-api-na-nuvem-com-o-serverless-framework
- https://solvimm.com/blog/como-adicionar-uma-chave-de-autorizacao-de-api-com-o-serverless-framework

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

```serverless deploy --aws-profile my-aws-profile```

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

Exemplo de requisição para api:

```
curl --request GET \
  --url https://7cq8ind2me.execute-api.us-east-1.amazonaws.com/dev/api/python/hello-world \
  --header 'x-api-key: CCJZLX0pQZ9zrbxi0shwR8e2Yz0bOG6A5hlJc7Ui'
```