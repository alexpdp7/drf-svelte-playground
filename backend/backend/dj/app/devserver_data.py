from django.contrib.auth import models as auth_models
from django_tws import users
from backend.dj.app import models

admin = users.user_manager().create_superuser("admin", password="admin")
staff = users.user_manager().create_user("staff", password="staff", is_staff=True)
user = users.user_manager().create_user("user", password="user")

group = auth_models.Group(name="group")
group.save()

for permission in [
    "add_cat",
    "change_cat",
    "delete_cat",
    "view_cat",
]:
    permission = auth_models.Permission.objects.get(codename=permission)
    group.permissions.add(permission)

group.user_set.add(staff)

models.Cat(name="Cleo").save()
