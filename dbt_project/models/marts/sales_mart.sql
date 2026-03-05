{{ config(materialized='table') }}

with joined as (
    select
        p.product_id,
        p.product_description,
        p.category,
        p.size,
        p.available_qty,
        p.warehouse,
        o.qty,
        o.unit_price,
        o.amount
    from {{ ref('stg_orders') }} o
    join {{ ref('stg_products') }} p
      on o.product_id = p.product_id
    where lower(o.order_status) not in ('cancelled', 'returned', 'picked')
)

select
    product_id,
    product_description,
    category,
    size,
    available_qty,
    warehouse,
    CAST(sum(qty) AS INTEGER)            as total_qty_sold,
    CAST(sum(qty * unit_price) AS REAL)  as actual_revenue,
    CAST(sum(amount) AS REAL)            as total_revenue
from joined
group by
    product_id,
    product_description,
    category,
    size,
    available_qty,
    warehouse