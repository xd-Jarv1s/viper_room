import requests
import json
from datetime import datetime

# Define your Telegram bot token and channel ID
TOKEN = '7162097876:AAE27cvUGt6tUzuX3NI9VoNnoUsbNYYnBUM'
CHANNEL_ID = '-1002278281776'  # Use '@channelusername' or '-1001234567890'


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


# Get today's date in the format 'dd.mm.yy'
today_date = datetime.now().strftime('%d.%m.%y')
print(f"Today's date: {today_date}.")

# Load events from the file
events = load_events_from_file()

# Process each event and send the message to Telegram if the date matches today's date
for event in events:
    event_date = event.get('date', 'Unknown date')

    # Check if the event's date matches today's date
    if event_date == today_date:
        title = event.get('title', 'Unknown title')
        location = event.get('location', 'Viper Room')
        link = event.get('link', 'No link available')

        # Prepare the message
        message = (
            f"📅 *Event*: {title}\n"
            f"🗓 *Date*: {event_date}\n"
            f"📍 *Location*: Viper room\n"
            f"🔗 {link}"
        )

        # Send the message to Telegram
        response = send_telegram_message(message)
        if response.get('ok'):
            print(f"Message sent successfully for event '{title}'.")
        else:
            print(f"Failed to send message for event '{title}'. Response: {response}")
    else:
        print(f"Event '{event.get('title', 'Unknown title')}' is not scheduled for today. Skipping.")
