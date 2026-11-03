# Scam or Smart Deal? | Investment Hype Awareness

**Community Engagement Project (CEP)**  
**MIT Chhatrapati Sambhajinagar**  
**SY B.Tech, Academic Year 2026–27**

An accessible, self-contained, static digital educational resource designed to help college students, first-time investors, and community members recognize warning signs in online investment promotions, fake trading apps, and unsolicited social-media stock tips.

---

## 1. Project Purpose & Scope

The purpose of this project is to foster financial literacy and digital self-defense against fraudulent investment hype. With the rapid growth of algorithmic trading claims, unauthorized social-media tip groups, and fake trading apps, this website provides plain-language, non-commercial education based directly on official advisories from the **Securities and Exchange Board of India (SEBI)** and the **Government of India National Cyber Crime Reporting Portal**.

### Core Boundaries:
- **Educational Only**: This is a non-commercial student project. It does not offer personalized financial advice, stock recommendations, brokerage services, or investment management.
- **Static & Privacy-Preserving**: No backend, no login, no database, no cookies, no tracking scripts, and no analytics. Quiz responses and scenario choices reside strictly in temporary browser memory and reset on page reload.
- **No Simulated Real Trading**: No live market feeds, price tickers, or investment calculators are used, preventing confusion with commercial trading platforms.

---

## 2. File Structure

```text
c:\another cep\
├── package.json        # NPM project configuration, scripts, and dev dependencies
├── vite.config.js      # Multi-page application (MPA) Vite configuration
├── .gitignore          # Git exclusion rules (node_modules, dist)
├── index.html          # Home overview & awareness modules portal hub
├── red-flags.html      # 6 Critical Red Flags dedicated page
├── how-it-works.html   # SEBI Fake App 6-stage lifecycle advisory page
├── scam-spotter.html   # Interactive Scam Spotter Challenge page
├── quiz.html           # 6-Question Interactive Awareness Quiz page
├── if-money-sent.html  # Emergency incident response & Helpline 1930 page
├── sources.html        # Verified SEBI & Gov of India official sources (Checked: Nov 2026)
├── css\
│   └── styles.css      # Editorial stylesheet with doodles, responsive MPA grid, and cobalt blue theme
├── js\
│   └── app.js          # Interactive scenarios, in-memory quiz engine, and UI navigation
├── README.md           # Documentation, customization guide, and pre-presentation checklist
├── Antigravity_Investment_Scam_Awareness_Website_Brief.md  # Original build brief
├── build_investment_cep_report.py   # Python script generating the academic companion report
└── Investment_Scam_Awareness_CEP_Research_Report.docx      # Academic CEP research report
```

---

## 3. How to Run & Build with NPM

This project is fully configured as an **npm-powered project** using Vite for instant development, hot module reloading, and production bundling.

### Development Mode
To start the local development server with instant live reload:
```powershell
npm run dev
```
Open the provided local URL (typically `http://localhost:5173`) in your browser.

### Production Build
To create an optimized, minified production build in the `dist/` directory:
```powershell
npm run build
```

### Preview Production Build
To preview the generated production build locally:
```powershell
npm run preview
```

### Direct Browser Open (Offline Alternative)
You can also open `index.html` directly in any web browser without running npm.

---

## 4. How to Customize Content & Replace Placeholders

All project metadata and editable fields are cleanly isolated with explicit placeholders:

### A. Team and Academic Details (Academic Companion Report)
Academic CEP submission information and student/guide placeholders are maintained in the companion research report (`Investment_Scam_Awareness_CEP_Research_Report.docx` and `build_investment_cep_report.py`). Replace the bracketed placeholders once confirmed:

| Placeholder | Meaning / Action |
|---|---|
| `[CONFIRM FROM COLLEGE FORMAT]` | Programme / Division (e.g., SY B.Tech Computer Science & Engineering) |
| `[ADD AFTER TEAM CONFIRMS]` | Student names and college roll numbers |
| `[ADD AFTER CONFIRMATION]` | Faculty Guide name and designation |
| `[ADD AFTER ACTIVITY]` | Community outreach location (e.g., local campus, community hall) |
| `[ADD AFTER COMPLETION, IF CONDUCTED]` | Dates of survey or awareness presentation sessions |
| `[ADD ONLY FROM VERIFIED PROJECT RECORDS]` | Actual participant count and verified feedback summaries |
| `[ADD ONLY AFTER DEPLOYMENT]` | Final live hosted URL (e.g., GitHub Pages) |

> **Note**: Do not invent survey statistics, test participant numbers, or deployment claims until the actual physical or digital outreach activity has been completed and verified.

