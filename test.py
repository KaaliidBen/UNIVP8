"""Reusable template for calling an OpenAPI/HTTP endpoint."""

import os
from typing import Any

import requests


BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com")
API_KEY = os.getenv("API_KEY", "")


def call_api(
	method: str,
	path: str,
	*,
	params: dict[str, Any] | None = None,
	payload: dict[str, Any] | None = None,
) -> Any:
	"""Send a request and return the decoded JSON response."""
	headers = {"Accept": "application/json", "Content-Type": "application/json"}
	if API_KEY:
		headers["Authorization"] = f"Bearer {API_KEY}"

	response = requests.request(
		method=method,
		url=f"{BASE_URL.rstrip('/')}/{path.lstrip('/')}",
		headers=headers,
		params=params,
		json=payload,
		timeout=30,
	)
	response.raise_for_status()
	return response.json() if response.content else None


if __name__ == "__main__":
	# Replace the path and parameters with those from your OpenAPI specification.
	result = call_api(
		"GET",
		"/v1/resource",
		params={"limit": 10},
	)
	print(result)
