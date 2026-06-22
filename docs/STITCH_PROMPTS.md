# Google Stitch prompts — Lawyer's Legal Documentation App

Style direction for every screen: **black & white, minimal, luxury law-firm
aesthetic** — think a high-end legal practice's letterhead, not a typical
SaaS dashboard. Generous whitespace, serif headings, thin hairline dividers,
no bright colors, no rounded "bubbly" UI, no emoji/icons unless line-art and
monochrome.

---

## Master style prompt (paste first, before any screen prompt)

```
Design system: pure black and white, minimal luxury law-firm aesthetic.
Background: off-white / ivory (#FAFAF8). Text: near-black (#111111).
One accent only: a single hairline gold or charcoal divider line — no other color.
Typography: elegant serif for headings (e.g. Canela, Times, or a Georgia-style serif),
clean sans-serif for body/data (e.g. Inter or Helvetica Neue).
Layout: generous margins, lots of negative space, content centered in a narrow
column (max ~900px), no card shadows, no gradients, no rounded pill buttons —
sharp/minimal rectangular buttons with a thin 1px border, fill on hover only.
Icons: thin line icons only, black, no fill, no color.
Overall feel: a private client report from a top-tier law firm, not a tech startup.
No illustrations, no stock photography, no bright call-to-action colors.
```

---

## Screen 1 — Upload batch

```
Screen: "Upload Client Documents"
A minimal, centered page. Top: small eyebrow text "LAWYER'S LEGAL DOCUMENTATION APP"
in tracked-out small caps, thin gold hairline underneath.
Large serif heading: "Begin a New Case File"
Subtext in sans-serif, muted gray: "Upload the client's documents. Each file is read,
classified, and arranged into a chronological record automatically."

Form fields:
- Text input, label "Client Name", minimal underline-only style (no boxed border)
- File drop zone: large dashed-border rectangle, centered icon (thin line document/upload icon),
  text "Drag files here or click to browse — PDF, JPG, PNG"
- Below drop zone: a quiet list of selected files as plain text rows with a thin divider,
  each row showing filename + a small "remove" (×) in the corner

Primary action: a black filled rectangular button, white serif text, "Process Documents",
full width or right-aligned, no rounded corners.
Below button: small muted status line for progress, e.g. "Reading document 3 of 12..."
```

---

## Screen 2 — Chronological document register

```
Screen: "Case File — Chronological Register"
Heading (serif): "Document Register"
Subtext: "Client: {client_name}  ·  Batch #{batch_id}  ·  {n} documents, sorted by date"

A clean table, no shading on rows, thin 1px horizontal hairlines only (no vertical lines):
Columns: Date | Document Type | Parties | Survey No. | Source File
- Date column: serif, e.g. "12 Mar 1987"
- Document Type: small caps sans-serif, e.g. "SALE DEED"
- Survey No. shown as a minimal outlined tag, black text, 1px black border, no fill
- Hover state on row: a very subtle 5% gray background, nothing else

Below table: a quiet text link-style button "Trace a Survey Number →"
```

---

## Screen 3 — Survey number trace / chain of title

```
Screen: "Trace a Survey Number"
Heading (serif): "Chain of Title"
Search field: minimal underline input, placeholder "Enter survey number, e.g. 2/A",
paired with a plain text button "Search" (no icon, no fill, just underline on hover)

Result: a vertical timeline laid out top to bottom (earliest at top), each entry as
a horizontal record:
- Left: the date, in serif, vertically aligned
- A thin vertical hairline connecting entries top to bottom (like a single quiet timeline rule)
- Right: document type (small caps), parties involved, one-line summary in muted gray

At the bottom of the timeline: a black outlined button (not filled), text
"Draft Legal Opinion for Survey {number}"
```

---

## Screen 4 — Legal opinion draft

```
Screen: "Legal Opinion — Draft"
Page styled like a formal printed legal document:
- Centered narrow column, like a letter/document, white background, generous margins
- Top: firm-style header block — "LEGAL OPINION ON TITLE" centered, small caps, serif,
  thin gold hairline beneath
- Below: meta block, right-aligned, muted gray small text: "Survey No. 2/A  ·  Drafted {date}"
- Body: justified serif paragraph text under numbered section headings:
  1. Description of Property
  2. Chronology of Title
  3. Present Ownership
  4. Encumbrances
  5. Observations
  6. Opinion
- Each section heading: small caps, letter-spaced, thin hairline underneath, serif
- Bottom: two plain outlined buttons side by side, no fill: "Edit" and "Export as PDF"
```

---

## Sample data to paste into Stitch for realistic mockups

```
Client: R. Subramaniam
Batch #: 14
Documents: 8

1. 14 Jan 1962 — Partition Deed — Between: Murugan Pillai (executant), Ramasamy Pillai (co-sharer) — Survey No. 1/A, 2/A
2. 09 Jun 1971 — Sale Deed — Seller: Ramasamy Pillai, Buyer: K. Velu — Survey No. 2/A
3. 22 Nov 1978 — Mortgage Deed — Mortgagor: K. Velu, Mortgagee: Indian Bank — Survey No. 2/A
4. 03 Mar 1985 — Release Deed — Released by: Indian Bank — Survey No. 2/A
5. 17 Aug 1990 — Gift Deed — Donor: K. Velu, Donee: K. Lakshmi — Survey No. 2/A, 3/A
6. 25 Dec 1999 — General Power of Attorney — Principal: K. Lakshmi, Agent: S. Raman — Survey No. 2/A
7. 11 Apr 2008 — Sale Deed — Seller: K. Lakshmi (through GPA), Buyer: R. Subramaniam — Survey No. 2/A
8. 30 Jul 2021 — Encumbrance Certificate — Survey No. 2/A — No pending encumbrance noted

Target survey number for trace screen: 2/A
```

---

## How to use in Stitch

1. Paste the **master style prompt** first as a global style instruction.
2. Generate each screen one at a time using its own prompt block above.
3. Paste the sample data into the prompt when Stitch asks for content, so the
   mockup shows realistic rows instead of generic placeholders.
4. Once you've generated/refined screens you like, export the design (PNG/HTML)
   and send it back here — I'll translate the approved layout into real
   HTML/CSS for `frontend/index.html`, replacing the current plain version.
