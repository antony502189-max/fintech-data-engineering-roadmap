"""Historical training examples: windows, knowledge, labels, and temporal splits."""
from datetime import timedelta
from fintech_lab.contracts import parse_time

def solve(data):
    as_of = parse_time(data['training_as_of'])
    train_end, validation_end = map(parse_time, (data['train_end'], data['validation_end']))
    labels = {r['decision']: r for r in data['labels']}
    included, excluded = [], []
    for decision in sorted(data['decisions'], key=lambda r: r['id']):
        instant = parse_time(decision['at'])
        label = labels.get(decision['id'])
        if instant + timedelta(days=data['maturity_days']) > as_of:
            reason = 'immature'
        elif label is None:
            reason = 'missing_label'
        elif parse_time(label['known_at']) > as_of:
            reason = 'label_not_yet_known'
        else:
            reason = None
        if reason:
            excluded.append({'id': decision['id'], 'reason': reason})
            continue
        start = instant - timedelta(seconds=data['window_seconds'])
        events = [r for r in data['events'] if r['entity'] == decision['entity']
                  and r['currency'] == decision['currency'] and r['kind'] == 'captured'
                  and start <= parse_time(r['event_time']) < instant
                  and parse_time(r['received_at']) <= instant]
        split = 'train' if instant < train_end else 'validation' if instant < validation_end else 'test'
        included.append({'id': decision['id'], 'split': split, 'label': label['value'],
                         'capture_minor': sum(r['amount_minor'] for r in events),
                         'event_ids': sorted(r['id'] for r in events)})
    return {'included': included, 'excluded': excluded}
