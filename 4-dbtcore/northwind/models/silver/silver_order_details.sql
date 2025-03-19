with renamed as (
    select 
        order_id,
        product_id,
        unit_price,
        quantity,
        discount
    from {{ref('bronze_order_details')}}
)

select *
from renamed