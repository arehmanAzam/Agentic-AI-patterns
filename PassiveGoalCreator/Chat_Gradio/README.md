# Chat Gradio Application

A simple chat application built with Gradio that integrates with a webhook endpoint for chat responses.

## Features

- 💬 Clean and modern chat interface
- 🔗 Webhook integration for chat responses
- 👤 Unique user and session ID generation
- 🚀 Easy to use and deploy
- 📱 Responsive design

## Installation

1. Install dependencies:
```bash
pip install -e .
```

Or install directly:
```bash
pip install gradio>=4.0.0 requests>=2.31.0
```

## Usage

1. Make sure your webhook server is running on `http://localhost:5678/webhook/chat`
2. Run the chat application:
```bash
python main.py
```
3. Open your browser and go to `http://localhost:7860`
4. Start chatting!

## Webhook Integration

The application sends POST requests to `http://localhost:5678/webhook/chat` with the following JSON structure:

```json
[
  {
    "headers": {
      "content-type": "application/json",
      "user-agent": "GradioChat/1.0"
    },
    "params": {},
    "query": {},
    "body": [
      {
        "message": "Your chat message here",
        "user_id": "generated-uuid",
        "session_id": "generated-uuid"
      }
    ],
    "webhookUrl": "http://localhost:5678/webhook/chat",
    "executionMode": "production"
  }
]
```

## Configuration

- **Webhook URL**: `http://localhost:5678/webhook/chat` (configurable in code)
- **App Port**: `7860` (configurable in code)
- **User ID**: Auto-generated UUID for each session
- **Session ID**: Auto-generated UUID for each session

## Troubleshooting

- **Connection Error**: Make sure your webhook server is running on port 5678
- **Timeout Error**: Check if your webhook responds within 30 seconds
- **Port Conflict**: Change the port in `main.py` if 7860 is already in use

## Example Webhook Response

Your webhook should return a JSON response or plain text. The app will handle both formats:

```json
{
  "message": "Hello! How can I help you today?"
}
```

Or simply return plain text:
```
Hello! How can I help you today?
```
