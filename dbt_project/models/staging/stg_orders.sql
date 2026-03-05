{{ config(materialized='table') }}

select
    Order_id     as order_id,
    Product_id   as product_id,
    Size         as size,
    Qty          as qty,
    UnitPrice    as unit_price,
    Amount       as amount,
    Order_status as order_status
from {{ ref('orders') }}