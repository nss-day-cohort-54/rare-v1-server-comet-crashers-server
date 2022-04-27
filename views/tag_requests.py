import sqlite3
import json
from models import Tags

def get_all_tags():
    # Open a connection to the database
    with sqlite3.connect("./rare.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        """)

        # Initialize an empty list to hold all category representations
        tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an tag instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # tag class above.
            tag = Tags(row['id'], row['label'])

            tags.append(tag.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(tags)

def get_single_tag(id):
    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM tags t
        WHERE t.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a tag instance from the current row
        tags = Tags(data['id'], data['label'])

        return json.dumps(tags.__dict__)
    
def create_tag(new_tag):
    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? );
        """, ( new_tag['label'], ))
        
        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid
        
        
        
        dataset = db_cursor.fetchall()
    
        for tag in new_tag['tags']:
            db_cursor.execute("""
            INSERT INTO Tags
                ( id )
            VALUES
                ( ? );
            """, (id, ))

    return json.dumps(new_tag)