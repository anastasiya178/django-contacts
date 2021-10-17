"""Custom template tags"""

from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    """Creates a has_group template tag
    for hiding Delete and Create buttons depending on user permissions
    """
    group = Group.objects.get(name=group_name)
    if group in user.groups.all():
        return True
    return False
