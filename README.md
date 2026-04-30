# 🤖 Rule-Based Chatbot

A simple rule-based chatbot built with **Node.js**, **Express.js**, and **EJS**. It responds to user messages using keyword pattern matching — no AI or machine learning involved. Built as **Task 1** of the CodSoft Artificial Intelligence Internship.

---

## 📁 Project Structure

```
Task1_chatbot/
├── views/
│   └── chatbot.ejs       # Frontend chat UI
├── public/
│   └── style.css         # Styling
├── app.js                # Express server
├── chatbot.js            # Chatbot logic (pattern matching)
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. User types a message in the browser
2. The frontend sends a POST request to `/chatbot` with the message
3. Express receives it and passes it to `chatbot.js`
4. `chatbot.js` normalizes the input (lowercase + trim) and matches it against predefined keywords
5. The matching response is sent back as JSON
6. The frontend displays the reply in the chat UI

---

## 🧠 Concepts Used

- **Rule-based responses** — if/else pattern matching on user input
- **Natural Language Processing (basic)** — keyword detection, input normalization
- **REST API** — POST route handling with Express
- **EJS templating** — server-side rendered frontend
- **Async/Await + Fetch API** — for sending and receiving messages without page reload

---

## 🚀 Getting Started

### Prerequisites
- Node.js installed
- npm installed
- nodemon installed

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/CODSOFT.git

# Navigate to the project folder
cd CODSOFT/Task1_chatbot

# Install dependencies
npm install
```

### Run the App

```bash
node app.js
```

Open your browser and go to:
```
http://localhost:4000
```

---

## 💬 Supported Commands

| User Input | Bot Response |
|---|---|
| hi / hello / hey | Greeting response |
| your name / who are you | Bot introduction |
| how are you | Status response |
| help / what can you do | Lists capabilities |
| joke | Random joke |
| time | Current time |
| date / today | Current date |
| bye / goodbye | Farewell message |
| thank / thanks | Acknowledgement |
| anything else | Default fallback |

---

## 🛠️ Built With

- [Node.js](https://nodejs.org/)
- [Express.js](https://expressjs.com/)
- [EJS](https://ejs.co/)

---

## 👩‍💻 Author

Made with ❤️ as part of the **CodSoft AI Internship — Task 1**




# 🎮 Tic Tac Toe AI 🤖

A smart and interactive **Tic Tac Toe Game** built using **Python** and **Tkinter GUI**, powered by the **Minimax Algorithm** to make the AI player unbeatable.

> Play against the computer if you dare 😈  
> The AI never loses.

---

## 🚀 Features

✅ Beautiful GUI using Tkinter  
✅ Human vs AI Gameplay  
✅ Unbeatable AI using Minimax Algorithm  
✅ Instant Win / Draw Detection  
✅ Restart Game Button  
✅ Smooth and Beginner-Friendly Code Structure  

---

## 🧠 AI Logic Used

This project uses the famous **Minimax Algorithm**, a decision-making algorithm used in:

- Chess Engines ♟️  
- Tic Tac Toe 🎮  
- Game Theory 🤖  
- Artificial Intelligence Systems

The AI checks every possible future move and always chooses the best one.

---

## 🖥️ Tech Stack

- **Python 3**
- **Tkinter** (for GUI)
- **Minimax Algorithm**

---

## 📂 Project Structure

```bash
TicTacToeAI/
│── tic_tac_toe.py          # Console Version
│── tic_tac_toe_gui.py      # GUI Version
│── README.md



# 📚 Book Recommendation AI

A premium **Book Recommendation Web App** built using **Python, Flask, Pandas, and Scikit-learn**.
Users can search for a book title and get smart recommendations with book covers and buy links.

---

## 🚀 Features

✅ Book recommendation system using Machine Learning
✅ Search by book title
✅ Similar books suggested instantly
✅ Premium dark UI design
✅ Book cover images
✅ Buy links for each recommended book
✅ Fast and lightweight Flask web app

---

## 🧠 Tech Stack

* **Python**
* **Flask**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **HTML**
* **CSS**

---

## 📂 Project Structure

```bash
Book-Recommender/
│── app.py
│── books.csv
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ How It Works

1. Dataset of books is loaded using Pandas
2. Author + Genre are combined as features
3. CountVectorizer converts text into numbers
4. Cosine Similarity finds similar books
5. Flask displays recommendations on website

---

## ▶️ Installation

### 1. Clone project

```bash
git clone <your-repo-link>
cd Book-Recommender
```

### 2. Install libraries

```bash
pip install flask pandas numpy scikit-learn
```

### 3. Run project

```bash
python app.py
```

### 4. Open browser

```text
http://127.0.0.1:5000
```

---

## 🔍 Example Search

Input:

```text
Harry Potter
```

Output:

* Percy Jackson
* Hobbit
* Narnia
* Eragon

---



## 💡 Future Improvements

* Login system
* Save favorite books
* Voice search
* Real 10k+ dataset
* Deploy online
* Personalized recommendations

---

## 📌 Resume Description

Built an AI-powered Book Recommendation System using Python, Flask, Pandas, and Machine Learning that recommends similar books based on title, genre, and author with an interactive web interface.

---

## 👨‍💻 Author

Made by **INCODEUSER**

---

## ⭐ If you like this project, give it a star on GitHub!
