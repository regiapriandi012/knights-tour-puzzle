class Matrices:
    def __init__(self):
        self.matrices = [["_" for _ in range(1, 9)] for _ in range(1, 9)]

    def ubah(self, row, col):
        self.matrices[int(col) - 1][int(row) - 1] = "X"
        print(" -------------------")
        for x in range(len(self.matrices), 0, -1):
            print("{0}| {1} |".format(str(x), " ".
                                      join(map(str, self.matrices[x - 1]))))
        print(" -------------------")
        print("   1 2 3 4 5 6 7 8")

    def output(self):
        while True:
            try:
                inputan = input("Enter the knight's starting position: ")
                i, j = inputan.split(" ")

                if not i.isdigit() or not j.isdigit():
                    print("Invalid dimensions!.")
                elif len(inputan.split()) > 2:
                    print("Invalid dimensions!")
                elif int(i) > 8 or int(j) > 8:
                    print("Invalid dimensions!")
                else:
                    Matrices().ubah(i, j)
                    break
            except ValueError:
                print("Invalid dimensions!")

Matrices().output()