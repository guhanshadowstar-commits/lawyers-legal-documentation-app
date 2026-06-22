# Google Stitch prompts — LegalCore

Style direction: **dark mode, modern, energetic** — based on a fitness-app
inspiration (near-black background, neon lime-green accent, rounded cards,
bold sans-serif, circular progress rings, pill buttons), adapted to a legal
document workflow.

---

## Master style prompt (paste first, before any screen prompt)

```
Design system: dark mode app UI. Background: near-black (#121212 / #1A1A1A).
Cards: slightly lighter dark gray (#1E1E1E), large rounded corners (20-24px radius).
Accent color: neon lime-green (#D6FF3F or similar), used boldly for primary
buttons, progress indicators, highlighted tags, and active nav states — only
one accent color, used generously and confidently (not timidly).
Text: white headings, light gray (#A0A0A0) for secondary/meta text.
Typography: bold, modern sans-serif (e.g. Inter, SF Pro, Poppins) — big bold
numbers for stats/counts, medium-weight body text.
Buttons: pill-shaped (fully rounded), lime-green fill with black text for
primary actions; dark outlined pill buttons for secondary actions.
Components: circular progress rings, rounded image cards with bold overlay
text, bottom navigation bar with a raised circular lime-green center button.
Icons: simple line icons, white or lime-green.
Overall feel: energetic, modern, premium tech product — like a fitness or
finance app, not a traditional law-firm document.
```

---

## Screen 1 — Upload batch

```
Screen: "New Case File"
Dark background. Top bar: small white text "LEGALCORE" top-left,
profile/avatar icon top-right.
Bold white heading: "Start a New Case"
Light gray subtext: "Upload your client's documents — we'll read, sort, and
organize them automatically."

Rounded dark card containing:
- Text input "Client Name", dark rounded field, lime-green focus outline
- Large rounded dashed-border drop zone, centered upload icon in lime-green,
  text "Drag files or tap to upload — PDF, JPG, PNG"
- Selected files shown as small rounded chips/pills with filename + an × to remove

Primary button: full-width pill button, lime-green fill, bold black text,
"Process Documents"
Below: a circular progress ring (like the fitness app's step ring) showing
upload/processing progress, e.g. "7 / 12 documents read"
```

---

## Screen 2 — Chronological document register

```
Screen: "Document Register"
Dark background. Bold white heading: "Your Case Timeline"
Subtext in light gray: "Client: {client_name} · {n} documents · sorted by date"

Stat row at top (like the fitness app's Steps/Calories row): 3 rounded dark
cards side by side showing big bold lime-green numbers:
- "12" Documents
- "1962–2021" Date Range
- "4" Survey Numbers

Below: a vertical list of rounded dark cards, one per document, each showing:
- Small lime-green pill tag with the document date
- Bold white document type (e.g. "SALE DEED")
- Light gray line: parties involved
- Small outlined pill tag(s) for survey number(s)
- Right-aligned chevron arrow to open detail

Bottom navigation bar: dark, icons for Home / Documents / Search / Profile,
with a raised circular lime-green "+" button in the center for new upload.
```

---

## Screen 3 — Survey number trace / chain of title

```
Screen: "Trace a Survey Number"
Dark background. Bold white heading: "Chain of Title"
Search bar: rounded dark pill input with search icon, placeholder
"Enter survey number, e.g. 2/A", lime-green search button.

Results shown as a vertical timeline of rounded dark cards connected by a
thin lime-green vertical line (like a fitness app's workout progress path):
- Each card: date in bold white, document type as a small lime-green pill tag,
  parties and one-line summary in light gray text
- Earliest entry at top, most recent at bottom

Bottom: full-width lime-green pill button, bold black text,
"Draft Legal Opinion for Survey 2/A"
```

---

## Screen 4 — Legal opinion draft

```
Screen: "Legal Opinion — Draft"
Dark background, but the opinion content sits inside a large rounded white
or light-cream card (like a "document" floating on the dark UI) for readability —
this is the one screen that breaks to a light surface intentionally, framed by
the dark app shell around it.
Card header: bold heading "Legal Opinion on Title", small lime-green pill tag
"Survey No. 2/A", meta text "Drafted {date}"

Numbered sections inside the card (clean black text on the light card surface):
1. Description of Property
2. Chronology of Title
3. Present Ownership
4. Encumbrances
5. Observations
6. Opinion

Below the card, on the dark background: two pill buttons side by side —
lime-green filled "Export as PDF" and dark outlined "Edit"
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
