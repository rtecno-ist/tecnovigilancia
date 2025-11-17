import os
import django

# Cambia "tu_proyecto.settings" por tu path real de settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Cambia los datos del superusuario aquí
USERNAME = "rtecnoist"
EMAIL = "rtecnoist@gmail.com"
PASSWORD = "rtecnoist123"

# Verifica si ya existe
if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superusuario {USERNAME} creado correctamente.")
else:
    print(f"Superusuario {USERNAME} ya existe.")
