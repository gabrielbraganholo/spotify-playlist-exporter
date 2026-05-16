import requests


class SpotifyClient:
    """
    Classe responsável por conversar com a API do Spotify
    """

    def __init__(self, token):

        # Salva o token recebido após login OAuth
        self.token = token

        # URL base da API do Spotify
        self.base_url = "https://api.spotify.com/v1"

        # Headers enviados em TODAS as requisições
        # Bearer = tipo de autenticação OAuth
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

        # NOVO endpoint da API Spotify
        # Antes era /tracks
        # Agora a Spotify mudou para /items
        url = f"{self.base_url}/playlists/{playlist_id}/items"

        # Lista onde iremos salvar todas as músicas
        tracks = []

        # Continua executando enquanto existir próxima página
        while url:

            # Faz requisição GET para a API
            response = requests.get(
                url,
                headers=self.headers
            )

            # Debug para mostrar status da resposta
            print(response.status_code)

            # Se der erro, interrompe programa
            if response.status_code != 200:

                print(response.text)

                raise Exception(
                    f"Erro ao buscar playlist: {response.text}"
                )

            # Converte JSON da resposta em dicionário Python
            data = response.json()

            # Percorre cada item da playlist
            for item in data["items"]:

                # Pega informações da música
                track = item["item"]

                # Algumas playlists podem ter itens vazios
                if track is None:
                    continue

                # Adiciona música na lista final
                tracks.append({

                    # Nome da música
                    "titulo": track["name"],

                    # Junta todos artistas em uma string
                    "artista": ", ".join(
                        [
                            artist["name"]
                            for artist in track["artists"]
                        ]
                    ),

                    # Data em que música foi adicionada
                    "data_adicao": item["added_at"]
                })

            # Próxima página da API
            # Se não existir próxima página:
            # next = None
            # e o while encerra
            url = data["next"]

        # Retorna lista final de músicas
        return tracks