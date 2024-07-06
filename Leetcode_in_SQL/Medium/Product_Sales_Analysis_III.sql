with min_years as (select product_id, min(year) as first_year
from sales
group by product_id)

select s.product_id, m.first_year, quantity, price
from sales s join min_years m on s.product_id = m.product_id
where s.year = first_year
