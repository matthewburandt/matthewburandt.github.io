#!/usr/bin/env python3
"""
Simple Python server for handling mailing list signups
"""

import json
import csv
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

class MailboxHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        """Handle POST requests for mailing list signups"""
        if self.path == '/api/subscribe':
            try:
                # Get content length
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                
                # Parse JSON data
                data = json.loads(post_data.decode('utf-8'))
                name = data.get('name', '').strip()
                email = data.get('email', '').strip()
                
                # Validate inputs
                if not name or not email:
                    self.send_response(400)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
                    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    response = {
                        'success': False,
                        'message': 'Name and email are required.'
                    }
                    self.wfile.write(json.dumps(response).encode())
                    return
                
                # Basic email validation
                if '@' not in email or '.' not in email:
                    self.send_response(400)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
                    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    response = {
                        'success': False,
                        'message': 'Invalid email address.'
                    }
                    self.wfile.write(json.dumps(response).encode())
                    return
                
                # Save to CSV file
                csv_file = 'mailing_list.csv'
                file_exists = os.path.exists(csv_file)
                
                with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    if not file_exists:
                        writer.writerow(['Name', 'Email'])
                    writer.writerow([name, email])
                
                # Send success response
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {
                    'success': True,
                    'message': 'Thank you for subscribing!'
                }
                self.wfile.write(json.dumps(response).encode())
                
            except Exception as e:
                print(f"Error processing request: {e}")
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {
                    'success': False,
                    'message': 'Server error. Please try again.'
                }
                self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        """Custom logging to show requests"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def run_server(port=3001):
    """Start the server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, MailboxHandler)
    print(f"Mailbox server running on http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    port = 3001
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 3001")
    
    run_server(port) 