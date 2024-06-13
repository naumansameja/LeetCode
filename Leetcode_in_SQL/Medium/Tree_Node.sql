# Write your MySQL query statement below
select id, 
(case 
    when P_id is null then 'Root'
    when 1 > (
        select count(p_id)
        from Tree
        where p_id = t.id) then 'Leaf'
    else 'Inner'
end) as type

from Tree t