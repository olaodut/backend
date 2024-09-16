from flask import Flask, jsonify
import nmap

app = Flask(__name__)

@app.route('/scan/<ip_range>', methods=['GET'])
def scan_network(ip_range):
    scanner = nmap.PortScanner()
    scanner.scan(ip_range, '1-1024', '-sV')
    scan_result = []

    for host in scanner.all_hosts():
        host_info = {
            "host": host,
            "state": scanner[host].state(),
            "open_ports": []
        }
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                host_info["open_ports"].append({
                    "port": port,
                    "state": scanner[host][proto][port]['state'],
                    "service": scanner[host][proto][port]['name']
                })
        scan_result.append(host_info)
    
    return jsonify(scan_result)

if __name__ == '__main__':
    app.run(debug=True)