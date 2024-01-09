import requests
from cryptography.fernet import Fernet

# Replace 'cloud_url' with the ngrok-generated HTTPS URL
cloud_url = 'https://your_ngrok_url.ngrok.io/store_data'

# Replace this key with your own Fernet key generated using Fernet.generate_key()
key = b'your_generated_key_here'

cipher_suite = Fernet(key)

# Encrypt function
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

# Read health data (e.g., temperature, heartbeat)
health_data = "Temperature: 37C, Heartbeat: 75bpm"

# Encrypt health data
encrypted_data = encrypt_data(health_data)

# Send encrypted data to the cloud
response = requests.post(cloud_url, data={'encrypted_data': encrypted_data}, verify=False)

print(response.text)
