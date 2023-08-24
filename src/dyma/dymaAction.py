class BaseAction:
    def __init__(self):
        pass

class FileAction(BaseAction):
    def __init__(self):
        pass

class DocAction(BaseAction):
    def __init__(self):
        pass

class AccountAction(BaseAction):
    def __init__(self):
        pass

# file actions
class FileFetchAll(FileAction):
    post_url = 'https://dynalist.io/api/v1/file/list'

    def __init__(self):
        pass

    @classmethod
    def act(cls) -> dict:
        return {}
    
class FileEdit(FileAction):
    
    post_url = 'https://dynalist.io/api/v1/file/edit'

    def __init__(self, **kwargs):
        pass
    
    @classmethod
    def act(cls, **kwargs) -> dict:
        assert kwargs.get('type') in ['document', 'folder']
        assert kwargs.get('file_id') is not None or kwargs.get('id') is not None

        if kwargs.get('id') is not None:
            kwargs['file_id'] = kwargs['id']
            del kwargs['id']

        return {
            'changes': [{"action": "edit"} | kwargs]
        }
    
class FileMove(FileAction):
    post_url = 'https://dynalist.io/api/v1/file/edit'

    def __init__(self, **kwargs):
        pass
    
    @classmethod
    def act(cls, **kwargs) -> dict:
        assert kwargs.get('type') in ['document', 'folder']
        assert kwargs.get('file_id') is not None or kwargs.get('id') is not None
        assert kwargs.get('parent_id') is not None
        assert kwargs.get('index') is not None

        if kwargs.get('id') is not None:
            kwargs['file_id'] = kwargs['id']
            del kwargs['id']

        return {
            'changes': [{"action": "move"} | kwargs]
        }

class FileCreate(FileAction):
    post_url = 'https://dynalist.io/api/v1/file/edit'

    def __init__(self, **kwargs):
        pass
    
    @classmethod
    def act(cls, **kwargs) -> dict:
        assert kwargs.get('type') in ['document', 'folder']
        assert kwargs.get('parent_id') is not None
        assert kwargs.get('index') is not None

        return {
            'changes': [{"action": "create"} | kwargs]
        }

# doc actions
class DocGet(DocAction):
    post_url = 'https://dynalist.io/api/v1/doc/read'

    def __init__(self):
        pass

    @classmethod
    def act(cls, id):
        return {
            'file_id': id
        }
    
class DocCheck(DocAction):
    post_url = 'https://dynalist.io/api/v1/doc/check_for_updates'

    def __init__(self):
        pass

    @classmethod
    def act(cls, ids):
        return {
            'file_ids': ids
        }
    
class DocInsert(DocAction):
    post_url = 'https://dynalist.io/api/v1/doc/edit'

    def __init__(self):
        pass

    @classmethod
    def act(cls, id, **kwargs):
        return {
            'file_id': id,
            'changes': [{"action": "insert"} | kwargs]
        }
    
class DocEdit(DocAction):
    post_url = 'https://dynalist.io/api/v1/doc/edit'

    def __init__(self):
        pass

    @classmethod
    def act(cls, id, **kwargs):
        return {
            'file_id': id,
            'changes': [{"action": "edit"} | kwargs]
        }

class DocMove(DocAction):
    post_url = 'https://dynalist.io/api/v1/doc/edit'

    def __init__(self):
        pass

    @classmethod
    def act(cls, id, **kwargs):
        return {
            'file_id': id,
            'changes': [{"action": "move"} | kwargs]
        }
    
class DocDelete(DocAction):
    post_url = 'https://dynalist.io/api/v1/doc/edit'

    def __init__(self):
        pass

    @classmethod
    def act(cls, id, **kwargs):
        return {
            'file_id': id,
            'changes': [{"action": "delete"} | kwargs]
        }
    
# account actions
class SendToInbox(AccountAction):
    post_url = 'https://dynalist.io/api/v1/inbox/add'

    def __init__(self):
        pass

    @classmethod
    def act(cls, **kwargs):
        return {
            'index': kwargs.get('index', -1),
            'content': kwargs.get('content', ''),
            'note': kwargs.get('note', ''),
            'checked': kwargs.get('checked', False),
            'checkbox': kwargs.get('checkbox', False),
            'heading': kwargs.get('heading', 0),
            'color': kwargs.get('color', 0),
        }

class Upload(AccountAction):
    post_url = 'https://dynalist.io/api/v1/upload'

    def __init__(self):
        pass

    @classmethod
    def act(cls, **kwargs):
        return {
            'filename': kwargs.get('filename', ''),
            'content_type': kwargs.get('content_type', ''),
            'data': kwargs.get('data', '')
        }
    
class GetPreference(AccountAction):
    post_url = 'https://dynalist.io/api/v1/pref/get'

    def __init__(self):
        pass

    @classmethod
    def act(cls, **kwargs):
        return {
            'key': kwargs.get('key', '')
        }
    
class SetPreference(AccountAction):
    post_url = 'https://dynalist.io/api/v1/pref/set'

    def __init__(self):
        pass

    @classmethod
    def act(cls, **kwargs):
        return {
            'key': kwargs.get('key', ''),
            'value': kwargs.get('value', '')
        }