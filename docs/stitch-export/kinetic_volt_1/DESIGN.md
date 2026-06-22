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
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 36px
    fontWeight: '800'
    lineHeight: 42px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  stat-value:
    fontFamily: Hanken Grotesk
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 40px
    letterSpacing: -0.03em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  container-padding-mobile: 20px
  container-padding-desktop: 40px
  gutter: 16px
  card-gap: 24px
---

## Brand & Style
The design system is engineered for high-performance contexts, blending a "Premium Tech" aesthetic with high-energy visuals. The brand personality is aggressive, precise, and electric. It targets power users who value speed, data visualization, and a cutting-edge interface. 

The design style is **High-Contrast / Bold** with elements of **Glassmorphism**. It utilizes a deep monochromatic base to let neon accents vibrate against the dark canvas. The emotional response should be one of empowerment and urgency, driven by thick strokes, massive typography, and vibrant feedback loops.

## Colors
The palette is dominated by a near-black background to provide maximum depth. The primary accent, a neon lime-green, is used sparingly but with high impact for critical actions and data visualization. 

- **Primary (#D6FF3F):** Reserved for "kinetic" elements—active states, primary buttons, and progress indicators.
- **Surface (#1E1E1E):** Used for card backgrounds to create a clear container hierarchy against the #121212 base.
- **Surface Elevated (#2C2C2C):** Used for hover states or tertiary nested containers.
- **Success/Warning/Error:** Use variants of the primary lime for success, a bright amber for warnings, and a saturated red-orange for errors to maintain the high-vibrancy theme.

## Typography
This design system utilizes **Hanken Grotesk** for its aggressive, modern geometric profile. High weights (Bold/ExtraBold) are required for headers to stand out against the dark background. 

For technical data, statistics, and small metadata, **JetBrains Mono** is introduced to provide a "developer-tool" precision feel. Statistical values should use the `stat-value` role, featuring tight letter spacing and heavy weights to emphasize numerical growth or performance metrics.

## Layout & Spacing
The layout follows a **Fluid Grid** model with high-density padding. We use an 8px base unit for all spatial relationships. 

- **Mobile:** 4-column grid with 20px side margins. Cards usually span the full width.
- **Desktop:** 12-column grid with 40px margins. Content is organized into modular "widgets" or "tiles" that emphasize a dashboard-like energy.
- **Rhythm:** Spacing between cards should be generous (24px) to allow the large corner radii to feel distinct and structural.

## Elevation & Depth
Depth is created through **Tonal Layers** rather than heavy shadows. Since the background is #121212, elevations are communicated by shifting to lighter grays.

- **Level 0 (Base):** #121212.
- **Level 1 (Cards/Navigation):** #1E1E1E.
- **Level 2 (Modals/Popovers):** #2C2C2C with a subtle 1px inner stroke of white at 10% opacity to define the edge.
- **Accents:** Active elements use a "glow" effect—a soft, low-opacity drop shadow using the primary lime-green color (#D6FF3F) to simulate light emission.

## Shapes
The shape language is defined by **Pill-shapes** and **Exaggerated Radii**. 
- **Cards:** Use a fixed 24px corner radius to create a friendly but structured container.
- **Interactive Elements:** Buttons, tags, and search bars use a fully rounded (pill) style. 
- **Data Visuals:** Progress bars and rings must use rounded caps to maintain consistency with the pill-shaped UI components.

## Components
### Buttons
- **Primary:** Full fill #D6FF3F with #000000 text. ExtraBold weight. Pill-shaped.
- **Secondary:** Transparent fill with a 2px stroke of #FFFFFF (at 20% opacity). White text.
- **Ghost:** No fill or stroke. Primary color text for actions; white text for navigation.

### Cards
Cards are the primary structural unit. They feature #1E1E1E backgrounds and 24px corner radius. Padding inside cards should be a minimum of 24px to accommodate the large corners without crowding content.

### Navigation
- **Bottom Bar:** A blurred #1E1E1E container. 
- **Center Action:** The "Kinetic Button" is a raised, circular lime-green button that sits slightly above the nav bar line, featuring a subtle outer glow of the primary color.

### Progress & Charts
Progress rings and line charts must use the primary neon-green. Lines should have a thickness of at least 3px with rounded joins to match the bold typography and pill-shaped buttons.

### Inputs
Search and text fields use the pill shape with a #2C2C2C fill. Active states are indicated by a 2px #D6FF3F border.