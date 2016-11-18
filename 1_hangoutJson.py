import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import seaborn.apionly as sns

from datetime import datetime

plt.style.use('bmh')
colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00',
          '#CC79A7', '#56B4E9', '#009E73', '#F0E442', '#0072B2']

# Import json data
with open('E:\Downloads\hangout.json', encoding="utf8") as json_file:
    json_data = json.load(json_file)


# Generate map from gaia_id to real name
def user_name_mapping(data):
    user_map = {'gaia_id': ''}
    for state in data['conversation_state']:
        participants = state['conversation_state']['conversation']['participant_data']
        for participant in participants:
            if 'fallback_name' in participant:
                user_map[participant['id']['gaia_id']] = participant['fallback_name']

    return user_map


# Parse data into flat list
def fetch_messages(data):
    messages = []
    for state in data['conversation_state']:
        conversation_state = state['conversation_state']
        conversation = conversation_state['conversation']
        conversation_id = conversation_state['conversation']['id']['id']
        participants = conversation['participant_data']

        all_participants = []
        for participant in participants:
            if 'fallback_name' in participant:
                user = participant['fallback_name']
            else:
                # Scope to call G+ API to get name
                user = participant['id']['gaia_id']
            all_participants.append(user)
            num_participants = len(all_participants)

        for event in conversation_state['event']:
            try:
                sender = user_dict[event['sender_id']['gaia_id']]
            except:
                sender = event['sender_id']['gaia_id']

            timestamp = datetime.fromtimestamp(float(float(event['timestamp']) / 10 ** 6.))
            event_id = event['event_id']

            if 'chat_message' in event:
                content = event['chat_message']['message_content']
                if 'segment' in content:
                    segments = content['segment']
                    for segment in segments:
                        if 'text' in segment:
                            message = segment['text']
                            message_length = len(message)
                            message_type = segment['type']
                            if len(message) > 0:
                                messages.append((conversation_id,
                                                 event_id,
                                                 timestamp,
                                                 sender,
                                                 message,
                                                 message_length,
                                                 all_participants,
                                                 ', '.join(all_participants),
                                                 num_participants,
                                                 message_type))

    messages.sort(key=lambda x: x[0])
    return messages


# Parse data into data frame
cols = ['conversation_id', 'event_id', 'timestamp', 'sender',
        'message', 'message_length', 'participants', 'participants_str',
        'num_participants', 'message_type']

data1=json_data['0']
# for i in json_data['conversation_state']:
#     print(2)
