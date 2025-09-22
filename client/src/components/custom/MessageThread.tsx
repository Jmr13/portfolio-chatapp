"use client";

import { useChat } from "@/context/ChatContext";
import MessageBubble from "./MessageBubble";

export default function MessageThread() {
  const { messages } = useChat();

  return (
    <div className="w-full space-y-4 pt-10 pb-40">
      {messages.map((message, index) => (
        <MessageBubble key={index} message={message} />
      ))}
    </div>
  );
}