### B. Educational Content & Red Flags
- **Red Flags**: Located in `index.html` under `<section id="red-flags">`. You can edit card descriptions and actionable "What to do" boxes.
- **Fake App Lifecycle**: Located in `index.html` under `<section id="how-it-works">`. Reflects the official 6-stage advisory from SEBI.

### C. Fictional Scenarios & Quiz Questions
- **Scenarios**: Markup is in `index.html` under `<section id="scam-spotter">`. Educational feedback text is stored in `js/app.js` under the `scenarioExplanations` object.
- **Quiz Questions**: Stored in `js/app.js` under `quizQuestions`. You can add, edit, or rephrase questions, multiple-choice options, and supportive feedback explanations.

---

## 5. Visual Theme & Accessibility Features

- **Primary Color Palette (Royal Cobalt Blue)**: The website uses a trustworthy Royal Cobalt Blue primary theme (`#1d4ed8` / `--color-primary`), deep navy body text (`#0f172a`), warm off-white surface (`#faf9f6`), warm amber for caution (`#b45309`), and selective restrained red for emergency warnings (`#b91c1c`).
- **Screen Reader Support**: Semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`), `aria-live="polite"` regions for feedback, and descriptive ARIA labels.
- **Keyboard Navigation**: Full Tab/Shift+Tab navigation, focus rings (`:focus-visible`), and `Escape` key support to close mobile menus.
- **No External CDNs**: All icons are embedded inline SVGs; system fonts are used to ensure instantaneous offline loading.
- **Responsive Layout**: Fluid breakpoints covering mobile phones (320px–768px), tablets (768px–1024px), and desktop displays.
- **Reduced Motion**: Respects `@media (prefers-reduced-motion: reduce)`.

---

## 6. Official Regulatory Sources (Checked: 2 November 2026)

All concepts, warning criteria, and reporting procedures on this website are based on verified official materials:

1. **SEBI Investor Education**: *How to Spot a Scam*  
   [https://investor.sebi.gov.in/spot-any-scam.html](https://investor.sebi.gov.in/spot-any-scam.html)
2. **SEBI Investor Advisory**: *Beware of Fake Trading App Scams*  
   [https://investor.sebi.gov.in/pdf/Fake%20trading%20app%20scam%20Landscape.pdf](https://investor.sebi.gov.in/pdf/Fake%20trading%20app%20scam%20Landscape.pdf)
3. **SEBI Investor Advisory**: *Stock Market Guru Scams*  
   [https://investor.sebi.gov.in/pdf/Stock%20Market%20Guru%20Scams%20final.pdf](https://investor.sebi.gov.in/pdf/Stock%20Market%20Guru%20Scams%20final.pdf)
4. **SEBI Investor Education**: *Factors to Consider Before Investing*  
   [https://investor.sebi.gov.in/investment-thingsbeforeinv.html](https://investor.sebi.gov.in/investment-thingsbeforeinv.html)
5. **Government of India (MHA)**: *National Cyber Crime Reporting Portal* & Helpline **1930**  
   [https://www.cybercrime.gov.in/](https://www.cybercrime.gov.in/)
6. **SEBI**: *SCORES 2.0 Investor Grievance Redressal Portal*  
   [https://scores.sebi.gov.in/](https://scores.sebi.gov.in/)

---

## 7. Pre-Presentation / Evaluation Checklist

Before submitting or presenting the project to academic evaluators, verify the following:

- [ ] **Static Independence**: All pages, scripts, styles, and SVG icons load with no internet connection (except clicking outgoing official reference links).
- [ ] **No Unverified Claims**: Ensure no fabricated participant counts, survey results, or deployment claims appear in the "About This CEP" section.
- [ ] **Keyboard Operability**: Navigate through all links, scenario buttons, and quiz options using only the `Tab`, `Enter`, `Space`, and `Esc` keys.
- [ ] **Responsive Test**: Inspect the site using browser developer tools across Mobile (e.g. 375px), Tablet (768px), and Desktop viewports.
- [ ] **Official Links**: Confirm external URLs open in a new tab (`target="_blank"` with `rel="noopener noreferrer"`).
- [ ] **Emergency Disclaimer**: Check that Helpline 1930 and SEBI SCORES instructions clearly state that reporting is an official step and does not guarantee fund recovery.
- [ ] **Quiz State**: Verify that refreshing the page clears quiz responses back to Question 1 with score 0 (ensuring in-memory privacy).

---

## 8. License & Attribution

Developed under the Community Engagement Project (CEP) framework at **MIT Chhatrapati Sambhajinagar** for academic year 2026–27. Non-commercial, educational use only.

