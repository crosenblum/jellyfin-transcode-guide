# jellyfin_config.py

# Base URL of your Jellyfin server (no trailing slash)
JELLYFIN_SERVER = "http://localhost:8096"

# Your Jellyfin API token
API_KEY = ""

# (Optional) User ID if you want to scope results to a specific user
USER_ID = ""

# Headers to use with all requests
HEADERS = {"X-Emby-Token": API_KEY, "Accept": "application/json"}
