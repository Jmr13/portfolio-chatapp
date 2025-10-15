export type Role = "user" | "assistant";

export interface Message {
  role: Role;
  content: string;
}

export interface ConversationRequest {
  messages: Message[];
}

export interface ConversationResponse {
  message: string;
}
