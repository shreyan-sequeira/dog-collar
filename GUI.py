import tkinter as tk
from tkinter import ttk
import geocoder

class GPSDesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPS Tracker App")

        # Labels for longitude and latitude
        self.longitude_label = ttk.Label(root, text="Longitude:")
        self.longitude_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.latitude_label = ttk.Label(root, text="Latitude:")
        self.latitude_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Get the current location based on the IP address
        location = geocoder.ip('me')
        if location.latlng:
            longitude, latitude = location.latlng
            # Update the GUI with the new coordinates
            self.longitude_label.config(text=f"Longitude: {longitude}")
            self.latitude_label.config(text=f"Latitude: {latitude}")
        else:
            self.longitude_label.config(text="Longitude: Unknown")
            self.latitude_label.config(text="Latitude: Unknown")

# Adjust the main function to start the GUI application
def main():
    root = tk.Tk()
    app = GPSDesktopApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


