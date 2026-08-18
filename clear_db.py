rom django.db import connection

print("Connecting to your database...")
with connection.cursor() as cursor:
    # 1. Force clear the order records securely
    cursor.execute("TRUNCATE TABLE checkout_order CASCADE;")
    
    # 2. Wipe out the stuck migration tracking rows
    cursor.execute("DELETE FROM django_migrations WHERE app = 'checkout';")

print("--- DATABASE WIPED SUCCESSFULLY ---")