from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


auth_code = None


class CallbackHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Método que é executado automaticamente quando o navegador
        faz uma requisição GET para o servidor local
        """

        global auth_code

        query = urlparse(self.path).query
        params = parse_qs(query)

        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<h1>Login realizado com sucesso</h1>"
            )


def start_server():
    """
    Função que inicia o servidor local para receber o callback do Spotify
    """

    server = HTTPServer(("127.0.0.1", 8888), CallbackHandler)
    print("Servidor iniciado em http://127.0.0.1:888")

    server.handle_request()

    return auth_code