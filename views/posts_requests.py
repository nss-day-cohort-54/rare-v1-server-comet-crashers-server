# the HTTP methods for posts will go here
import sqlite3
import json
from datetime import datetime
from models.category import Category
from models.user import User
from models.post import Post


def get_all_posts():
    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.content,
            p.publication_date,
            u.username username,
            u.first_name first_name,
            u.last_name last_name,
            c.label category_label
        FROM Posts p  
        JOIN Users u
            On u.id = p.user_id
        JOIN Categories c
            On c.id = p.category_id 
        
        ORDER BY p.publication_date  
        """)
        
        posts = []
        
        dataset = db_cursor.fetchall()
        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['content'], row['publication_date'])
            post.user = f"{row['first_name']}  {row['last_name']}"
            post.category = row['category_label']
            
            # post.user = user.__dict__
            # post.category = category.__dict__
            
            posts.append(post.__dict__)
        
    return json.dumps(posts)
def get_single_post(id):
    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.content,
            p.publication_date,
            u.username username,
            u.first_name first_name,
            u.last_name last_name,
            c.label category_label
        FROM Posts p  
        JOIN Users u
            On u.id = p.user_id
        JOIN Categories c
            On c.id = p.category_id 
        WHERE p.id = ? 
        ORDER BY p.publication_date  
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'], data['content'], data['publication_date'])
        post.user = f"{data['first_name']}  {data['last_name']}"
        post.category = data['category_label']

        return json.dumps(post.__dict__)
def create_post(new_post):
    with sqlite3.connect("./rare.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute(""" 
        INSERT INTO Posts
            (user_id, category_id, title, content, publication_date )
        VALUES
            ( ?, ?, ?, ?, ? );              
        """, ( new_post['userId'], 
            new_post['categoryId'], 
            new_post['title'], 
            new_post['content'], 
            datetime.now(),
            ))
        id = db_cursor.lastrowid
        
        new_post['id'] = id
        
    return json.dumps(new_post)
def update_post(id, new_post):
    with sqlite3.connect("./rare.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                content = ?,
                publication_date = ?
        WHERE id = ?
        """, ( new_post['userId'], 
            new_post['categoryId'], 
            new_post['title'],  
            new_post['content'], 
            new_post['publicationDate'], id,  ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def delete_post(id):
    with sqlite3.connect("./rare.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))
        
def get_posts_by_user(user_id):

    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.content,
            u.username username,
            u.first_name first_name,
            u.last_name last_name
        FROM Posts p  
        JOIN Users u
            On u.id = p.user_id 
        WHERE user_id = ?   
        """, (user_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'],

                        row['title'], row['publication_date'], row['content'])
            post.user = f"{row['first_name']}  {row['last_name']}"

            post.category = row['category_label']

            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)

    return json.dumps(posts)

# Given the user is on the /posts
# When they select a category from the "Search by Category" dropdown
# Then the list should update to show only posts from that category

def get_posts_by_category(category_id):

    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.content,
            p.publication_date,
            u.username username,
            u.first_name first_name,
            u.last_name last_name,
            c.label category_label
        FROM Posts p  
        JOIN Users u
            On u.id = p.user_id
        JOIN Categories c
            On c.id = p.category_id 
        WHERE category_id = ?   
        ORDER BY p.publication_date
        """, (category_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'],
                        row['title'], row['publication_date'], row['content'])

            post.user = f"{row['first_name']}  {row['last_name']}"
            post.category = row['category_label']
            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)

    return json.dumps(posts)
