class User():
    def __init__(self, id, first_name, last_name, username, created_on="", active = 0, password="", profile_image_url="", email="",  bio=""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.created_on = created_on
        self.active = active
        self.password = password
        self.profile_image_url = profile_image_url
        self.email = email
        self.bio = bio
       