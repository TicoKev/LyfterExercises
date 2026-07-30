class Category:
  def __init__(self, category_type, color):
    if not category_type or not isinstance(category_type, str):
      raise ValueError("Category type must be a non-empty string.")
    if not color or not isinstance(color, str):
      raise ValueError("Color must be a valid string.")
    self.category_type = category_type.strip()
    self.color = color.strip()
