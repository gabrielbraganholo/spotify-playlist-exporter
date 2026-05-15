import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

TOKEN_URL = "https://accounts.spotify.com/api/token"


def get_acess_token():
    """
    Função responsável por pedir ao Spotify um token de acesso
    Esse token é o que permite acessar a API
    """


    if not CLIENT_ID or not CLIENT_SECRET:
        raise Exception("CLIENT_ID ou CLIENT_SECRET nãoo configurados no .env")
    
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"

    auth_bytes = auth_str.encode("utf-8")

    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)

    if response.status_code != 200:
        raise Exception(f"Erro ao obter token: {response.text}")
    
    return response.json()["access_token"]