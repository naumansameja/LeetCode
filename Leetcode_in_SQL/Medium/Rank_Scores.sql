# Write your MySQL query statement below
select Score, (select count( distinct score) from Scores where score >= sc.score) as 'rank'
from Scores as sc
order by score desc