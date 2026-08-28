# Test Case Catalogue

## Visitor Chat

| Test ID | Test Scenario | Expected Result | Status |
| --- | --- | --- | --- |
| TC-001 | Enter valid question | Question appears in input | |
| TC-002 | Submit valid question | Request sent and AI response displayed | |
| TC-003 | Submit empty/whitespace message | Submission rejected | |
| TC-004 | Ask follow-up question | Previous conversation context is available | |
| TC-005 | Submit question requiring AI response | Azure OpenAI response displayed | |

## Resume

| Test ID | Test Scenario | Expected Result | Status |
| --- | --- | --- | --- |
| TC-006 | Ask chatbot for resume | AI invokes resume tool when appropriate | |
| TC-007 | Request supported resume format | Correct configured resume link returned | |
| TC-008 | Change `RESUME_LINK` | Application uses new configured link | |

## WebSocket/Admin

| Test ID | Test Scenario | Expected Result | Status |
| --- | --- | --- | --- |
| TC-009 | Visitor establishes WebSocket | Connection established | |
| TC-010 | Visitor sends message | Connected administrator receives message | |
| TC-011 | Admin sends message to `client_id` | Correct visitor receives message | |
| TC-012 | Admin connects with valid token | Connection accepted | |
| TC-013 | Admin connects from unauthorized IP | Connection rejected | |
| TC-014 | Admin connects with invalid token | Connection rejected | |

## UI

| Test ID | Test Scenario | Expected Result | Status |
| --- | --- | --- | --- |
| TC-015 | Send message while request is processing | Send control disabled | |
| TC-016 | Open application on mobile | UI remains usable | |
| TC-017 | Move mouse around interactive eye | Eye responds to mouse movement | |

## Error Handling

| Test ID | Test Scenario | Expected Result | Status |
| --- | --- | --- | --- |
| TC-018 | Backend unavailable | User receives safe error message | |
| TC-019 | Azure OpenAI request fails | User receives appropriate fallback | |
| TC-020 | Invalid API request | Backend returns appropriate validation error | |