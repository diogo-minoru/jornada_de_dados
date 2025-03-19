with customers as (
    select
        customer_id,
        company_name,
        country,
        city
    from {{ref('bronze_customers')}}
)

select *
from customers