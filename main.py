import gradio as gr
from backend import chain  # Keeping your original import

def create_custom_theme():
    return gr.Theme.from_hub("gradio/soft")

def chat(message, history):
    if not message.strip():  # Check if message is empty or just whitespace
        return "👋 Please ask a question! I'm here to help."
    
    response = chain.invoke(message)
    return response

# Custom CSS for additional styling
custom_css = """
.message-wrap {
    background: linear-gradient(135deg, #6e8efb, #a777e3);
    border-radius: 15px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.message.user {
    background: linear-gradient(135deg, #ff9966, #ff5e62) !important;
    color: white !important;
}
.message.bot {
    background: linear-gradient(135deg, #4e54c8, #8f94fb) !important;
    color: white !important;
}
"""

# Create the chat interface without retry, undo, and clear buttons
demo = gr.ChatInterface(
    fn=chat,
    title="✨ AI Customer Support Assistant ✨",
    description="Welcome! I'm here to help you with your questions. 🌟",
    theme=create_custom_theme(),
    css=custom_css,
    examples=[
        "How can I create an account?",
        "What is your return policy?",
        " How can I track my order?",
        "What payment methods do you accept?",
    ],
)

# Launch the interface
if __name__ == "__main__":
    demo.launch(
        share=True,  # Creates a public link
         # Enables queuing for multiple users
        height=700,  # Sets the height of the interface
          # S# Bind Gradio to all network interfaces (0.0.0.0) and expose it on port 8000
           
          server_port=7860,
       
    )
