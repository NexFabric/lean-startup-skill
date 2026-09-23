# The Lean Startup — Agent Skill (2026 Edition)

> **Stop wasting months building features nobody wants.**  
> This skill transforms **Claude Code**, **Google Antigravity**, **Cursor**, and AI coding agents into an adversarial startup operating partner that ruthlessly shreds vanity metrics, scopes 7-day MVPs, and outputs execution-ready experiment specifications.

---

## ⚡ What This Skill Actually Delivers to the User

Rather than generating vague book summaries or conversational advice, this skill enforces a **deterministic output contract**. When you prompt your agent, it produces 4 concrete, actionable artifacts:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AGENT OUTPUT CONTRACT                           │
├──────────────────────────────┬─────────────────────────────────────────┤
│ 1. 🧪 EXPERIMENT SPEC        │ 1-Page blueprint with Leap-of-Faith     │
│    (BML LOOP PLAN)           │ hypothesis, exact traffic channel, and  │
│                              │ pre-committed numerical FAIL criteria.  │
├──────────────────────────────┼─────────────────────────────────────────┤
│ 2. ✂️ MVP DECONSTRUCTION     │ Cuts 9 out of 10 roadmap features.      │
│    SCOPING SPEC              │ Scopes a 48-hour Concierge or Wizard of │
│                              │ Oz manual test before writing code.     │
├──────────────────────────────┼─────────────────────────────────────────┤
│ 3. 📊 COHORT RETENTION &     │ Shreds cumulative "up-and-to-the-right" │
│    MARGIN DIAGNOSTIC         │ vanity graphs into Day 1/7/30 cohorts   │
│                              │ and Gross-Margin-Adjusted LTV/CPA math. │
├──────────────────────────────┼─────────────────────────────────────────┤
│ 4. 🔄 PIVOT-OR-PERSEVERE     │ Board-ready analysis evaluating tuning  │
│    DECISION MEMO             │ exhaustion, runway in pivots remaining, │
│                              │ and matching to 1 of 10 pivot types.    │
└──────────────────────────────┴─────────────────────────────────────────┘
```

---

## 🚀 Quick Install

### 1. Claude Code
Clone directly into your Claude skills directory:
```bash
git clone https://github.com/NexFabric/lean-startup-skill.git ~/.claude/skills/lean-startup
```

### 2. Google Antigravity / Gemini CLI
Symlink into your Antigravity skills directory:
```bash
ln -s ~/.claude/skills/lean-startup ~/.gemini/config/skills/lean-startup
```

### 3. Cursor / Custom Prompts
Reference [SKILL.md](SKILL.md) directly in your `.cursorrules` or project instructions.

---

## 🎯 When to Use This Skill

### Trigger Prompts (EN & TR):
- *"How do we test this SaaS idea fast without building the full product?"* / *"Fikrimi kod yazmadan nasıl hızlı test ederim?"*
- *"What should our MVP look like (Smoke test, Video, Concierge, Wizard of Oz)?"* / *"Bu ürün için MVP tasarımı yap"*
- *"Our dashboard shows 10,000 signups but revenue is flat. What's wrong?"* / *"Vanity metric tuzağında mıyız?"*
- *"We ran 5 A/B tests and conversion hasn't moved. Should we pivot?"* / *"Pivot etmeli miyiz, persevering mi yapmalıyız?"*
- *"Audit our innovation accounting and cohort retention curves."*

### Exclusions & Handoffs:
- **Scaling proven PMF in enterprise**: Use *Crossing the Chasm*.
- **Customer conversation questioning technique**: Use *The Mom Test*.
- **Enterprise sales objection handling**: Use *SPIN Selling*.
- **High-ticket offer construction & bonuses**: Use *$100M Offers*.
- **Pricing tier optimization**: Use *Monetizing Innovation*.

---

## 📂 Repository Structure

| File | Content & Purpose |
|---|---|
| **[`SKILL.md`](SKILL.md)** | **Core agent runtime contract (<170 lines)**: Enforced output schemas (Experiment Spec & Pivot Audit), operational guardrails, engine mechanics, and decision trees. Optimized for LLM primacy/recency attention. |
| **[`frameworks.md`](frameworks.md)** | **Deep-dive mechanics**: Reverse planning (Learn → Measure → Build), value vs. growth hypotheses, analogs/antilogs, math of the 3 engines, SMED, continuous deployment, Andon cord, Five Whys, and corporate Innovation Sandboxes. |
| **[`cases.md`](cases.md)** | **14 detailed case studies**: IMVU (continuous deployment), Zappos (Wizard of Oz), Dropbox (video MVP), Groupon (WordPress MVP), Grockit (cohort analysis), Votizen (pivot acceleration), Wealthfront, Intuit SnapTax, etc. |
| **[`examples.md`](examples.md)** | **Actionable templates & worksheets**: BML cycle planner, MVP selection worksheet, innovation accounting setup template, pivot meeting agenda, Five Whys template, and end-to-end MealSync case study. |
| **[`integration.md`](integration.md)** | **Strategic interoperability**: How Lean Startup integrates with *Four Steps to the Epiphany*, *The Mom Test*, *Crossing the Chasm*, *$100M Offers*, *SPIN Selling*, *Obviously Awesome*, *Monetizing Innovation*, and *Blue Ocean Strategy*. |
| **[`evals/`](evals/)** | **10-case benchmark test suite** verifying that AI models output structured deliverables, call out vanity metrics, enforce distribution plans, and respect regulatory boundaries. |

---

## 🛡️ Operational Guardrails (2026 Reality Filters)

1. **Zero Theory Lectures**: The agent will never lecture you on Eric Ries quotes. It generates immediate experiment specifications or audits.
2. **Mandatory Distribution Plan**: An MVP without traffic yields 0 data. The agent strictly rejects any Smoke Test that lacks an explicit, realistic traffic source (targeted subreddit, cold outreach list, ad campaign budget).
3. **Statistical Rigor ($N \ge 30$)**: In small cohorts ($N < 30$), percentage split tests are statistical noise. The agent demands qualitative commitment signals (deposits, signed letters of intent) rather than percentage conversions.
4. **AI Unit Economics (Token COGS)**: In AI products, the agent evaluates Paid Engine viability as $(\text{Gross Margin} \times \text{LTV}) > \text{CPA}$, preventing runaway token inference burn from disguising as "growth."
5. **Safety-Critical Domain Fence**: In medical, clinical, fintech, or legal custody domains, the agent strictly halts deceptive fake-door smoke tests and enforces verified discovery proxies.

---

## 📄 License

MIT License — Copyright (c) 2026 NexFabric. Free to use, adapt, and share.
