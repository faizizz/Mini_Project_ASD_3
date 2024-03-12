import os
os.system("cls")

class Node:
    def __init__(self, id, jenis, harga, tahun_terbit, penerbit):
        self.id = id
        self.jenis = jenis
        self.harga = harga
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, id, jenis, harga, tahun_terbit, penerbit):
        new_node = Node(id, jenis, harga, tahun_terbit, penerbit)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, id, jenis, harga, tahun_terbit, penerbit):
        new_node = Node(id, jenis, harga, tahun_terbit, penerbit)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, id, jenis, harga, tahun_terbit, penerbit):
        if prev_node is None:
            print("Node sebelumnya tidak ditemukan")
            return
        new_node = Node(id, jenis, harga, tahun_terbit, penerbit)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, id):
        temp = self.head
        if temp is not None:
            if temp.id == id:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.id == id:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print("ID tidak ditemukan")
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print("Nomor:", temp.id, '| Jenis:', temp.jenis, '| Harga:', temp.harga, '| Tahun Terbit:', temp.tahun_terbit, "| Penerbit:", temp.penerbit)
            temp = temp.next

    def merge_sort(self, head, attribute, order):
        if head is None or head.next is None:
            return head

        left, right = self.split_list(head)
        left = self.merge_sort(left, attribute, order)
        right = self.merge_sort(right, attribute, order)

        return self.merge_lists(left, right, attribute, order)

    def split_list(self, head):
        if head is None:
            return None, None
        if head.next is None:
            return head, None

        slow = head
        fast = head.next

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next

        mid = slow.next
        slow.next = None

        return head, mid

    def merge_lists(self, left, right, attribute, order):
        if left is None:
            return right
        if right is None:
            return left

        if order == 'asc':
            if getattr(left, attribute) <= getattr(right, attribute):
                result = left
                result.next = self.merge_lists(left.next, right, attribute, order)
            else:
                result = right
                result.next = self.merge_lists(left, right.next, attribute, order)
        elif order == 'desc':
            if getattr(left, attribute) >= getattr(right, attribute):
                result = left
                result.next = self.merge_lists(left.next, right, attribute, order)
            else:
                result = right
                result.next = self.merge_lists(left, right.next, attribute, order)

        return result

    def sort(self, attribute, order='asc'):
        self.head = self.merge_sort(self.head, attribute, order)

datamajalah = LinkedList()

datamajalah.append(1, "Kesehatan", 20000, 2022, "Sparkle Media")
datamajalah.append(2, "Teknologi", 20000, 2024, "Green Planet")
datamajalah.append(3, "Travel", 20000, 2024, "Travelogue Ltd")
datamajalah.append(4, "Lingkungan", 20000, 2023, "Green Planet")

def additem():
    input_id = int(input('MASUKKAN NOMOR MAJALAH (NOMOR TIDAK BOLEH SAMA): '))
    input_jenis = str(input('\nMASUKKAN JENIS/NAMA MAJALAH (JENIS/NAMA TIDAK BOLEH SAMA): '))
    input_harga = int(input('\nMASUKKAN HARGA MAJALAH: '))
    input_tahun_terbit = int(input('\nMASUKKAN TAHUN TERBIT MAJALAH: '))
    input_penerbit = str(input('\nMASUKKAN PENERBIT MAJALAH: '))

    temp = datamajalah.head
    while temp:
        if input_id == temp.id:
            print('\nNomor yang dimasukkan sudah digunakan silahkan ulangi lagi\n')
            pilihan_menu()
            return
        elif input_jenis == temp.jenis:
            print('JENIS/NAMA yang dimasukkan sudah digunakan silahkan ulangi lagi\n')
            pilihan_menu()
            return
        temp = temp.next

    datamajalah.append(input_id, input_jenis, input_harga, input_tahun_terbit, input_penerbit)
    print('\nPRODUK BERHASIL DITAMBAHKAN')
    pilihan_menu()

def deleteitem():
    datamajalah.display()
    print('')
    input_id = int(input('MASUKKAN NOMOR MAJALAH: '))
    datamajalah.delete_node(input_id)
    print('')
    print('MAJALAH BERHASIL DIHAPUS')
    pilihan_menu()

def updateitem():
    datamajalah.display()
    print('')
    input_nomor = int(input('MASUKKAN NOMOR MAJALAH: '))

    temp = datamajalah.head
    prev = None
    while temp:
        if input_nomor == temp.id:
            input_jenis = str(input('\nMASUKKAN JENIS/NAMA MAJALAH YANG BARU: '))
            input_harga = int(input('\nMASUKKAN HARGA MAJALAH YANG BARU: '))
            input_tahun_terbit = int(input('\nMASUKKAN TAHUN TERBIT MAJALAH YANG BARU: '))
            input_penerbit = str(input('\nMASUKKAN PENERBIT MAJALAH YANG BARU: '))
            datamajalah.delete_node(input_nomor)
            if prev is None:
                datamajalah.prepend(input_nomor, input_jenis, input_harga, input_tahun_terbit, input_penerbit)
            else:
                datamajalah.insert_after(prev, input_nomor, input_jenis, input_harga, input_tahun_terbit, input_penerbit)
            print('\nPRODUK BERHASIL DIPERBARUI')
            pilihan_menu()
            return
        prev = temp
        temp = temp.next

    print('\nMAJALAH DENGAN NOMOR YANG DIMASUKKAN TIDAK DITEMUKAN, SILAHKAH COBA LAGI')
    pilihan_menu()

def sortitem():
    print('')
    print("PILIHAN SORTING: ")
    print('')
    print("1. Ascending")
    print("2. Descending")
    print('')
    pilihan_sort = int(input("PILIHAN SORTING (1/2): "))
    if pilihan_sort == 1:
        order = 'asc'
    elif pilihan_sort == 2:
        order = 'desc'
    else:
        print('Pilihan tidak valid')
        pilihan_menu()
        return

    print('')
    print("PILIHAN ATRIBUT UNTUK SORTING: ")
    print('')
    print("1. Harga")
    print("2. Tahun Terbit")
    print('')
    pilihan_atribut = int(input("PILIHAN ATRIBUT (1/2): "))
    if pilihan_atribut == 1:
        attribute = 'harga'
    elif pilihan_atribut == 2:
        attribute = 'tahun_terbit'
    else:
        print('Pilihan tidak valid')
        pilihan_menu()
        return

    datamajalah.sort(attribute, order)
    print('\nPRODUK BERHASIL DIURUTKAN')
    pilihan_menu()

def pilihan_menu():
    while True:
        print('')
        print("PILIHAN MENU : ")
        print('')
        print("1. LIST PRODUK")
        print("2. TAMBAH PRODUK")
        print("3. HAPUS PRODUK")
        print("4. UBAH PRODUK")
        print("5. SORT PRODUK")
        print("6. KELUAR")
        print('')
        pilihan_menu = int(input("PILIHAN MENU (1/2/3/4/5) : "))

        if pilihan_menu == 1:
            print('')
            print('LIST PRODUK KAMI ADALAH: \n')
            datamajalah.display()
        elif pilihan_menu == 2:
            print('')
            additem()
        elif pilihan_menu == 3:
            print('')
            deleteitem()
        elif pilihan_menu == 4:
            print('')
            updateitem()
        elif pilihan_menu == 5:
            print('')
            sortitem()
        elif pilihan_menu == 6:
            raise SystemExit

print('')
print("=" * 31)
print("SELAMAT DATANG DI MAGAZINE ZONE")
print("=" * 31)

pilihan_menu()
