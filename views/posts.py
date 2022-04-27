# the HTTP methods for posts will go here
import sqlite3
import json
from datetime import datetime
from models.category import Category

from models.post import Post
from models.user import User

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
            p.publication_date,
            p.content,
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
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['content'])
            post.user = f"{row['first_name']}  {row['last_name']}"
            post.category = row['category_label']
            
        
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
            p.publication_date,
            p.content,
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
        
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'], data['publication_date'], data['content'])
        post.user = f"{data['first_name']}  {data['last_name']}"
        post.category = data['category_label']
        
        
        
        return json.dumps(post.__dict__)