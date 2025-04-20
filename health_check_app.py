from flask import Flask, jsonify
import datetime
import logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(filename='health.log', level=logging.INFO)

@app.route('/health')
def health_check():
    timestamp = datetime.datetime.now().isoformat()
    logging.info(f"Health check at {timestamp}")
    return jsonify({"status": "healthy", "timestamp": timestamp})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
