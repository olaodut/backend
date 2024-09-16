from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-scan', methods=['GET'])
def run_scan():
    # Running a simple Nmap scan
    result = subprocess.run(['nmap', '-sP', '192.168.1.1/24'], capture_output=True, text=True)
    return jsonify({"result": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)
