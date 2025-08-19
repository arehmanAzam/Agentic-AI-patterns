# Agentic AI Design Patterns

A comprehensive collection of Agentic AI design patterns that are highly effective for building autonomous agents, automations, and chat/voice agents. Each pattern includes both theoretical implementation and practical demonstrations with interactive frontends.

## 🎯 Purpose

This repository serves as an educational resource for learning and implementing various Agentic AI design patterns. Each pattern demonstrates how AI agents can autonomously plan, execute, and adapt to achieve specific goals without constant human intervention.

## 📁 Repository Structure

Each Agentic AI design pattern follows a consistent structure:

```
PatternName/
├── Chat_Gradio/                    # Frontend interface
│   ├── main.py                     # Gradio application
│   ├── pyproject.toml              # Python dependencies
│   ├── README.md                   # Pattern-specific documentation
│   └── uv.lock                     # Dependency lock file
└── PatternName.json                # Workflow definition (n8n/LangChain/LangGraph)
```

## 🤖 Available Patterns

### 1. Passive Goal Creator
- **Location**: `PassiveGoalCreator/`
- **Description**: An agent that creates goals based on user input and context
- **Frontend**: Gradio-based chat interface
- **Workflow**: JSON configuration for goal creation logic

### 2. Proactive Goal Creator
- **Location**: `ProactiveGoalCreator/`
- **Description**: An agent that proactively identifies and creates goals
- **Status**: Coming soon

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher (for Python implementations)
- [uv](https://docs.astral.sh/uv/) (recommended) or pip for dependency management
- [n8n](https://n8n.io/) (for no-code implementations)
- Git

### Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Agentic-AI-patterns.git
   cd Agentic-AI-patterns
   ```

2. **Choose a pattern to explore**:
   ```bash
   cd PassiveGoalCreator  # or any other pattern folder
   ```

3. **Follow the pattern-specific instructions**:
   - Each pattern folder contains detailed setup instructions
   - Read the `README.md` file within the chosen pattern folder
   - Follow the step-by-step guide for your preferred implementation (n8n or Python)

### Example: Running PassiveGoalCreator
```bash
cd PassiveGoalCreator/Chat_Gradio
# Follow the instructions in PassiveGoalCreator/README.md
uv sync
uv run python main.py
```

## 🛠️ Implementation Options

Each pattern includes complete workflows that can be implemented using two different approaches:

### Option 1: No-Code with n8n Automation Tool
- **Ready-to-Use**: Complete n8n workflow JSON files provided
- **Direct Import**: Import workflows directly into your n8n instance
- **Visual Flow**: Drag-and-drop interface for understanding and modifying agent logic
- **Quick Setup**: No coding required, perfect for rapid prototyping

### Option 2: Python Frameworks
- **Complete Implementation**: Full Python-based agentic workflows provided
- **Framework Support**: Ready-to-use implementations using LangChain, LangGraph, or custom Python
- **Gradio Frontend**: Interactive chat interfaces for testing and demonstration
- **Extensible**: Modify and extend patterns for your specific use cases

## 📋 Implementation Instructions

**Important**: Each pattern folder contains complete implementation instructions for both n8n and Python approaches. Always refer to the specific README.md file within each pattern folder for detailed setup and configuration steps.

### For n8n Implementation
1. Navigate to the pattern folder (e.g., `PassiveGoalCreator/`)
2. Follow the n8n setup instructions in the pattern's README.md
3. Import the provided JSON workflow file
4. Configure your API keys and endpoints as specified
5. Test the workflow using the provided examples

### For Python Implementation
1. Navigate to the pattern's `Chat_Gradio/` subfolder
2. Follow the Python setup instructions in the pattern's README.md
3. Install dependencies and configure environment variables
4. Run the Gradio frontend to test the implementation
5. Explore and modify the code as needed

## 📚 Learning Path

1. **Choose your implementation approach**: Decide between n8n (no-code) or Python (code-based)
2. **Start with Passive Goal Creator**: Understand basic agentic patterns
3. **Follow the pattern-specific guide**: Each folder has detailed instructions for setup and usage
4. **Explore the implementation**: 
   - For n8n: Study the visual workflow and node configurations
   - For Python: Examine the Gradio frontend and agent logic
5. **Test and experiment**: Use the provided examples and create your own scenarios
6. **Customize and extend**: Modify patterns for your specific use cases
7. **Build your own patterns**: Use the template structure for new implementations

## 🤝 Contributing

We welcome contributions! To add a new pattern:

1. Create a new folder following the naming convention
2. Include both frontend (`Chat_Gradio/`) and workflow (`.json`) components
3. Add comprehensive documentation
4. Update this README with your pattern description
5. Submit a pull request

## 📖 Documentation

Each pattern includes:
- **Pattern README**: Detailed explanation of the specific pattern
- **Code comments**: Inline documentation for implementation details
- **Workflow documentation**: Comments within JSON configurations

## 🔧 Technical Stack

### Frontend & Demo
- **Interface**: Gradio for rapid prototyping and user interfaces
- **Backend**: Python with various AI/ML libraries
- **Dependency Management**: uv for fast and reliable Python package management

### Implementation Options
- **No-Code**: n8n automation tool for visual workflow building
- **Python Frameworks**: LangChain, LangGraph, or custom Python implementations
- **Workflow Format**: JSON configurations compatible with multiple platforms

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

If you have questions or need help:
1. Check the pattern-specific README files
2. Open an issue on GitHub
3. Join our community discussions

---

**Happy Learning!** 🚀 Dive into the world of Agentic AI and discover how autonomous agents can transform your applications.
