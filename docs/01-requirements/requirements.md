# Requirements Document

## Summary

The Personal Portfolio Chatbot is a web-based conversational application designed to provide visitors with an interactive way to learn about a candidate/applicant through an AI-powered assistant.

The system combines a **Next.js** frontend, a **FastAPI** backend, and **Azure OpenAI** to answer visitor questions. The chatbot maintains the conversation during the current browser session and can use a tool to provide a link to the applicant's resume in PDF, DOCX, or TXT format.

The application also provides a **real-time administrator communication channel** using WebSockets. Messages from connected visitors can be forwarded to the administrator when the administrator is available. The administrator can then respond directly to a specific visitor through the same real-time channel.

This functionality allows the administrator to handle and respond to visitor queries directly, without relying on the AI, whenever human intervention is needed.

Administrator access is secured through IP allowlisting and token-based authentication, ensuring that only authorized administrators can access the communication channel.

## Objective

The primary objective is to create an interactive portfolio experience that allows recruiters, hiring managers, clients, and other visitors to obtain information about the applicant without requiring them to navigate multiple portfolio pages.

## The chatbot should:

- Present the applicant's professional information conversationally.
- Answer questions from website visitors.
- Maintain context across messages within a conversation.
- Provide access to the applicant's resume/cv.
- Allow an administrator to monitor visitor conversations.
- Allow an administrator to intervene in a visitor conversation when required

## Goals
| Goal | Description |
| ---- | --- |
| G1 | Improve visitor engagement with the applicant's portfolio |
| G2 | Make professional information accessible through natural-language conversation |
| G3 | Reduce friction when recruiters want to learn about the applicant |
| G4 | Provide information regarding applicant's professional experience |
| G5 | Enable human intervention when an AI-only response is insufficient |
| G6 | Provide a visually distinctive portfolio experience |
| G7 | Protect administrator functionality from unauthorized access |

## Scope
### In Scope

The application scope includes:

- Web-based chatbot/chat interface.
- Conversation history during the active browser session.
- Administrator IP restriction & token authentication
- Responsive portfolio interface.

### Out of Scope

The application does not establish requirements for:

- User registration or login.
- Persistent user accounts.
- Database-backed conversation history.
- Analytics dashboards.
- Multiple administrator accounts.
- File uploading by visitors.
- Voice conversations.
- Image-based conversations.
- Payments.
- CRM integration.
- Automated recruitment workflows.

## MVP Definition

The Minimum Viable Product (MVP) consists of:

- Responsive and interactive portfolio website.
- AI chatbot.
- Multi-turn conversation within the active session.
- Azure OpenAI integration.
- Resume/CV retrieval using Retrieval Augmented Generation.
- Visitor/Admin WebSocket communication.
- Administrator authentication.
- Basic error handling.

## Project Requirements

### Functional Requirements

| ID | Requirement | Description |
|---|---|---|
| FR-01 | Visitor can enter a text question | The visitor can enter a question using the chatbot text input. |
| FR-02 | Visitor can submit a question | The visitor can submit a valid question and receive a response from the system. |
| FR-03 | System rejects empty messages | The system rejects messages that are empty or contain only whitespace. |
| FR-04 | System maintains current conversation context | The system maintains the current conversation context so that follow-up questions can be understood based on previous messages. |
| FR-05 | AI generates a response | The system sends valid questions to Azure OpenAI and displays the generated AI response. |
| FR-06 | AI can invoke resume retrieval | The AI can invoke the configured resume retrieval tool when a visitor requests the resume. |
| FR-07 | Resume can be requested in PDF/DOCX/TXT format | The system provides the configured resume in the supported PDF, DOCX, or TXT format when requested. |
| FR-08 | Resume link is configurable | The resume link can be changed through the `RESUME_LINK` configuration without modifying the application logic. |
| FR-09 | Visitor can maintain a WebSocket connection | A visitor can establish and maintain a WebSocket connection with the backend. |
| FR-10 | Visitor messages can be forwarded to admin | Visitor messages can be forwarded through the WebSocket connection to a connected administrator. |
| FR-11 | Admin can send messages to a specific visitor | An administrator can send a message to a specific visitor using the visitor's `client_id`. |
| FR-12 | Admin access requires token authentication | Administrator WebSocket connections require a valid `ADMIN_TOKEN` for authentication. |
| FR-13 | Admin access requires an allowed IP | Administrator WebSocket connections are accepted only when the source IP is included in `ALLOWED_ADMIN_IPS`. |
| FR-14 | UI differentiates user and AI messages | The chatbot interface visually distinguishes messages sent by the visitor from messages generated by the AI. |
| FR-15 | Send control is disabled while processing | The send control is disabled while a chatbot request is being processed to prevent duplicate submissions. |
| FR-16 | UI is responsive | The chatbot interface remains usable across different screen sizes, including mobile devices. |
| FR-17 | Interactive eye animation is displayed | The interface displays an interactive eye animation that responds to visitor mouse movement. |

### Non-Functional Requirements

| ID | Requirement | Description |
|---|---|---|
| NFR-01 | Protect sensitive configuration and credentials | Azure credentials, administrator tokens, and configuration secrets shall not be exposed to the browser and shall be stored securely on the backend. |
| NFR-02 | Maintain chatbot availability independently of administrator availability | The chatbot should remain available to visitors when the administrator is offline. Human intervention is an optional capability rather than a prerequisite for normal AI conversations. |
| NFR-03 | Provide responsive chatbot interactions | Normal chatbot requests should return within an acceptable interactive web response time, subject to Azure OpenAI latency and network conditions. |
| NFR-04 | Support an increasing number of simultaneous visitors | The system should be designed so that the number of simultaneous visitors can increase without requiring changes to the visitor-facing workflow. |
| NFR-05 | Minimize the collection and retention of visitor information | The system should minimize the collection and retention of visitor information and avoid unnecessary persistent storage of visitor conversations. |
| NFR-06 | Keep application configuration separate from source code | API endpoints, Azure credentials, resume links, administrator IPs, and administrator tokens shall remain externalized through environment configuration. |
| NFR-07 | Provide an intuitive chatbot interface | The chatbot should be understandable without requiring instructions. Visitors should immediately recognize where to type and submit a question. |

## User Roles and Permissions
| Capability | Visitor | Administrator |
|---|---|---|
| Use chatbot | ✓ | ✓ |
| Submit questions | ✓ | ✓ |
| Receive AI responses | ✓ | ✓ |
| Request resume | ✓ | ✓ |
| Connect to visitor WebSocket | ✓ | — |
| Receive visitor messages | — | ✓ |
| Send direct message to visitor | — | ✓ |
| Access admin WebSocket | — | ✓ |
| Bypass AI response | — | ✓ |