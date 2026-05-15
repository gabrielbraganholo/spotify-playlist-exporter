# 🎵 Spotify Playlist Exporter

Aplicação em Python que acessa uma playlist pública do Spotify e exporta todas as músicas para um arquivo `.csv`.

O projeto utiliza a API oficial do Spotify e faz as requisições manualmente usando `requests`, sem bibliotecas específicas do Spotify.

---

# 📌 Funcionalidades

- Exporta título das músicas
- Exporta nome dos artistas
- Exporta data de adição na playlist
- Gera arquivo `.csv`
- Sobrescreve automaticamente exportações antigas
- Utiliza autenticação oficial da API do Spotify
- Estrutura modular e organizada

---

# 🛠️ Tecnologias utilizadas

- Python
- Requests
- Python Dotenv
- Spotify Web API

---

# 📂 Estrutura do projeto

```txt
spotify-playlist-exporter/
│
├── src/
│   ├── auth.py
│   ├── spotify.py
│   ├── exporter.py
│   └── main.py
│
├── output/
│   └── playlist.csv
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---
# 🔑 Configuração da API do Spotify

## 1. Acesse o Spotify for Developers

https://developer.spotify.com/dashboard

---

## 2. Crie uma aplicação

Após criar o app, copie:

- Client ID
- Client Secret

---

## 3. Crie um arquivo `.env`

```env
CLIENT_ID=SEU_CLIENT_ID
CLIENT_SECRET=SEU_CLIENT_SECRET
```

---

# ▶️ Executando a aplicação

```bash
python src/main.py
```

A aplicação solicitará a URL da playlist.

Exemplo:

```txt
https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
```

---

# 📄 Exemplo do CSV gerado

```csv
titulo,artista,data_adicao
Numb,Linkin Park,2025-05-10T14:32:11Z
505,Arctic Monkeys,2025-05-11T09:21:55Z
```

---

# 🔒 Segurança

O arquivo `.env` está listado no `.gitignore` para evitar o vazamento das credenciais da API.

---

# 📚 Conceitos praticados

- Consumo de API REST
- Requisições HTTP
- OAuth Client Credentials
- Manipulação de JSON
- Escrita de arquivos CSV
- Paginação de API
- Estruturação de projetos Python
- Variáveis de ambiente

---

# 🚀 Melhorias futuras

- Exportação para JSON
- Interface gráfica
- Suporte a playlists privadas
- Integração com banco de dados
- Estatísticas da playlist
- Interface web com Flask

---

# ⭐ Apoie o projeto

Se este projeto foi útil para você ou te ajudou de alguma forma, considere deixar uma estrela no repositório.
