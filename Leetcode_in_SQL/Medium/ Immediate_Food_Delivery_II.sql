

with first_orders as (select customer_id, order_date, customer_pref_delivery_date
from delivery d
where order_date = (select min(order_date) from delivery where customer_id = d.customer_id))

select round((sum(order_date=customer_pref_delivery_date) * 100 / count(customer_id)),2) as immediate_percentage
from first_orders