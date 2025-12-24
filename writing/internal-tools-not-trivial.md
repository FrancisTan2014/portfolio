---
layout: default
title: Why “fetch → format → display” is not trivial
---

For years, I believed internal tooling systems were simple: fetch data, format it, and display it.
Compared to customer-facing products, they appeared low-risk and straightforward.

That perception comes from focusing on what these systems do, rather than how they behave under real organizational and operational constraints.

### Technical correctness vs human trust
Even when the system is technically correct, internal tools often fail at a different boundary: human trust.
For internal users, correctness is necessary but insufficient; reliability and predicability shape whether 
the tool is trusted at all.
Once that trust erodes, users do not wait for fixes —— they route around the system with spreadsheets, 
scripts, or alternative tools.
At that point, the system may still function as designed, but it has already failed in practice.
This boundary cannot be addressed clearer requirements alone; it requires understanding how the 
tool fits into real human workflows and what failures users are willing —— or unwilling —— to tolerate. 