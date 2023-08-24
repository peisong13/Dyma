
from .features import Features
from .dymaHandler import FileHandler, DocHandler, AccountHandler


class DyManager:

    def __init__(self, token):
 
        self.token = token
    
        # let FileHandler and DocHandler be the intsance of Dyma
        self.file = FileHandler(self.token)
        self.doc = DocHandler(self.token)
        self.account = AccountHandler(self.token)
        self.features = Features(self.token)

    # apis directly used
    def send_to_inbox(self, **kwargs):
        return self.account.send_to_inbox(**kwargs)

    def upload(self, **kwargs):
        return self.account.upload(**kwargs)

    def get_preference(self, **kwargs):
        return self.account.get_preference(**kwargs)

    def set_preference(self, **kwargs):
        return self.account.set_preference(**kwargs)
    
    def backup(self):
        self.features.backup()

