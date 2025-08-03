#!/usr/bin/env python3
"""
Quick test to verify server is working
"""

import urllib.request
import json

# Test data
data = {"name": "Quick Test", "email": "quick@test.com"}
json_data = json.dumps(data).encode('utf-8')

# Create request
req = urllib.request.Request(
    'http://localhost:3001/api/subscribe',
    data=json_data,
    headers={'Content-Type': 'application/json'}
)

try:
    print("Testing server...")
    with urllib.request.urlopen(req, timeout=5) as response:
        print(f"✅ Server responded with status: {response.status}")
        result = response.read()
        print(f"Response: {result}")
except Exception as e:
    print(f"❌ Error: {e}")
    print("But check if data was saved to mailing_list.csv anyway!") 