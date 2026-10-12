# Capstone 2: point-in-time fraud data

## Problem

Build synthetic decision features: captures over one hour, declines over one day, and merchant-tier age. Labels appear after thirty days under the teaching policy. Include late events and profile corrections.

## Plan

1. Preserve entity_id, decision_at, event_time, received_at, and label_recorded_at.
2. Define half-open feature windows.
3. Use only information known at decision time.
4. Track validity and knowledge for mutable attributes; simple SCD2 cannot recreate old knowledge.
5. Apply temporal train/validation/test splits and label maturity.
6. Preserve dataset manifests and feature versions.

## Negative cases

e6 predates the decision in business time but arrives later. Equal timestamps need clear ordering. A label may not be mature. Later profile corrections must not appear in historical as-known data. Other currencies must not enter a monetary feature.

## Acceptance

Baseline p3 is zero before receipt and 2500 afterward. Every feature row can identify contributing events. Immature labels are excluded or marked by contract. Rebuild yields identical entity/decision keys. Offline and online meanings agree, and serving limits are explicit.

A classifier is optional: trustworthy data is the primary deliverable. A good model score does not establish absence of leakage.
