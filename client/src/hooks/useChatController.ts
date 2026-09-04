"use client";

import { useState, type ChangeEvent, type FormEvent } from "react";
import type { Message } from "@/types/chat";
import { sendMessage } from "@/actions/conversation";
import { useChat } from "@/context/ChatContext";

interface ChatController {
    input: string;
    loading: boolean;
    setInput: (event: ChangeEvent<HTMLTextAreaElement>) => void;
    handleSubmit: (event: FormEvent<HTMLFormElement>) => Promise<void>;
}

export function useChatController(): ChatController {
    const { messages, addMessage } = useChat();
    const [input, setInputValue] = useState("");
    const [loading, setLoading] = useState(false);

    const setInput = (event: ChangeEvent<HTMLTextAreaElement>) => {
        setInputValue(event.target.value);
    };

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const trimmed = input.trim();
        if (trimmed === "" || loading) {
            return;
        }

        const userMessage: Message = { role: "user", content: trimmed };
        const conversation = [...messages, userMessage];

        setInputValue("");
        setLoading(true);
        addMessage(userMessage);

        try {
            const result = await sendMessage({ messages: conversation });
            addMessage({ role: "assistant", content: result.message });
        } catch (error) {
            console.error("Error sending to API", error);
            addMessage({ role: "assistant", content: "Error occurred" });
        } finally {
            setLoading(false);
        }
    };

    return { input, loading, setInput, handleSubmit };
}
