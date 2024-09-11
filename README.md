# 🌟 Summarizer App for YouTube & Websites 🌟

This **Summarizer App** allows you to generate concise summaries from YouTube videos and website URLs in just a few clicks! Using powerful LLMs and LangChain, the app extracts key points, topics, and conclusions to provide a clear, concise overview of the content.

---

## 🚀 Features

- 🌐 **Summarize Web Pages:** Input any website URL and get a short, precise summary.
- 🎥 **Summarize YouTube Videos:** Extract key takeaways from YouTube videos with ease.
- 🤖 **Powered by Groq & LangChain:** Utilizes the **ChatGroq** model with LangChain for accurate and efficient text summarization.
- 🖼️ **Streamlit Interface:** Simple and user-friendly UI for quick interaction.

---

## 🛠️ Tech Stack

- **Streamlit**: Frontend UI for interacting with the app.
- **LangChain**: Framework for building applications with LLMs.
- **ChatGroq**: The model for generating summaries.
- **YouTubeLoader & UnstructuredURLLoader**: Fetches data from YouTube videos and web pages.
- **Python**: Core language for the project.

---

## 📝 How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Khatri4/summarizer-app.git
   cd summarizer-app
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file**:

   Create a `.env` file in the root of your project and add your **Groq API Key**:
   ```bash
   GROQ_API_KEY=your-groq-api-key
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

5. **Input your URL** and click "Summarize" to get an overview of any YouTube video or website content.

---

## ⚙️ Configuration

Ensure you add your **Groq API Key** in the `.env` file:
```bash
GROQ_API_KEY=your-groq-api-key
```
This API key is required for the app to interact with the Groq model.

---

## 💡 Example

- Input a YouTube URL or any website URL to get the key takeaways summarized in under 400 words.
- The app will handle both YouTube video content and regular web page text!

---

## 📦 Dependencies

- `streamlit`
- `langchain`
- `langchain_community`
- `groq`
- `validators`
- `dotenv`
- `langchain_groq`

Install all dependencies using:
```bash
pip install -r requirements.txt
```
---

Enjoy the Summarizer App! 😊
