from hatchet_sdk import Hatchet
import os

# Initialize Hatchet client
print("Initializing Hatchet client...")
print(f"HATCHET_CLIENT_HOST: {os.getenv('HATCHET_CLIENT_HOST')}")
print(f"HATCHET_CLIENT_PORT: {os.getenv('HATCHET_CLIENT_PORT')}")
print(f"HATCHET_CLIENT_TLS_STRATEGY: {os.getenv('HATCHET_CLIENT_TLS_STRATEGY')}")
print(f"HATCHET_CLIENT_TOKEN exists: {bool(os.getenv('HATCHET_CLIENT_TOKEN'))}")

hatchet = Hatchet(debug=True)
print("Hatchet client initialized.")
print(f"Hatchet client details: {hatchet.__dict__}")