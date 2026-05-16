# 🎵 Spotify Playlist Export Sloan

Aplicação em Python que acessa uma playlist do Spotify e exporta todas as músicas para um arquivo `.csv`.

O projeto utiliza a API oficial do Spotify e faz as requisições manualmente com `requests`, sem bibliotecas prontas tipo `spotipy`.

---

## 📌 Funcionalidades

- Exporta título das músicas  
- Exporta nome dos artistas  
- Exporta data de adição na playlist  
- Gera arquivo `.csv`  
- Sobrescreve automaticamente exportações antigas  
- Autenticação via OAuth 2.0 (Spotify Web API)  
- Estrutura modular e organizada  

---

## 🛠️ Tecnologias utilizadas

- Python  
- Requests  
- Python Dotenv  
- HTTP Server (`BaseHTTPRequestHandler`)  
- Spotify Web API  

---

## 📂 Estrutura do projeto

```txt
spotify-playlist-exporter/
│
├── src/
│   ├── main.py
│   ├── auth.py
│   ├── spotify.py
│   ├── exporter.py
│   └── callback_server.py
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

## 🔑 Configuração da API do Spotify

1. Acesse o dashboard de desenvolvedor:  
   [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)  
2. Crie uma nova aplicação.  
3. Copie:  
   - `Client ID`  
   - `Client Secret`  
4. Defina a **Redirect URI** (obrigatória):  
   `http://127.0.0.1:8888/callback`  

No arquivo `.env`:

```env
CLIENT_ID=SEU_CLIENT_ID
CLIENT_SECRET=SEU_CLIENT_SECRET
REDIRECT_URI=http://127.0.0.1:8888/callback
```

---

## ▶️ Execução

No terminal, na raiz do projeto:

```bash
python src/main.py
```

Quando solicitado, cole a URL da playlist:

```text
https://open.spotify.com/playlist/xxxxxxxxxxxx
```

---

## 🔐 Fluxo de autenticação

1. O navegador abre a página de login do Spotify.  
2. Após o login, o Spotify redireciona para o callback local (`http://127.0.0.1:8888/callback`).  
3. `callback_server.py` captura o parâmetro `code` da URL.  
4. `auth.py` troca esse `code` por um `access_token`.  
5. A API do Spotify é acessada com o `access_token` válido para exportar as músicas.  

---

## 📄 Exemplo de CSV gerado

```csv
titulo,artista,data_adicao
Numb,Linkin Park,2025-05-10T14:32:11Z
505,Arctic Monkeys,2025-05-11T09:21:55Z
```

---

## 🔒 Segurança

- O arquivo `.env` está no `.gitignore`, protegendo credenciais.  
- Chaves sensíveis não são expostas no repositório.  
- O `access_token` é temporário e gerado apenas na sessão de exportação.  

---

## 📚 Conceitos aplicados

- REST API  
- OAuth 2.0  
- HTTP requests com `requests`  
- Parsing de JSON em Python  
- Servidor HTTP local com `BaseHTTPRequestHandler`  
- Exportação de dados para CSV  

---

## ⭐ Curta o projeto

Se curtir o projeto, deixe uma estrela no repositório! 🌟
