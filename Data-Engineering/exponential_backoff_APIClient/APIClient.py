import time
import logging
from typing import Dict, Any, Optional

import requests


class APIClient:
    """Handles API requests with retry logic."""

    def __init__(self, headers: Dict[str, str], max_retries: int = 3, backoff_factor: int = 2):
        """Initialize the client with common request settings.

        Args:
            headers: A dict of HTTP headers to include on every request.
            max_retries: How many times to retry on failure.
            backoff_factor: Base for exponential backoff between retries.
        """
        self.headers = headers
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def post(self, url: str, body: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Send a POST request with retry logic and return the parsed JSON.

        Args:
            url: The target endpoint.
            body: The JSON-serializable payload.

        Returns:
            The parsed JSON response as a dict, or None if all retries fail.
        """
        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.post(url, json=body, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                print(f"Attempt {attempt} failed: {e}")
                if attempt < self.max_retries:
                    # wait: backoff_factor^attempt seconds
                    time.sleep(self.backoff_factor ** attempt)
                else:
                    print("All retry attempts failed.")
        return None

    def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Send a GET request with retry logic and return the parsed JSON.

        Args:
            url: The endpoint URL.
            params: Optional query parameters.

        Returns:
            The parsed JSON response as a dict, or None if all retries fail.
        """
        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.get(
                    url,
                    params=params,
                    headers=self.headers,
                    timeout=10
                )
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                logging.warning(f"Attempt {attempt} failed: {e}")
                if attempt < self.max_retries:
                    time.sleep(self.backoff_factor ** attempt)
                else:
                    logging.error("All retry attempts failed.")
        return None
        
if __name__ == "__main__":
    client = APIClient(headers={"Authorization": "Bearer token"}, max_retries=3, backoff_factor=2)

    url = "https://api.example.com/data"
    payload = {"query": "example"}

    # POST example
    result = client.post(url, body=payload)
    print("POST result:", result)

    # GET example
    result = client.get(url)
    print("GET result:", result)