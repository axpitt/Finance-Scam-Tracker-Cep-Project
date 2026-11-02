from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.section import WD_SECTION

OUT = r'C:\another cep\Investment_Scam_Awareness_CEP_Research_Report.docx'

doc = Document()
sec = doc.sections[0]
sec.page_width = Inches(8.27)
sec.page_height = Inches(11.69)
sec.top_margin = Inches(0.85)
sec.bottom_margin = Inches(0.8)
sec.left_margin = Inches(1.0)
sec.right_margin = Inches(0.85)

styles = doc.styles
normal = styles['Normal']
normal.font.name = 'Calibri'
normal.font.size = Pt(11)
normal.font.color.rgb = RGBColor(0, 0, 0)
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.08
for name, size, color in [
    ('Title', 24, '000000'),
    ('Heading 1', 20, '000000'),
    ('Heading 2', 16, '6E2E9F'),
    ('Heading 3', 13, '365F91'),
    ('Heading 4', 11, '4F81BD'),
]:
    st = styles[name]
    st.font.name = 'Calibri'
    st.font.size = Pt(size)
    st.font.color.rgb = RGBColor.from_string(color)
    st.font.bold = name != 'Title'
    st.paragraph_format.space_before = Pt(10 if name != 'Title' else 0)
    st.paragraph_format.space_after = Pt(5)

def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:fill'), fill)
    tc_pr.append(shd)

def set_cell_text(cell, text, bold=False, color=None, size=9):
    cell.text = ''
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(text)
    r.bold = bold
    r.font.name = 'Calibri'
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

