# constructor for post will go here
class Post():
    def __init__(self, id, user_id, category_id, title, content, publication_date, image_url=""):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.content = content
        self.publication_date = publication_date
        self.image_url = image_url
