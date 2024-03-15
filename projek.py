import itertools

class TSPSolver:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.distances = [[0] * num_cities for _ in range(num_cities)]

    def take_input(self):
        print("Masukkan jarak antara setiap pasangan kota:")
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    distance = float(input(f"Jarak dari kota {i+1} ke kota {j+1}: "))
                    self.distances[i][j] = distance

    def tsp_brute_force(self):
        min_distance = float('inf')
        min_path = None
        for perm in itertools.permutations(range(self.num_cities)):
            distance = 0
            for i in range(self.num_cities - 1):
                distance += self.distances[perm[i]][perm[i+1]]
            distance += self.distances[perm[-1]][perm[0]]  # Kembali ke kota awal
            if distance < min_distance:
                min_distance = distance
                min_path = perm
        return min_path, min_distance

def main():
    num_cities = int(input("Masukkan jumlah kota: "))
    tsp_solver = TSPSolver(num_cities)
    tsp_solver.take_input()

    start_city = int(input("Masukkan kota asal (indeks): ")) - 1
    end_city = int(input("Masukkan kota tujuan (indeks): ")) - 1

    path, distance = tsp_solver.tsp_brute_force()

    print("Jalur terpendek:", path)
    print("Jarak terpendek:", distance)

if __name__ == "__main__":
    main()
