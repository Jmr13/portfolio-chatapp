# Requirements Traceability Matrix

## Functional Requirements Traceability

| ID | Requirement | Source Requirement | Design Component | Implementation Component | Test Case | Coverage |
| --- | --- | --- | --- | --- | --- | --- |
| FR-01 | Visitor can enter text question | R-001 | Chat UI | Textarea | TC-001 | 🟢 |
| FR-02 | Visitor can submit question | R-001 | Chat submission flow | Chat submit handler | TC-002 | 🟢 |
| FR-03 | System rejects empty messages | R-001 | Input validation | Frontend validation | TC-003 | 🟢 |
| FR-04 | System maintains current conversation context | R-002 | Conversation state | `messages` collection | TC-004 | 🟢 |
| FR-05 | AI generates response | R-003 | AI service | Azure OpenAI | TC-005 | 🟢 |
| FR-06 | AI can invoke resume retrieval | R-005 | Tool-calling architecture | `get_resume` | TC-006 | 🟢 |
| FR-07 | Resume available as PDF/DOCX/TXT | R-004 | Resume retrieval service | Resume tool | TC-007 | 🟢 |
| FR-08 | Resume link configurable | R-006 | Configuration management | `RESUME_LINK` | TC-008 | 🟢 |
| FR-09 | Visitor maintains WebSocket connection | R-007 | WebSocket architecture | Visitor WebSocket | TC-009 | 🟢 |
| FR-10 | Visitor messages forwarded to admin | R-007 | WebSocket message routing | `ConnectionManager` | TC-010 | 🟢 |
| FR-11 | Admin sends message to specific visitor | R-008 | Admin WebSocket routing | `send_to_user()` | TC-011 | 🟢 |
| FR-12 | Admin requires token authentication | R-009 | Authentication | `ADMIN_TOKEN` | TC-012 | 🟢 |
| FR-13 | Admin requires allowed IP | R-010 | IP allowlisting | `ALLOWED_ADMIN_IPS` | TC-013 | 🟢 |
| FR-14 | UI differentiates user/AI messages | R-011 | Presentation layer | Message components | TC-002, TC-005 | 🟢 |
| FR-15 | Send control disabled during processing | R-012 | UI state management | Loading state | TC-015 | 🟢 |
| FR-16 | UI responsive | R-014 | Responsive UI | Responsive CSS/classes | TC-016 | 🟢 |
| FR-17 | Interactive eye animation displayed | R-015 | Interactive visual component | SVG eye | TC-017 | 🟢 |

## Non-Functional Requirements Traceability

| ID | Requirement | Design Area | Implementation / Evidence | Verification | Status |
| --- | --- | --- | --- | --- | --- |
| NFR-01 | Protect sensitive configuration and credentials | Security architecture | Backend environment variables | Security test + configuration inspection | 🟢 Implemented |
| NFR-02 | Chatbot remains available without administrator | Availability architecture | AI operates independently of admin WebSocket | Availability test | 🟢 Implemented |
| NFR-03 | Provide responsive chatbot interactions | Performance architecture | Azure OpenAI-dependent request flow | TC-002, TC-005, TC-015 + performance test | 🟡 Partially defined |
| NFR-04 | Support increasing simultaneous visitors | Scalability architecture | In-memory WebSocket connections | TC-009, TC-010 + load/scalability test | 🔴 Current limitation |
| NFR-05 | Minimize collection and retention of visitor information | Privacy architecture | No persistent conversation database | Privacy/data-retention review | 🟡 Partially defined |
| NFR-06 | Separate configuration from source code | Configuration architecture | Environment variables | Configuration inspection | 🟢 Implemented |
| NFR-07 | Provide intuitive chatbot interface | UX architecture | Text input + send button | TC-001, TC-002, TC-015, TC-016 | 🟢 Implemented |