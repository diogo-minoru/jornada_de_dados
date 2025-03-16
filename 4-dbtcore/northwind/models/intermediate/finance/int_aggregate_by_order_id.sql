with int_aggregate_by_order_id as(
    select 
        order_id,
        sum(total_order) as valor_total_pedido
    from {{ref('stg_crm__order_details')}}
    group by order_id
)

select *
from int_aggregate_by_order_id