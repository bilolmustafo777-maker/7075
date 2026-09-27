import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8912448379:AAEXcjd5wgm3B_z3yggBm1QYVkVLGXNC2t0", "")
ADMIN_ID = int(os.getenv("8962547818", "0") or "0")
DB_PATH = os.getenv("DB_PATH", "taxi.db")

# Joyni band qilish uchun garov puli (so'm)
DEPOSIT_AMOUNT = 35_000

# Botda taklif qilinadigan shaharlar ro'yxati (kerak bo'lsa qo'shib/o'chirib turing)
CITIES = [
    "Toshkent", "Termiz", "Samarqand", "Buxoro", "Andijon",
    "Farg'ona", "Namangan", "Qarshi", "Nukus", "Urganch",
    "Guliston", "Jizzax", "Navoiy",
]

# Ruxsat etilgan mashina turlari
CAR_TYPES = ["Gentra", "Cobalt", "Onix", "Tracker", "Monza"]
