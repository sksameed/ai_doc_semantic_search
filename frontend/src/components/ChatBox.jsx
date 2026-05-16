// TODO: Build chat interface component
import { useState } from "react";
import axios from "axios";
import Message from "./Message";

const ChatBox = () => {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);

  const askQuestion = async () => {
    if (!question) return;

    const userMessage = {
      role: "user",
      text: question
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question
        }
      );

      const botMessage = {
        role: "assistant",
        text: response.data.answer
      };
       setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Something went wrong"
        }
      ]);
    }

    setQuestion("");
  };

  return (
    <div
      style={{
        marginTop: "20px",
        padding: "20px",
        border: "1px solid #374151",
        borderRadius: "10px"
      }}
    >
      <h2>Chat With Documents</h2>

      <div>
        {messages.map((msg, index) => (
          <Message key={index} role={msg.role} text={msg.text} />
        ))}
      </div>
      <input
        type="text"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{
          width: "70%",
          padding: "10px",
          marginRight: "10px"
        }}
      />

      <button onClick={askQuestion}>Send</button>
    </div>
  );
};

export default ChatBox;