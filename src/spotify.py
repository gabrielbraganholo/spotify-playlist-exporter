import requests


class SpotifyClient:
    """
    Classe que conversa com o Spotify
    Usa token para acessar dados da API
    """

    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.spotify.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_playlist_tracks(self, playlist_id):
        """Método que busca todas as músicas de uma playlist

        Args:
            playlist_id (str): ID da playlist do Spotify

        Returns:
            list: Lista de músicas com título, artista e data de adição
        """

        url = f"{self.base_url}/playlists/{playlist_id}/tracks"
        tracks = []

        while url:

            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                raise Exception(f"Erro ao buscar playlist: {response.text}")
            
            data = response.json
            for item in data:
                track = item["track"]

                if track is None:
                    continue

                tracks.append({
                    "titulo": track["name"],
                    "artista": ", ".join([a["name"] for a in track["artists"]]),
                    "data_adicao": item["added_at"]
                })

            url = data.get("next")

        return tracks