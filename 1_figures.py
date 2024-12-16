#принцип изначально нарушался в наследующем классе Square:
#в Square ширина и высота всегда должны быть равны, так как это квадрат.
#если бы мы создали объект Square и установили его ширину через свойство width, 
#то, при отсутствии специальной обработки, высота осталась бы неизменной, 
#что нарушило бы инвариант квадрата (равенство сторон).
#для решения задачи используем свойства и переопределчем их так, чтобы при установке ширины и высоты 
#в квадрате изменялись обе стороны, сохраняя одинаковые значения.
#тем самым принцип больше не нарушен: теперь, если мы изменим ширину квадрата, 
#автоматически изменится и высота (и наоборот), поддерживая равенство сторон.
class Shape:
  #базовый класс для фигур с координатами x и y
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y  

class Rectangle(Shape):
  def __init__(self, width, height, x=0, y=0):
    super().__init__(x, y)
    self._width = width
    self._height = height

  @property
  def width(self):
    return self._width #возвращаем ширину прямоугольника

  @width.setter
  def width(self, value):
    self._width = value #устанавливаем значение ширины прямоугольника

  @property
  def height(self):
    return self._height #возвращаем высоту прямоугольника

  @height.setter
  def height(self, value):
    self._height = value #устанавливаем значение высоты прямоугольника

class Square(Rectangle):
  def __init__(self, side, x=0, y=0):
    super().__init__(side, side, x, y)
    
class Square1(Rectangle):
  def __init__(self, side, x=0, y=0):
    super().__init__(side, side, x, y)

  @property
  def width(self):
    return self._width #возвращаем ширину квадрата

  @width.setter
  def width(self, value):
    self._width = value
    self._height = value  #устанавливаем одинаковые значения для ширины и высоты квадрата

  @property
  def height(self):
    return self._height #возвращаем высоту квадрата

  @height.setter
  def height(self, value):
    self._height = value
    self._width = value  #устанавливаем одинаковые значения для ширины и высоты квадрата

#протестируем: покажем, что класс Square нарушает LSP, класс Square1 этот принцип нарушать не будет

print("Пример для Square:")
square = Square(4)
print("Изначальная ширина:", square.width)
print("Изначальная высота:", square.height)

#изменение только ширины
square.width = 8
print("После изменения ширины:")
print("Ширина:", square.width)  # 8
print("Высота:", square.height)  # 4 (нарушение: стороны квадрата должны быть равны)

print("\nПример для Square1:")
square1 = Square1(4)
print("Изначальная ширина:", square1.width)
print("Изначальная высота:", square1.height)

#изменение ширины
square1.width = 8
print("После изменения ширины:")
print("Ширина:", square1.width)  # 8
print("Высота:", square1.height)  # 8 (корректное поведение: стороны равны)

#изменение высоты
square1.height = 6
print("После изменения высоты:")
print("Ширина:", square1.width)  #6
print("Высота:", square1.height)  #6 (корректное поведение: стороны равны)
