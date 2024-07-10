from collections import deque

class RestaurantQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Pesanan '{order}' ditambahkan ke dalam antrian.")

    def dequeue(self):
        if not self.queue:
            print("Antrian kosong. Tidak ada pesanan untuk diproses.")
            return None
        order = self.queue.popleft()
        print(f"Pesanan '{order}' telah diproses dan dihapus dari antrian.")
        return order

    def display(self):
        if not self.queue:
            print("Antrian kosong.")
        else:
            print("Daftar pesanan dalam antrian:")
            for i, order in enumerate(self.queue, 1):
                print(f"{i}. {order}")

# Membuat objek antrian pesanan
restaurant_queue = RestaurantQueue()

# Menambahkan pesanan ke dalam antrian
restaurant_queue.enqueue('sushi')
restaurant_queue.enqueue('katsu')
restaurant_queue.enqueue('ramen')
restaurant_queue.enqueue('jus alpukat')


print("\nAntrian setelah menambahkan pesanan:")
print("\nMemproses pesanan pertama:")
print("\nAntrian saat ini:")
print("\nMemproses pesanan berikutnya:")
restaurant_queue.display()
restaurant_queue.dequeue()
restaurant_queue.display()
restaurant_queue.dequeue()


print("\nMencoba memproses pesanan ketika antrian kosong:")
restaurant_queue.dequeue()

    