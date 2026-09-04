# Requirements Traceability Matrix

## Functional Requirements Traceability

| ID | Requirement | Source Requirement | Design Component | Implementation Evidence | Test Case Specification | Verification Status |
| --- | --- | --- | --- | --- | --- | --- |
| FR-01 | Visitor can enter text question | FR-01 | Chat UI | `client/src/components/custom/ChatBox.tsx` (`Textarea`) | TC-001 | Specified; implementation evidence present; test not executed |
| FR-02 | Visitor can submit question | FR-02 | Chat submission flow | `client/src/components/custom/ChatBox.tsx` (`handleSubmit`) | TC-002 | Specified; implementation evidence present; test not executed |
| FR-03 | System rejects empty messages | FR-03 | Input validation | `ChatBox.tsx` trims and rejects empty input | TC-003 | Specified; implementation evidence present; test not executed |
| FR-04 | System maintains conversation context across a revisit | FR-04 | Conversation persistence | `client/src/context/ChatContext.tsx` stores messages only in frontend memory | TC-004 | Requirement revised to require availability after at least one hour; current implementation does not evidence persistence; test not executed |
| FR-05 | AI generates response | FR-05 | AI service | `server/app/services/conversation_service.py`; Azure client | TC-005 | Specified; implementation evidence present; test not executed |
| FR-06 | AI can invoke resume retrieval | FR-06 | Tool-calling architecture | `server/app/core/tools.py` (`get_resume`) | TC-006 | Specified; implementation evidence present; test not executed |
| FR-07 | Resume link can be requested by format | FR-07 | Resume retrieval service | `tools.py` accepts `pdf`, `docx`, `txt`; `server/app/external/index.py` returns the same configured link with the requested version | TC-007 | Current scope: format is returned as metadata; format-specific file selection is a future feature; test not executed |
| FR-08 | Resume link configurable | FR-08 | Configuration management | `server/app/core/config.py` (`RESUME_LINK`) | TC-008 | Specified; implementation evidence present; test not executed |
| FR-09 | Visitor maintains WebSocket connection | FR-09 | WebSocket architecture | `server/app/routers/websockets.py` (`/ws/{client_id}`) | TC-009 | Specified; implementation evidence present; test not executed |
| FR-10 | Visitor messages forwarded to admin | FR-10 | WebSocket message routing | `server/app/services/connection_manager.py`; connected admin required | TC-010 | Specified; implementation evidence present; test not executed |
| FR-11 | Admin can take over a visitor conversation | FR-11 | Admin WebSocket routing and conversation state | `connection_manager.py` (`send_to_user`) | TC-011, TC-021 | Direct messaging is evidenced; takeover state and AI-routing bypass are not implemented; TC-021 not executed |
| FR-12 | Admin requires token authentication | FR-12 | Authentication | `websockets.py`; `ADMIN_TOKEN` from `config.py` | TC-012, TC-014 | Specified; implementation evidence present; test not executed; credential exposure risk documented |
| FR-13 | Admin requires an allowed IP | FR-13 | IP allowlisting | `websockets.py`; `ALLOWED_ADMIN_IPS` from `config.py` | TC-013 | Specified; implementation evidence present; test not executed |
| FR-14 | UI differentiates user/AI messages | FR-14 | Presentation layer | `client/src/components/custom/MessageBubble.tsx` and message types | TC-002, TC-005 | Specified; implementation evidence present; test not executed |
| FR-15 | Send control disabled during processing | FR-15 | UI state management | `ChatBox.tsx` (`loading`) | TC-015 | Specified; implementation evidence present; test not executed |
| FR-16 | UI responsive | FR-16 | Responsive UI | `client/src/app/globals.css` and component classes | TC-016 | Specified; implementation evidence present; test not executed |
| FR-17 | Interactive eye animation displayed | FR-17 | Interactive visual component | `client/src/components/custom/EyeWatch.tsx` | TC-017 | Specified; implementation evidence present; test not executed |
| FR-18 | AI session end prompts for email | FR-18 | Conversation completion flow | None; email collection is not implemented | TC-022 | Planned requirement; implementation and test evidence missing |
| FR-19 | Admin can end a conversation | FR-19 | Admin conversation controls and completion flow | None; end control and email collection are not implemented | TC-023 | Planned requirement; implementation and test evidence missing |

## Non-Functional Requirements Traceability

| ID | Requirement | Design Area | Implementation / Evidence | Verification | Status |
| --- | --- | --- | --- | --- | --- |
| NFR-01 | Protect sensitive configuration and credentials | Security architecture | Backend reads secrets from environment; `client/public/templates/admin.html` currently contains an empty `ADMIN_TOKEN` placeholder and no secret value | Security review; no security test executed | Credential source is defined as backend `.env`; protected delivery and security verification remain missing |
| NFR-02 | Chatbot remains available without administrator | Availability architecture | Conversation endpoint does not depend on `ConnectionManager` | Availability test; not executed | Implementation path supports requirement; verification missing |
| NFR-03 | Return chatbot responses without a fixed response-time target | Availability and response flow | `server/app/routers/conversations.py` calls Azure-dependent flow synchronously | Functional response verification; no response-time target | Requirement defined; response-time performance test not required |
| NFR-04 | Use a single backend process | Deployment architecture | `ConnectionManager` stores connections in process memory | Deployment/configuration inspection | Confirmed constraint; visitor capacity target not specified |
| NFR-05 | Retain visitor messages for the defined user experience | Privacy architecture | `ChatContext` stores messages in frontend memory; no persistence path is evidenced | Persistence and data-retention review; not executed | One-hour revisit requirement defined; implementation and longer-term retention remain unverified |
| NFR-06 | Separate configuration from source code | Configuration architecture | `server/app/core/config.py` reads environment variables; `client/public/templates/admin.html` contains only an empty token placeholder | Configuration inspection; not executed | Backend `.env` source is defined; protected admin-page delivery remains undefined |
| NFR-07 | Provide intuitive chatbot interface | UX architecture | `ChatBox.tsx` provides textarea, placeholder, and send button | TC-001, TC-002, TC-015, TC-016; not executed | Implementation evidence present; verification missing |

## Traceability Notes

- `Source Requirement` now references the requirement's own ID. The former `R-*` identifiers were not defined anywhere in the requirements document.
- Entries in `docs/05-testing/test_cases.md` are test specifications only. Their blank status fields provide no evidence that tests have been executed.
- “Implementation evidence present” means the referenced source path contains a relevant implementation path; it does not mean the requirement has passed an automated or manual test.
- The matrix does not claim coverage for requirements without a defined acceptance target or executed verification evidence.
- The architecture flow in `docs/03-design/architecture.md` distinguishes current behavior from planned behavior; email collection, email delivery, disclaimers, and persistent human takeover are not currently implemented.