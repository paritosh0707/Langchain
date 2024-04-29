# Video link - https://youtu.be/XWB5DXP-DO8?feature=shared
**Introduction:**

This video lecture provides a comprehensive guide to creating APIs for deploying LangChain-based large language models (LLMs). By enabling API integration, developers can seamlessly interact with LLMs, making them accessible for a wide range of applications.

**Creating APIs with LangChain:**

1. **Introduction:**
   - APIs are essential for integrating LLMs into applications.
   - LangChain provides a component called LangServe for creating APIs.

2. **Code Structure:**
   - Create a separate folder for API development.
   - Establish a directory structure within the API folder.

3. **Library Installations:**
   - Update requirements.txt to install LangServe, FastAPI, and Uvicorn.
   - Run `pip install -r requirements.txt` to install the required libraries.

4. **App.py:**
   - Import necessary libraries (FastAPI, LangChain, Langserve).
   - Create a FastAPI application.
   - Initialize OpenAI API key from environment variables.

5. **Defining Routes:**
   - Add routes for different LLM models (e.g., ChatGPT, Llama 2).
   - Specify model and prompt templates for each route.

6. **Client.py:**
   - Import required libraries (requests, streamlit).
   - Define functions to send requests to the APIs (e.g., `get_openai_response`).
   - Create a Streamlit application for the API interface.
   - Display the API response in the Streamlit interface.

7. **Local Server:**
   - Run the API server using `python app.py`.
   - Verify the API functionality by using the `docs` endpoint to view Swagger UI documentation.

8. **Client-API Interaction:**
   - Run the client application using `streamlit run client.py`.
   - Enter text inputs and observe the corresponding LLM responses.

**Conclusion:**

By following these steps, developers can create APIs to interact with LangChain-based LLMs. This allows for the integration of these powerful language models into web applications, mobile apps, and other software solutions.