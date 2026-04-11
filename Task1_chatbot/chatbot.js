// chatbot.js
function getResponse(message) {
  const msg = message.toLowerCase().trim();

  // Greetings
  if (msg.includes("hello") || msg.includes("hi") || msg.includes("hey")) {
    return "Hey there! 👋 How can I help you today?";
  }

  // Name
  if (msg.includes("your name") || msg.includes("who are you")) {
    return "I'm a simple rule-based chatbot built with Express.js!";
  }

  // How are you
  if (msg.includes("how are you") || msg.includes("how r u")) {
    return "I'm just a bot, but I'm doing great! How about you?";
  }

  // Help
  if (msg.includes("help") || msg.includes("what can you do")) {
    return "I can answer basic questions! Try asking: who are you, tell me a joke, what time is it, or say bye!";
  }

  // Joke
  if (msg.includes("joke")) {
    const jokes = [
      "Why don't scientists trust atoms? Because they make up everything!",
      "Why did the developer go broke? Because he used up all his cache!",
      "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads."
    ];
    return jokes[Math.floor(Math.random() * jokes.length)];
  }

  // Time
  if (msg.includes("time")) {
    return `Current time is: ${new Date().toLocaleTimeString()}`;
  }

  // Date
  if (msg.includes("date") || msg.includes("today")) {
    return `Today is: ${new Date().toLocaleDateString()}`;
  }

  // Goodbye
  if (msg.includes("bye") || msg.includes("goodbye") || msg.includes("see you")) {
    return "Goodbye! Have a great day! 👋";
  }

  // Thanks
  if (msg.includes("thank")) {
    return "You're welcome! 😊";
  }

  // Default fallback
  return "Hmm, I didn't understand that. Try asking for help, a joke, or say hi!";
}

module.exports = { getResponse };