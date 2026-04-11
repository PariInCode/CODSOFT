const express = require('express');
const app = express();

app.set('view engine','ejs');
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({extended:true}));

const { getResponse} = require('./chatbot')

app.get('/', (req, res) => {
    
    res.render('chatbot',{ messages: [] });
});
app.post('/chatbot', (req, res) => {
    
    const userMesssage = req.body.message || "";
    const botreply = getResponse(userMesssage)
    res.json({ reply: botreply });
});

app.listen(4000, () => {
    console.log("Server running on http://localhost:4000");
});