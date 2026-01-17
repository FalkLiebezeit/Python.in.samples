"""HTTP Requests Examples using the requests library

This module demonstrates various HTTP request patterns including:
- GET and POST requests
- Session management
- Response handling
- Error handling with status codes
"""

import requests
from requests.exceptions import HTTPError, RequestException


def example_basic_requests():
    """Demonstrate basic GET requests."""
    print("=" * 60)
    print("1. Basic GET Requests")
    print("=" * 60)
    
    # Method 1: Using requests.request()
    try:
        response = requests.request('GET', 'http://www.alandmoore.com/', timeout=5)
        print(f"Using request(): {response}")
        print(f"Status Code: {response.status_code}")
    except RequestException as e:
        print(f"Request failed: {e}")
    
    # Method 2: Using requests.get() (preferred)
    try:
        response = requests.get('http://www.alandmoore.com', timeout=5)
        print(f"Using get(): {response}")
        print(f"Status Code: {response.status_code}\n")
    except RequestException as e:
        print(f"Request failed: {e}\n")


def example_post_request():
    """Demonstrate POST request with data."""
    print("=" * 60)
    print("2. POST Request with Data")
    print("=" * 60)
    
    try:
        # Make a POST with search parameters
        response = requests.post(
            'https://duckduckgo.com',
            data={'q': 'tkinter', 'ko': '-2', 'kz': '-1'},
            timeout=5
        )
        print(f"POST Response: {response}")
        print(f"Status Code: {response.status_code}")
        print(f"Content Length: {len(response.content)} bytes\n")
    except RequestException as e:
        print(f"POST request failed: {e}\n")


def example_sessions():
    """Demonstrate session usage for persistent connections."""
    print("=" * 60)
    print("3. Using Sessions")
    print("=" * 60)
    
    # Create a session object
    s = requests.Session()
    
    try:
        # Simulate login (example.com doesn't actually have this endpoint)
        # In real scenarios, this would set cookies/tokens
        print("Attempting login simulation...")
        login_response = s.post(
            'http://httpbin.org/post',  # Using httpbin for testing
            data={'username': 'test', 'password': 'test'},
            timeout=5
        )
        print(f"Login Response: {login_response.status_code}")
        
        # Subsequent requests would maintain session cookies
        response = s.get('http://httpbin.org/cookies', timeout=5)
        print(f"Session cookies: {s.cookies.items()}")
        print(f"Response cookies: {response.json()}\n")
        
    except RequestException as e:
        print(f"Session request failed: {e}\n")
    finally:
        s.close()


def example_response_objects():
    """Demonstrate working with response objects."""
    print("=" * 60)
    print("4. Response Objects and Headers")
    print("=" * 60)
    
    try:
        r = requests.get('http://httpbin.org/get', timeout=5)
        
        # Display some headers
        print("Response Headers:")
        for key, value in list(r.headers.items())[:5]:  # Show first 5 headers
            print(f"  {key}: {value}")
        
        print(f"\nContent-Type: {r.headers.get('Content-Type')}")
        print(f"Status Code: {r.status_code}\n")
        
    except RequestException as e:
        print(f"Request failed: {e}\n")


def example_error_handling():
    """Demonstrate proper error handling with HTTP status codes."""
    print("=" * 60)
    print("5. Error Handling")
    print("=" * 60)
    
    # Example 1: Handling 404 error gracefully
    try:
        print("Attempting to access non-existent page...")
        r = requests.get('http://httpbin.org/status/404', timeout=5)
        print(f"Status Code: {r.status_code}")
        
        # This will raise an HTTPError for 4xx/5xx status codes
        r.raise_for_status()
        
    except HTTPError as e:
        print(f"✓ HTTP Error caught: {e}")
        print(f"  Status Code: {e.response.status_code}")
        
    except RequestException as e:
        print(f"Request failed: {e}")
    
    # Example 2: Checking status code manually
    print("\nManual status code checking:")
    try:
        r = requests.get('http://httpbin.org/status/200', timeout=5)
        if r.status_code == 200:
            print(f"✓ Success! Status Code: {r.status_code}")
        elif r.status_code == 404:
            print(f"Page not found: {r.status_code}")
        else:
            print(f"Unexpected status: {r.status_code}")
            
    except RequestException as e:
        print(f"Request failed: {e}")
    
    print()


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("HTTP Requests Library Examples")
    print("=" * 60 + "\n")
    
    example_basic_requests()
    example_post_request()
    example_sessions()
    example_response_objects()
    example_error_handling()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
