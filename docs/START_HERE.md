# Start here

The goal is to explain every amount in an analytical dataset: its source, transformation rule, behavior under replay or lateness, and verification.

## Your first session

1. Read the [README](../README.md) and run the lab demo.
2. Open `work/demo/report.json` and find p3 and p9: deliberate reconciliation defects.
3. Initialize E01, implement its function, and grade it.
4. Complete [E05](../practice/E05.md): events and payments have different grains.
5. Choose a [learning path](LEARNING_PATHS.md) and keep a progress checklist in your fork.

No pip installation is needed for the baseline: Decimal, sqlite3, unittest, json, and datetime are standard-library modules. If sqlite3 is missing, use a CPython distribution that includes it.

## Working through a lesson

Restate the outcome in your own words. Inspect the example and failure mode, then complete the task. Watching a video is not completing the exercise. Retain a reproducible artifact, verification, and tradeoff explanation. Answer the self-check without looking at the reading.

Allow roughly 2–4 hours for a first pass; real Spark workloads, distributed recovery, and security reviews require more than a tiny fixture. If skipping a topic, record what evidence from your existing work establishes the required understanding.

## Progress gates

After SQL, explain grain, fanout, NULL, and boundaries. After modeling, choose facts and dimension history. After ingestion, explain replay, conflicts, snapshots, and deletes. After fintech, distinguish balance, reconciliation, currencies, and close. After AI, identify executable verification and permission boundaries.

The [practice guide](../practice/README.md) has four exercises per module; lesson assignments extend them into designs and integrations. Finish with a [capstone](../projects/README.md) rather than merely running references.

## When stuck

Reduce the input to two events and calculate the expected answer manually. Locate the first difference in parsing, joins, filters, aggregation, or publication. Consult the [dictionary](DATA_DICTIONARY.md), [SQL patterns](SQL_PATTERNS.md), and [FAQ](FAQ.md). Issues should contain synthetic data, an exact command, Python version, and expected versus actual output.
