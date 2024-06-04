select distinct l1.num ConsecutiveNums
from Logs l1 join Logs l2 on l1.num = l2.num
join Logs l3 on l3.num = l2.num
where l1.id + 1= l2.id and l2.id + 1 = l3.id 
