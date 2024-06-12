# NL2SQL and RAG Chatbot Application

Welcome to the NL2SQL and Retrieval Augmented Generation (RAG) Chatbot application! This project revolutionizes the way we interact with databases by combining Natural Language Processing (NLP) with powerful language models and vector databases. Users can query databases using natural language and receive intuitive responses, making complex data interactions accessible to everyone.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Live Demo](#live-demo)

## Introduction

This application leverages advanced NLP techniques to translate natural language queries into SQL commands and retrieve relevant data. By integrating LangChain, HuggingFace, FAISS, and OpenAI, we have created a seamless and efficient system for database querying and data retrieval.

## Features

- **Natural Language to SQL (NL2SQL):** Translates user queries into SQL commands.
- **Retrieval Augmented Generation (RAG):** Enhances data retrieval and response generation using vector databases and LLMs.
- **Dynamic Few-Shot Learning:** Adapts model responses based on context-specific examples.
- **Context-Aware Table Selection:** Ensures precise and relevant query handling.
- **Conversational Memory:** Retains context to handle follow-up questions efficiently.
- **Advanced Prompt Engineering:** Utilizes techniques like Self-Refine and Chain-of-Thought for optimized model outputs.

## Installation

To set up the application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hiteshpatil237/sqlangchain.git
   cd sqlangchain

2. **Install the required packages:**
   ```bash
   pip install langchain_openai langchain_community langchain pymysql chromadb faiss-cpu

3. **Set up environment variables:**
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   export DB_USER='your_db_user'
   export DB_PASSWORD='your_db_password'
   export DB_HOST='your_db_host'
   export DB_NAME='your_db_name'

## Usage

1. **Run Application:**
   ```bash
   streamlit run main.py

## Technologies Used

1. **LangChain**: Framework for natural language and SQL integration.
2. **OpenAI**: Large language models for natural language understanding and generation.
3. **HuggingFace Sentence Transformers** Sentence Transformer: For generating embeddings.
4. **FAISS**: For efficient similarity searches in vector databases.
5. **Python**: Programming language for building the application.

## Live Demo

**This app is hosted on**: https://sqlangchain.streamlit.app/
