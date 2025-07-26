import gradio as gr
from main import answer_query

def chatbot_fn(query):
    return answer_query(query)

gr.Interface(
    fn=chatbot_fn,
    inputs="text",
    outputs="text",
    title="RAG Chatbot using Gemini Flash 1.5",
    description="Ask any question based on the uploaded document knowledge base."
).launch()
