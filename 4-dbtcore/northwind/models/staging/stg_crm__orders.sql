with orders as (
    select 
        order_id,
        customer_id
    from {{ref('raw_crm__orders')}}
)

select *
from orders