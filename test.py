import boto3
import json
import botocore

# Create a boto3 client for Bedrock Runtime
client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

# Ask user for input
user_question = input("Ask me anything about AWS or Bedrock: ")

# Prepare Bedrock API request (single user message)
body = {
    "anthropic_version": "bedrock-2023-05-31",
    "messages": [
        {"role": "user", "content": user_question}
    ],
    "max_tokens": 200,
    "temperature": 0.5
}

# Convert to JSON string
body_str = json.dumps(body)

# Invoke Claude 3 Sonnet
try:
    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        accept="application/json",
        body=body_str
    )

    result = json.loads(response['body'].read())
    print("\n✅ RESPONSE:")
    print(result['content'][0]['text'])

except botocore.exceptions.ClientError as error:
    print("❌ ClientError:", error)
