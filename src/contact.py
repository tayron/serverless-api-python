import boto3
import os
import uuid

def get_dynamo_table():
    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ["TABLE"]
    return dynamodb.Table(table_name)

def create(event, context):
    body = event["body"]

    if ("name" in body and "phone" in body):
        table = get_dynamo_table()

        table.put_item(
            Item={
                "id": str(uuid.uuid4()),
                "name": body["name"],
                "phone": body["phone"]
            }
        )

        return {
            "status": 200,
            "body": "OK"
        }

    return {
        "status": 422,
        "body": "Nenhum nome ou telefone foi informado"
    }