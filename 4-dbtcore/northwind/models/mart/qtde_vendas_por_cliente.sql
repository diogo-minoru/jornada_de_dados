select a.customer_id, b.company_name, count(distinct a.order_id)
from {{ref('silver_orders')}} a
join {{ref('silver_customers')}} b on a.customer_id = b.customer_id
group by a.customer_id, b.company_name
order by 3 desc