import os
import base64
import requests
import webbrowser
from urllib.parse import urlencode
from dotenv import load_dotenv
from callback_server import start_server


load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"


def get_acess_token():
    """
    Função responsável por fazer a autenticação OAuth completa do Spotify
    """

    if not CLIENT_ID or not CLIENT_SECRET:
        raise Exception("CLIENT_ID ou CLIENT_SECRET nãoo configurados no .env")

    scope = "playlist-read-private"

    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": scope
    }

    auth_request_url = (f"{AUTH_URL}?{urlencode(params)}")

    print("Abrindo navegador para login Spotify...")
    print(auth_request_url)
    webbrowser.open(auth_request_url)

    code = start_server()
    print("Code recebido com sucesso!")

    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_str.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)

    if response.status_code != 200:
        raise Exception(f"Erro ao obter token: {response.text}")
    
    return response.json()["access_token"]