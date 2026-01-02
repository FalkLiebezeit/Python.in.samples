"""urllib Examples - HTTP Requests using Python's built-in urllib library

This module demonstrates HTTP operations using urllib (no external dependencies):
- GET requests and response handling
- POST requests with encoded data
- Response headers and status codes
- Error handling
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError
import json


def example_basic_get():
    """Demonstrate basic GET request and response examination."""
    print("=" * 60)
    print("1. Basic GET Request")
    print("=" * 60)
    
    try:
        # Using httpbin.org for reliable testing
        response = urlopen('http://httpbin.org/get', timeout=10)
        
        # Examine response headers
        print(f"Content-Type: {response.getheader('Content-Type')}")
        print(f"Server: {response.getheader('Server')}")
        print(f"Status Code: {response.status}")
        print(f"Reason: {response.reason}")
        
        # Read response body
        html = response.read()
        print(f"\nRaw bytes (first 50): {html[:50]}")
        print(f"Decoded text (first 50): {html.decode('utf-8')[:50]}...")
        
        # Parse JSON response
        data = json.loads(html.decode('utf-8'))
        print(f"Request URL: {data['url']}\n")
        
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Error: {e}")


def example_get_with_headers():
    """Demonstrate GET request with custom headers."""
    print("=" * 60)
    print("2. GET Request with Custom Headers")
    print("=" * 60)
    
    try:
        # Create request with custom headers
        req = Request('http://httpbin.org/headers')
        req.add_header('User-Agent', 'Python-urllib/3.12')
        req.add_header('Accept', 'application/json')
        
        response = urlopen(req, timeout=10)
        data = json.loads(response.read().decode('utf-8'))
        
        print("Request headers sent:")
        for key, value in data['headers'].items():
            print(f"  {key}: {value}")
        print()
        
    except Exception as e:
        print(f"Error: {e}\n")


def example_post_simple():
    """Demonstrate simple POST request with data."""
    print("=" * 60)
    print("3. Simple POST Request")
    print("=" * 60)
    
    try:
        # Simple POST with raw data
        data = b'q=tkinter&category=python'
        response = urlopen('http://httpbin.org/post', data=data, timeout=10)
        
        result = json.loads(response.read().decode('utf-8'))
        print(f"Posted data: {result['data']}")
        print(f"Form data parsed: {result['form']}\n")
        
    except Exception as e:
        print(f"Error: {e}\n")


def example_post_encoded():
    """Demonstrate POST request with URL-encoded data."""
    print("=" * 60)
    print("4. POST Request with URL-Encoded Data")
    print("=" * 60)
    
    try:
        # Create form data
        data = {
            'q': 'tkinter, python',
            'language': 'en',
            'category': 'programming'
        }
        
        # Encode the data
        encoded_data = urlencode(data)
        print(f"Encoded data: {encoded_data}")
        
        # Send POST request
        response = urlopen(
            'http://httpbin.org/post',
            data=encoded_data.encode('utf-8'),
            timeout=10
        )
        
        result = json.loads(response.read().decode('utf-8'))
        print(f"\nServer received form data:")
        for key, value in result['form'].items():
            print(f"  {key}: {value}")
        print()
        
    except Exception as e:
        print(f"Error: {e}\n")


def example_error_handling():
    """Demonstrate proper error handling."""
    print("=" * 60)
    print("5. Error Handling")
    print("=" * 60)
    
    # Test 404 error
    print("Testing 404 Not Found:")
    try:
        response = urlopen('http://httpbin.org/status/404', timeout=10)
    except HTTPError as e:
        print(f"✓ Caught HTTP Error: {e.code} - {e.reason}")
    except URLError as e:
        print(f"URL Error: {e.reason}")
    
    # Test timeout
    print("\nTesting timeout (with very short timeout):")
    try:
        response = urlopen('http://httpbin.org/delay/5', timeout=1)
    except URLError as e:
        print(f"✓ Caught timeout error: {e.reason}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test invalid URL
    print("\nTesting invalid URL:")
    try:
        response = urlopen('http://this-domain-does-not-exist-12345.com', timeout=5)
    except URLError as e:
        print(f"✓ Caught URL error: {e.reason}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()


def example_response_analysis():
    """Demonstrate detailed response analysis."""
    print("=" * 60)
    print("6. Detailed Response Analysis")
    print("=" * 60)
    
    try:
        response = urlopen('http://httpbin.org/get', timeout=10)
        
        # Get all headers
        print("All Response Headers:")
        for header, value in response.headers.items():
            print(f"  {header}: {value}")
        
        # Response metadata
        print(f"\nResponse URL: {response.geturl()}")
        print(f"HTTP Version: HTTP/1.1")
        print(f"Status: {response.status} {response.reason}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    print()


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("urllib Library Examples")
    print("Python's built-in HTTP client library")
    print("=" * 60 + "\n")
    
    example_basic_get()
    example_get_with_headers()
    example_post_simple()
    example_post_encoded()
    example_error_handling()
    example_response_analysis()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
