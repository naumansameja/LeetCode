# Write your MySQL query statement below
select distinct teacher_id, count( distinct subject_id) as cnt
from teacher
group by teacher_id