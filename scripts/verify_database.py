from sqlalchemy import text

from database.connection import engine


TABLES = [
    "regions",
    "customers",
    "products",
    "employees",
    "orders",
    "order_items",
    "payments",
]


with engine.connect() as connection:
    print("AIDesk Database Verification")
    print("-" * 35)

    for table in TABLES:
        result = connection.execute(text(f"SELECT COUNT(*) FROM {table}"))

        count = result.scalar()

        print(f"{table:15} : {count}")

print("-" * 35)
print("Database verification: SUCCESS")
