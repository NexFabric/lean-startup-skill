# Lean Startup — Agent Skill

> An AI agent skill implementing Eric Ries's **Lean Startup** methodology for building products under extreme uncertainty.
> Compatible with **Claude Code**, **Google Antigravity**, **Cursor**, and any agent platform supporting markdown skills.

---

## 📌 Overview

This skill equips AI agents with the mental models, decision trees, case studies, and practical templates from Eric Ries's *The Lean Startup* (2011). It guides founders and product teams through the **Build-Measure-Learn** feedback loop, testing leap-of-faith assumptions, designing minimum viable products (MVPs), practicing innovation accounting, and making disciplined pivot-or-persevere decisions.

---

## 🚀 Quick Install

### 1. Claude Code
Clone or symlink into your Claude skills directory:
```bash
git clone https://github.com/NexFabric/lean-startup-skill.git ~/.claude/skills/lean-startup
```

### 2. Google Antigravity / Gemini CLI
Symlink into your Antigravity skills directory:
```bash
ln -s ~/.claude/skills/lean-startup ~/.gemini/config/skills/lean-startup
```

### 3. Cursor / Custom Prompts
Reference [SKILL.md](SKILL.md) directly in your `.cursorrules` or agent instructions.

---

## 📂 Repository Structure

| File | Content & Purpose |
|---|---|
| **[`SKILL.md`](SKILL.md)** | **Core agent instruction file** containing the 5 principles, Build-Measure-Learn loop, MVP types, Innovation Accounting milestones, 10 Pivots, 3 Engines of Growth, Small Batches, Five Whys, decision trees, and modern relevance. |
| **[`frameworks.md`](frameworks.md)** | **Deep-dive mechanics**: Reverse planning (Learn → Measure → Build), value vs. growth hypotheses, analogs/antilogs, math of the 3 engines of growth, SMED, continuous deployment, Andon cord, Five Whys rules, and corporate Innovation Sandboxes. |
| **[`cases.md`](cases.md)** | **14 detailed real-world case studies**: IMVU, Zappos, Dropbox, Groupon, Grockit, Votizen, Wealthfront, QuickBooks / Intuit, IGN Entertainment, SGW Designworks, School of One, Food on the Table, and cautionary disasters (Webvan, Apple Newton, Iridium). |
| **[`examples.md`](examples.md)** | **Actionable templates & worksheets**: Build-Measure-Learn cycle planner, MVP selection worksheet, innovation accounting funnel template, pivot-or-persevere agenda, engine of growth diagnostic, cohort analysis tracker, Five Whys template, and an end-to-end startup case study (MealSync). |
| **[`integration.md`](integration.md)** | **Strategic interoperability**: How Lean Startup integrates with *Four Steps to the Epiphany*, *The Mom Test*, *Crossing the Chasm*, *$100M Offers*, *SPIN Selling*, *Obviously Awesome*, *Monetizing Innovation*, and *Blue Ocean Strategy*, plus the master 3-phase sequence (Search → Launch → Scale). |

---

## 🎯 When to Use This Skill

### Triggers:
- "How do we test this idea fast without building the full product?"
- "What should our MVP look like (Smoke test, Video, Concierge, Wizard of Oz)?"
- "Our metrics look good on the dashboard, but revenue isn't growing (vanity metrics trap)."
- "Should we pivot or persevere?"
- "We're building features nobody seems to use."
- "How do we measure validated learning?"
- "How do we set up innovation accounting and cohort retention?"

### When NOT to Use:
- **Proven Product/Market Fit**: Scaling an established playbook in enterprise tech → use *Crossing the Chasm*.
- **Market Type Classification**: Determining if you are entering an existing, resegmented, or new market → use *Four Steps to the Epiphany*.
- **Qualitative Customer Interviews**: Learning how to interview customers without biasing them → use *The Mom Test*.
- **Offer Construction & Packaging**: Designing high-converting guarantees and bonuses once value is proven → use *$100M Offers*.
- **Pricing Strategy**: Designing product tiers around willingness to pay → use *Monetizing Innovation*.

---

## 🧠 Core Mental Models

```
         IDEAS
        /      \
       /        \
  LEARN          BUILD
      \          /
       \        /
        DATA--PRODUCT
        (Measure)

  Rule: Plan in reverse (Learn -> Measure -> Build).
        Execute forward (Build -> Measure -> Learn).
```

### The Three Engines of Growth
1. **Sticky Engine**: Driven by retention. Growth = New Acquisition Rate − Churn Rate.
2. **Viral Engine**: Driven by side effect of usage. Viral coefficient $k > 1.0$ produces exponential growth.
3. **Paid Engine**: Driven by unit economics. Growth occurs when Customer Lifetime Value exceeds Cost Per Acquisition ($\text{LTV} > \text{CPA}$).

### Innovation Accounting Milestones
1. **Establish the Baseline**: Ship an MVP and measure real customer behavior (cohort conversion, retention).
2. **Tune the Engine**: Run single-variable experiments to move metrics toward the ideal model.
3. **Pivot or Persevere**: Evaluate if progress is sufficient to achieve the model before runway runs out (Runway = Pivots Remaining).

---

## 📜 Intellectual Lineage & Fair Use Notice

This skill is an independent analytical synthesis and practical adaptation for AI agents. It does not replace Eric Ries's original book *The Lean Startup* (Crown Business, 2011). We strongly recommend reading the original text for full historical context and philosophical depth.

---

## 📄 License

MIT License. Free to use, adapt, and share.
