
def triangle_area((v1), (v2), (v3)):
    vertices = []
    v1 = (0, 0)
    v2 = (1, 0)
    v3 = (0, 2)
    vertices.append(v1)
    vertices.append(v2)
    vertices.append(v3)
    A = (0.5*abs(vertices[1][0]*vertices[2][1] - vertices[2][0]*vertices[1][1] - vertices[0][0]*vertices[2][1] +vertices[2][0]*vertices[0][1] + vertices[0][0]*vertices[1][1] - vertices[1][0]*vertices[0][1]))
    return A

print triangle_area((0, 0), (1, 0), (0, 2))