def table(headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, h in enumerate(headers):
        set_cell_text(t.rows[0].cells[i], h, bold=True, color='FFFFFF', size=9)
        shade(t.rows[0].cells[i], '365F91')
    for row in rows:
        cells = t.add_row().cells
        for i, value in enumerate(row):
            set_cell_text(cells[i], value, size=9)
            if len(t.rows) % 2 == 0:
                shade(cells[i], 'F2F5F8')
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

def p(text='', style=None, bold_lead=None, align=None):
    para = doc.add_paragraph(style=style)
    if align is not None:
        para.alignment = align
    if bold_lead and text.startswith(bold_lead):
        para.add_run(bold_lead).bold = True
        para.add_run(text[len(bold_lead):])
    else:
        para.add_run(text)
    return para

def h(text, level=1):
    doc.add_heading(text, level=level)

def numbered(text):
    return p(text, 'List Number')

def bullet(text):
    return p(text, 'List Bullet')

# Cover page
for _ in range(2):
    p('')
p('MAHARASHTRA INSTITUTE OF TECHNOLOGY', align=WD_ALIGN_PARAGRAPH.CENTER).runs[0].bold = True
p('CHHATRAPATI SAMBHAJINAGAR', align=WD_ALIGN_PARAGRAPH.CENTER).runs[0].bold = True
p('An Autonomous Institute Affiliated to Dr. Babasaheb Ambedkar Marathwada University', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Community Engagement Project', align=WD_ALIGN_PARAGRAPH.CENTER)
p('RESEARCH REPORT DRAFT', align=WD_ALIGN_PARAGRAPH.CENTER).runs[0].bold = True
title = doc.add_paragraph(style='Title')
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title.add_run('Investment Scam Awareness and Digital Safety Platform')
p('Spotting Fake Investment Hype on Social Media', align=WD_ALIGN_PARAGRAPH.CENTER)
for _ in range(2):
    p('')
p('Submitted by', align=WD_ALIGN_PARAGRAPH.CENTER)
p('[Student name and roll number(s) to be added]', align=WD_ALIGN_PARAGRAPH.CENTER)
p('SY B.Tech | Academic Year 2026–27', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Under the guidance of [Guide name to be confirmed]', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Institution: MIT Chhatrapati Sambhajinagar', align=WD_ALIGN_PARAGRAPH.CENTER)
doc.add_page_break()

h('ABSTRACT', 1)
p('This Community Engagement Project proposes a compact, browser-based learning resource about investment promotions that use misleading or suspicious claims on social media. The planned site will help students and community members notice warning signs such as guaranteed or unusually high returns, urgency, unverifiable success screenshots, unregistered promoters, unfamiliar trading-app links, requests to pay third parties, and blocked withdrawals followed by extra fee demands. The concept is informed by current investor-awareness material from the Securities and Exchange Board of India (SEBI) and official cybercrime reporting information. The project is intentionally distinct from a broader cybersecurity and UPI-safety website: it focuses on securities-market investment hype and how to pause, verify, and find official help. A first version can be implemented as a static page with a checklist, fictional interactive scenarios, a short quiz, and official source links. No backend or collection of financial or personal data is proposed. Survey responses, community testing, deployment, and learning outcomes have not yet been collected or completed; this draft therefore reports a proposed plan rather than results.')
p('Keywords: investment scam awareness; social media; fake trading apps; investor education; financial cyber fraud', bold_lead='Keywords:')

h('PROJECT COMPARISON AND SCOPE', 1)
p('The peer CEP report shared for comparison addresses general cybersecurity and digital safety, including phishing, passwords, personal-data protection, OTP and UPI safety, and cybercrime response. The proposed project keeps the community-education format but narrows its financial focus to misleading investment promotions and securities-market scams. The comparison below is about project scope; the peer report’s survey counts and outcomes are not evidence for this project.')
table(['Aspect', 'Cybersecurity CEP shared for comparison', 'Proposed investment-awareness CEP'], [
    ('Main focus', 'Broad digital safety: suspicious links, credentials, privacy, account safety, payment fraud, and reporting.', 'Investment hype: social-media “gurus,” guaranteed-return claims, fake trading apps, misleading profit displays, and withdrawal barriers.'),
    ('Learner action', 'Recognise cyber risks and choose safer online or payment behaviour.', 'Pause before investing, identify red flags, verify an entity or platform through official sources, and know where to report suspected cyber financial fraud.'),
    ('Possible website', 'Cyber-safety guides and an interactive quiz.', 'A red-flag checklist, fictional investment posts, short scenario feedback, a five-question quiz, and official investor-education links.'),
    ('Overlap', 'Both use plain-language education, fictional examples, a quiz, official sources, and careful incident-response guidance.', 'Keep the shared educational format, but write original investment-specific research, scenarios, quiz content, and evaluation questions.'),
    ('Evidence boundary', 'Its survey results describe its own small respondent group.', 'No survey results, community outcomes, user counts, or learning impact are available yet for this project.')
], widths=[1.15, 2.6, 2.6])

h('CONTENTS', 1)
for item in [
    '1. Introduction', '2. Literature Survey', '3. Problem Definition and Objectives',
    '4. Proposed Methodology and System Design', '5. Proposed Website Implementation',
    '6. Evaluation Plan and Pending Evidence', '7. Conclusion and Future Scope',
    'References', 'Appendix A. Draft Awareness Questionnaire', 'Appendix B. Sample Scenario and Quiz Content'
]:
    bullet(item)

h('ABBREVIATIONS', 1)
table(['Term', 'Meaning'], [
    ('CEP', 'Community Engagement Project'),
    ('SEBI', 'Securities and Exchange Board of India'),
    ('I4C', 'Indian Cyber Crime Coordination Centre'),
    ('HTML', 'HyperText Markup Language'),
    ('CSS', 'Cascading Style Sheets'),
    ('JS', 'JavaScript')
], widths=[1.05, 5.3])

h('1. INTRODUCTION', 1)
h('1.1 Background', 2)
p('People encounter investment claims through social-media posts, messaging groups, online advertisements, videos, and app links. A post may use success screenshots, an “expert” identity, a limited-time invitation, or promises of quick returns to encourage an immediate decision. SEBI’s investor guidance identifies guaranteed or near-certain returns, unusually high returns, unregistered entities, complex strategies that the person does not understand, and pressure to act quickly as warning signs [1].')
p('SEBI’s public material on fake trading-app scams describes a pattern in which social-media promotions lead people to a fake app, displayed profits encourage further deposits, and withdrawal attempts are blocked or followed by requests for additional fees [2]. These examples make the topic suitable for practical awareness learning: students can examine fictional messages, identify what should prompt a pause, and practise finding official verification routes.')
h('1.2 Community Problem', 2)
p('The project addresses a learning need: people may see investment offers online without knowing which claims deserve closer scrutiny or how to verify the promoter and platform. General warnings such as “be careful” are less useful than showing concrete signs and a safe next step. The project does not assume that every high-return claim is fraudulent or make a legal determination about any real person or company. It teaches users to pause, question claims, check official sources, and avoid sending money or installing unfamiliar software based only on a social-media message.')
h('1.3 Project Overview', 2)
p('The proposed deliverable is a lightweight static website called “Scam or Smart Deal?” The site will teach red flags in investment promotions using short fictional scenarios and a quiz. It can be made with a single HTML page and a small amount of CSS and JavaScript. It will not need a server, accounts, analytics, external forms, or storage of quiz responses. A first demonstration version is intentionally limited so it can be built quickly with a vibe-coding tool and reviewed by the student team.')
h('1.4 Community Engagement Approach', 2)
p('The team may introduce the site in a short awareness session and ask voluntary, non-identifying questions about whether the examples and explanations are understandable. A brief anonymous paper questionnaire or a team-managed form can be used only if the team is prepared to review the responses. No names, phone numbers, account identifiers, investment amounts, screenshots, or individual loss details are needed. Results should be aggregated and reported with the sample size, collection date, method, and limitations.')
h('1.5 Scope and Significance', 2)
p('The scope is investment-hype awareness, especially online claims about securities-market products, trading tips, fake apps, and requests to add funds. The site will distinguish warning signs from proof: one red flag cannot by itself establish that a post or entity is fraudulent. A registration check helps verify status, but it does not guarantee returns or eliminate all risks. The site will direct people to relevant official channels and will not provide investment recommendations.')

h('2. LITERATURE SURVEY', 1)
h('2.1 Investment Risk and Promises of Certainty', 2)
p('SEBI’s investor guidance states that securities-market investments carry risk and advises people to be suspicious of assured, guaranteed, or near-certain returns. It also identifies unusually high returns regardless of market conditions, pushy sales tactics, missing documentation, and strategies that are too complex to understand as warning signs [1]. The project should therefore teach users to question the claim and the source rather than judge an offer by a polished design or persuasive wording.')
h('2.2 Social-Media “Guru” and Stock-Tip Promotions', 2)
p('SEBI investor-awareness material describes “stock market guru” scam patterns involving self-promotion as an expert, profit claims, paid courses or private groups, urgency, and success stories that may be fabricated or exaggerated [3]. The material supports using fictional posts that show how popularity, followers, testimonials, or screenshots can create trust without proving a claim. The site should not identify real individuals or repeat unverified allegations.')
h('2.3 Fake Trading Apps and the Deposit-to-Withdrawal Pattern', 2)
p('SEBI’s fake trading-app advisory outlines a progression from social-media advertising and trust-building to an unfamiliar app, displayed profits, pressure to invest more, and blocked withdrawals with excuses or extra fees [2]. It flags unverified app links or APK files, payments to third-party accounts, and unrealistic promises. It recommends checking platform legitimacy through official exchange and SEBI investor resources. These details can become a short “follow the pattern” interactive sequence in the site.')
h('2.4 Verification and Its Limits', 2)
p('SEBI advises checking whether an entity offering or promoting an investment product or strategy is regulated, and researching the entity and its track record through credible sources [1]. Verification should be done independently using an official website reached directly, rather than trusting a link or contact supplied in the message. The educational material must avoid saying that registration makes an investment safe, guarantees performance, or proves that an account contacting the user is genuine. Impersonation can misuse names and logos, so the exact identity and platform matter.')
h('2.5 Reporting and Appropriate Channels', 2)
p('For suspected cyber financial fraud in India, the National Cyber Crime Reporting Portal identifies 1930 as the helpline for immediate reporting and provides an online reporting route [4]. The project should present these as official reporting options and encourage prompt contact with the bank or payment provider where money has been transferred. The guidance must not promise recovery. A securities-market grievance is not automatically the same as cyber financial fraud; users should consult the relevant official SEBI or exchange complaint channel for the type of issue involved [5].')
h('2.6 Scenario-Based Learning', 2)
p('A short scenario can connect a warning sign to an action: read the fictional post, select what you would do, then see the red flags and a verification step. This approach suits a small static website because it gives immediate feedback without a backend. The quiz is a learning aid, not a validated measure of financial knowledge or proof that a user can avoid fraud in a real situation.')
h('2.7 Research Gap and Relevance', 2)
p('The comparison report shared by the user already covers broad cybersecurity and digital-safety topics, including online fraud, payment credentials, suspicious links, and reporting. The proposed project fills a narrower content gap by focusing on investment promotions, fake trading applications, social-media stock-tip groups, and the way false displays of profit can be used to solicit more deposits. It will reuse the educational approach, not the other project’s survey data, claims, or wording.')

h('3. PROBLEM DEFINITION AND OBJECTIVES', 1)
h('3.1 Problem Definition', 2)
p('Students and community members may encounter online investment promotions that use guaranteed-return claims, pressure, unverifiable success evidence, or unfamiliar trading platforms. They need a simple way to recognise warning signs, pause before acting, and locate official verification and reporting information.')
h('3.2 Aim', 2)
p('To develop a simple web-based awareness resource that helps users identify common red flags in online investment promotions and practise safer next steps.')
h('3.3 Objectives', 2)
for x in [
    'Summarise current SEBI guidance on investment-scam warning signs and fake trading apps in clear, student-friendly language.',
    'Create fictional social-media examples that teach users to notice unrealistic promises, urgency, unverified promoters, suspicious app links, third-party payment requests, and withdrawal barriers.',
    'Build a static website with a checklist, interactive scenarios, a short quiz, and official source links.',
    'Keep the site privacy-first by avoiding accounts, backend storage, analytics, and collection of financial or identity data.',
    'Plan a small awareness activity and evaluate clarity and usability without claiming unmeasured impact.'
]: numbered(x)
h('3.4 Scope and Constraints', 2)
p('The first version is educational and front-end only. It does not verify investments, provide financial advice, make legal findings, process reports, or guarantee that users can identify every scam. Examples are fictional and use no real account details, phone numbers, UPI IDs, or downloadable software. The first build should stay small enough for a short vibe-coding session; translation, videos, and a larger evaluation can be considered later.')

h('4. PROPOSED METHODOLOGY AND SYSTEM DESIGN', 1)
h('4.1 Overall Workflow', 2)
for x in [
    'Review the official SEBI and National Cyber Crime Reporting Portal sources listed in this report.',
    'Convert the guidance into a short red-flag checklist and fictional examples.',
    'Generate a static one-page site with accessible controls and immediate local feedback.',
    'Check every link, button, quiz answer, and small-screen layout; have a team member review wording against the sources.',
    'Demonstrate the site in a CEP awareness session and collect voluntary, non-identifying feedback only if approved by the project team and college process.'
]: numbered(x)
h('4.2 Proposed Questionnaire and Ethics', 2)
p('A draft anonymous questionnaire is provided in Appendix A. It asks about exposure to general online promotions, recognition of warning signs, preferred learning formats, and clarity of the website. It should not ask for account details, investment amounts, personal losses, screenshots, or identifying information. Participation should be voluntary. If fewer than a useful number of responses are obtained, report the actual number and treat the findings as exploratory; do not extrapolate to the wider population.')
h('4.3 Static Website Architecture', 2)
table(['Part', 'Purpose', 'Implementation'], [
    ('Content', 'Red flags, fictional scenarios, quiz explanations, and source links.', 'Plain text in the page or a small local JavaScript data array.'),
    ('Interface', 'Readable sections, scenario choices, quiz feedback, and clear navigation.', 'Semantic HTML and responsive CSS.'),
    ('Interactions', 'Reveal explanations and calculate a local quiz score.', 'Small browser-side JavaScript; answers stay in memory.'),
    ('Privacy', 'Avoid collecting or transmitting personal or financial information.', 'No login, server, external form, analytics, or persistence.')
], widths=[1.05, 2.45, 2.85])
h('4.4 Content Review', 2)
p('Before sharing the site, the team should check that each warning sign matches official source material, that examples remain fictional, that all official links open correctly, and that the language does not imply guaranteed recovery or investment safety. Record the date on which the sources were checked and review them again before final submission or publication.')

h('5. PROPOSED WEBSITE IMPLEMENTATION', 1)
h('5.1 Page Structure', 2)
for x in [
    'Hero section: “Scam or Smart Deal?” with one-sentence purpose and a start button.',
    'Red-flag checklist: guaranteed or unusually high returns, urgency, unverified “experts,” profit screenshots, unfamiliar app links, third-party payments, and withdrawal barriers.',
    'Scenario cards: fictional promotions with two or three choices and plain-language explanations.',
    'Quick quiz: five questions, immediate feedback, score summary, and retry control.',
    'If money was sent: contact the bank/payment provider promptly; for suspected cyber financial fraud, use 1930 or the official portal; do not promise recovery.',
    'Sources and note: official links and a clear statement that the site is general awareness information, not investment advice.'
]: bullet(x)
h('5.2 Sample Interaction', 2)
p('A fictional post says: “Join our private group today. Our expert gives guaranteed daily stock profits. Limited seats; download this app from the link and deposit now.” The learner selects a response. Feedback points out several warning signs: guaranteed profit, urgency, a private tips group, and an unfamiliar app link. The safer learning response is to pause, not install or pay based on the message, and independently check the relevant official sources. The scenario does not assert that a real group or person committed a crime.')
h('5.3 Quick Build Boundary', 2)
p('For a first 15-minute vibe-coding build, keep the site to a single page, one visual theme, four scenario cards, and five quiz items. Use no backend, login, third-party API, data submission, or paid library. The first version is a demonstration prototype; accessibility, factual review, responsive layout, and all links still need a deliberate team check before the site is used in a community activity.')

h('6. EVALUATION PLAN AND PENDING EVIDENCE', 1)
p('No project-specific survey, community session, deployment, usability study, or learning assessment has been documented yet. This section is an evaluation plan, not a results section. The team should fill it only after collecting verifiable project evidence.')
table(['Evidence to collect', 'How to record it', 'Current status'], [
    ('Survey responses', 'Actual count, dates, distribution method, and aggregated answers; exclude identifying fields.', 'Not collected yet'),
    ('Website checks', 'Record device/browser, links and interactions checked, and issues fixed.', 'Not completed yet'),
    ('Awareness activity', 'Record actual session date, location, and participant count if the activity occurs.', 'Not completed yet'),
    ('Participant feedback', 'Summarise anonymous comments or rating totals, with sample size and limitations.', 'Not collected yet'),
    ('Learning outcomes', 'Use an optional short pre/post knowledge check only if the team has a suitable process; report actual results and limits.', 'Not measured yet'),
    ('Deployment', 'Add the public URL only after deployment has occurred and the team has checked it.', 'Not deployed yet')
], widths=[1.35, 3.4, 1.6])
p('A small convenience sample can describe only the people who responded. A quiz score or positive feedback should not be presented as proof that the site prevents fraud or changes real-world financial behaviour. Keep reporting transparent about what was built, what was checked, and what remains unknown.')

h('7. CONCLUSION AND FUTURE SCOPE', 1)
h('7.1 Conclusion', 2)
p('Investment promotions on social media can use signals that SEBI identifies as reasons for caution, including guaranteed or unusually high returns, pressure to act quickly, unregistered entities, complex strategies, fake trading applications, and barriers to withdrawal. A focused, static awareness page can turn this official guidance into a brief checklist and interactive learning exercise. Compared with the broad cybersecurity CEP shared for reference, this project has a distinct securities-investment focus while retaining a similar community-learning format.')
p('This document describes a proposed project. It does not claim that a website has been built, deployed, tested with residents, or shown to improve awareness. Those statements can be added only when the team has completed the work and recorded the evidence.')
h('7.2 Future Scope', 2)
for x in [
    'Add Marathi and Hindi versions after review by fluent speakers.',
    'Expand examples to cover impersonation of regulated entities and misleading testimonials, while keeping all scenarios fictional.',
    'Run a small usability session with consent and report the actual method and sample size.',
    'Review SEBI and government links periodically and record the check date.',
    'Add a pre/post learning check only if the college project process permits it and the team can analyse it responsibly.'
]: bullet(x)

h('REFERENCES', 1)
refs = [
    '[1] Securities and Exchange Board of India (SEBI), “How to Spot a Scam,” SEBI Investor. https://investor.sebi.gov.in/spot-any-scam.html (accessed 2 November 2026).',
    '[2] SEBI Investor, “Beware of Fake Trading App Scams!” https://investor.sebi.gov.in/pdf/Fake%20trading%20app%20scam%20Landscape.pdf (accessed 2 November 2026).',
    '[3] SEBI Investor, “Stock Market Guru Scams.” https://investor.sebi.gov.in/pdf/Stock%20Market%20Guru%20Scams%20final.pdf (accessed 2 November 2026).',
    '[4] Government of India, National Cyber Crime Reporting Portal, financial cyber fraud information and helpline 1930. https://www.cybercrime.gov.in/ (accessed 2 November 2026).',
    '[5] SEBI, SCORES investor grievance redressal portal. https://scores.sebi.gov.in/ (accessed 2 November 2026).',
    '[6] SEBI Investor, “Factors to Consider Before Investing.” https://investor.sebi.gov.in/investment-thingsbeforeinv.html (accessed 2 November 2026).',
    '[7] SEBI Investor, “Caution to Investor.” https://investor.sebi.gov.in/cautiontoinvestor.html (accessed 2 November 2026).'
]
for ref in refs:
    p(ref)

h('APPENDIX A. DRAFT AWARENESS QUESTIONNAIRE', 1)
p('For voluntary, anonymous use if the project team decides to conduct a needs assessment or collect feedback. Do not collect names, phone numbers, account details, investment values, screenshots, or personal loss stories. Confirm the college process before circulation.')
for q in [
    'How often do you see investment-related posts, ads, or tips on social media? (Often / Sometimes / Rarely / Never / Not sure)',
    'Which of these would make you pause before acting? (Guaranteed returns / Urgent deadline / Unfamiliar app link / Request to pay a third-party account / None of these / Not sure; select all that apply)',
    'If a social-media post promises fixed daily profits, what would you do first? (Act quickly / Ask the promoter for proof / Pause and check official sources / Not sure)',
    'How confident are you about finding official information to check an investment entity or platform? (Very / Somewhat / Not very / Not at all / Not sure)',
    'Which format would help you learn this topic? (Short checklist / Fictional examples / Quiz / Short video / Step-by-step guide; select all that apply)',
    'After using the awareness page, how clear are the warning signs? (Very clear / Mostly clear / Unclear / Not sure)',
    'Which part of the page was easiest or hardest to understand? (Optional; do not include personal financial information.)'
]: numbered(q)

h('APPENDIX B. SAMPLE SCENARIO AND QUIZ CONTENT', 1)
h('B.1 Scenario', 2)
p('A fictional creator posts: “I made 40% this week. Join my private group now for guaranteed calls. Download the app in my bio. Pay a small activation fee to unlock your profits.”')
p('Question: Which details should make the learner pause?')
bullet('The guarantee and unusually high return claim.')
bullet('The urgency and private-group invitation.')
bullet('The unfamiliar app link and request to pay a fee.')
p('Feedback: These are warning signs described in SEBI investor-awareness materials. Do not treat screenshots or a displayed account balance as proof. Pause and use official sources to check the entity and platform. The example is fictional and does not identify a real person or company.')
h('B.2 Quiz Questions', 2)
quiz = [
    ('A post promises guaranteed daily profits from securities-market trading. What is the best awareness response?', 'Treat the promise as a warning sign and independently verify the source; do not rush.'),
    ('A group shares screenshots of large profits. Do the screenshots prove that the offer is genuine?', 'No. Screenshots alone do not verify performance or legitimacy.'),
    ('A promoter sends an unfamiliar APK trading-app link. What should the learner do?', 'Do not install it based on the message. Check platform legitimacy using official sources.'),
    ('An app displays profits but blocks withdrawals and asks for another fee. What should the learner recognise?', 'Blocked withdrawals and extra fee requests are red flags described in SEBI’s fake trading-app advisory.'),
    ('Someone has sent money after an online investment promotion and suspects cyber financial fraud. What official option is listed for immediate reporting in India?', 'Call 1930 or use the National Cyber Crime Reporting Portal; also contact the bank/payment provider promptly. Recovery is not guaranteed.')
]
for i, (question, answer) in enumerate(quiz, 1):
    p(f'{i}. {question}', bold_lead=f'{i}.')
    p(f'Answer and learning point: {answer}', bold_lead='Answer and learning point:')

# Page number field in footer
for section in doc.sections:
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer.add_run('CEP Research Report Draft  |  Page ')
    run.font.name = 'Calibri'
    run.font.size = Pt(9)
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'PAGE')
    footer._p.append(fld)

doc.core_properties.title = 'Investment Scam Awareness and Digital Safety Platform'
doc.core_properties.subject = 'Community Engagement Project research report draft'
doc.core_properties.author = 'Student team - details to be completed'
doc.core_properties.keywords = 'CEP, investment scam awareness, SEBI, digital safety'
doc.save(OUT)
print(OUT)
