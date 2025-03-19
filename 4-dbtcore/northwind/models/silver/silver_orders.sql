with orders as (
    select 
        order_id,
        customer_id
    from {{ref('bronze_orders')}}
)

select *
from orders