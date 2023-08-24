# Dyma: Your Dynalist Manager

Note: this project is in very early stage. Major changes could happen and cause conflict with current usage. 

## Features

Dynalist API manager, written in Python.

Back up all your files and folders in just one line.

## Usage

### 1. start

```python
from dyma import DyManager

dm = DyManager(token="") # insert your token here

# or
dm = DyManager()
dm.token = "" # insert your token here
```

### 2. file-level usage

```python
# fetch all files
files = dm.file.fetch_all()

# make changes: move, edit, create
results = dm.file.edit(type='document', id="your document id", title="new title")

results = dm.file.move(type='folder', id="your foler id", parent_id="parent id", index=3)

results = dm.file.create(type='document', parent_id='parent id', index=3, title='new title')

# the above equals to

results = dm.file(action='edit', ...) # action= edit | move | create, other paramters are the same
```

### 3. document-level usage

```python
# get content of a document
results = dm.doc.get(id="your file id")

# check if documents has been updated
result = dm.doc.check(ids="your file ids") # or use list of file ids

# make change to che content of a document
results = dm.doc.insert(id='your doc id', parent_id = 'parent node id (default: root)', content='hello world')

result = dm.doc.edit(id='your doc id', node_id='node id', content='hello world')

result = dm.doc.move(id='your doc id', node_id='node id', parent_id='parent node id', index=3)

result = dm.doc.delete(id='your doc id', node_id='node id')

results = dm.doc(action='insert',...) # action= insert | edit | move | delete, other paramters are the same
```

### 4. account-level usage
```python
# sent to inbox
results = dm.send_to_inbox(index=-1, content='hello world', note="", checked=True, checkbox=True)

# upload file (Pro only)
results = dm.upload(filename='', content_type='', data='')

# get preference
result = dm.get_preference(key='')

# set preference
result = dm.set_preference(key='', value='')
```

### 5. advanced features
```python
# one-line backup
dm.backup()
```
