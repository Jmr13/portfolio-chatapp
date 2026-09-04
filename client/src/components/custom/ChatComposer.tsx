"use client";

import { SendHorizontal } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { useChatController } from "@/hooks/useChatController";

export default function ChatComposer() {
    const { input, loading, setInput, handleSubmit } = useChatController();

    return (
        <form
            onSubmit={handleSubmit}
            className="fixed bottom-0 w-10/12 md:w-1/2 bg-white border border-black text-black rounded-2xl px-4 py-2 place-self-center mb-4 z-10"
        >
            <Textarea
                placeholder="Ask me anything"
                value={input}
                onChange={setInput}
                disabled={loading}
                className="w-full border-0 resize-none focus:ring-0 focus-visible:ring-0 focus:outline-none shadow-none"
            />
            <div className="flex justify-end">
                <Button
                    type="submit"
                    variant="ghost"
                    size="icon"
                    className="cursor-pointer size-8"
                    disabled={loading}
                    aria-label="Send message"
                >
                    <SendHorizontal />
                </Button>
            </div>
        </form>
    );
}