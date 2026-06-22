---
name: Kinetic Volt
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c5c9ae'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8f937a'
  outline-variant: '#454934'
  surface-tint: '#afd500'
  primary: '#ffffff'
  on-primary: '#293500'
  primary-container: '#caf231'
  on-primary-container: '#586c00'
  inverse-primary: '#526600'
  secondary: '#c8c6c5'
  on-secondary: '#303030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#ffffff'
  on-tertiary: '#303030'
  tertiary-container: '#e4e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#caf231'
  primary-fixed-dim: '#afd500'
  on-primary-fixed: '#171e00'
  on-primary-fixed-variant: '#3d4c00'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1b1c'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 52px
    letterSpacing: -0.02em
  display-stat:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 38px
  headline-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 30px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 18px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-padding: 20px
  stack-gap: 16px
  inline-gap: 12px
  section-margin: 32px
  card-padding: 24px
---

## Brand & Style

The design system is engineered for a high-performance fitness and fintech crossover, targeting users who demand precision, speed, and motivation. The aesthetic is rooted in **Modern Minimalism** with a **High-Contrast** edge, utilizing a deep nocturnal palette to make data and action points vibrate with energy.

The emotional response is "Aggressive Progress"—the UI should feel like a premium piece of athletic gear or a high-end racing dashboard. We achieve this through:
- **Kinetic Energy:** Large-scale typography and vibrant neon accents that command attention.
- **Precision:** Clean, geometric layouts that organize complex biometric and financial data without friction.
- **Premium Tech:** Subtle depth through tonal layering and high-fidelity iconography.

## Colors

The palette is dominated by a dark mode architecture to reduce eye strain during workouts and provide a sophisticated backdrop for financial tracking.

- **Primary (Neon Lime):** Reserved for primary actions, progress indicators, and critical data highlights. It represents energy and "go" states.
- **Neutral Stack:** A three-tier dark gray system. `#121212` for the base canvas, `#1A1A1A` for section grouping, and `#1E1E1E` for interactive cards.
- **Functional Colors:** Success states utilize the primary lime, while destructive actions should use a high-chroma red to maintain the intense visual language.

## Typography

This design system uses a triple-font approach to balance readability with high-impact visual hierarchy.

- **Hanken Grotesk** is used for primary headlines and display text, providing a sharp, contemporary "tech" feel.
- **Space Grotesk** is utilized for statistics, numbers, and technical labels. Its geometric nature excels in data-heavy views.
- **Inter** handles all body copy and long-form text, ensuring maximum legibility across all device types.

**Usage Note:** Numbers (especially weights, reps, and currency) should always be rendered in the `display-stat` or `label-bold` styles to emphasize the "fintech" precision aspect of the app.

## Layout & Spacing

The layout follows a **Fluid Grid** model designed for mobile-first consumption.

- **Margins:** A consistent 20px horizontal margin is maintained globally to ensure content doesn't bleed into screen edges.
- **Rhythm:** An 8px base grid drives all spacing. Elements are grouped using 16px gaps, while major sections are separated by 32px to create clear visual breathing room.
- **Adaptation:** On larger displays, cards should move into a 2-column masonry or grid format rather than stretching horizontally, maintaining the 24px internal card padding.

## Elevation & Depth

Depth is achieved through **Tonal Layering** rather than traditional shadows. This maintains the clean, flat aesthetic while providing necessary hierarchy.

- **Level 0 (Canvas):** `#121212` - The base background.
- **Level 1 (Cards):** `#1E1E1E` - Floating containers for primary content.
- **Level 2 (In-Card Elements):** `#2C2C2C` - Used for input fields or nested items within cards.
- **Accent Elevation:** The primary Neon Lime (#D6FF3F) creates its own "optical elevation" due to its high luminance. No shadows are required for lime-colored elements; their brightness acts as a natural lift.

## Shapes

The shape language is characterized by **Generous Radii** mixed with **Pill-Geometric** accents.

- **Main Containers:** All primary cards use a 24px (`rounded-xl` in this context) corner radius. This softens the aggressive color palette and makes the app feel premium and modern.
- **Buttons:** All buttons must be full-pill shaped (height / 2) to distinguish them immediately from content cards.
- **Progress Indicators:** Use circular forms for biometric data (rings) to contrast against the rectangular grid of the UI.

## Components

### Buttons
- **Primary:** Pill-shaped, #D6FF3F background, #000000 text. Used for the most important action on a screen.
- **Secondary:** Pill-shaped, transparent background, 1.5px border in #2C2C2C or #D6FF3F (context-dependent), white text.
- **Floating Action (FAB):** The bottom nav features a raised, oversized circular button in #D6FF3F with a black plus icon, centered to anchor the UI.

### Cards
- **Standard Card:** #1E1E1E background, 24px radius, no border.
- **Status Card:** Incorporates a 4px left-border of #D6FF3F to denote an "active" or "in-progress" workout/transaction.

### Input Fields
- Dark background (#1A1A1A) with a subtle #2C2C2C border.
- On focus, the border transitions to #D6FF3F with a 1px thickness.

### Progress Rings
- Background track: #2C2C2C.
- Active track: #D6FF3F.
- Use a thick stroke (6px+) to emphasize the "bold" brand personality.

### Navigation
- Bottom navigation bar should be #121212 with a slight blur backdrop. Icons are #A0A0A0 when inactive and #D6FF3F when active.