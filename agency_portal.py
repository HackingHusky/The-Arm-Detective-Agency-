import os
import sys
import argparse
import http.server
from urllib.parse import parse_qs

# --- Dazai's Personal Detective Aesthetic ---
TRENCH_BROWN = "\033[38;5;137m"     # Detective Trench Coat Brown
BANDAGE_WHITE = "\033[38;5;253m"    # Crisp White Bandages
SUICIDE_BLUE = "\033[38;5;24m"      # Deep Melancholic River Blue
DETECTIVE_GRAY = "\033[38;5;244m"   # Apathetic Office Gray
RESET = "\033[0m"
BOLD = "\033[1m"

def print_banner():
    print(f"""{TRENCH_BROWN}{BOLD}
    ┌────────────────────────────────────────────────────────┐
    │  [🩹]  ARMED DETECTIVE AGENCY: WEB PORTAL              │
    │      "Bypass firewall rules via clean HTTP tunnels"    │
    └────────────────────────────────────────────────────────┘{RESET}""")

class AgencyPortalHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler allowing both directory downloads and clean file uploads."""
    
    def log_message(self, format, *args):
        """Overrides standard logging to make it cleaner under exam pressure."""
        sys.stderr.write(f"{DETECTIVE_GRAY}[*] Request Received -> {format%args}{RESET}\n")

    def do_POST(self):
        """Handles incoming file exfiltration uploads smoothly."""
        try:
            # Parse content length to process data streams accurately
            content_length = int(self.headers['Content-Length'])
            
            # Extract target filename from headers or query parameters if present
            filename = self.headers.get('X-File-Name', 'exfiltrated_loot.dat')
            
            # Read the incoming data stream
            post_data = self.rfile.read(content_length)
            
            # Prevent path traversal attacks inside our staging folder
            safe_filename = os.path.basename(filename)
            upload_path = os.path.join(os.getcwd(), safe_filename)
            
            with open(upload_path, 'wb') as f:
                f.write(post_data)
                
            print(f"{SUICIDE_BLUE}[+] NO LONGER HUMAN: File Successfully Intercepted -> {safe_filename} ({content_length} bytes){RESET}")
            
            # Respond with a successful landing confirmation code
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Data secured by the Armed Detective Agency.\n")
            
        except Exception as e:
            print(f"{TRENCH_BROWN}[!] Upload failed or was deflected: {e}{RESET}")
            self.send_response(500)
            self.end_headers()

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Dazai's Light HTTP Evasion Server")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Port to bind the web portal to (Default: 8080)")
    parser.add_argument("-d", "--directory", default=".", help="Directory to serve/store files (Default: current directory)")
    args = parser.parse_args()

    # Change working context to the targeted sharing space
    abs_share_dir = os.path.abspath(args.directory)
    os.chdir(abs_share_dir)

    server_address = ('0.0.0.0', args.port)
    httpd = http.server.HTTPServer(server_address, AgencyPortalHandler)

    print(f"{TRENCH_BROWN}{BOLD}[+] Web Portal active! Serving from: {abs_share_dir}{RESET}")
    print(f"{BANDAGE_WHITE}[*] Listening for traffic loops on port {args.port}... Close with Ctrl+C{RESET}\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{DETECTIVE_GRAY}[*] Shuttering agency portal. Footprints cleaned.{RESET}")

if __name__ == "__main__":
    main()
