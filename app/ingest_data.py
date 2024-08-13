import psycopg2
import json
import os
from datetime import datetime

# Database connection details
DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://user:password@db:5432/metrics_db')

# Connect to the PostgreSQL database
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

def insert_talked_time(user_id, session_id, talked_time, timestamp, location):
    cursor.execute("""
        INSERT INTO talked_time (user_id, session_id, talked_time, timestamp, location)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, session_id, talked_time, timestamp, location))
    conn.commit()

def insert_microphone_used(user_id, session_id, microphone_used, timestamp, microphone_type):
    cursor.execute("""
        INSERT INTO microphone_used (user_id, session_id, microphone_used, timestamp, microphone_type)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, session_id, microphone_used, timestamp, microphone_type))
    conn.commit()

def insert_speaker_used(user_id, session_id, speaker_used, timestamp, speaker_type):
    cursor.execute("""
        INSERT INTO speaker_used (user_id, session_id, speaker_used, timestamp, speaker_type)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, session_id, speaker_used, timestamp, speaker_type))
    conn.commit()

def insert_voice_sentiment(user_id, session_id, voice_sentiment, timestamp, confidence_score):
    cursor.execute("""
        INSERT INTO voice_sentiment (user_id, session_id, voice_sentiment, timestamp, confidence_score)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, session_id, voice_sentiment, timestamp, confidence_score))
    conn.commit()

def fetch_and_process_data():
    data = [
        {
            "type": "talked_time",
            "user_id": "123e4567-e89b-12d3-a456-426614174000",
            "session_id": "789e4567-e89b-12d3-a456-426614174001",
            "talked_time": 120.5,
            "timestamp": datetime.now(),
            "location": "office"
        },
    ]

    for record in data:
        if record['type'] == 'talked_time':
            insert_talked_time(record['user_id'], record['session_id'], record['talked_time'], record['timestamp'], record['location'])
        elif record['type'] == 'microphone_used':
            insert_microphone_used(record['user_id'], record['session_id'], record['microphone_used'], record['timestamp'], record['microphone_type'])
        elif record['type'] == 'speaker_used':
            insert_speaker_used(record['user_id'], record['session_id'], record['speaker_used'], record['timestamp'], record['speaker_type'])
        elif record['type'] == 'voice_sentiment':
            insert_voice_sentiment(record['user_id'], record['session_id'], record['voice_sentiment'], record['timestamp'], record['confidence_score'])

if __name__ == "__main__":
    fetch_and_process_data()

# Close the database connection
cursor.close()
conn.close()
