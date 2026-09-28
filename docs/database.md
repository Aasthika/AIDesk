# AIDesk Database Design

## 1. Database

AIDesk uses PostgreSQL through Supabase.

The database stores structured business data used by the AI Analyst,
Text-to-SQL system, analytics, and future evaluation workflows.

---

## 2. Tables

### regions

Stores geographical regions.

Columns:

- region_id — Primary Key
- region_name
- country
- created_at

---

### customers

Stores customer information.

Columns:

- customer_id — Primary Key
- customer_name
- email — Unique
- region_id — Foreign Key → regions.region_id
- created_at

Relationship:

regions 1 → many customers

---

### products

Stores products and their current inventory information.

Columns:

- product_id — Primary Key
- product_name
- category
- unit_price
- stock_quantity
- created_at

---

### employees

Stores employees associated with regions.

Columns:

- employee_id — Primary Key
- employee_name
- email — Unique
- role
- region_id — Foreign Key → regions.region_id
- created_at

Relationship:

regions 1 → many employees

---

### orders

Stores customer orders.

Columns:

- order_id — Primary Key
- customer_id — Foreign Key → customers.customer_id
- order_date
- status
- total_amount
- created_at

Relationship:

customers 1 → many orders

---

### order_items

Stores individual products belonging to an order.

Columns:

- order_item_id — Primary Key
- order_id — Foreign Key → orders.order_id
- product_id — Foreign Key → products.product_id
- quantity
- unit_price

Relationships:

orders 1 → many order_items

products 1 → many order_items

Therefore:

orders many ↔ many products

through order_items.

`unit_price` is stored here because the transaction price should remain
historically available even if the product's current price changes.

---

### payments

Stores payment information for orders.

Columns:

- payment_id — Primary Key
- order_id — Foreign Key → orders.order_id
- payment_method
- amount
- payment_status
- payment_date

Relationship:

orders 1 → many payments

---

## 3. Database Relationships

```text
regions
   |
   +---- customers
   |        |
   |        +---- orders
   |               |
   |               +---- order_items ---- products
   |
   +---- employees
                   
orders
   |
   +---- payments