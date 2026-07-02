# Project 3 — RAG Document Intelligence System

> Simulating a Retrieval-Augmented Generation (RAG) workflow for legal document analysis using Claude Projects

---

## Problem Statement

A law firm has 500-page contracts that take hours to read manually. They need a tool that can:
- Instantly summarize key clauses
- Answer specific questions about the document
- **Never hallucinate** (make up facts)
- Cite exact sections for every answer
- Automatically extract Risks, Dates, and Stakeholders

---

## What is RAG? (Simple Explanation)

```
Without RAG:
Question → AI uses memory → might hallucinate ❌

With RAG:
Question → AI searches document → finds relevant
           section → generates answer from THAT
           section only → cites source ✅
```

Think of it like an open-book exam — the AI only answers from what's in front of it.

---

## What Was Built

A complete RAG workflow using Claude Projects that:

| Feature | Result |
|---------|--------|
| Document Q&A with citations | ✅ Every answer cites Section X.X |
| Zero hallucination | ✅ 0/4 hallucination test failed |
| Auto Risk extraction | ✅ 7 risks found and classified |
| Auto Date extraction | ✅ 11 key dates identified |
| Auto Stakeholder extraction | ✅ 9 stakeholders found |
| Executive Summary | ✅ 3-paragraph professional summary |

---

## Sample Document Used

**Software Services Agreement — NSA-2024-0892-ENTERPRISE**

| Field | Details |
|-------|---------|
| Parties | NexaCore Technologies Inc. vs Meridian Global Partners LLC |
| Contract Value | USD $4,750,000 |
| Term | January 15, 2024 — January 14, 2027 (3 Years) |
| Pages | 8 pages, 12 sections |

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Claude Projects (claude.ai) | Primary RAG platform — document upload + chat |
| ReportLab (Python) | Generated sample legal contract PDF |

---

## Prompt Engineering Techniques

### 1. Citation Forcing Prompt
Forces the AI to cite every answer with section number:
```
For EVERY answer you give, you MUST cite:
→ Section number (e.g. Section 3.1)
→ Exact clause name
Format: [SOURCE: Section X.X — Clause Name]
```

### 2. Grounding Rules (Anti-Hallucination)
```
1. ONLY use information found in the uploaded document
2. NEVER use outside knowledge or make assumptions
3. If information is NOT in the document, say:
   "This information is not found in the provided document."
4. Never guess or hallucinate facts
```

### 3. Structured Extraction Prompt
Single prompt that extracts all three categories simultaneously with consistent formatting.

---

## Test Results

### Test 1 — Document Verification
| Question | Answer | Citation | Status |
|----------|--------|----------|--------|
| Party names? | NexaCore + Meridian | Party Details / Section 1 | ✅ |
| Contract value? | $4,750,000 | Section 4.1 | ✅ |
| Start date? | January 15, 2024 | Section 3.1 | ✅ |

### Test 2 — Citation Prompt
| Question | Citations Found | Status |
|----------|----------------|--------|
| Early termination? | Section 3.3, 3.4, 3.5 | ✅ |

### Test 3 — Hallucination Test (Most Important)
| Question | Expected | Actual | Status |
|----------|----------|--------|--------|
| CEO phone number? | NOT FOUND | NOT FOUND | ✅ |
| Software crash penalty? | NOT FOUND | NOT FOUND | ✅ |
| Cloud hosting region? | NOT FOUND | NOT FOUND | ✅ |
| Project manager name? | NOT FOUND | NOT FOUND | ✅ |

**Hallucination Rate: 0% — Perfect Score**

---

## Summary Dashboard Results

### Risks Extracted (7 Total)
| # | Risk | Severity | Section |
|---|------|----------|---------|
| R1 | Early termination fee (20%) | HIGH | 3.3 |
| R2 | Late payment interest (18% p.a.) | HIGH | 4.2 |
| R3 | Liability cap (12-month ceiling) | HIGH | 9.1 |
| R4 | Data breach 48-hour notification | HIGH | 6.3 |
| R5 | No consequential damages | MEDIUM | 9.2 |
| R6 | Auto-renewal risk | MEDIUM | 3.2 |
| R7 | IP ownership on full payment only | MEDIUM | 5.1 |

### Key Dates Extracted (11 Total)
| Date | Purpose | Section |
|------|---------|---------|
| Jan 15, 2024 | Contract start + deposit ($475K) | 3.1 / 4.1 |
| Apr 30, 2024 | Phase 1 payment ($712,500) | 4.1 |
| Aug 31, 2024 | Phase 2 payment ($712,500) | 4.1 |
| Dec 31, 2024 | Go-Live payment ($950,000) | 4.1 |
| Jan 15, 2025 | Year 2 fee ($950,000) | 4.1 |
| Jan 15, 2026 | Year 3 fee ($950,000) | 4.1 |
| Jan 14, 2027 | Contract expiry | 3.1 |
| 90 days before expiry | Non-renewal notice deadline | 3.2 |
| 180 days notice | Convenience termination notice | 3.3 |
| 30 days cure period | Material breach cure period | 3.4 |
| 5 years post-term | Confidentiality survival period | 7.2 |

### Stakeholders Found (9 Total)
| Name | Role | Section |
|------|------|---------|
| NexaCore Technologies Inc. | Service Provider | Recitals |
| Meridian Global Partners LLC | Client | Recitals |
| Jonathan R. Whitfield | CEO, NexaCore (Signatory) | Signature |
| Sarah K. Montgomery | COO, Meridian (Signatory) | Signature |
| Rachel P. Dunmore | General Counsel, NexaCore | Signature |
| Marcus T. Belleview | Senior Legal Counsel, Meridian | Signature |
| AWS / Microsoft Azure | Cloud Subcontractors | 2.1 |
| Bloomberg / Salesforce / SAP | Integrated Systems | 2.1 |
| JAMS / AAA | Dispute Resolution Bodies | 11.2/11.3 |

---

## Folder Structure

```
RAG-Document-Intelligence/
├── 01-Document/
│   └── Sample_Legal_Contract.pdf
├── 02-Prompts/
│   ├── citation-prompt.txt
│   ├── dashboard-prompt.txt
│   └── hallucination-test-prompt.txt
├── 03-QA-Results/
│   └── qa-test-results.txt
├── 04-Dashboard/
│   └── dashboard-results.txt
├── 05-Hallucination-Test/
│   └── (screenshots)
├── 06-Final-Results/
│   └── (all screenshots)
└── README.md
```

---

## Key Learnings

- RAG grounding completely eliminates hallucination when prompts are well-engineered
- Citation forcing prompts make AI responses verifiable and trustworthy
- Structured extraction prompts can replace hours of manual document review
- Claude Projects is highly effective for document intelligence tasks
- Negative space testing (asking for things NOT in document) is critical for validation

---

## Screenshots

All test result screenshots are saved in `06-Final-Results/` folder.

---

*Completed: June 2026 | AI/ML Internship Program*
