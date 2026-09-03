# Current State Snapshot

## Purpose

This document records the implementation status of the portfolio chat application as it exists in the current repository. It is intended to distinguish evidence-backed behaviors from planned requirements and future enhancements.

## Confirmed implementation status

### Frontend

- The client is implemented with Next.js and React.
- The chat experience uses a browser-side `ChatContext` to store active-message state in memory.
- The interface supports a basic visitor message flow: a visitor types a message, the message is added to the local session state, and the UI renders the conversation.
- The active message state is ephemeral; it is not persisted to browser storage or a backend database, so messages are not retained across page refreshes or revisit flows without a separate persistence implementation.
- The UI contains an eye animation and responsive layout patterns, but the final implementation status of those features should be validated against the current UI behaviour in a browser session.

### Backend

- The FastAPI application exposes a visitor WebSocket at `/ws/{client_id}`.
- The backend tracks active user sockets and a single connected admin socket in `ConnectionManager`.
- A connected admin WebSocket is accepted only when the socket includes a valid token in the `sec-websocket-protocol` header and the connecting client IP is in `ALLOWED_ADMIN_IPS`.
- The admin socket can forward a message to a specific visitor using `client_id`.
- The backend reads configuration values from environment variables, including `RESUME_LINK`, `ADMIN_TOKEN`, and `ALLOWED_ADMIN_IPS`.
- The configured resume tool accepts supported request formats and returns the configured resume link for each supported value.

### AI and tool behavior

- The system is wired to Azure OpenAI and supports tool invocation patterns for the configured resume flow.
- The resume tool is configured through environment variables and is not hard-coded in the application logic.
- The current implementation does not evidence persistent conversation storage, session takeover state, or end-of-conversation email collection.

## Planned or incomplete behaviors

The following behaviors are documented in the requirements and design files but are not evidenced by the current repository implementation:

- Visitor conversation persistence after a one-hour revisit.
- Human takeover mode that stops AI processing for an active visitor session.
- Admin end-of-conversation flow with email collection.
- Production admin dashboard and protected delivery of admin credentials.
- Structured logging, monitoring, analytics, and automated tests.
- Secure WSS deployment and a production-grade reverse proxy or TLS setup.

## Evidence-based conclusion

The repository represents a prototype implementation that validates the core interaction model and the security gate pattern for admin access, but it does not yet satisfy the full production target-state requirements described in the planning and requirements documents.

## Decision impact

The current gap is primarily in persistence, admin workflow maturity, and production hardening rather than in the basic visitor chat flow. The project plan should therefore treat the current phase as a prototype-to-production transition rather than a fully completed system.
