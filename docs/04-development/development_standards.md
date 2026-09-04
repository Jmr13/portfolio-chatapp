# Development Standards and Environment Guide

## Purpose

This directory captures the implementation guidance that is supported by the current repository state. It records the verified conventions for the frontend, backend, environment configuration, and the prototype-to-production boundary that the project currently reflects.

## Verified project structure

The current workspace shows two primary implementation areas:

- Frontend: `client/` using Next.js, React, and TypeScript.
- Backend: `server/` using FastAPI and Python.

Repository evidence:

- `client/package.json` defines a Next.js app with a `dev`, `build`, and `start` script.
- `server/requirements.txt` lists FastAPI, Uvicorn, OpenAI, python-dotenv, and related dependencies.
- `server/app/main.py` mounts the conversation and WebSocket routers.

## Frontend conventions

### Application layout

- The client uses the Next.js App Router layout in `client/src/app/`.
- UI components live under `client/src/components/`, with custom chat components under `client/src/components/custom/`.
- Shared UI primitives are stored under `client/src/components/ui/`.
- Conversation-related state is currently kept in React context via `client/src/context/ChatContext.tsx`.

### State and persistence

The repository currently evidences ephemeral browser-side state only. `ChatProvider` stores message arrays in React state and exposes `addMessage` and `clearMessages` without any browser-storage or backend persistence layer. This means the present implementation does not yet satisfy the one-hour revisit persistence requirement documented in the requirements artifacts.

## Backend conventions

### Application entry point

- `server/app/main.py` creates the FastAPI app and includes both routers.
- `server/app/routers/conversations.py` handles conversational requests.
- `server/app/routers/websockets.py` handles visitor and admin WebSocket traffic.

### Configuration and environment

Backend configuration is centralized in `server/app/core/config.py` and uses `python-dotenv` to load environment values from `.env` files.

Verified environment variables in the current code:

- `MS_AZURE_ENDPOINT`
- `MS_AZURE_DEPLOYMENT_NAME`
- `MS_AZURE_SUBSCRIPTION_KEY`
- `MS_AZURE_API_VERSION`
- `RESUME_LINK`
- `ALLOWED_ADMIN_IPS`
- `ADMIN_TOKEN`

This matches the requirements and design documents: credentials and admin settings remain backend-only and are not embedded in the frontend or static admin page.

### Admin access model

The prototype admin connection logic in `server/app/routers/websockets.py` currently does the following:

- accepts a visitor WebSocket at `/ws/{client_id}`
- requires an admin token in the `sec-websocket-protocol` header
- checks the connecting client IP against `ALLOWED_ADMIN_IPS`
- forwards direct messages to a specific visitor using `client_id`

This is a prototype security gate, not a final production admin delivery model. The requirement and design documents correctly mark the protected admin-page delivery and takeover workflow as future work.

## Local development setup

The following commands are directly supported by the repository evidence and should be treated as the current local setup path.

### Server

From the `server/` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

This matches the instructions in `server/README.md`.

### Client

From the `client/` directory:

```bash
npm install
npm run dev
```

This matches the scripts defined in `client/package.json`.

## Security and configuration handling

The following guidance is the current documented standard for the repository:

- keep secret values in backend environment configuration, not in frontend files or static HTML;
- do not place administrator credentials in `client/public/templates/admin.html`;
- use `.env` values as the source of truth for Azure, admin, and resume configuration;
- treat any production-grade admin delivery mechanism as a future enhancement until the stakeholder validates the final access model.

## Prototype-to-production boundary

The implementation is currently best described as a prototype that validates the interaction model and admin WebSocket gate pattern. The following behaviors remain unimplemented or are planned rather than evidenced by the repository:

- browser or server persistence for visitor conversation history across a revisit;
- human takeover state that stops AI processing during an admin session;
- end-of-conversation email collection;
- a final production admin dashboard and protected admin delivery flow;
- automated testing and production monitoring.

## Documentation status

This development guide fills the current gap created by the empty `docs/04-development/` phase folder and aligns the recorded project conventions with the actual repository evidence.
