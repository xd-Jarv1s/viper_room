import requests
import json

# Define your Telegram bot token and channel ID
TOKEN = '7162097876:AAE27cvUGt6tUzuX3NI9VoNnoUsbNYYnBUM'
CHANNEL_ID = '-1002450905511'  # Use '@channelusername' or '-1001234567890'

# Function to send a message to Telegram
def send_telegram_message(message):
    print(f"Sending message to Telegram:\n{message}")
    response = requests.post(
        f'https://api.telegram.org/bot{TOKEN}/sendMessage',
        data={'chat_id': CHANNEL_ID, 'text': message, 'parse_mode': 'Markdown'}
    )
    print(f"Telegram response: {response.status_code} - {response.json()}")
    return response.json()

# Load events from viperroom_events.json file
def load_events_from_file():
    try:
        with open('viperroom_events.json', 'r', encoding='utf-8') as file:
            events = json.load(file)
            print(f"Loaded {len(events)} events from file.")
            return events
    except FileNotFoundError:
        print("The file 'viperroom_events.json' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error parsing the JSON file.")
        return []

# Load events from the external file
events = load_events_from_file()

# Process each event and send the message to Telegram
for event in events:
    title = event.get('title', 'Unknown title')
    start_date = event.get('date', 'Unknown date')
    location = event.get('location', 'Viper Room')
    link = event.get('link', 'No link available')

    # Prepare the message
    message = (
        f"📅 *Event*: {title}\n"
        f"🗓 *Date*: {start_date}\n"
        f"📍 *Location*: Viper Room\n"
        f"🔗 {link}"
    )

    # Send the message to Telegram
    response = send_telegram_message(message)
