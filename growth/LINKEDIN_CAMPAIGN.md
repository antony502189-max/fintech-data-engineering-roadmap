# LinkedIn growth campaign

**Status:** publication-ready drafts for maintainer review. None of the posts below has been published.

**Goal:** teach practical data engineering and earn qualified discovery for the repository. A GitHub star is optional support, never a condition of access. Proposed cadence is one post weekly for ten weeks, starting October 27, 2026 after review. Do not publish all ten during the initial sprint.

## 1. A Balanced Ledger Can Still Hide a Missing Dollar

**Format:** text + five-slide document carousel. **Link:** include the repo link at the end.

> A balanced payment journal can still be wrong about what the processor paid.
>
> In this small synthetic example, six events are ingested. Replaying the same delivery inserts zero new events and identifies six duplicates. Every journal pair balances.
>
> Reconciliation still finds two exceptions:
> - p3: expected 2,500 USD cents; settlement reports 2,400. That is a $1 shortfall.
> - p9: settlement contains $5 with no matching internal payment. Its expected amount is unknown; treating it as zero would hide the distinction.
>
> These are three separate checks: replay safety, journal balance, and agreement with an external settlement. Passing one does not prove the others.
>
> The example uses synthetic data and a simplified SQLite teaching model. The five-minute run needs Python and Git, but no paid cloud or API key: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> What additional reconciliation status would you want an analyst to see first?

**Carousel panels:** (1) “Balanced ≠ reconciled”; (2) six events → replay → 0 inserted / 6 duplicates; (3) p3 expected 2500, external 2400, delta −100 cents; (4) p9 external-only, expected = unknown; (5) name the three checks and link the runnable experiment. Label all amounts USD minor units and fixture data synthetic.

## 2. 5 Data Engineering Mistakes That Break Payment Systems

**Format:** checklist carousel. **Link:** optional, on final panel.

> Five small data mistakes can turn a payment report into a confident wrong answer:
>
> 1. Parse money through binary floats. Preserve decimal input and store integer minor units at a defined currency scale.
> 2. Join captures, fees, and attempts before aggregating. One-to-many joins multiply rows; aggregate each source at its intended grain first.
> 3. Assume delivery happens once. Make ingestion idempotent, then test replay explicitly.
> 4. Treat event time as arrival time. Late events change what was knowable at an earlier cutoff.
> 5. Convert “no matching record” into zero. Unknown, missing, and zero are different states.
>
> A useful review question is: what is the row grain before and after each join?
>
> The payment lab and SQL bug hunt in this roadmap use synthetic fixtures to practice these failure modes: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> Which one has caused the most confusing dashboard discrepancy for you?

**Carousel panels:** one mistake per slide with symptom and prevention; last slide asks the grain question. Keep the last-panel project link optional and disclose the examples are educational simulations.

## 3. Python Money: Parse Decimal Strings into Minor Units

**Format:** short Python tutorial/code card. **Link:** optional link to the money lesson.

> For payment amounts, this is a risky boundary:
>
> ```python
> amount = 12.34  # already a binary float
> ```
>
> The lab makes the input contract explicit: accept decimal text, validate the currency scale, then store an integer number of minor units.
>
> ```python
> to_minor("12.34", "USD")  # 1234
> to_minor("12.345", "USD") # rejected: too many fractional digits
> to_minor(12.34, "USD")    # rejected: input must be a string
> ```
>
> The important part is not merely using `Decimal`; it is preventing an imprecise value from crossing the boundary unnoticed, and deciding what fractional precision each supported currency permits.
>
> This repository’s small implementation uses Python’s standard library and a deliberately limited teaching contract. It is not a complete currency or accounting library: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> Where does your system enforce the money representation contract: API edge, ingestion, or database schema?

## 4. SQL Fan-Out: Why `SUM(DISTINCT)` Is Not a Fix

**Format:** SQL mini-tutorial, before/after snippet.

> When captures join to multiple fees and multiple attempts, the result has a multiplied row count. Summing after the join inflates totals.
>
> `SUM(DISTINCT amount)` looks tempting, but it removes equal-valued legitimate rows too. Two real captures of 100 cents are still two captures.
>
> A safer pattern is to aggregate each table at its own grain first:
>
> ```sql
> WITH captures AS (
>   SELECT payment, currency, SUM(amount) AS gross
>   FROM capture_events GROUP BY payment, currency
> ), fees AS (
>   SELECT payment, currency, SUM(amount) AS fee
>   FROM fee_events GROUP BY payment, currency
> )
> SELECT c.payment, c.currency, c.gross - COALESCE(f.fee, 0)
> FROM captures c
> LEFT JOIN fees f USING (payment, currency);
> ```
>
> The key is grain: payment + currency for these aggregates. A left join also keeps a payment with no fee row.
>
> The roadmap’s C07 exercise starts with runnable incorrect SQL and asks you to repair the totals: https://github.com/antony502189-max/fintech-data-engineering-roadmap

## 5. Practice Data Engineering Without Paying for Cloud

**Format:** practical tip.

> You can practice important data engineering ideas before opening a cloud account.
>
> A local SQLite database is enough to explore event ingestion, idempotent replay, exact minor-unit money, journal checks, reconciliation, slowly changing dimensions, and point-in-time features. The project’s first demo uses only Python’s standard library and synthetic events.
>
> A local lab will not teach cloud IAM, managed Kafka operations, production scale, or real settlement integrations. It can still teach the invariants and failure modes those systems need to preserve.
>
> Start with a five-minute command, inspect the discrepancy, then change one fixture value and predict the result. That feedback loop is more useful than provisioning infrastructure before you know what you want to test.
>
> The README lists the setup and limitations: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> What is your favorite local-first tool for practicing data workflows?

