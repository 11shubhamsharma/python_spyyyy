# define calls user and chat message for use in main file
from datetime import datetime

class user:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class Chat_message:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = user('bond', 'Mr.', 24, 4.7)

friend_one = user('Raja', 'Mr.', 4.9, 27)
friend_two = user('Mata Hari', 'Ms.', 4.39, 21)
friend_three = user('No', 'Dr.', 4.95, 37)


friends_detail = [friend_one, friend_two, friend_three]#define list for use in main file