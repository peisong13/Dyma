import os
import json

from ..dymaHandler import FileHandler, DocHandler
from ..util import sort_file_by_ids

class Features:
    def __init__(self, token):
        self.token = token
        self.file = FileHandler(self.token)

    def backup(self, path=None):

        # fetch all files
        json_response = self.file.fetch_all().json()
        all_files = json_response['files']
        root_file_id = json_response['root_file_id']

        # sort
        sorted_files = sort_file_by_ids(all_files, root_file_id)

        self.recr_fetch_and_save(sorted_files, path)


    def recr_fetch_and_save(self, file: dict, path: str | None) -> None:

        ''' recursively save file to path '''

        if not path:
            path = os.getcwd()
        else:
            path = os.path.abspath(path) if os.path.isabs(path) else os.path.join(os.getcwd(), path)

        # save file, if file is a document, get its content and sort it by ids and save it
        # if file is a folder, make a folder and recursively save its children
        if file.get('type') == 'document':
            filename = file.get('title') + '.json'
            filepath = os.path.join(path, filename)

            file_content = DocHandler(self.token).get(id=file.get('id')).json()
            file_content['nodes'] = sort_file_by_ids(file_content['nodes'])

            with open(filepath, 'w', encoding='utf-8') as f:
                print(f"save {filename} to {filepath}")
                json.dump(file_content, f, ensure_ascii=False, indent=4)

        elif file.get('type') == 'folder':
            foldername = file.get('title')
            folderpath = os.path.join(path, foldername)

            print(f"make folder {foldername} in {folderpath}")
            os.mkdir(folderpath)

            for child in file.get('children_node'):
                self.recr_fetch_and_save(child, folderpath)
