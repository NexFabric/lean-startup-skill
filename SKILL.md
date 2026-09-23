---
name: lean-startup
description: "Validates early-stage products and features under extreme uncertainty using Eric Ries's Lean Startup framework. Use for MVP scoping, Build-Measure-Learn cycle specs, vanity vs. actionable metric audits, and pivot-or-persevere decisions. Triggers: test idea fast, MVP design, vanity metrics, pivot or persevere, innovation accounting, build-measure-learn, fikri test etme, MVP tasarımı, vanity metric tuzağı, pivot kararı. Exclusions: Scaling proven PMF -> crossing-the-chasm; Interview script mechanics -> mom-test; Enterprise sales -> spin-selling; Pricing -> monetizing-innovation."
---

# The Lean Startup — Agent Skill

## ⚡ Operational Guardrails for AI Agents

1. **Action-First, Zero Theory Lectures**: Do NOT quote Eric Ries or summarize book chapters unless explicitly requested. Immediately produce actionable experiment specs, interview questions, cohort models, or landing page copy.
2. **Mandatory Distribution Plan**: An MVP with 0 traffic yields 0 data. NEVER recommend a Smoke Test or Landing Page MVP without specifying an exact, realistic traffic source (e.g., targeted subreddit, cold outbound list, ad campaign with budget, existing user base).
3. **Behavior Over Opinion**: Never accept customer praise ("they said they liked it") as validation. Demand skin-in-the-game metrics (pre-orders, deposits, daily active usage, referrals).
4. **Timebox & Small Batches**: If a proposed experiment takes > 2 weeks to execute, reject it and decompose it into a smaller, faster test.
5. **Statistical Rigor ($N \ge 30$)**: In small cohorts ($N < 30$), percentage-based split tests are statistical noise. Demand qualitative commitment signals (deposits, signed letters of intent, completed onboarding), NOT percentage conversion conclusions.
6. **Safety & Regulatory Boundaries**: In regulated, clinical, safety-critical, or high-liability domains (medical, legal, financial custody), strictly forbid deceptive fake-door smoke tests. Use non-clinical workflow proxies or verified customer discovery.

---

## 📋 Mandatory Output Contracts

Whenever asked to test an idea, design an MVP, or evaluate metrics, output one of the following structured schemas. Do NOT output unstructured conversational essays.

### Contract A: Experiment Specification (BML Loop Plan)
```markdown
### 🧪 Experiment Spec: [Hypothesis Name]
**Cycle #**: [N] | **Timebox**: [Max 14 days] | **MVP Type**: [Smoke / Concierge / Wizard of Oz / Single-feature]

| Dimension | Specification |
|---|---|
| **Leap-of-Faith Hypothesis** | "We believe that [Customer Segment] will [Action/Commitment] because [Pain/Value]." |
| **Hypothesis Type** | [Value Hypothesis OR Growth Hypothesis] |
| **MVP Architecture** | [Concise execution steps: what is built vs. faked/manual] |
| **Target Traffic Source** | [Specific distribution channel: subreddit, cold outbound list, ad budget] |
| **Primary Metric** | [Actionable metric, e.g. % pre-orders from qualified visitors] |
| **Falsification Threshold** | [Hard FAIL number: e.g., "< 5% pre-order rate on N=100 qualified visitors = Invalidate"] |
| **Explicit Non-Goals** | [What will NOT be built during this test] |
```

### Contract B: Pivot-or-Persevere Audit
```markdown
### 🔄 Pivot-or-Persevere Audit: [Product Name]
**Current Status**: [Persevere / Pivot Required / Inconclusive]

1. **Baseline vs. Current Metric Movement**:
   - Target Assumption: [Assumption]
   - Baseline Metric: [Baseline] -> Current Level: [Current]
   - Convergence Trend: [Flatlined / Diminishing Returns / Accelerating]
2. **Tuning Exhaustion Analysis**:
   - Have micro-optimizations (copy tweaks, UI button changes) failed to alter cohort retention? [Yes/No]
3. **Runway Assessment**:
   - Remaining Cash / Time: [X months]
   - Calculated Pivots Remaining: [Runway / Time-per-Pivot-Cycle]
4. **Prescribed Action**:
   - If Pivot: Select 1 of 10 types [Zoom-in, Zoom-out, Customer Segment, Customer Need, Platform, Architecture, Value Capture, Engine, Channel, Tech] with rationale.
```

