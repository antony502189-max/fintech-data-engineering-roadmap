-- SQLite. Run after ingesting fintech_lab.synthetic.payments().
-- Task: return event_id,currency for broken journal groups AND raw events
-- with no journal. Sorted by event_id,currency. Correct fixture returns [].
-- A journal group is broken when count!=2 or sum(signed_minor)!=0.
-- Replace this deliberate placeholder in your personal copy:
SELECT 'TODO' AS event_id, 'TODO' AS currency;
