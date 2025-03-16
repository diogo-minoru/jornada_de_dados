with customers as (
    select
        customer_id,
        company_name,
        country,
        city
    from {{ref('raw_crm__customers')}}
)

select *
from customers