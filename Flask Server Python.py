from flask import Flask, request, jsonify

app = Flask(__name__)
live_signals = []

@app.route("/signal", methods=["POST"])
def receive_signal():
    data = request.get_json()
    live_signals.append(data)
    print("Signal Received:", data)
    return jsonify({"status": "ok"})

@app.route("/get-signals", methods=["GET"])
def get_signals():
    return jsonify(live_signals[-10:])  # সর্বশেষ ১০টা সিগন্যাল

if __name__ == "__main__":
    app.run(port=5000)
