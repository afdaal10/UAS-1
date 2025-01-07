class Process:
    def __init__(self):
        self.data = Data()  # Inisialisasi objek Data.
        self.view = View()  # Inisialisasi objek View.

    def get_user_input(self):
        # Mengambil input dari pengguna.
        while True:
            try:
                name = input("Masukkan nama (atau 'exit' untuk keluar): ")
                if name.lower() == 'exit':
                    break
                age = int(input("Masukkan usia: "))
                if age < 0:
                    raise ValueError("Usia tidak boleh negatif.")
                
                self.data.add_entry(name, age)
            except ValueError as e:
                print(f"Input tidak valid: {e}")

    def display_results(self):
        # Menampilkan hasil setelah pengguna selesai memasukkan data.
        entries = self.data.get_entries()
        self.view.display_table(entries)
