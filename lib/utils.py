from flask import current_app, url_for
import os, re

def dated_url_for(endpoint, **values):
    if re.match('^static', endpoint):
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(current_app.root_path,
                                     endpoint, filename)
            values['cache_busting'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)