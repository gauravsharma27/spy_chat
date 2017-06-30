from datetime import datetime
class Spy :
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online = True
        self.chat = []
        self.current_status_message = None
spy = Spy('holmes','mr','40',4.7)
friend_1 = Spy('john','mr','25','4.39')
friend_2 = Spy('jony','miss','28','4.98')
friend_3 = Spy('jack','mr','32','5')
friends = [friend_1,friend_2,friend_3]


class chatmessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
        