---

## Should You Use This Skill?

```
Are you building something under conditions of extreme uncertainty?
|-- YES --> Do you know who your customers are?
|   |-- NO  --> Start with Four Steps (Customer Discovery), use Lean
|   |           Startup for iteration speed within that process
|   +-- YES --> Do you have product/market fit?
|               |-- NO  --> THIS SKILL. Build-Measure-Learn loop.
|               +-- YES --> Use Crossing the Chasm for mainstream scaling
+-- NO  --> Are you optimizing an existing product in a known market?
            |-- YES --> Lean Startup principles apply (small batches, Five Whys)
            +-- NO  --> Rethink what you're doing
```

---

## Core Mental Models & Rules of Thumb

### The Two Leap-of-Faith Assumptions
| Assumption | Core Question | Validation Method |
|---|---|---|
| **Value hypothesis** | Does the product deliver value once used? | Retention, repeat usage, willingness to pay |
| **Growth hypothesis** | How will new customers discover the product? | Sustainable engine mechanics (churn, viral $k$, LTV/CPA) |

### The Three Engines of Growth (Focus on ONE)
| Engine | Core Metric | Growth Condition | Anti-Pattern |
|---|---|---|---|
| **Sticky** | Churn rate | Acquisition > Churn | Spending on ads before fixing 15% monthly churn |
| **Viral** | Viral coefficient ($k$) | $k > 1.0$ | Forcing viral loops onto confidential B2B enterprise software |
| **Paid** | CPA vs. LTV | $(\text{Gross Margin} \times \text{LTV}) > \text{CPA}$ | Scaling paid spend with negative gross margins or token burn |

### Innovation Accounting: Three Milestones
1. **Establish Baseline**: Test MVP with real cohort; measure conversion & retention.
2. **Tune Engine**: Single-variable experiments moving baseline toward target.
3. **Pivot or Persevere**: If tuning hits diminishing returns without reaching viability -> PIVOT.

### The 10 Structural Pivot Types
`Zoom-in`, `Zoom-out`, `Customer Segment`, `Customer Need`, `Platform`, `Business Architecture`, `Value Capture`, `Engine of Growth`, `Channel`, `Technology`.

---

## Decision Trees

### "What should our MVP be?"
```
What do you need to LEARN?
|-- "Do customers want this at all?"
|   +-- Smoke test (landing page + traffic) or Video MVP
|-- "Will customers pay for this?"
|   +-- Concierge or Wizard of Oz (deliver manually, charge real money)
+-- "Which features matter?"
    +-- Single-feature MVP + split testing (N >= 30)
```

### "Should we pivot?"
```
Are experiments moving metrics toward the ideal?
|-- YES, meaningfully --> Persevere. Keep tuning.
|-- YES, but very slowly --> Investigate. Are you out of easy optimizations?
|   |-- YES --> Consider pivot
|   +-- NO  --> Keep tuning, but set a deadline
+-- NO --> Have you exhausted experiment ideas for current strategy?
          |-- YES --> PIVOT. Convene pivot meeting; select structural pivot.
          +-- NO  --> Run more experiments, but set a time box.
```

---

## Supporting Files

- **[frameworks.md](frameworks.md)** - Full academic theory: BML cycle deep-dive, engines math, SMED, Five Whys, Sandboxes.
- **[cases.md](cases.md)** - 14 real-world cases: IMVU, Zappos, Dropbox, Groupon, Grockit, Votizen, Wealthfront, Intuit, etc.
- **[examples.md](examples.md)** - Complete printable worksheets, templates, and end-to-end MealSync case walkthrough.
- **[integration.md](integration.md)** - Hand-offs: Mom Test, Four Steps, Crossing the Chasm, $100M Offers, SPIN Selling.
