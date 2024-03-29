# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users (user_id),
    level VARCHAR(10),
    song_id TEXT REFERENCES songs (song_id),
    artist_id TEXT REFERENCES artists (artist_id),
    session_id INTEGER,
    location VARCHAR(100),
    user_agent VARCHAR(200)
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender CHAR(1),
    level VARCHAR(10)
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id TEXT PRIMARY KEY,
    title VARCHAR(100),
    artist_id TEXT NOT NULL REFERENCES artists (artist_id),
    year INTEGER,
    duration FLOAT
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id TEXT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    latitude NUMERIC(8,6),
    longitude NUMERIC(9,6)
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday INTEGER
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = (""" 
SELECT s.song_id, a.artist_id 
FROM songs as s JOIN artists as a ON (s.artist_id=a.artist_id) 
WHERE s.title=(%s) AND a.name=(%s) AND s.duration=(%s);
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]