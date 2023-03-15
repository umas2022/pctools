import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller \n
        定位到xxx/resource"""
    base_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.split(base_path)[0]
    return os.path.join(base_path, relative_path)