SELECT event_id,currency FROM ledger_entries
GROUP BY event_id,currency
HAVING sum(signed_minor)<>0 OR count(*)<>2
UNION
SELECT r.event_id,r.currency FROM raw_events r
WHERE NOT EXISTS (SELECT 1 FROM ledger_entries l WHERE l.event_id=r.event_id)
ORDER BY event_id,currency;
