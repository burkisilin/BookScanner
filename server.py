from http.server import BaseHTTPRequestHandler
from os import getcwd

dosyadizini = getcwd()


class RequestHandler_httpd(BaseHTTPRequestHandler):

    def do_GET(self):
        sunucuverisi = self.requestline
        sunucuverisi = sunucuverisi[5: int(len(sunucuverisi) - 9)]
        print(f"Sunucu isteği alındı: {sunucuverisi}")

        f = open(f"{dosyadizini}\komut.txt", "w")
        f.write(sunucuverisi)
        f.close()

        yanitmesaji = bytes("Başarılı", "utf8")
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(yanitmesaji))
        self.end_headers()
        self.wfile.write(yanitmesaji)

        return
