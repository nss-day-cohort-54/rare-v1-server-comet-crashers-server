# the HTTP methods for posts will go here
import sqlite3
import json
from datetime import datetime

def get_all_entries():
    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date,
            t.id tag_id,
            t.tag,
            m.label mood_label
        FROM Entry e  
        JOIN Mood as m
            On m.id = e.mood_id 
        JOIN entrytag as et
            On et.entry_id = e.id   
        JOIN Tag as t
            On t.id = et.tag_id
        ORDER BY e.id   
        """)
        entries = []
        
        dataset = db_cursor.fetchall()
        entry = Entry(0,'','',0,'')
        for row in dataset:
            # not reset the entry if the entry exists, but still add tag onto entry's array
            if row['id'] != entry.id:
                # explicity set tags to a new list in model
                entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'], [])
                mood = Mood(row['id'], row['mood_label'])
                entry.mood = mood.__dict__
                
            tag = Tag(row['tag_id'],row['tag'])
            entry.tags.append(tag.__dict__)
            # does current row id match next row id,
            # if doesn't, then add entry 
            try:
                if dataset[dataset.index(row)]['id'] != dataset[(dataset.index(row)) +1]['id']:              
                    entries.append(entry.__dict__)
            except:
                entries.append(entry.__dict__)
        return json.dumps(entries)