# Definisi kelas Parent
class Parent:
    def __init__(self, name, warna,):
        self.name = name
        self.warna = warna
        

    def introduce(self):
        print(f"Nama saya {self.name} saya suka {self.warna}.")

    def parent_method(self):
        print("metode dari kelas Parent.")

# Definisi kelas Child yang mewarisi dari kelas Parent
class Child(Parent):
    def __init__(self, name, warna, rasa):
        # Memanggil constructor kelas Parent
        super().__init__(name, warna)
        self.rasa = rasa

    def introduce(self):
        # Memanggil metode introduce dari kelas Parent
        super().introduce()
        print(f"saya suka rasa {self.rasa}.")

    def child_method(self):
        print("Ini adalah metode dari kelas Child.")

# Membuat instance objek dari kelas Child
child_instance = Child("mangga", "orange", "manis")

# Memanggil atribut dan metode dari objek child_instance
print(f"Nama: {child_instance.name}")
print(f"warna: {child_instance.warna}")
print(f"rasa: {child_instance.rasa}")

# Memanggil metode introduce yang telah dioverride
# child_instance.introduce()

# Memanggil metode dari kelas Parent
child_instance.parent_method()

# Memanggil metode dari kelas Child
child_instance.child_method()
