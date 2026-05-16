import requests


class SpotifyClient:
    """
    Classe responsável por conversar com a API do Spotify
    """

    def __init__(self, token):

        self.token = token
        self.base_url = "https://api.spotify.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_playlist_tracks(self, playlist_id):
        """
        Busca todas as músicas de uma playlist

        Args:
            playlist_id (str): ID da playlist Spotify

        Returns:
            list: Lista contendo informações das músicas
        """

        url = f"{self.base_url}/playlists/{playlist_id}/items"

        tracks = []

        while url:

            response = requests.get(url, headers=self.headers)

            if response.status_code != 200:

                print(response.text)

                raise Exception(
                    f"Erro ao buscar playlist: {response.text}"
                )

            data = response.json()

            for item in data["items"]:
                track = item["item"]

                if track is None:
                    continue

                tracks.append({
                    "titulo": track["name"],
                    "artista": ", ".join([artist["name"]for artist in track["artists"]]),
                    "data_adicao": item["added_at"]
                })

            url = data["next"]

        return tracks