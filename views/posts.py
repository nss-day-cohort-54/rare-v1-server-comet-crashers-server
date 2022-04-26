# the HTTP methods for posts will go here
import sqlite3
import json
from datetime import datetime
from models.category import Category

from models.post import Post
from models.user import User

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
            p.date,
            u.username username,
            u.first_name first_name,
            u.last_name last_name,
            c.label category_label
        FROM Posts p  
        JOIN Users u
            On u.id = p.users_id
        JOIN Categories c
            On c.id = p.category_id  
        ORDER BY p.date   
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        post = Post(data['id'], data['user_id'], data['category_id'], data['publication_date'], data['title'], data['content'])
        user = User(data['id'], data['first_name'], data['last_name'], data['username'])
        category = Category(data['id'], data['category_label'])
        
        post.user = user.__dict__
        post.category = category.__dict__
        
        
        
        return json.dumps(post.__dict__)