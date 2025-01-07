class Shoe:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

class Data:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

    def get_all_shoes(self):
        return self.shoes

class View:
    @staticmethod
    def display_shoes(shoes):
        print("\nDaftar Sepatu:")
        print(f"{'Brand':<15}{'Size':<10}{'Price':<10}")
        print("-" * 35)
        for shoe in shoes:
            print(f"{shoe.brand:<15}{shoe.size:<10}{shoe.price:<10}")

class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def input_shoe(self):
        try:
            brand = input("Masukkan merek sepatu: ")
            size = float(input("Masukkan ukuran sepatu: "))
            price = float(input("Masukkan harga sepatu: "))

            if size <= 0 or price < 0:
                raise ValueError("Ukuran dan harga harus positif.")

            new_shoe = Shoe(brand, size, price)
            self.data.add_shoe(new_shoe)
            print("Sepatu berhasil ditambahkan!")
        
        except ValueError as e:
            print(f"Input tidak valid: {e}")

    def show_all_shoes(self):
        shoes = self.data.get_all_shoes()
        if shoes:
            self.view.display_shoes(shoes)
        else:
            print("Tidak ada data sepatu.")

def main():
    process = Process()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Sepatu")
        print("2. Tampilkan Semua Sepatu")
        print("3. Keluar")

        choice = input("Pilih opsi (1/2/3): ")
        
        if choice == '1':
            process.input_shoe()
        elif choice == '2':
            process.show_all_shoes()
        elif choice == '3':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
