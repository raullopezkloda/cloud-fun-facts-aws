import boto3
import random
import json

# DynamoDB connection
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudFacts")

# Bedrock client
bedrock = boto3.client("bedrock-runtime")

def lambda_handler(event, context):
    # Fetch all facts from DynamoDB
    response = table.scan()
    items = response.get("Items", [])
    if not items:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"fact": "No facts available in DynamoDB."})
        }

    fact = random.choice(items)["FactText"]

    # Messages for Claude Sonnet 4
    messages = [
        {
            "role": "user",
            "content": f"Toma este dato sobre la computación en la nube y conviértelo en algo divertido y atractivo en un máximo de 1-2 frases. Sé breve e ingenioso: {fact}"
        }
    ]

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 100,
        "messages": messages,
        "temperature": 0.7
    }

    try:
        # Call Claude Sonnet 4 on Bedrock usando EU inference profile
        resp = bedrock.invoke_model(
            modelId="eu.anthropic.claude-sonnet-4-20250514-v1:0",  # EU inference profile
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )

        # Parse response
        result = json.loads(resp["body"].read())
        witty_fact = ""

        # Claude v4 response: look inside "content"
        if "content" in result and result["content"]:
            for block in result["content"]:
                if block.get("type") == "text":
                    witty_fact = block["text"].strip()
                    break

        # Fallback if empty or too long
        if not witty_fact or len(witty_fact) > 300:
            witty_fact = fact

    except Exception as e:
        print(f"Bedrock error: {e}")
        witty_fact = fact

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({"fact": witty_fact})
    }
