"use server";

import type { ConversationRequest, ConversationResponse } from "@/types/chat";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export async function sendMessage(
  requestBody: ConversationRequest
): Promise<ConversationResponse> {

  if (!API_BASE_URL) {
    throw new Error("API base URL is not defined in the environment variables");
  }

  const response = await fetch(`${API_BASE_URL}/conversation/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(requestBody),
  });

  if (!response.ok) {
    throw new Error(`API responded with status ${response.status}`);
  }

  const json = await response.json();

  return json;
}