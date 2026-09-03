# Requirements Assumptions and Open Questions

This document records confirmed requirement decisions and limitations that cannot be verified from the current source or test catalogue.

## Confirmed Decisions

| ID | Decision | Related requirements | Evidence or limitation |
| --- | --- | --- | --- |
| D-01 | Resume format values identify the visitor's requested format, but do not currently select different files. Format-specific file selection is a future feature. | FR-07 | `get_resume_link()` returns the configured `RESUME_LINK` for every supported value. |
| D-02 | Visitor messages shall remain available when the visitor revisits the page after at least one hour. | FR-04, NFR-05 | Confirmed stakeholder decision; the current `ChatContext` only stores messages in frontend memory, so the required persistence path is not implemented. |
| D-03 | Administrator intervention will enter the visitor's chat session and immediately stop subsequent AI processing for that session. | FR-11, NFR-02 | This is a confirmed future behavior; no takeover state or AI-routing bypass is currently evidenced. |
| D-04 | `client/public/templates/admin.html` is the prototype basis for the future administrator UI and client-side WebSocket interaction logic. | FR-11, FR-12, FR-13 | The template demonstrates the intended admin controls and message routing. It currently contains an empty token placeholder and a local `ws://` endpoint; neither defines the production security model. |
| D-05 | The deployment will use one backend process. No simultaneous visitor capacity target or requirement for multiple backend processes/instances is specified. | NFR-04 | Confirmed stakeholder decision; the current connection manager stores connections in process memory. |
| D-06 | Visitors may wait as long as necessary for a chatbot response; no maximum response-time target is specified. | NFR-03 | Confirmed stakeholder decision; no response-time performance target or verification requirement remains. |
| D-07 | Administrator credentials shall originate from backend `.env` configuration and shall not be embedded in the deployed admin page. | NFR-01, NFR-06 | Confirmed stakeholder decision; the current template has an empty token placeholder, but a protected server-side delivery mechanism is not evidenced. |
| D-08 | The admin page shall be included in the deployed site and communicate with the production backend through HTTPS/REST APIs. | FR-12, FR-13 | Confirmed stakeholder decision; the current admin prototype uses a local WebSocket endpoint, so the production transport and API implementation are not yet evidenced. |
| D-09 | Visitor chat history will be stored in browser storage, specifically cookies, and will expire after one hour. | FR-04, NFR-05 | Confirmed stakeholder decision; messages remain available after a revisit within the one-hour window, and browser-side storage is expected to expire automatically. |
| D-10 | All credentials will be stored in backend `.env` variables. | FR-12, FR-13, NFR-01, NFR-06 | Confirmed stakeholder decision; secrets remain on the server and are not embedded in the frontend or static admin page. |
| D-11 | Human takeover mode is a planned feature and is not yet implemented in the current system. | FR-11, NFR-02 | Confirmed stakeholder decision; the current backend can forward messages to an admin, but it does not yet maintain takeover state or stop AI processing when an admin enters the session. |
| D-12 | End-of-session email capture is not yet implemented. | FR-18, FR-19 | Confirmed stakeholder decision; this behavior remains planned and unimplemented in the current repository and requires future design and testing before release. |

## Open Decisions Requiring Stakeholder Input

No unresolved design decisions remain in this section at this time. The current unresolved items are already captured as future work or implementation gaps in the planning and traceability documents, rather than as open stakeholder decisions.
