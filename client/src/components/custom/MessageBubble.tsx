"use client";

import { Message } from "@/types/chat";

interface MessageBubbleProps {
  message: Message;
}

export default function MessageBubble({ message }: MessageBubbleProps) {
  const isUserMessage = message.role === "user";

  return (
    <div className={`flex ${isUserMessage ? "justify-end" : "justify-start"}`}>
      <div
        className={`border px-4 py-2 rounded-lg max-w-xs text-sm ${isUserMessage
          ? "bg-black text-white"
          : "bg-white text-black"
          }`}
      >
        {message.content}
      </div>
    </div>
  );
}