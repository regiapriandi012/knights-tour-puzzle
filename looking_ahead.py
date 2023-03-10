class Matrices:
    def __init__(self, ukuran_col, ukuran_row):
        self.ukuran_col = ukuran_col
        self.ukuran_row = ukuran_row
        self.matrices = [["_" * len(str(self.ukuran_col * self.ukuran_row))
                          for _ in range(1, self.ukuran_col + 1)]
                         for _ in range(1, self.ukuran_row + 1)]
        self.perpindahan_blok = []
        self.kemungkinan_perpindahan_balok = []

    def kemungkinan(self, col, row):
        """
        Membuat kemungkinan perpindahan
        X dengan pola L ke semua arah
        pada matrik
        """
        perpindahan = [
            [-2, 1], [-2, -1], [2, 1], [2, -1],
            [-1, 2], [1, 2], [-1, -2], [1, -2]
        ]

        """
        Perulangan untuk menerapkan
        kemungkinan perpindahan X
        pada matrik menggunakan for
        loop
        """
        kemungkinan_perpindahan = 0

        for i in perpindahan:
            if 0 <= int(row) + (i[0]) - 1 < self.ukuran_row and \
                    0 <= int(col) + (i[1]) - 1 < self.ukuran_col:
                kemungkinan_perpindahan += 1

        return kemungkinan_perpindahan

    def ubah(self, col, row):
        self.matrices[int(row) - 1][int(col) - 1] = \
            " " * (len(str(self.ukuran_col * self.ukuran_row)) - 1) + "X"

        """
        Membuat kemungkinan perpindahan
        X dengan pola L ke semua arah
        pada matrik
        """
        perpindahan = [
            [-2, 1], [-2, -1], [2, 1], [2, -1],
            [-1, 2], [1, 2], [-1, -2], [1, -2]
        ]

        """
        Perulangan untuk menerapkan
        kemungkinan perpindahan X
        pada matrik menggunakan for
        loop
        """
        try:
            for i in perpindahan:
                if 0 <= int(row) + (i[0]) - 1 < self.ukuran_row and \
                        0 <= int(col) + (i[1]) - 1 < self.ukuran_col:
                    # ingat dihapus -1 nya buat menyesuaikan di index
                    self.perpindahan_blok.append([int(row) +
                                                  (i[0]), int(col) + (i[1])])
        except IndexError:
            pass

        """
        keterangan
        """
        for i, j in self.perpindahan_blok:
            self.kemungkinan_perpindahan_balok.append(self.kemungkinan(i, j))

        """
        Mencetak kemungkinan perpindahan
        """
        nomor = 0
        try:
            for i in perpindahan:
                if 0 <= int(row) + (i[0]) - 1 < self.ukuran_row and \
                        0 <= int(col) + (i[1]) - 1 < self.ukuran_col:
                    self.matrices[int(row) +
                                  (i[0]) - 1][int(col) + (i[1]) - 1] \
                        = (" " * (len(str(self.ukuran_col *
                                          self.ukuran_row)) - 1) +
                           f"{self.kemungkinan_perpindahan_balok[nomor] - 1}")
                    nomor += 1
        except IndexError:
            pass

        """
        output program
        """
        setrip_angka = 0
        setrip = ""
        angka_baris = ""

        setrip_angka += self.ukuran_col * (len(self.matrices[1][0]) + 1) + 3
        for _ in range(setrip_angka):
            setrip += "-"

        for i in range(1, self.ukuran_col + 1):
            angka_baris += str(i) + \
                           " " * (len(str(self.ukuran_col * self.ukuran_row)))

        print("", setrip)
        for x in range(len(self.matrices), 0, -1):
            print("{0}| {1} |".format(str(x), " ".
                                      join(map(str, self.matrices[x - 1]))))
        print("", setrip)
        print("", " " * (len(str(self.ukuran_col * self.ukuran_row))),
              angka_baris.strip())

    def output(self):
        while True:
            try:
                inputan = input("Enter the knight's starting position: ")
                i, j = inputan.split(" ")

                if not i.isdigit() or not j.isdigit() \
                        or int(i) == 0 or int(j) == 0:
                    print("Invalid dimensions!.")
                elif int(i) > self.ukuran_col or int(j) > self.ukuran_row:
                    print("Invalid dimensions!")
                else:
                    Matrices(self.ukuran_col, self.ukuran_row).ubah(i, j)
                    break
            except ValueError:
                print("Invalid dimensions!")


while True:
    try:
        inputan_dimensi = input("Enter your board dimensions: ")
        dimensi_row, dimensi_col = inputan_dimensi.split(" ")

        if not dimensi_col.isdigit() or not dimensi_row.isdigit():
            print("Invalid dimensions!.")
        else:
            break
    except ValueError:
        print("Invalid dimensions!")

Matrices(int(dimensi_row), int(dimensi_col)).output()
