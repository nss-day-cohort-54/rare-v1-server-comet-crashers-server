# # the HTTP methods for posts will go here
# import sqlite3
# import json
# from datetime import datetime

# from models.post import Post
# from models.user import User

# def get_all_posts():
#     with sqlite3.connect("./rare.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
        
#         db_cursor = conn.cursor()
#         db_cursor.execute("""
#         SELECT
#             p.id,
#             p.user_id,
#             p.category_id,
#             p.title,
#             p.date,
#             u.username username,
#             c.label category_label
#         FROM Posts p  
#         JOIN Users u
#             On u.id = p.users_id
#         JOIN Categories c
#             On c.id = p.category_id  
#         ORDER BY p.date   
#         """)
#         posts = []
        
#         dataset = db_cursor.fetchall()
#         for row in dataset:
#             post = Post(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'], [])
#             user = User(row['id'], row['mood_label'])
#             category = Category(row['id'], row['category_label'])
            
#             post.user = user.__dict__
#             post.category = category.__dict__
            
#             posts.append = (post.__dict__)
        
#         return json.dumps(posts)