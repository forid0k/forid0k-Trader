import websocket
import json
import threading

# Asset list
ASSETS = ['EURUSD', 'GBPUSD', 'USDJPY', 'AUDUSD']

def on_message(ws, message):
    try:
        data = json.loads(message)
        if isinstance(data, dict):
            print("[RECEIVED]", json.dumps(data, indent=2))
    except Exception as e:
        print("Error decoding message:", e)

def on_error(ws, error):
    print("[ERROR]", error)

def on_close(ws, close_status_code, close_msg):
    print("[DISCONNECTED]")

def on_open(ws):
    print("[CONNECTED]")
    
    # Subscribe to multiple assets
    for asset in ASSETS:
        payload = {
            "event": "#subscribe",
            "data": {
                "room": f"candles-{asset}-60"
            }
        }
        ws.send(json.dumps(payload))
        print(f"[SUBSCRIBED] {asset}")

def run_socket():
    socket_url = "wss://ws2.market-qx.trade/socket.io/?EIO=3&transport=websocket"
    ws = websocket.WebSocketApp(
        socket_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

if __name__ == "__main__":
    socket_thread = threading.Thread(target=run_socket)
    socket_thread.start()
