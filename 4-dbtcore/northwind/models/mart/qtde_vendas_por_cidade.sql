select b.country, b.city, count(distinct a.order_id)
from {{ref('silver_orders')}} a
join {{ref('silver_customers')}} b on a.customer_id = b.customer_id
group by b.country, b.city
order by 3 desc