with 
    source as (
        select * 
        from {{ref('bronze_customers')}}
    ),

    customers as (
    select
        customer_id,
        company_name,
        country,
        city
    from source
    )

select *
from customers