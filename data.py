class Data:
    def __init__(self):
        self.entries = []  # Menyimpan daftar entri pengguna.

    def add_entry(self, name, age):
        # Menambahkan entri baru ke daftar.
        self.entries.append({'name': name, 'age': age})

    def get_entries(self):
        # Mengambil semua entri yang ada.
        return self.entries
