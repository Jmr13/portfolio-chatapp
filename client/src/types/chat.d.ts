export type Role = "user" | "assistant";

export interface Message {
  role: Role;
  content: string;
}

export interface ConversationRequest {
  messages: Message[];
}

export interface TimeResponse {
  location: string;
  current_time: string;
}

export interface ConversationResponse {
  current_time: string;
}
