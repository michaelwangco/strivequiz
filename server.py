# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime
import time
import cgi
import sqlite3

hostName = "localhost"
serverPort = 8080

con = sqlite3.connect('quiz.db')
#cur = con.cursor()
#now = datetime.now()
#cur.execute("insert into question_response values (?, ?, ?, ?, ?)", (now, id+1, msg[response], msg[id], 1))
#con.commit()
#(creationdate, response_id, quiz_response, question_id, quiz_id)

class MyServer(BaseHTTPRequestHandler):
    response_id = 1

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _wrap_bytes(self, msg):
        return bytes(msg, "utf-8")

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        ls = []
        cur = con.cursor()
        for row in cur.execute("select question_id, prompt from quiz_questions where quiz_id = 1 order by question_id"):
            ls.append({'question_id': row[0], 'prompt': row[1]})
        self.wfile.write(self._wrap_bytes(json.dumps(ls)))

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        msg = json.loads(self.rfile.read(length))

        cur = con.cursor()
        now = datetime.now()
        self.response_id += 1
        cur.execute("insert into question_response values (?, ?, ?, ?, ?)",
                (now, response_id, msg[response], msg[question_id], 1))
        con.commit()

        # add a property to the object, just to mess with data
        message['received'] = 'ok'

        # send the message back
        self._set_headers()
        self.wfile.write(self._wrap_bytes(json.dumps(message)))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

    con.close()
    print("DB connection closed.")
