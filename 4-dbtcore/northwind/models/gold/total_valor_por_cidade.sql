select c.country, c.city, round(cast(sum(a.unit_price * a.quantity - discount) as numeric), 2) as total_order_value
from {{ref('silver_order_details')}} a
join {{ref('silver_orders')}} b on a.order_id = b.order_id
join {{ref('silver_customers')}} c on b.customer_id = c.customer_id
group by c.country, c.city