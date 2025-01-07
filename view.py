class View:
    @staticmethod
    def display_table(entries):
        # Menampilkan data dalam format tabel.
        print("\nDaftar Pengguna:")
        print("{:<20} {:<10}".format("Nama", "Usia"))
        print("-" * 30)
        for entry in entries:
            print("{:<20} {:<10}".format(entry['name'], entry['age']))
