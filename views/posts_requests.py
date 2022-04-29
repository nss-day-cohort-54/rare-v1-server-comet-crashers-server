# the HTTP methods for posts will go here
import sqlite3
import json
from datetime import datetime
from models.category import Category
from models.tag import Tag
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
            t.id tag_id,
            t.label,
            c.label category_label
        FROM Posts p  
        JOIN Users u
            On u.id = p.user_id
        JOIN Categories c
            On c.id = p.category_id
        JOIN PostTags as pt
            On pt.post_id = p.id   
        JOIN Tags as t
            On t.id = pt.tag_id 
        ORDER BY p.id  
        """)
        
        posts = []
        
        dataset = db_cursor.fetchall()       
        post = Post(0, 0, 0, 0,'', '', '')
        for row in dataset:
            if row['id'] != post.id:
                post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['content'], row['publication_date'], "", [])
                post.user = f"{row['first_name']}  {row['last_name']}"
                post.category = row['category_label']
            
            # post.user = user.__dict__
            # post.category = category.__dict__
            tag = Tag(row['tag_id'],row['label'])
            post.tags.append(tag.__dict__)
            try:
                if dataset[dataset.index(row)]['id'] != dataset[(dataset.index(row)) +1]['id']:              
                    posts.append(post.__dict__)
            except:
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
            t.id tag_id,
            t.label,
            c.label category_label
        FROM Posts p  
        JOIN Users u
            On u.id = p.user_id
        JOIN Categories c
            On c.id = p.category_id
        JOIN PostTags as pt
            On pt.post_id = p.id   
        JOIN Tags as t
            On t.id = pt.tag_id 
        WHERE p.id = ?
        ORDER BY p.id  
        """, (id, ))
        
        dataset = db_cursor.fetchall()       
        post = Post(0, 0, 0, 0,'', '', '')
        for row in dataset:
            if row['id'] != post.id:
                post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['content'], row['publication_date'], "", [])
                post.user = f"{row['first_name']}  {row['last_name']}"
                post.category = row['category_label']
            
            # post.user = user.__dict__
            # post.category = category.__dict__
            tag = Tag(row['tag_id'],row['label'])
            post.tags.append(tag.__dict__)
            try:
                if dataset[dataset.index(row)]['id'] != dataset[(dataset.index(row)) +1]['id']:              
                    post.__dict__
            except:
                post.__dict__
        
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
        
        for tag in new_post['tags']:
            db_cursor.execute("""
            INSERT INTO PostTags
                ( post_id, tag_id  )
            VALUES
                ( ?, ?);
            """, (new_post['id'], tag,  ))
        
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
        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE post_id = ?              
        """, (id, )) 
        for tag in new_post['tags']:
            db_cursor.execute("""
            INSERT INTO PostTags
                ( post_id, tag_id )
            VALUES
                ( ?, ?);
            """, (id, tag, ))
        

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
        
        db_cursor.execute("""
        DELETE FROM PostTag
        WHERE post_id = ?              
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
            p.content,
            p.publication_date,
            u.username username,
            u.first_name first_name,
            u.last_name last_name,
            t.id tag_id,
            t.label,
            c.label category_label
        FROM Posts p  
        JOIN Users u
            On u.id = p.user_id
        JOIN Categories c
            On c.id = p.category_id
        JOIN PostTags as pt
            On pt.post_id = p.id   
        JOIN Tags as t
            On t.id = pt.tag_id 
        WHERE p.user_id = ?   
        ORDER BY p.id  
        """, (user_id, ))

        posts = []
        
        dataset = db_cursor.fetchall()       
        post = Post(0, 0, 0, 0,'', '', '')
        for row in dataset:
            if row['id'] != post.id:
                post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['content'], row['publication_date'], "", [])
                post.user = f"{row['first_name']}  {row['last_name']}"
                post.category = row['category_label']
            
            # post.user = user.__dict__
            # post.category = category.__dict__
            tag = Tag(row['tag_id'],row['label'])
            post.tags.append(tag.__dict__)
            try:
                if dataset[dataset.index(row)]['id'] != dataset[(dataset.index(row)) +1]['id']:              
                    posts.append(post.__dict__)
            except:
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
            t.id tag_id,
            t.label,
            c.label category_label
        FROM Posts p  
        JOIN Users u
            On u.id = p.user_id
        JOIN Categories c
            On c.id = p.category_id
        JOIN PostTags as pt
            On pt.post_id = p.id   
        JOIN Tags as t
            On t.id = pt.tag_id 
        WHERE p.category_id = ?   
        ORDER BY p.id 
        """, (category_id, ))

        posts = []
        
        dataset = db_cursor.fetchall()       
        post = Post(0, 0, 0, 0,'', '', '')
        for row in dataset:
            if row['id'] != post.id:
                post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['content'], row['publication_date'], "", [])
                post.user = f"{row['first_name']}  {row['last_name']}"
                post.category = row['category_label']
            
            # post.user = user.__dict__
            # post.category = category.__dict__
            tag = Tag(row['tag_id'],row['label'])
            post.tags.append(tag.__dict__)
            try:
                if dataset[dataset.index(row)]['id'] != dataset[(dataset.index(row)) +1]['id']:              
                    posts.append(post.__dict__)
            except:
                posts.append(post.__dict__)
        
    return json.dumps(posts)
