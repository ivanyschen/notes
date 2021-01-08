- zipping folder
```python
import os
import zipfile

def zip(source, destination=None):
    destination = '.'.join([source.split('.')[0], 'zip']) if destination is None else destination
    with zipfile.ZipFile(destination, 'w') as zip_file:
        for root, _, files in os.walk(source):
            for file in files:
                full_path = os.path.join(root, file)
                zip_file.write(full_path, os.path.relpath(full_path, source))
```
