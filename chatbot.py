import streamlit as st
import boto3
import json

# Claude model ID – change as needed (example: Claude 3 Sonnet)
MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"
REGION = "us-east-1"

# Streamlit UI
st.set_page_config(page_title="Claude Chatbot", page_icon="🤖")
st.title("💬 Claude Chatbot with Bedrock")

# Input from user
user_input = st.text_input("🧑‍💻 You:", placeholder="Ask me anything...")

# If input is given
if user_input:
    # Prepare Claude messages format
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 1024
    }

    # Call Bedrock Runtime
    try:
        client = boto3.client("bedrock-runtime", region_name=REGION)
        response = client.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )
        result = json.loads(response["body"].read())

        # Show Claude response
        st.markdown("🤖 **Claude:**")
        st.write(result["content"][0]["text"])

    except Exception as e:
        st.error(f"❌ Error: {e}")
