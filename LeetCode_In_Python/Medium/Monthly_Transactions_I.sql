-- # Write your MySQL query statement below
select distinct concat(year(trans_date),'-', lpad(month(trans_date),2,'0')) as month, country,count(id) as trans_count, 
sum(state = 'approved') as approved_count,
sum(amount) as trans_total_amount, 
sum((state = 'approved')*amount)  as approved_total_amount
from transactions t
group by month,country
