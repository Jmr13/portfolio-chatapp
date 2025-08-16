import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { SendHorizontal } from "lucide-react";
import EyeWatch from "@/components/custom/EyeWatch";
import MessageThread from "@/components/custom/MessageThread";
import ChatBox from "@/components/custom/ChatBox";

export default function Home() {
  return (
    <>
      <div className="h-screen w-full md:w-1/2 flex flex-col items-center place-self-center space-y-4 p-4 md:p-0 py-4">
        <EyeWatch />
        <MessageThread />
      </div>
      <ChatBox />
    </>
  );
}