
    (select p.product_id, round(COALESCE(SUM(p.price * u.units), 0) / COALESCE(SUM(u.units), 1),2) as average_price
    from prices p left join unitssold u
    on p.product_id = u.product_id
    and u.purchase_date >= p.start_date and u.purchase_date <= p.end_date
    group by p.product_id)

