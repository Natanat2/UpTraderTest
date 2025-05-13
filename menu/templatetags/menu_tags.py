from django import template
from django.urls import resolve
from menu.models import Menu, MenuItem
from collections import defaultdict

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    items = MenuItem.objects.filter(menu=menu).select_related('parent')

    current_path = request.path
    active_item = None

    for item in items:
        if item.get_url() == current_path:
            active_item = item
            break

    tree = defaultdict(list)
    item_dict = {}

    for item in items:
        tree[item.parent_id].append(item)
        item_dict[item.id] = item

    open_ids = set()
    if active_item:
        current = active_item
        while current:
            open_ids.add(current.id)
            current = current.parent
        for child in tree.get(active_item.id, []):
            open_ids.add(child.id)

    def build_tree(parent_id=None):
        result = []
        for item in tree.get(parent_id, []):
            result.append({
                'item': item,
                'children': build_tree(item.id),
                'open': item.id in open_ids,
                'active': item == active_item,
            })
        return result

    return {'menu_tree': build_tree(None)}
