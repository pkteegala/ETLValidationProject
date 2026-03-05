{{ config(materialized='table') }}

{{ config(materialized='table') }}

select
    Product_id          as product_id,
    Product_description as product_description,
    Category            as category,
    Size                as size,
    Available_qty       as available_qty,
    Warehouse           as warehouse
from {{ ref('products') }}