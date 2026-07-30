def get_category_by_name(category_list, name):
    return next((c for c in category_list if c.category_type == name), None)


def get_category_color(category_list, name):
    obj = next((c for c in category_list if c.category_type == name), None)
    return obj.color if obj else ""