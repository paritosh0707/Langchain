# Video Link - https://youtu.be/5CJA1Hbutqc?feature=shared
**Introduction:**

This video tutorial covers the creation of chatbot applications using both paid language AI (LLM) APIs and open-source LLMs, focusing on the integration with the Langchain ecosystem.

**Prerequisites:**

* Python environment with version 3.9 or higher
* Understanding of Langchain and the basics of LLMs
* Knowledge of streamlit

**Creating a Chatbot Application with OpenAI API:**

1. **Environment Setup:**
   * Create a new virtual environment and install the required dependencies.
   * Set environment variables for OpenAI API key, Langchain project key, and project name.

2. **Code Implementation:**
   * Import necessary libraries: Langchain core, prompt templates, output parsers, streamlit, OS, environment variables.
   * Define prompt template with system and user prompts.
   * Create a streamlit framework with title, text input, and OpenAI LLM call.
   * Combine prompt, LLM, and output parser into a chain.
   * Run the application and provide user input to get responses from OpenAI.

**Monitoring with Langchain Tracking:**

* Background: Langchain introduces a new feature called "tracing" for monitoring API calls and model performance.
* Implementation: Disable tracing by setting Langchain_TRACING environment variable to "false" for local development.

**Creating a Chatbot Application with Open-Source LLM (via Llama):**

1. **LLlama Installation and Configuration:**
   * Download and install Llama (Large Language Model Access).
   * Import necessary libraries: Langchain core, prompt templates, output parsers, streamlit, OS, environment variables, Langchain Community.
   * Use Langchain Community to integrate Llama models.

2. **Code Implementation:**
   * Replace OpenAI API call with Llama call.
   * Download the desired model (e.g., Llama 2) using "Ollama run Llama2" command.
   * Run the application and provide user input to get responses from the open-source LLM.

**Tracking with Llama:**

* Background: Llama provides its own monitoring capabilities.
* Implementation: Monitor Llama requests and model performance within the Langchain dashboard.

**Conclusion:**

* Summary of the two methods for creating chatbot applications with LLMs.
* Emphasis on the benefits of Langchain's ecosystem and the versatility of using both paid and open-source models.