import os
from django.shortcuts import redirect

def change_filename(filename):
    if ' ' in filename:
        filename = filename.replace(' ', '_')
    return filename

def create_file(filename, content):
    try:
        filename = change_filename(filename) + '.html'
        path = "media/fs_storage/doc"
        f = open(os.path.join(path, filename), 'wt', encoding='utf-8')
        f.write(content)
        f.close()

        return os.path.join(path, filename)
    except Exception as e:
        redirect('/')