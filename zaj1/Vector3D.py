import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def getX(self):
        return self.x

    def setX(self, value):
        self.x = value

    def getY(self):
        return self.y

    def setY(self, value):
        self.y = value

    def getZ(self):
        return self.z

    def setZ(self, value):
        self.z = value

    def norm(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)

    @staticmethod
    def are_orthogonal(vec1, vec2):
        return vec1.dot(vec2) == 0

vector = Vector3D(3, 4, 5)
print(vector)
vector.setX(7)
vector.setY(8)
vector.setZ(9)
print(vector)
print(vector.norm())

v1 = Vector3D(7,8,9)
v2 = Vector3D(3,4,5)

vectorAdd = v1 + v2
vectorSub = v1 - v2
vectorMul = v1 * v2

print(vectorAdd)
print(vectorSub)
print(vectorMul)

print(v1.dot(v2))

vectorCross = v1.cross(v2)
print(vectorCross)

print(Vector3D.are_orthogonal(v1, v2))

v3 = Vector3D(1, 0, 0)
v4 = Vector3D(0, 1, 0)

print(Vector3D.are_orthogonal(v3, v4))