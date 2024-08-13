-- Database initialization script

-- Table for talked time metrics
CREATE TABLE talked_time (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    session_id UUID NOT NULL,
    talked_time FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    location TEXT
);

-- Table for microphone usage metrics
CREATE TABLE microphone_used (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    session_id UUID NOT NULL,
    microphone_used BOOLEAN NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    microphone_type TEXT
);

-- Table for speaker usage metrics
CREATE TABLE speaker_used (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    session_id UUID NOT NULL,
    speaker_used BOOLEAN NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    speaker_type TEXT
);

-- Table for voice sentiment metrics
CREATE TABLE voice_sentiment (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    session_id UUID NOT NULL,
    voice_sentiment TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    confidence_score FLOAT
);

-- Indexes for performance on talked_time table
CREATE INDEX idx_user_id ON talked_time(user_id);
CREATE INDEX idx_session_id ON talked_time(session_id);
CREATE INDEX idx_timestamp ON talked_time(timestamp);

-- Indexes for performance on microphone_used table
CREATE INDEX idx_user_id_microphone ON microphone_used(user_id);
CREATE INDEX idx_session_id_microphone ON microphone_used(session_id);
CREATE INDEX idx_timestamp_microphone ON microphone_used(timestamp);

-- Indexes for performance on speaker_used table
CREATE INDEX idx_user_id_speaker ON speaker_used(user_id);
CREATE INDEX idx_session_id_speaker ON speaker_used(session_id);
CREATE INDEX idx_timestamp_speaker ON speaker_used(timestamp);

-- Indexes for performance on voice_sentiment table
CREATE INDEX idx_user_id_sentiment ON voice_sentiment(user_id);
CREATE INDEX idx_session_id_sentiment ON voice_sentiment(session_id);
CREATE INDEX idx_timestamp_sentiment ON voice_sentiment(timestamp);
