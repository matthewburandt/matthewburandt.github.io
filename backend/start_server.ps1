Write-Host "Starting Mailbox Server..." -ForegroundColor Green
Write-Host ""
Write-Host "This will start the mailing list server on http://localhost:3001" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server when you're done" -ForegroundColor Yellow
Write-Host ""

try {
    python mailbox_server.py
} catch {
    Write-Host "Error: Could not start the server. Make sure Python is installed." -ForegroundColor Red
    Write-Host "You can download Python from https://python.org" -ForegroundColor Red
}

Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 