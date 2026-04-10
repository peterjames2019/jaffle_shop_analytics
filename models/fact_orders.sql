with orders as (
    select * from {{ ref('stg_orders') }}
),

order_items as (
    select * from {{ ref('stg_items') }}
),

products as (
    select * from {{ ref('stg_products') }}
),

order_details as (
    select
        order_items.order_id,
        sum(products.price) as total_item_value -- assuming products has a price column
    from order_items
    left join products on order_items.sku = products.sku
    group by 1
),

final as (
    select
        orders.order_id,
        orders.customer_id,
        orders.order_date,
        orders.order_total,
        coalesce(order_details.total_item_value, 0) as calculated_revenue
    from orders
    left join order_details using (order_id)
)

select * from final