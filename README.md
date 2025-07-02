# legendary-sniffle
 # AI Calendar Assistant

A personal Flask-based web assistant that parses natural language event descriptions using Google's Gemini API and adds them directly to your Google Calendar. Voice input and profile picture support included.

> This project is designed for single-user use only. OAuth tokens are stored locally. Do **not** deploy this version publicly with credentials or tokens exposed.

---

## Features

- Natural Language Parsing: Uses Gemini (Google GenAI) to convert user input into structured calendar events.
- Voice Input: Record speech directly from the UI and convert it into calendar events.
- Google Calendar Integration: Authenticates with Google OAuth 2.0 and inserts events.
- Google Profile Picture Display: Fetches and displays the user's Google profile photo.
- Night-Themed UI: Sleek, responsive frontend with dark mode styling.

---

## Tech Stack

- Frontend: HTML, JavaScript, CSS (Dark Theme), Web Speech API
- Backend: Flask, Google OAuth 2.0, Google Calendar API, Gemini GenAI
