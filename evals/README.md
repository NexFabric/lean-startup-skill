# Evaluation Suite — Lean Startup Agent Skill

This directory contains benchmark test cases designed to evaluate whether an AI agent equipped with `lean-startup` acts in accordance with Eric Ries's methodology rather than falling into standard startup traps or giving generic advice.

---

## 🧪 Test Scenarios (`test_cases.json`)

| Test ID | Scenario | Pass Criteria |
|---|---|---|
| `eval-01-vanity-metrics-trap` | Founder excited about cumulative downloads | Identifies vanity metrics; demands cohort retention data before scaling. |
| `eval-02-overengineered-mvp` | 7-month software build before user validation | Deconstructs into a Concierge / Wizard of Oz experiment in under 2 weeks. |
| `eval-03-distribution-blind-smoke-test` | Zero signups on an unpromoted landing page | Checks traffic sources before concluding hypothesis is invalidated. |
| `eval-04-stalled-engine-pivot` | Diminishing returns on minor A/B copy tweaks | Calls for a Pivot-or-Persevere meeting; evaluates structural pivot types. |
| `eval-05-engine-mismatch` | Attempting viral loops for enterprise B2B compliance | Rejects viral engine for high-ticket B2B; enforces Sticky/Paid engine alignment. |

---

## 🏃 Running Evals

You can use these prompts to test any LLM agent (Claude Code, Gemini CLI, Cursor, etc.):

```bash
# Feed any test prompt into your agent session and verify against evaluation_criteria:
python3 -c "
import json
with open('evals/test_cases.json') as f:
    cases = json.load(f)
for c in cases:
    print(f'=== {c[\"id\"]}: {c[\"title\"]} ===')
    print(f'Prompt: {c[\"prompt\"]}\n')
"
```
