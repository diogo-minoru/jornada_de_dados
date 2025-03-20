with 
    source as (
    select *
    from {{ref('bronze_order_details')}}
    ),

    renamed as (
    select 
        order_id,
        product_id,
        unit_price,
        quantity,
        discount
    from source
)

select *
from renamed