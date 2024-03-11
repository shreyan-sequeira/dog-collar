import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt


class GPSDesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPS Tracker App")

        self.latitude_label = ttk.Label(root, text="Latitude:")
        self.latitude_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.longitude_label = ttk.Label(root, text="Longitude:")
        self.longitude_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # MQTT Settings
        self.mqtt_broker = "broker.hivemq.com"  # MQTT broker address
        self.mqtt_topic = "gps_coordinates"  # Replace with MQTT topic

        # MQTT Client
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message

        # Connect to the MQTT broker
        self.mqtt_client.connect(self.mqtt_broker, 1883, 60)

        # Start the MQTT loop (non-blocking)
        self.mqtt_client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        # Subscribe to the GPS coordinates topic
        client.subscribe(self.mqtt_topic)

    def on_message(self, client, userdata, msg):
        # Process the received GPS coordinates
        try:
            payload = msg.payload.decode("utf-8")
            latitude, longitude = map(float, payload.split(','))

            # Need to update UI with the latest GPS coordinates
            self.latitude_label.config(text=f"Latitude: {latitude}")
            self.longitude_label.config(text=f"Longitude: {longitude}")
        except Exception as e:
            print(f"Error processing message: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GPSDesktopApp(root)
    root.mainloop()
