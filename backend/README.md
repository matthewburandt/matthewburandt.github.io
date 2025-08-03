# Mailbox Server

A simple Python-based server for handling mailing list signups.

## Requirements

- Python 3.6 or higher (usually comes pre-installed on Windows 10/11)

## Quick Start

### Option 1: Using the batch file (Windows)
1. Double-click `start_server.bat`
2. The server will start on http://localhost:3001
3. Press Ctrl+C to stop the server

### Option 2: Using PowerShell
1. Right-click `start_server.ps1` and select "Run with PowerShell"
2. The server will start on http://localhost:3001
3. Press Ctrl+C to stop the server

### Option 3: Command line
1. Open Command Prompt or PowerShell
2. Navigate to the backend folder: `cd backend`
3. Run: `python mailbox_server.py`
4. Press Ctrl+C to stop the server

## How it works

- The server runs on port 3001
- It accepts POST requests to `/api/subscribe`
- Subscribers are saved to `mailing_list.csv`
- The server handles CORS for cross-origin requests

## Testing

Once the server is running, you can test it by:

1. Opening your website (index.html) in a browser
2. Going to the "Mailing List" section
3. Filling out the form and submitting

The server will log all requests to the console.

## Data Storage

Subscribers are stored in `mailing_list.csv` with the following format:
```
Name,Email
John Doe,john@example.com
Jane Smith,jane@example.com
```

## Troubleshooting

- **"python is not recognized"**: Install Python from https://python.org
- **Port already in use**: Change the port in the script or close other applications using port 3001
- **CORS errors**: Make sure the server is running before testing the form 