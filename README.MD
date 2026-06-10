# Computing Historian AI Agent

An AI-powered agent specialising in the history of computing and artificial intelligence, built as part of the **Microsoft Learn Skills Fest 2026**.

## Project Overview

This project demonstrates the end-to-end development and deployment of a custom AI agent using Microsoft Azure AI Foundry. The agent is designed to answer questions about significant people, events, and milestones in computing history, including pioneers like Alan Turing and Grace Hopper, early machines like the ENIAC, and the evolution of AI over time.

## Technologies Used

- **Azure AI Foundry** — agent creation, system prompt configuration, and model deployment
- **Python** — agent interaction via the Azure AI Projects SDK
- **Azure AI Projects SDK** — programmatic access to the deployed agent
- **Azure Identity** — credential management and authentication
- **Flask** — lightweight web application frontend
- **Visual Studio Code** — development environment

## Features

- Custom system prompt restricting the agent to computing history topics
- Interactive command-line loop for multi-turn conversations
- Flask web UI for browser-based interaction
- Azure credential authentication via DefaultAzureCredential

## Setup

1. Clone this repository
2. Create a virtual environment and install dependencies:
```bash
   pip install azure-ai-projects azure-identity openai
```
3. Create a `.env` file in the project root with the following:
AGENT_ENDPOINT=your-azure-endpoint-here
AGENT_NAME=computing-historian
AGENT_VERSION=1

4. Authenticate with Azure:
```bash
   az login
```
5. Run the agent:
```bash
   python agent.py
```

## What I Learned

- Deploying and configuring AI agents in Azure AI Foundry
- Connecting a Python application to a cloud-hosted AI agent via SDK
- Debugging Azure authentication and deployment errors
- Building a Flask web interface to front an AI backend
- Using Git and GitHub for version control of an AI project

## Acknowledgements

Built as part of the Microsoft Learn Skills Fest 2026 programme.