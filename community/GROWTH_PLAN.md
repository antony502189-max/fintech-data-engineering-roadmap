# Help the right learners discover the roadmap

The maintainer's goal is 1,000 voluntary GitHub stars. On October 21, 2026,
the GitHub repository API reported 2 stars. This is a baseline, not evidence of
traction or a prediction. There is no guaranteed timeline to reach the goal.

## Lead with one reproducible result

Use the [missing-dollar experiment](../docs/FIRST_WIN.md) as the entry point.
The audience is an analyst moving into engineering, a backend engineer handling
payments, or a data engineer learning financial correctness. The value proposition:
learn why idempotency and a balanced journal cannot replace reconciliation.

Only promote commands already available on the default branch. A screenshot or
recording must show an actual run, with synthetic data and the current commit.
Do not describe the local simulations as deployed Kafka, dbt, or banking systems.

## First 30 days

| Window | Deliverable | What to learn |
|---|---|---|
| Days 1-3 | Merge and check the first-win experience; record a 45-60 second terminal demo | Can someone reproduce the result using only the README? |
| Days 4-7 | Publish one personal LinkedIn or DEV post using the sharing drafts | Which questions or startup problems do readers report? |
| Week 2 | Share a technical explanation in one relevant community that permits project sharing | Is the problem useful to that audience? |
| Week 3 | Publish a second worked example from C07, including the wrong SQL and its corrected totals | Do readers continue from the demo to an exercise? |
| Week 4 | Fix the top onboarding problems and publish a short changelog with verified examples | Did feedback produce a better learning experience? |

The owner chooses channels and posts. Check each community's current rules before
sharing. Answer questions with useful technical detail; avoid repeating the same
link across unrelated threads. Ask before quoting someone's feedback publicly.
Do not buy stars, exchange stars, send unsolicited bulk messages, or invent users.

## A weekly record

Use the repository's Insights traffic view when available. Record the observation
time and window: traffic is a rolling view, so save observations regularly.
Do not infer individual learning progress from anonymous visits or clones.

| Week ending | Stars at observation | Unique visitors and window | Unique cloners and window | Post URL | Reproducible feedback | Fix shipped |
|---|---:|---|---|---|---|---|
| 2026-10-21 baseline | 2 | 5; returned daily buckets October 7-20, 2026 UTC | 31; returned daily buckets October 7-20, 2026 UTC | None in this launch | Not captured | Pending review |

Baseline source: authenticated GitHub REST repository metadata and traffic
`views` / `clones` endpoints, observed October 21, 2026. The same traffic responses
reported 9 total views and 79 total clones. Automated activity may be included;
unique cloners are not necessarily learners. The dates above describe returned
daily buckets, not a lifetime total.

Use total stars as the goal indicator. Use startup reports, completed exercise
examples shared voluntarily, and substantive contributions as evidence of utility.
Do not call stars divided by weekly visitors a conversion rate: the populations
and time windows do not establish attribution.

At 10 stars, focus on first-session failures. At 100, improve the examples readers
use most. At 300, seek an optional walkthrough or contribution from an educator.
At 1,000, publish what improved and credit contributors. These are checkpoints,
not promised outcomes or deadlines.

## Decide the next change

- Visitors but repeated setup failures: simplify instructions and reproduce the failure.
- Few visitors: try one better-matched channel and a more concrete technical example.
- Demo runs but learners get stuck: improve that task's contract and error explanation.
- Useful feedback: ship a focused fix and link the resulting changelog from the next post.

See [sharing drafts](SHARING.md). Update the baseline with real observations;
leave unknown values blank or explicitly unknown.
