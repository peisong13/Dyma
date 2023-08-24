import requests

from .dymaAction import FileEdit, FileFetchAll, FileMove, FileCreate
from .dymaAction import DocGet, DocCheck, DocInsert, DocEdit, DocMove, DocDelete
from .dymaAction import SendToInbox, Upload, GetPreference, SetPreference

class FileHandler:
    def __init__(self, token):
        self.token = token

    def __call__(self, action=None, **kwargs):
        assert action in ['fetch_all', 'edit', 'move', 'create']
        # given str action, call the corresponding method, use dict to pass kwargs
        dymaAction = {
            'fetch_all': FileFetchAll,
            'edit': FileEdit,
            'move': FileMove,
            'create': FileCreate
        }
        return self.handler(self, action=dymaAction[action], **kwargs)

    # if there are kwargs, let general handler handle it
    @staticmethod
    def handler(self, action=None, **kwargs):
        json_data = {
            'token': self.token
        }
        json_data = json_data | action.act(**kwargs)
        print(f"{json_data=}")
        results = requests.post(action.post_url, json=json_data)
        return results
    
    ###
    # actual apis, fecth_all, edit, move, create

    def fetch_all(self):
        return self.handler(self, action=FileFetchAll)
    
    def edit(self, **kwargs):
        # print('edit', kwargs)
        return self.handler(self, action=FileEdit, **kwargs)

    def move(self, **kwargs):
        return self.handler(self, action=FileMove, **kwargs)

    def create(self, **kwargs):
        return self.handler(self, action=FileCreate, **kwargs)

class DocHandler:
    def __init__(self, token):
        self.token = token

    def __call__(self, action=None, **kwargs):
        # assert action
        assert action in ['insert', 'edit', 'move', 'delete', 'get', 'check']
        # given str action, call the corresponding method, use dict to pass kwargs
        dymaAction = {
            'insert': DocInsert,
            'edit': DocEdit,
            'move': DocMove,
            'delete': DocDelete,
            'get': DocGet,
            'check': DocCheck
        }
        return self.handler(self, action=dymaAction[action], **kwargs)

    @staticmethod
    def handler(self, action=None, **kwargs) -> requests.Response:
        json_data = {
            'token': self.token
        }
        json_data = json_data | action.act(**kwargs)
        print(f"{json_data=}")
        results = requests.post(action.post_url, json=json_data)
        return results

    ###
    # actual apis, get, check, insert, edit, move, delete

    def get(self, id=None):
        return self.handler(self, action=DocGet, id=id)
    
    def check(self, ids):
        return self.handler(self, action=DocCheck, ids=ids)
    
    def insert(self, **kwargs):
        ## if there is no parent_id, set it to root
        if kwargs.get('parent_id') is None:
            kwargs['parent_id'] = 'root'
        return self.handler(self, action=DocInsert, **kwargs)
    
    def edit(self, **kwargs):
        return self.handler(self, action=DocEdit, **kwargs)
    
    def move(self, **kwargs):
        return self.handler(self, action=DocMove, **kwargs)
    
    def delete(self, **kwargs):
        return self.handler(self, action=DocDelete, **kwargs)

    
class AccountHandler:
    def __init__(self, token):
        self.token = token

    def __call__(self, action=None, **kwargs):
        assert action in ['send_to_inbox', 'upload', 'get_preference', 'set_preference']
        # given str action, call the corresponding method, use dict to pass kwargs
        dymaAction = {
            'send_to_inbox': SendToInbox,
            'upload': Upload,
            'get_preference': GetPreference,
            'set_preference': SetPreference
        }
        return self.handler(self, action=dymaAction[action], **kwargs)
    
    @staticmethod
    def handler(self, action=None, **kwargs):
        json_data = {
            'token': self.token
        }
        json_data = json_data | action.act(**kwargs)
        print(f"{json_data=}")
        results = requests.post(action.post_url, json=json_data)
        return results
    
    ###
    # actual apis, send_to_inbox, upload, get_preference, set_preference
    def send_to_inbox(self, **kwargs):
        return self.handler(self, action=SendToInbox, **kwargs)
    
    def upload(self, **kwargs):
        return self.handler(self, action=Upload, **kwargs)
    
    def get_preference(self, **kwargs):
        return self.handler(self, action=GetPreference, **kwargs)
    
    def set_preference(self, **kwargs):
        return self.handler(self, action=SetPreference, **kwargs)

