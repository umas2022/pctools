import os

def resource_path(relative_path):
    """ 返回静态资源的绝对路径定位到xxx/resource\n
    例如resource_path("img/mati_ei_256.ico")"""
    base_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.split(base_path)[0]
    return os.path.join(base_path, relative_path)