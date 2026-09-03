# Project Roadmap

This roadmap distinguishes the current implementation status from the target-state requirements. The repository contains a working prototype, while the production-level requirements and open decisions remain documented in the requirement and design artifacts. A snapshot of the current prototype state is recorded in `current_state_snapshot.md`.

Evidence note: the roadmap is based on verified repository implementation as of the current workspace state and should not be read as a production release commitment. Items marked as future work, planned behavior, or prototype-only remain unimplemented and should be treated as pending scope rather than shipped functionality.

All of the previously open assumptions have now been answered and reflected in the requirements, design, and planning records. The project plan therefore treats the current workspace as a prototype with a defined production target, rather than as a completed release candidate.

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
| Centralized portfolio knowledge base | ❌ | No confirmed database or vector-store implementation is present in the current repository; this remains a planned knowledge-base capability. |
| System prompt/persona management | ❌ | `run_conversation()` sends the supplied messages directly to Azure OpenAI. There is no system message or configurable persona/system-prompt management. |
| Better resume/file management | 🟡 | A `get_resume` tool supports PDF, DOCX, and TXT, and `RESUME_LINK` is configurable through an environment variable. All requested versions currently use the same configured `RESUME_LINK`; selecting separate files by format is a confirmed future feature. |
| Source attribution for portfolio answers | ❌ | `ConversationResponse` contains only `message: str`. There are no source references, citations, document IDs, retrieved chunks, or attribution metadata. |

### Phase 3 — Admin Experience

| Enhancement | Status | Evidence / Notes |
|---|---|---|
| Dedicated administrator dashboard | 🟡 | `client/public/templates/admin.html` is the confirmed prototype basis for the future administrator UI and WebSocket logic. A production dashboard and protected delivery mechanism are not yet implemented. |
| Visitor/session list | 🟡 | `ConnectionManager` maintains `user_connections: Dict[int, WebSocket]`, which provides in-memory tracking of connected visitors. However, there is no admin API or dashboard for viewing the visitor/session list. |
| Conversation history | ❌ | Conversation history is maintained only in the frontend `ChatContext` during the active browser session. There is no server-side or database persistence, and no email-based history retrieval is implemented. |
| Online/offline indicators | 🟡 | The backend can detect WebSocket connections and disconnections through `connect_user()` and `disconnect_user()`, but no visitor/admin online/offline indicator is exposed in a UI. |
| Human takeover mode | 🟡 | The confirmed future behavior is for admin entry to immediately stop subsequent AI processing for that visitor session. The admin can currently send direct messages through `send_to_user()`, but no takeover state, end-conversation control, or AI-routing bypass is implemented. |
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