-- Задание 1
SELECT
    c.login AS courier_login,
    COUNT(o.*) FILTER (WHERE o."inDelivery" = true) AS in_delivery_count
FROM "Couriers" c
LEFT JOIN "Orders" o ON o."courierId" = c.id
GROUP BY c.login
ORDER BY in_delivery_count DESC;

-- Задание 2
SELECT
    o.track,
    CASE
        WHEN o.finished = true THEN 2
        WHEN o.cancelled = true THEN -1
        WHEN o."inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders" o;