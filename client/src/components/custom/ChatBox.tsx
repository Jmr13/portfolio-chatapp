"use client";

import { useState, FormEvent, ChangeEvent } from "react";
import type { Message, ConversationResponse } from "@/types/chat";
import { sendMessage } from "@/actions/chat";
import { useChat } from "@/context/ChatContext";

import { SendHorizontal } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

export default function ChatBox() {
  const { messages, addMessage } = useChat();
  const [input, setInput] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  const resetInput = () => setInput("");
  
  const appendUserMessage = (content: string) => {
    const msg: Message = { role: "user", content };
    addMessage(msg);
    return msg;
  };

  const appendAssistantMessage = (content: string) => {
    const msg: Message = { role: "assistant", content };
    addMessage(msg);
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const trimmed = input.trim();
    if (trimmed === "") {
      return;
    }

    resetInput();
    setLoading(true);

    const userMsg = appendUserMessage(trimmed);

    try {
      const result: ConversationResponse = await sendMessage({
        messages: [...messages, userMsg]
      });
      appendAssistantMessage(result.current_time);
    } 
    catch (error) {
      console.error("Error sending to API", error);
      appendAssistantMessage("Error occurred");
    } 
    finally {
      setLoading(false);
    }
  };

  return (
    <>
      <form
        onSubmit={handleSubmit}
        className="fixed bottom-0 w-10/12 md:w-1/2 bg-white border border-black text-black rounded-2xl px-4 py-2 place-self-center mb-4 z-10"
      >
        <Textarea
          placeholder="Ask me anything"
          value={input}
          onChange={(e: ChangeEvent<HTMLTextAreaElement>) =>
            setInput(e.target.value)
          }
          className="w-full border-0 resize-none focus:ring-0 focus-visible:ring-0 focus:outline-none shadow-none"
        />
        <div className="flex justify-end">
          <Button
            variant="ghost"
            size="icon"
            className="cursor-pointer size-8"
            disabled={loading}
          >
            <SendHorizontal />
          </Button>
        </div>
      </form>
    </>
  );
}