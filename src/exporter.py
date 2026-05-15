import csv
import os


def export_to_csv(tracks, output_path="output/playlist.csv"):
    """Função que salva as músicas em um arquivo csv

    Args:
        tracks (list): Lista de músicas contendo título, artista e data de adição
        output_path (str, optional): Caminho do arquivo CSV de saída
            Padrão: "output/playlist.csv"
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        
        writer = csv.DictWriter(file, fieldnames=["titulo", "artista", "data_adicao"])

        writer.writeheader()

        for track in tracks:
            writer.writerow(track)

    print(f"CSV gerado com sucesso em {output_path}")