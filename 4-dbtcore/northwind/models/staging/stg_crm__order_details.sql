with renamed as (
    select 
        order_id,
        product_id,
        unit_price * quantity as total_order
    from {{ref('raw_crm__order_details')}}
)

select *
from renamed