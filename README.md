# API Serverless

## Descrição
Exemplo de uma API Serverless usando Serverless Framework e deploy no AWS utilizando os serviços da Amazon
- AWS Lambda
- API Gateway

## Tutorial seguido
https://solvimm.com/blog/como-construir-sua-primeira-api-na-nuvem-com-o-serverless-framework

## Comandos

Comando para gravar credencial localmente da AWS
```
serverless config credentials \
--provider aws \
--key apiKeyAqui \
--secret chaveSecretaAqui \
--profile my-aws-profile
```

Comando para realizar deploy
```serverless deploy --aws-profile my-aws-profile```

Comando para remover api em produção
```serverless remove --aws-profile my-aws-profile --stage dev```