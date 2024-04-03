import React, { useState } from "react";
import axios from "axios";
import { FaRobot } from "react-icons/fa"; // Bot icon
import { FaUser } from "react-icons/fa"; // User icon

const Ui = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    const userMessage = document.getElementById("userInput").value;
    document.getElementById("userInput").value = "";

    setMessages([...messages, { text: userMessage, sender: "user" }]);

    // Send the userMessage to your Flask backend
    const response = await axios.post(' http://127.0.0.1:5000/api/chat', {
      text: userMessage
    });

    const botResponse = response.data.message;

    // Add the bot's response to the messages
    setMessages([...messages, { text: userMessage, sender: "user" }, { text: botResponse, sender: "bot" }]);
  }

  return (
    <div className="m-12 bg-black  shadow-slate-600" >
      <h1 className="text-blue-500 text-3xl mb-4 font-bold">Diabetes Detection Chatbot</h1>
      <div id="chatbox" className="h-96 border-2 border-black p-4 overflow-y-scroll mb-4">
        {messages.map((message, index) => (
          <div key={index} className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`rounded-lg px-4 py-2 ${message.sender === 'user' ? 'bg-green-500 text-white' : 'bg-red-500 text-white'}`}>
              {message.sender === 'user' ? <FaUser /> : <FaRobot />}
              {message.text}
            </div>
          </div>
        ))}
      </div>
      <input id="userInput" type="text" className="w-full mb-4 p-2 border-2 border-gray-300" />
      <button onClick={handleSend} className="w-full py-2 bg-blue-500 text-white">Send</button>
    </div>
  );
};

export default Ui;
