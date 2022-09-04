from django import template

from entities_rbac.checkers import has_role, has_permission, has_object_permission


register = template.Library()


@register.simple_tag(name="has", takes_context=True)
def has_roles_template_tag(context, permission, obj, user=None):
    if not user:
        user = context.get("user")

    if user:
        return has_roles(permission, user, obj)

    return False


@register.simple_tag(name="can", takes_context=True)
def has_permissions_template_tag(context, permission, obj, user=None):
    if not user:
        user = context.get("user")

    if user:
        return has_object_permissions(permission, user, obj)

    return False


@register.simple_tag(name="list_roles", takes_context=True)
def list_roles_template_tag(context, permission, obj, user=None):

    return False  # ToDo: A list of roles


@register.simple_tag(name="list_permissions", takes_context=True)
def list_permissions_template_tag(context, permission, obj, user=None):

    return False  # ToDo: A list of permissions
