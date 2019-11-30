# data-model-songplays

## Background

The analytics team for music streaming startup Spakify wants to anaylze the song-listening activity of their users.  This analysis will be based on JSON user activity logs and song metadata that exist on their mobile app. 

## Objective

The goal of this project is to design a database schema and create an ETL pipeline that enters data from the activity and song metadata JSON files, and deliver tables in a Postgres database against which the analtyics team can run optimized queries for performing song play analysis.

## Data model

<img src="songplays.png" width="75%" height="75%" />

## ETL summary

<ol>
<li>Process song files</li>
<ol>
<li>Insert unique <b>songs</b> records</li>
<li>Insert unique <b>artists</b> records</li>
</ol>
</li>
<li>Process log files</li>
<ol>
<li>Filter by "NextSong" action</li>
<li>Insert <b>time</b> records</li>
<li>Insert unique user records</li>
<li>Insert <b>songplays</b> records, getting songid and artistid from <b>songs</b> and <b>artists</b> tables, respetively</li>
</ol>
</ol> 

## Project files

- `sql_queries.py` - queries for creating tables and entering data
- `create_tables.py` - drops and creates tables, used to reset tables prior to running ETL scripts
- `etl.ipynb` - notebook for developing ETL process, runs insert queries with sample data from  `song_data` and `log_data`
- `test.ipynb` - selects and displays data from each table to ensure data is correctly entered 
- `etl.py` - primary ETL file, populates tables based on all activity and song metadata files

## Steps to run project

1. Create tables

```
python create_tables.py
```

2. Execute ETL pipeline

```
python etl.py
```