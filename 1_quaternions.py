import math
import unittest
from math import sqrt, radians, sin, cos


class Quaternion:
    def __init__(self, w, x, y, z):
        """Инициализация кватерниона"""
        self.w = w  # Скалярная часть
        self.x = x  # Векторная часть (i)
        self.y = y  # Векторная часть (j)
        self.z = z  # Векторная часть (k)

    def __add__(self, other):
        """Сложение кватернионов"""
        return Quaternion(self.w + other.w,
                          self.x + other.x,
                          self.y + other.y,
                          self.z + other.z)

    def __sub__(self, other):
        """Вычитание кватернионов"""
        return Quaternion(self.w - other.w,
                          self.x - other.x,
                          self.y - other.y,
                          self.z - other.z)

    def __mul__(self, other):
        """Умножение кватернионов"""
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(w, x, y, z)

    def __truediv__(self, scalar):
        """Деление кватерниона на скаляр"""
        if scalar == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return Quaternion(self.w / scalar, self.x / scalar, self.y / scalar, self.z / scalar)


    def conjugate(self):
        """Сопряженный кватернион"""
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def norm(self):
        """Норма кватерниона"""
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """Нормализация кватерниона"""
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError("Невозможно нормализовать нулевой кватернион.")
        return Quaternion(self.w / n, self.x / n, self.y / n, self.z / n)

    def inverse(self):
        """Обратный кватернион"""
        norm_squared = self.norm()**2
        if norm_squared == 0:
            raise ZeroDivisionError("Невозможно найти обратный квантерион для нулевого кватерниона.")
        conjugate = self.conjugate()
        return Quaternion(conjugate.w / norm_squared,
                          conjugate.x / norm_squared,
                          conjugate.y / norm_squared,
                          conjugate.z / norm_squared)

    def rotate_vector(self, vector):
        """Поворот вектора с использованием кватерниона.
        
        vector: список или кортеж длины 3 (x, y, z).
        """
        q_vector = Quaternion(0, vector[0], vector[1], vector[2])
        q_rotated = self * q_vector * self.inverse()
        return [q_rotated.x, q_rotated.y, q_rotated.z]

    def __repr__(self):
        """Строковое представление кватерниона"""
        return f"Quaternion({self.w}, {self.x}, {self.y}, {self.z})"


class TestQuaternion(unittest.TestCase):

    def round_to_zero(self, vector, epsilon=1e-10):
        return [0 if abs(x) < epsilon else x for x in vector]

    def test_add(self):
        q1 = Quaternion(1, 2, 3, 4)
        q2 = Quaternion(4, 3, 2, 1)
        result = q1 + q2
        expected = Quaternion(5, 5, 5, 5)
        print("Сложение:", q1, q2)
        print("Результат:", result, "Ожидался:", expected)

    def test_sub(self):
        q1 = Quaternion(1, 2, 3, 4)
        q2 = Quaternion(4, 3, 2, 1)
        result = q1 - q2
        expected = Quaternion(-3, -1, 1, 3)
        print("Вычитание:", q1, q2)
        print("Результат:", result, "Ожидался:", expected)

    def test_mult(self):
        q1 = Quaternion(1, 0, 1, 0)
        q2 = Quaternion(0, 1, 0, 1)
        result = q1 * q2
        expected = Quaternion(-1, 1, 1, 1)
        print("Умножение:", q1, q2)
        print("Результат:", result, "Ожидался:", expected)

    def test_div(self):
        q = Quaternion(4, 8, 12, 16)
        scalar = 4
        result = q / scalar
        expected = Quaternion(1, 2, 3, 4)
        print("Деление", q, "на", scalar)
        print("Результат:", result, "Ожидался:", expected)

    def test_con(self):
        q = Quaternion(1, 2, 3, 4)
        result = q.conjugate()
        expected = Quaternion(1, -2, -3, -4)
        print("Сопряженный кватернион", q)
        print("Результат:", result, "Ожидался:", expected)

    def test_norm(self):
        q = Quaternion(1, 2, 2, 1)
        result = q.norm()
        expected = sqrt(1**2 + 2**2 + 2**2 + 1**2)  
        print("Норма кватерниона", q)
        print("Результат:", result, "Ожидался:", expected)

    def test_normal(self):
        q = Quaternion(0, 3, 0, 4)
        result = q.normalize()
        norm = sqrt(3**2 + 4**2)  
        expected = Quaternion(0 / norm, 3 / norm, 0 / norm, 4 / norm)
        print("Нормализация кватерниона", q)
        print("Результат:", result.w, "Ожидался:", expected.w)
        print("Результат:", result.x, "Ожидался:", expected.x)
        print("Результат:", result.y, "Ожидался:", expected.y)
        print("Результат:", result.z, "Ожидался:", expected.z)

    def test_inv(self):
        q = Quaternion(0, 3, 0, 4)
        result = q.inverse()
        norm_squared = (q.norm())**2
        expected = Quaternion(0 / norm_squared,
                              -3 / norm_squared,
                              -0 / norm_squared,
                              -4 / norm_squared)
        print("Обратный кватернион", q)
        print("Результат:", result.w, "Ожидался:", expected.w)
        print("Результат:", result.x, "Ожидался:", expected.x)
        print("Результат:", result.y, "Ожидался:", expected.y)
        print("Результат:", result.z, "Ожидался:", expected.z)

    def test_rotv(self):
        angle = radians(90)  
        axis = [0, 0, 1]    
        sin_half_angle = sin(angle / 2)
        cos_half_angle = cos(angle / 2)

        rotation_quaternion = Quaternion(cos_half_angle,
                                          axis[0] * sin_half_angle,
                                          axis[1] * sin_half_angle,
                                          axis[2] * sin_half_angle)

        vector = [1, 0, 0]

        rotated_vector = rotation_quaternion.rotate_vector(vector)
        rotated_vector = self.round_to_zero(rotated_vector)

        print("Исходный вектор:", vector)
        print("Повернутый вектор:", rotated_vector)

    def test_zero_norm(self):
        q = Quaternion(0, 0, 0, 0)
        with self.assertRaises(ZeroDivisionError):
            q.normalize()
        print("Невозможно нормализовать нулевой кватернион.")

    def test_zero_inv(self):
        q = Quaternion(0, 0, 0, 0)
        with self.assertRaises(ZeroDivisionError):
            q.inverse()
        print("Невозможно найти обратный квантерион для нулевого кватерниона.")


if __name__ == "__main__":
    unittest.main()



