import tkinter as tk
from tkinter import ttk
import threading
import queue
import time

class GPSDesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPS Tracker App")

        # Labels for longitude and latitude
        self.longitude_label = ttk.Label(root, text="Longitude:")
        self.longitude_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.latitude_label = ttk.Label(root, text="Latitude:")
        self.latitude_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Queue for simulated GPS coordinates
        self.gps_queue = queue.Queue()

        # Start GPS tracking in a separate thread
        self.gps_thread = threading.Thread(target=self.track_gps)
        self.gps_thread.start()

    def track_gps(self):
        # Example coordinates
        coordinates = [(37.7749, -122.4194), (34.0522, -118.2437), (40.7128, -74.0060)]
        for coord in coordinates:
            # Put the coordinates into the queue
            self.gps_queue.put(coord)
            # Wait for a short period before generating new coordinates
            time.sleep(1)

    def update_gps_coordinates(self):
        if not self.gps_queue.empty():
            longitude, latitude = self.gps_queue.get()
            # Update the GUI with the new coordinates
            self.longitude_label.config(text=f"Longitude: {longitude}")
            self.latitude_label.config(text=f"Latitude: {latitude}")

    def mainloop(self):
        while True:
            self.root.update()
            self.update_gps_coordinates()
            time.sleep(0.01) # Prevent high CPU usage

# Adjust the main function to start the GUI application
def main():
    root = tk.Tk()
    app = GPSDesktopApp(root)
    app.mainloop()

if __name__ == "__main__":
    main()

