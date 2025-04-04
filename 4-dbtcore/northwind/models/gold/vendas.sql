{{ config(
    materialized = 'incremental',
    unique_key = 'order_id'
)}}

with vendas as(
    select *
    from {{ref('silver_order_details')}}
)

select * from vendas

{% if is_incremental() %}
where order_id > (select max(order_id) from {{this}})
{% endif %}