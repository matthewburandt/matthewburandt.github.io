#!/usr/bin/env python3
"""
Test script for the mailbox server
"""

import requests
import json
import time

def test_server():
    """Test the mailbox server"""
    base_url = "http://localhost:3001"
    
    print("Testing Mailbox Server...")
    print("=" * 40)
    
    # Test 1: Valid subscription
    print("\n1. Testing valid subscription...")
    test_data = {
        "name": "Test User",
        "email": "test@example.com"
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/subscribe",
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Success: {result.get('message', 'Unknown response')}")
        else:
            print(f"❌ Error: Status {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server")
        print("Make sure the server is running on http://localhost:3001")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    # Test 2: Invalid email
    print("\n2. Testing invalid email...")
    test_data = {
        "name": "Test User",
        "email": "invalid-email"
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/subscribe",
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 400:
            result = response.json()
            print(f"✅ Success: {result.get('message', 'Unknown response')}")
        else:
            print(f"❌ Error: Expected 400, got {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Missing fields
    print("\n3. Testing missing fields...")
    test_data = {
        "name": "",
        "email": ""
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/subscribe",
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 400:
            result = response.json()
            print(f"✅ Success: {result.get('message', 'Unknown response')}")
        else:
            print(f"❌ Error: Expected 400, got {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 40)
    print("Test completed!")
    return True

if __name__ == '__main__':
    test_server() 