from http.server import BaseHTTPRequestHandler, HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content_type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>hello!</body></html>"
				self.wfile.write(output.encode())
				print(output)

		except IOError:
			self.sent_error(404, "file not found %s" %self.path)

def main():
	try:
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print("web server running on port %s" % port)
		server.serve_forever()

	except KeyboardInterrupt:
		server.socket.close()
	
if __name__ == '__main__':
	main()