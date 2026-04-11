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