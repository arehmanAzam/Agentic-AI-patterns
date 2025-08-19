import gradio as gr
import requests
import json
import uuid
from typing import List, Tuple

class ChatApp:
    def __init__(self):
        self.webhook_url = "http://localhost:5678/webhook/chat"
        self.user_id = str(uuid.uuid4())
        self.session_id = str(uuid.uuid4())
        
    def send_message_to_webhook(self, message: str) -> str:
        """Send message to webhook and return response"""
        try:
            payload = [{
                "headers": {
                    "content-type": "application/json",
                    "user-agent": "GradioChat/1.0"
                },
                "params": {},
                "query": {},
                "body": [{
                    "message": message,
                    "user_id": self.user_id,
                    "session_id": self.session_id
                }],
                "webhookUrl": self.webhook_url,
                "executionMode": "production"
            }]
            
            headers = {
                "Content-Type": "application/json"
            }
            
            response = requests.post(
                self.webhook_url,
                data=json.dumps(payload),
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                try:
                    # Try to parse JSON response
                    response_data = response.json()
                    # Extract message from response if it's structured
                    if isinstance(response_data, dict) and "output" in response_data:
                        return response_data["output"]
                    elif isinstance(response_data, dict) and "message" in response_data:
                        return response_data["message"]
                    elif isinstance(response_data, dict) and "response" in response_data:
                        return response_data["response"]
                    else:
                        return str(response_data)
                except json.JSONDecodeError:
                    # If not JSON, return raw text
                    return response.text
            else:
                return f"Error: Received status code {response.status_code}. Response: {response.text}"
                
        except requests.exceptions.ConnectionError:
            return "Error: Could not connect to the webhook. Please make sure the webhook server is running on http://localhost:5678"
        except requests.exceptions.Timeout:
            return "Error: Request timed out. The webhook took too long to respond."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def chat_function(self, message: str, history: List[dict]) -> Tuple[str, List[dict]]:
        """Process chat message and update history"""
        if not message.strip():
            return "", history
        
        # Send message to webhook and get response
        bot_response = self.send_message_to_webhook(message.strip())
        
        # Add the conversation to history using the new messages format
        history.append({"role": "user", "content": message.strip()})
        history.append({"role": "assistant", "content": bot_response})
        
        return "", history
    
    def generate_new_session(self):
        """Generate a new session ID and return the updated display"""
        self.session_id = str(uuid.uuid4())
        print(f"🔄 [DEBUG] New session ID generated: {self.session_id}")
        return f"**Session ID:** `{self.session_id}`"
    
    def create_interface(self):
        """Create and return the Gradio interface"""
        with gr.Blocks(
            title="Chat Application",
            theme=gr.themes.Soft(),
            css="""
            .chat-container {
                max-height: 500px;
                overflow-y: auto;
            }
            """
        ) as demo:
            gr.Markdown("# 💬 Chat Application")
            gr.Markdown("Connect to your webhook-powered chat service")
            
            # Display session info
            with gr.Row():
                gr.Markdown(f"**User ID:** `{self.user_id}`")
                session_display = gr.Markdown(value="", visible=True)
            
            # Chat interface
            chatbot = gr.Chatbot(
                label="Chat History",
                height=400,
                container=True,
                elem_classes=["chat-container"],
                type="messages"
            )
            
            with gr.Row():
                msg_input = gr.Textbox(
                    placeholder="Type your message here...",
                    show_label=False,
                    scale=4,
                    container=False
                )
                send_btn = gr.Button("Send", variant="primary", scale=1)
            
            # Clear chat button
            clear_btn = gr.Button("Clear Chat", variant="secondary")
            
            # Event handlers
            def clear_chat():
                return [], ""
            
            # Send message on button click or Enter key
            send_btn.click(
                self.chat_function,
                inputs=[msg_input, chatbot],
                outputs=[msg_input, chatbot]
            )
            
            msg_input.submit(
                self.chat_function,
                inputs=[msg_input, chatbot],
                outputs=[msg_input, chatbot]
            )
            
            # Clear chat functionality
            clear_btn.click(
                clear_chat,
                outputs=[chatbot, msg_input]
            )
            
            # Generate new session ID on page load
            demo.load(
                self.generate_new_session,
                outputs=[session_display]
            )
            
            # Instructions
            with gr.Accordion("ℹ️ Instructions", open=False):
                gr.Markdown("""
                ### How to use this chat application:
                
                1. **Type your message** in the text box below
                2. **Press Enter** or click the **Send** button
                3. Your message will be sent to the webhook at: `http://localhost:5678/webhook/chat`
                4. The response will appear in the chat history above
                
                ### Webhook Details:
                - **URL:** `http://localhost:5678/webhook/chat`
                - **Method:** POST
                - **User ID:** `{}`
                - **Session ID:** `{}`
                
                ### Troubleshooting:
                - Make sure your webhook server is running on port 5678
                - Check that the webhook endpoint accepts the expected JSON format
                - Look at the browser console for any error messages
                """.format(self.user_id, self.session_id))
        
        return demo

def main():
    """Main function to run the chat application"""
    chat_app = ChatApp()
    demo = chat_app.create_interface()
    
    print(f"🚀 Starting Chat Application...")
    print(f"📡 Webhook URL: {chat_app.webhook_url}")
    print(f"👤 User ID: {chat_app.user_id}")
    print(f"🔗 Session ID: {chat_app.session_id}")
    print(f"🌐 The app will be available at: http://localhost:7860")
    
    # Launch the application
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )

if __name__ == "__main__":
    main()