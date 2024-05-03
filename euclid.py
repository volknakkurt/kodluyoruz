import math

def euclidean_distance(point1, point2):
  """
  İki nokta arasındaki Öklid mesafesini hesaplar.

  Args:
    point1: (x1, y1) şeklinde bir demet.
    point2: (x2, y2) şeklinde bir demet.

  Returns:
    İki nokta arasındaki Öklid mesafesi.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
  """
  Ana fonksiyon. Noktaları tanımlar, mesafeleri hesaplar ve minimum mesafeyi yazdırır.
  """
  # Noktaları tanımlayın
  points = [(1, 2), (4, 5), (7, 1), (3, 6)]

  # Mesafeleri hesaplayın
  distances = []
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      distance = euclidean_distance(points[i], points[j])
      distances.append(distance)

  # Minimum mesafeyi bulun
  min_distance = min(distances)

  # Sonuçları yazdırın
  print("Noktalar:", points)
  print("Mesafeler:", distances)
  print("Minimum mesafe:", min_distance)

if __name__ == "__main__":
  main()
