#!/usr/bin/env python3
"""
Simple test script using only built-in libraries
"""

import urllib.request
import urllib.parse
import json

def test_server():
    """Test the mailbox server using built-in libraries"""
    print("Testing Mailbox Server...")
    print("=" * 40)
    
    # Test data
    test_data = {
        "name": "Test User",
        "email": "test@example.com"
    }
    
    # Convert to JSON
    json_data = json.dumps(test_data).encode('utf-8')
    
    # Create request
    req = urllib.request.Request(
        'http://localhost:3001/api/subscribe',
        data=json_data,
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        # Send request
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print(f"✅ Success: {result.get('message', 'Unknown response')}")
            return True
    except urllib.error.URLError as e:
        print(f"❌ Error: Could not connect to server")
        print(f"Make sure the server is running on http://localhost:3001")
        print(f"Error details: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == '__main__':
    test_server() 