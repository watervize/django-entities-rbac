from django.apps import AppConfig

from entities_rbac.loader import load_roles_and_permissions


class EntitiesRBAC(AppConfig):
    name = "entities_rbac"
    verbose_name = "Django Entities RBAC"

    def ready(self):
        load_roles_and_permissions()
