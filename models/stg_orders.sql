select
    id as order_id,
    customer_id,
    store_id,
    order_date,
    subtotal,
    tax_paid,
    order_total
from raw_data.raw_orders