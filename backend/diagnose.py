#!/usr/bin/env python3
"""
Diagnostic script to test server connection
"""

import urllib.request
import urllib.parse
import json
import time

def test_server():
    """Test the server with detailed logging"""
    print("=== Server Diagnostic Test ===")
    
    # Test data
    test_data = {
        "name": "Diagnostic Test",
        "email": "test@diagnostic.com"
    }
    
    # Convert to JSON
    json_data = json.dumps(test_data).encode('utf-8')
    
    print(f"1. Preparing request with data: {test_data}")
    
    # Create request
    req = urllib.request.Request(
        'http://localhost:3001/api/subscribe',
        data=json_data,
        headers={'Content-Type': 'application/json'}
    )
    
    print("2. Sending request to http://localhost:3001/api/subscribe")
    print("3. Request headers:", dict(req.headers))
    print("4. Request data:", json_data)
    
    try:
        print("5. Attempting to connect...")
        start_time = time.time()
        
        # Send request with timeout
        with urllib.request.urlopen(req, timeout=10) as response:
            end_time = time.time()
            response_time = end_time - start_time
            
            print(f"6. ✅ Connection successful!")
            print(f"7. Response time: {response_time:.2f} seconds")
            print(f"8. Response status: {response.status}")
            print(f"9. Response headers: {dict(response.headers)}")
            
            # Read response
            response_data = response.read()
            print(f"10. Response data (raw): {response_data}")
            
            # Parse JSON
            try:
                result = json.loads(response_data.decode())
                print(f"11. ✅ Parsed JSON: {result}")
                return True
            except json.JSONDecodeError as e:
                print(f"11. ❌ JSON parse error: {e}")
                print(f"    Raw response: {response_data}")
                return False
                
    except urllib.error.URLError as e:
        print(f"6. ❌ Connection failed: {e}")
        print(f"   Error type: {type(e).__name__}")
        return False
    except Exception as e:
        print(f"6. ❌ Unexpected error: {e}")
        print(f"   Error type: {type(e).__name__}")
        return False

if __name__ == '__main__':
    test_server() 