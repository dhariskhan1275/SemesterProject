# ✨ E-Commerce Amazon Electronics Chatbot

Welcome to the **E-Commerce Amazon Electronics Chatbot** project! This semester-long collaborative project showcases a cutting-edge AI-powered chatbot that enhances customer support for an e-commerce platform, specifically in the electronics domain.

## 🏗️ Project Overview

This project combines the power of AI and natural language processing to create a chatbot that can:
- Answer customer queries about products, policies, and more.
- Retrieve and present relevant data using similarity-based searches.
- Respond dynamically with rich, conversational text using Gradio.

## 👥 Team Contributions

This project is a result of teamwork and collaboration:
- **Backend Development:** Muhammad Haris
- **Frontend Development:** Noman Ali Tasawer
- **Data Collection and Generation:** Hizbullah

## 🔧 Features
- **Smart Retrieval:** Uses OpenAI embeddings with Chroma for similarity-based search.
- **Interactive Frontend:** A beautiful, user-friendly interface designed with Gradio.
- **Context-Aware Responses:** Answers questions based on provided data only.
- **Custom Styling:** Aesthetic gradients for user and bot messages.

## 🛠️ Technologies Used
- **Python**
- **LangChain**
- **ChromaDB**
- **OpenAI (GPT-4o-mini)**
- **Gradio**
- **PyPDF**
- **MongoDB**

## 📂 Project Structure
```
myenv Data
├── chromadb/               # Persistent vectorstore data
├── main.py                # Frontend and Gradio integration
├── backend.py             # Backend logic for the chatbot
├── requirements.txt       # Dependencies
├── .env                   # Environment variables
├── Data/                  # PDF files for chatbot data
└── README.md              # Project documentation
```

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ecommerce-chatbot.git
cd ecommerce-chatbot
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Prepare the Environment
Create a `.env` file to store your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the Chatbot
To start the chatbot, execute:
```bash
python main.py
```
The Gradio interface will be accessible at `http://localhost:7860`.

## 📊 Data Sources
The chatbot is powered by PDF documents stored in the `Data/` folder. These documents are split into chunks and embedded for efficient retrieval.

## 🎨 Custom Styling
- **User Messages:** Gradient background from orange to red.
- **Bot Messages:** Gradient background from blue to violet.
- **Enhanced UI:** Styled using custom CSS and Gradio themes.

## 🚀 Deployment
This chatbot can be deployed using platforms like Hugging Face. Set up the environment and dependencies, then upload your files to Hugging Face Spaces for public access.

## 🤝 Acknowledgments
This project was completed as part of our **7th Semester Computer Science Project** at UET Peshawar. We extend our gratitude to our advisors and peers for their guidance and support.

## 📝 License
This project is open-source and available under the MIT License.

## 💬 Feedback
Feel free to open issues or create pull requests for any suggestions or improvements!

---

### ⭐ Give this repository a star if you found it helpful!

---

**Authors:**
- Muhammad Haris ([GitHub](https://github.com/dhariskhan1275))  
- Noman Ali Tasawer
- Hizbullah
