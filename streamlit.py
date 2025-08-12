import streamlit as st
import boto3
import json

# Claude 3 Sonnet model ID
MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

# Create Bedrock client
client = boto3.client("bedrock-runtime", region_name="us-east-1")

st.set_page_config(page_title="Claude 3 Chatbot 💬", page_icon="🤖")

st.title("💬Insurance/Finance Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat UI
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

user_input = st.chat_input("Ask me anything about insurance or finance...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Claude 3 expects messages format
    claude_messages = [{"role": "user", "content": user_input}]
    payload = {
        "messages": claude_messages,
        "max_tokens": 512,
        "temperature": 0.5,
        "anthropic_version": "bedrock-2023-05-31"
    }

    try:
        response = client.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(payload)
        )

        result = json.loads(response['body'].read())
        reply = result['content'][0]['text']

        # Show bot reply
        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"❌ Error: {e}")
