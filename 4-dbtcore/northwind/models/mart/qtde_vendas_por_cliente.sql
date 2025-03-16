select a.customer_id, b.company_name, count(distinct a.order_id)
from {{ref('stg_crm__orders')}} a
join {{ref('stg_crm__customers')}} b on a.customer_id = b.customer_id
group by a.customer_id, b.company_name
order by 3 desc