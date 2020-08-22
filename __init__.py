import os,sys
from django.conf import settings
ROOT_PATH=str(os.path.sep).join(str(settings.BASE_DIR).split(os.path.sep)[:-2])
if ROOT_PATH not in sys.path:sys.path.append(ROOT_PATH)