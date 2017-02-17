import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print('claro', BASE_DIR)


MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
