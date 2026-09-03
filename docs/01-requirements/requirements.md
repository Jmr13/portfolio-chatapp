# Requirements Document

## Summary

The Personal Portfolio Chatbot is a web-based conversational application designed to provide visitors with an interactive way to learn about a candidate/applicant through an AI-powered assistant.

The system combines a **Next.js** frontend, a **FastAPI** backend, and **Azure OpenAI** to answer visitor questions. Visitor messages remain available when the visitor revisits the page after at least one hour, and the chatbot can use a tool to provide the configured resume link for a requested PDF, DOCX, or TXT version.

The application also provides a **real-time administrator communication channel** using WebSockets. Messages from connected visitors can be forwarded to the administrator when the administrator is available. The administrator can then respond directly to a specific visitor through the same real-time channel.

This functionality allows the administrator to handle and respond to visitor queries directly, without relying on the AI, whenever human intervention is needed.

Administrator access is intended to be controlled through IP allowlisting and token-based authentication. The deployed admin page communicates with the production backend through HTTPS/REST APIs, and administrator credentials originate from backend `.env` configuration without being exposed to visitors.

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
- Conversation history available when the visitor revisits the page after at least one hour.
- Administrator IP restriction and token authentication.
- Responsive portfolio interface.

### Out of Scope

The application does not establish requirements for:

- User registration or login.
- Persistent user accounts.
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
- Multi-turn conversation with messages retained for at least one hour.
- Azure OpenAI integration.
- Resume/CV link retrieval using the configured resume tool.
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
| FR-04 | System maintains conversation context across a revisit | The system retains conversation messages so that the visitor can revisit the page after at least one hour and continue the conversation context. |
| FR-05 | AI generates a response | The system sends valid questions to Azure OpenAI and displays the generated AI response. |
| FR-06 | AI can invoke resume retrieval | The AI can invoke the configured resume retrieval tool when a visitor requests the resume. |
| FR-07 | Resume link can be requested by format | The system accepts `pdf`, `docx`, or `txt` as the requested resume version and returns the configured resume link. Separate links for each format are not currently specified. |
| FR-08 | Resume link is configurable | The resume link can be changed through the `RESUME_LINK` configuration without modifying the application logic. |
| FR-09 | Visitor can maintain a WebSocket connection | A visitor can establish and maintain a WebSocket connection with the backend. |
| FR-10 | Visitor messages can be forwarded to admin | Visitor messages can be forwarded through the WebSocket connection to a connected administrator. |
| FR-11 | Admin can take over a visitor conversation | An administrator can send a message to a specific visitor using the visitor's `client_id`; when the administrator enters the session, subsequent AI processing for that visitor session stops immediately. This takeover behavior is planned and is not currently implemented. |
| FR-12 | Admin access requires token authentication | Administrator WebSocket connections require a valid `ADMIN_TOKEN` for authentication. |
| FR-13 | Admin access requires an allowed IP | Administrator WebSocket connections are accepted only when the source IP is included in `ALLOWED_ADMIN_IPS`. |
| FR-14 | UI differentiates user and AI messages | The chatbot interface visually distinguishes messages sent by the visitor from messages generated by the AI. |
| FR-15 | Send control is disabled while processing | The send control is disabled while a chatbot request is being processed to prevent duplicate submissions. |
| FR-16 | UI is responsive | The chatbot interface remains usable across different screen sizes, including mobile devices. |
| FR-17 | Interactive eye animation is displayed | The interface displays an interactive eye animation that responds to visitor mouse movement. |
| FR-18 | AI session end prompts for email | When an AI chat session ends, the system asks the visitor for their email address. This is planned and is not currently implemented. |
| FR-19 | Admin can end a conversation | When an administrator ends an active conversation using the end-conversation control, the system stops the conversation and asks the visitor for their email address. This is planned and is not currently implemented. |

### Non-Functional Requirements

| ID | Requirement | Description |
|---|---|---|
| NFR-01 | Protect sensitive configuration and credentials | Azure credentials, administrator tokens, and configuration secrets shall not be exposed to the browser and shall be stored securely on the backend. |
| NFR-02 | Maintain chatbot availability independently of administrator availability | The chatbot should remain available to visitors when the administrator is offline. Human intervention is an optional capability rather than a prerequisite for normal AI conversations. |
| NFR-03 | Return chatbot responses without a fixed response-time target | The system shall process valid chatbot requests and return a response when the backend and Azure OpenAI service are available. No maximum response-time target is specified. |
| NFR-04 | Use a single backend process | The deployment shall use one backend process. No simultaneous visitor capacity target or requirement for multiple backend processes or instances is specified. |
| NFR-05 | Retain visitor messages for the defined user experience | Visitor messages shall remain available when the visitor revisits the page after at least one hour, while retention beyond that period and operational-log retention remain unspecified. |
| NFR-06 | Keep application configuration separate from source code | API endpoints, Azure credentials, resume links, administrator IPs, and administrator tokens shall remain externalized through environment configuration. |
| NFR-07 | Provide an intuitive chatbot interface | The chatbot should be understandable without requiring instructions. Visitors should immediately recognize where to type and submit a question. |

## Acceptance Criteria and Confirmed Decisions

The scenarios in `docs/05-testing/test_cases.md` define the current functional verification cases for FR-01 through FR-17. The following items are now confirmed by the resolved assumptions in `docs/01-requirements/assumptions_and_open_questions.md` and should be treated as target-state requirements rather than as unresolved debates:

- **NFR-03:** Given a valid chatbot request and an available backend and Azure OpenAI service, when the request is processed, then the system returns a chatbot response. No maximum response-time target is specified.
- **FR-04 / NFR-05:** Visitor chat history is expected to remain available after a one-hour revisit using browser storage with a one-hour expiry window. The current implementation does not yet provide this persistence path.
- **FR-07:** The resume tool accepts `pdf`, `docx`, and `txt`, but it currently returns the same configured `RESUME_LINK` for each format. Format-specific file selection remains a future enhancement.
- **FR-11 / NFR-02:** Admin takeover is a confirmed planned behavior in which the admin enters the visitor session and stops subsequent AI processing for that visitor. The current implementation does not yet maintain takeover state or route messages away from the AI.
- **FR-18 / FR-19:** End-of-session email prompts are planned future behaviors, not currently implemented in the repository.
- **NFR-01 / NFR-06 / D-10:** Credentials and admin configuration remain backend-only and come from environment variables. The prototype demonstrates the access pattern but does not yet implement the final protected admin delivery model.
- **FR-12 / FR-13 / D-08:** Administrator authentication and IP allowlisting remain required. The production admin design uses HTTPS/REST access, while the current prototype uses WebSockets and requires migration.

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