## 6. Idempotent Replay Is Not Reconciliation

**Format:** technical breakdown.

> Idempotency answers: “If I receive this event again, will I count it twice?”
>
> Reconciliation answers: “Does my expected payment result agree with the independent settlement record?”
>
> In the demo, the same six events are delivered twice. The second pass inserts zero and reports six duplicates. That is good replay behavior. The settlement still reports p3 at 2,400 cents against 2,500 expected, and includes p9 with no internal record.
>
> A deduplication key cannot detect a processor shortfall by itself. A balanced journal cannot prove that an external file is complete. Keep these controls separate and report their outcomes separately.
>
> The example is reproducible with local SQLite and synthetic data: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> Which check runs first in your pipeline, and what evidence does it produce?

## 7. Late Events: Event Time Is Not Arrival Time

**Format:** timeline diagram or five-slide carousel.

> A feature can be correct for today and still be wrong for yesterday’s model training set.
>
> Consider an event whose event time is January 1 but whose system receipt time is January 3. Before receipt, a point-in-time query should not pretend that the pipeline knew about it. After receipt, the feature may change.
>
> Keep both timestamps. Then ask the question your use case needs:
> - What happened by event time T?
> - What had arrived and was knowable by cutoff time C?
>
> Those are different temporal queries. Mixing them can leak future information into a historical feature or make an operational report appear to have known about an event early.
>
> The local lab includes a late p3 event and shows its feature as zero before receipt and 2,500 minor units afterward. Synthetic teaching example, not a production feed: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> Do you model event time and ingestion time separately?

**Carousel panels:** timeline (event Jan 1 / received Jan 3); “as happened” query; “as known then” query; leakage example; keep both clocks and choose the cutoff explicitly.

## 8. From SQL Beginner to Fintech Data Engineer

**Format:** learning-path carousel.

> A practical learning path is a sequence of things you can demonstrate, not a list of tools to memorize.
>
> 1. Learn Python, Git, tests, APIs, and data types.
> 2. Practice SQL grain, joins, NULLs, windows, and transactions.
> 3. Model facts, dimensions, and history.
> 4. Build ingestion that handles duplicate delivery, schema change, and late events.
> 5. Add payment lifecycle, exact amounts, refunds, and reconciliation.
> 6. Practice reliability: quality checks, recovery, access, and observability.
>
> At each step, produce an artifact: a tested function, a query with known cases, a model contract, or a runbook. Then explain what failure it prevents and what it cannot prevent.
>
> The free roadmap maps those stages to 100 lessons and 40 exercises; the first pass is substantial and the project estimates 200–400 hours. Choose the beginner, analyst, backend, or experienced-engineer path: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> What would you add between SQL fundamentals and production pipelines?

**Carousel panels:** six stages above, each with one artifact; final panel links to learning paths. State that the time estimate is the project’s estimate, not a promise.

## 9. I Built a Free 100-Lesson Fintech Data Engineering Roadmap

**Format:** open-source project announcement. Include transparent provenance.

> I maintain an open learning path for data engineering, data warehousing, and financial data.
>
> It now includes 100 lessons, 40 foundation exercises, eight scenario labs, and a runnable payment example. The core local labs use synthetic data, Python, and SQLite; no paid cloud account or API key is required to start.
>
> The aim is to make practical ideas testable: exact money, duplicate delivery, late events, SQL grain, settlement reconciliation, backup recovery, and point-in-time features. Each exercise has a defined task and a way to check the result.
>
> The first edition was created with AI assistance; the repository documents provenance and verification scope. All examples are educational models, not production banking infrastructure.
>
> If you work in data engineering or teach it, I’d value specific feedback on a confusing lesson or a missing failure case. Browse it here: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> A star is optional; use or share the material freely under its license.

## 10. The SQL Query Runs. The Payment Totals Are Still Wrong.

**Format:** case study/code snippet.

> A query can be valid SQL and still report the wrong money.
>
> In the roadmap’s C07 bug hunt, captures, fees, and attempts are joined at payment level before aggregation. Multiple rows on both sides fan out. The starter then uses `SUM(DISTINCT amount)`, which hides some duplicated values but also collapses separate legitimate rows with the same amount.
>
> The repair is to aggregate each source at its real grain, preserve the currency key, and left-join the summaries so payments without fees remain visible. Count attempts in their own aggregate too.
>
> The debugging sequence: write down the grain of each input, calculate the expected row multiplication, compare raw and aggregated counts, then test equal-valued events and zero-fee payments.
>
> C07 has a runnable starter and reference solution: https://github.com/antony502189-max/fintech-data-engineering-roadmap
>
> What test case most often exposes fan-out in your warehouse?

## Editorial and publishing notes

- These are AI-assisted drafts for review, not evidence of publication or personal experience. The repository confirms the maintainer and project facts; it does not support invented employment stories or anecdotes, so none are used.
- Before each post, verify the relevant file and example still exist on the default branch. Keep links only where useful; the project link is not required on every post.
- The requested ownership and experience statements should remain first-person only where directly true of the maintainer. The announcement says “I maintain” because the repository names the maintainer; it does not claim industry employment experience.
- Publish manually or through a specifically authorized integration whose terms allow the action. Current workspace has no LinkedIn publishing integration. Do not automate browser activity, scraping, messaging, comments, or connection requests.
- After publishing, record the exact post URL and actual observations in `METRICS.md`. Never infer that a star increase came from a post without reliable attribution.

