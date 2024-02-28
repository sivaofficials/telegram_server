import requests
import time

bot_token = "6999655234:AAFQeUcvkEU0tZK3bIAInRK7dlAGPSBeEzU"
chat_id = "1719199629"


def get_public_ip():
    try:
        # Use a public IP address service
        response = requests.get('https://api64.ipify.org?format=json')
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response to get the IP address
            ip_address = response.json()['ip']
            print(f"Public IP address: {ip_address}")
            return ip_address
        else:
            message = f"Failed to retrieve public IP. Status Code: {response.status_code}"
            print(message)
            return message
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to get the initial public IP
initial_ip = get_public_ip()

# Corrected URL for sending a message
url_send_message = f'https://api.telegram.org/bot{bot_token}/sendMessage'

# Initial message with the public IP
initial_message_text = f"Your current public IP address is: {initial_ip}"

# Function to send a message
def send_message(chat_id, text):
    data = {'chat_id': chat_id, 'text': text}
    response_send_message = requests.post(url_send_message, data=data)
    data = response_send_message.json()
    print(f"Message sent to Telegram. Response: {data}")

# Call the function to send the initial message
send_message(chat_id, initial_message_text)

# Main loop to check for changes in public IP
while True:
    time.sleep(60)
    new_ip = get_public_ip()
    
    if new_ip != initial_ip:
        initial_ip = new_ip
        message_text = f"Your new public IP address is: {initial_ip}"
        send_message(chat_id, message_text)
    else:
        print("IP address unchanged.")
