import os
from celery import Celery

# establece la variable de entorno DJANGO_SETTINGS_MODULE para que Celery sepa
# dónde están los ajustes de tu proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_site.settings')

app = Celery('blog_site')

# Aquí estamos utilizando el string 'django' para que Celery encuentre y cargue automáticamente
# el archivo de configuración de Django.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carga las tareas de los módulos 'tasks.py' en cada app Django.
app.autodiscover_tasks()

# Agregamos el pool que se va a ejecutar por defecto en este caso gevent
# Esto soluciona el bug en el que no funcionaba en windows https://github.com/celery/celery/issues/3759
app.conf.worker_pool = 'threads'