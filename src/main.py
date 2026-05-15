from auth import get_acess_token
from spotify import SpotifyClient
from exporter import export_to_csv


def extract_playlist_id(url):
    """Função que extrai o id de dentro da URL da playlist

    Args:
        url (str): URL completa da playlist do Spotify

    Returns:
        str: ID da playlist extraído da URL
    """

    return url.split("/playlist/")[1].split("?")[0]


def main():

    print("Spotify Playlist Exporter\n")

    playlist_url = input("Cole a URL da playlist: ").strip()
    playlist_id = extract_playlist_id(playlist_url)
    print("\nPegando token de acesso...")

    token = get_acess_token()
    print("Buscando músicas da playlist...")

    client = SpotifyClient(token)
    tracks = client.get_playlist_tracks(playlist_id)

    tracks = sorted(tracks, key=lambda x: x["artista"].split(",")[0].strip().lower())

    print(f"\n{len(tracks)} músicas encontradas\n")

    print("Exportando CSV...")
    export_to_csv(tracks)

    print("Finalizado com sucesso!")


if __name__ == "__main__":
    main()