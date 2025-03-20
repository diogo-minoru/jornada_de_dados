with 
    source as (
    select *
    from {{ref('bronze_orders')}}
    ),
    
    orders as (
    select 
        order_id,
        customer_id
    from source
)

select *
from orders