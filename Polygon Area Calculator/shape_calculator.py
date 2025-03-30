class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self,new_width):
    self.width = new_width

  def set_height(self,new_height):
    self.height = new_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      string = ''
      height = self.height
      while height > 0:
        string += f'{"*" * self.width}\n'
        height -= 1
      return string

  def get_amount_inside(self, other_shape):
    width_per = int(self.width / other_shape.width)
    height_per = int(self.height / other_shape.height)
    if width_per >= 1 and height_per >= 1:
      return width_per * height_per
    else:
      return 0
  
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side

  def set_width(self,new_width):
    self.set_side(new_width)

  def set_height(self,new_height):
    self.set_side(new_width)
