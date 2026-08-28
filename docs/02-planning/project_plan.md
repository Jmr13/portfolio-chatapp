# Project Roadmap

## Development phases

### Phase 1 — Production

| Enhancement | Status | Evidence / Notes |
|---|---|---|
| Secure WebSocket deployment using WSS | 🟡 | WebSocket endpoints exist, but no TLS/WSS configuration is present in the application code. Secure deployment would need to be handled by the deployment environment or reverse proxy. |
| Stronger authentication and authorization | 🟡 | Admin WebSocket access uses both `ALLOWED_ADMIN_IPS` and `ADMIN_TOKEN`. However, visitor WebSockets have no captcha to verify whether the visitor is authentic or a bot |
| Input validation and rate limiting | 🟡 | Pydantic validates the conversation request structure, and the frontend rejects empty/whitespace-only messages. However, there are no explicit message length/content limits and no rate-limiting mechanism. |
| Structured logging | ❌ | The application uses `print()` in the backend and `console.error()` in the frontend. No structured logging framework or centralized logging configuration is present. |
| Monitoring and alerting | ❌ | No application metrics, health monitoring, tracing, uptime monitoring, or alerting implementation is present. |
| Better API error responses | 🟡 | The backend relies on default FastAPI error handling and the frontend displays `"Error occurred"`. There are no custom error response schemas, centralized exception handlers, or actionable error messages. |
| Automated tests | ❌ | No automated test files or test implementation are included in the supplied source code. |

### Phase 2 — Portfolio Intelligence

| Enhancement | Status | Evidence / Notes |
|---|---|---|
| Centralized portfolio knowledge base | ✅ | No database but implementation of vector store/document store for centralized portfolio knowledge source is present. |
| System prompt/persona management | ❌ | `run_conversation()` sends the supplied messages directly to Azure OpenAI. There is no system message or configurable persona/system-prompt management. |
| Better resume/file management | 🟡 | A `get_resume` tool supports PDF, DOCX, and TXT, and `RESUME_LINK` is configurable through an environment variable. However, all requested versions currently use the same configured `RESUME_LINK`; there is no separate file-management system. |
| Source attribution for portfolio answers | ❌ | `ConversationResponse` contains only `message: str`. There are no source references, citations, document IDs, retrieved chunks, or attribution metadata. |

### Phase 3 — Admin Experience

| Enhancement | Status | Evidence / Notes |
|---|---|---|
| Dedicated administrator dashboard | ❌ | No administrator dashboard, or admin page is present in the supplied Next.js source code. Only the template which was written in pure HTML |
| Visitor/session list | 🟡 | `ConnectionManager` maintains `user_connections: Dict[int, WebSocket]`, which provides in-memory tracking of connected visitors. However, there is no admin API or dashboard for viewing the visitor/session list. |
| Conversation history | ❌ | Conversation history is maintained only in the frontend `ChatContext` during the active browser session. There is no server-side or database persistence. Both visitor and admin can have the history of conversation by providing their email |
| Online/offline indicators | 🟡 | The backend can detect WebSocket connections and disconnections through `connect_user()` and `disconnect_user()`, but no visitor/admin online/offline indicator is exposed in a UI. |
| Human takeover mode | 🟡 | The admin can send messages directly to a visitor through `send_to_user()`, but there is no persistent takeover state or mechanism that prevents subsequent visitor messages from being processed by the AI. |
| Admin notifications | 🟡 | Visitor messages are forwarded to the connected administrator through WebSocket, but there is no browser notification, push notification, or notification management system. |

### Phase 4 — Analytics

| Enhancement | Status | Evidence / Notes |
|---|---|---|
| Visitor count | ❌ | No persistent visitor counter, analytics event tracking, or visitor statistics implementation is present. |
| Most frequently asked questions | ❌ | Conversations are not persisted or aggregated, so there is no mechanism for calculating frequently asked questions. |
| Resume-request count | ❌ | The `get_resume` tool exists, but tool calls are not recorded or counted for analytics purposes. |
| Conversation completion rate | ❌ | There is no conversation-completion definition, tracking mechanism, or analytics calculation. |
| AI vs. human intervention rate | ❌ | There is no tracking of AI responses versus administrator interventions or takeover events. |
| Response latency | ❌ | No request timing, response-latency measurement, or performance metrics are recorded. |
| Error rate | ❌ | Errors are surfaced through exceptions, `console.error()`, or `print()`, but no error events are persisted or aggregated into an error-rate metric. |