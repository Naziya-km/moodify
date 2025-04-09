import base64
import requests

# Replace these with your actual Client ID and Secret from Spotify Developer Dashboard
CLIENT_ID = "c700eb94861c45b9b0b2c546b50018f6"
CLIENT_SECRET = "e57506598e114feab5a1cd08b85e5636"

def get_access_token():
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth_str}",
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    return None

def get_song_for_mood(mood):
    token = get_access_token()
    if not token:
        return None

    search_query = f"{mood} music"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": search_query,
        "type": "track",
        "limit": 1
    }

    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    if response.status_code == 200:
        items = response.json()["tracks"]["items"]
        if items:
            track = items[0]
            return {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "url": track["external_urls"]["spotify"]
            }
    return None
