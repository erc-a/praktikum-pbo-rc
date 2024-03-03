class Karakter:
    def __init__(self, nama_player, armor, senjata):
        self.nama_player = nama_player
        self.armor = armor
        self.senjata = senjata
        self.hp = 100
        self.attack_power = 0
        self.shield_active = False
        self.enchantment = None

    def attack(self, target):
        if self.senjata == 'Sword Kayu':
            self.attack_power = 10
        elif self.senjata == 'Sword Emas':
            self.attack_power = 20
        elif self.senjata == 'Sword Besi':
            self.attack_power = 30
        elif self.senjata == 'Sword Diamond':
            self.attack_power = 40
        elif self.senjata == 'Sword Netherite':
            self.attack_power = 50
        elif self.senjata == 'Axe Kayu':
            self.attack_power = 10
        elif self.senjata == 'Axe Emas':
            self.attack_power = 20
        elif self.senjata == 'Axe Besi':
            self.attack_power = 30
        elif self.senjata == 'Axe Diamond':
            self.attack_power = 40
        elif self.senjata == 'Axe Netherite':
            self.attack_power = 50
        elif self.senjata == 'Panah':
            self.attack_power = -25
        else: # Jika tidak menggunakan senjata, attack menggunakan tangan
            self.attack_power = 2

        if self.enchantment == 'Sharpness':
            self.attack_power += 5 

        if target.armor == 'Kulit':
            target.receive_damage(self.attack_power * 0.10)
        elif target.armor == 'Emas':
            target.receive_damage(self.attack_power * 0.20)
        elif target.armor == 'Besi':
            target.receive_damage(self.attack_power * 0.30)
        elif target.armor == 'Diamond':
            target.receive_damage(self.attack_power * 0.40)
        elif target.armor == 'Netherite':
            target.receive_damage(self.attack_power * 0.50)

    def receive_damage(self, damage):
        if self.shield_active:
            damage = 0  # Jika shield aktif, damage menjadi 0
        self.hp -= damage
        if self.hp <= 0:
            print(f'{self.nama_player} telah mati.')

    def activate_shield(self):
        self.shield_active = True

    def deactivate_shield(self):
        self.shield_active = False

    def add_enchantment(self, enchantment):
        self.enchantment = enchantment

class Makan:
    def __init__(self, makanan):
        self.makanan = makanan

    def heal(self, player):
        if self.makanan == 'Bread':
            player.hp += 30
        elif self.makanan == 'Apple':
            player.hp += 20
        elif self.makanan == 'Cake':
            player.hp += 20
        elif self.makanan == 'Golden Carrot':
            player.hp += 20
        elif self.makanan == 'Golden Apple':
            player.hp += 20

# Contoh penggunaan:
steve = Karakter('Steve', 'Netherite', 'Kapak Kayu')
alex = Karakter('Alex', 'Besi', 'Sword Emas')

# Steve menyerang Alex
steve.attack(alex)
print(f'{alex.nama_player} HP: {alex.hp}')

# Alex mengaktifkan shield
alex.activate_shield()

# Steve menyerang Alex lagi
steve.attack(alex)
print(f'{alex.nama_player} HP: {alex.hp}')

# Alex menyerang Steve
alex.attack(steve)
print(f'{steve.nama_player} HP: {steve.hp}')

# Menambahkan enchantment Sharpness ke senjata Steve
steve.add_enchantment('Sharpness')

# Steve menyerang Alex dengan enchantment Sharpness
steve.attack(alex)
print(f'{alex.nama_player} HP: {alex.hp}')
