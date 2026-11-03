from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE

OUT = r'C:\another cep\Investment_Scam_Awareness_CEP_Project_Report.docx'
doc = Document()

def set_font(run, size=12, bold=None, italic=None):
    run.font.name = 'Times New Roman'
    run._element.get_or_add_rPr().rFonts.set(qn('w:ascii'), 'Times New Roman')
    run._element.get_or_add_rPr().rFonts.set(qn('w:hAnsi'), 'Times New Roman')
    run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if italic is not None: run.italic = italic

def shade(cell, fill):
    pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:fill'), fill); pr.append(shd)

def set_cell(cell, text, bold=False, fill=None, size=10.5, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ''
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(str(text)); set_font(r, size, bold)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    if fill: shade(cell, fill)

def page_num(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = paragraph.add_run()
    fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE'); r._r.addnext(fld)

def configure_section(sec, footer=True, first_page=False):
    sec.page_width = Inches(8.27); sec.page_height = Inches(11.69)
    sec.top_margin = Inches(1); sec.bottom_margin = Inches(1)
    sec.left_margin = Inches(1.25); sec.right_margin = Inches(1)
    sec.gutter = Inches(0); sec.gutter_pos = 0
    sec.header_distance = Inches(0.45); sec.footer_distance = Inches(0.45)
    if first_page:
        sec.different_first_page_header_footer = True
    if footer:
        page_num(sec.footer.paragraphs[0])

configure_section(doc.sections[0], footer=False, first_page=True)
styles = doc.styles
normal = styles['Normal']
normal.font.name = 'Times New Roman'; normal.font.size = Pt(12)
normal._element.rPr.rFonts.set(qn('w:ascii'), 'Times New Roman')
normal._element.rPr.rFonts.set(qn('w:hAnsi'), 'Times New Roman')
normal.paragraph_format.line_spacing = 1.5
normal.paragraph_format.first_line_indent = Inches(.5)
normal.paragraph_format.space_after = Pt(0)
for stylename in ['Title','Heading 1','Heading 2','Heading 3']:
    st = styles[stylename]
    st.font.name = 'Times New Roman'; st.font.color.rgb = RGBColor(0,0,0)
    st._element.rPr.rFonts.set(qn('w:ascii'), 'Times New Roman')
    st._element.rPr.rFonts.set(qn('w:hAnsi'), 'Times New Roman')
    st.paragraph_format.keep_with_next = True
styles['Title'].font.size = Pt(18); styles['Title'].font.bold = True
styles['Heading 1'].font.size = Pt(14); styles['Heading 1'].font.bold = True
styles['Heading 1'].paragraph_format.space_before = Pt(0); styles['Heading 1'].paragraph_format.space_after = Pt(10)
styles['Heading 2'].font.size = Pt(12); styles['Heading 2'].font.bold = True
styles['Heading 2'].paragraph_format.space_before = Pt(8); styles['Heading 2'].paragraph_format.space_after = Pt(3)
styles['Heading 3'].font.size = Pt(12); styles['Heading 3'].font.bold = True
styles['Heading 3'].paragraph_format.space_before = Pt(5); styles['Heading 3'].paragraph_format.space_after = Pt(2)

def para(text='', bold=False, italic=False, align=None, indent=True, space_after=0, line=1.5):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = line
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.first_line_indent = Inches(.5) if indent else Inches(0)
    if align is not None: p.alignment = align
    r = p.add_run(text); set_font(r, 12, bold, italic)
    return p

def heading(text, level=2, chapter=False):
    if chapter:
        p = doc.add_paragraph(style='Heading 1'); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.page_break_before = True
        p.add_run(text.upper())
    else:
        p = doc.add_paragraph(style='Heading 2' if level == 2 else 'Heading 3')
        p.add_run(text.upper() if level == 2 else text)
    for r in p.runs: set_font(r, 14 if chapter else 12, True)
    return p

def body(text): return para(text)

def bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Inches(.5); p.paragraph_format.first_line_indent = Inches(-.25)
    p.paragraph_format.line_spacing = 1.5; p.paragraph_format.space_after = Pt(0)
    set_font(p.add_run(text), 12)
    return p

def table(title, headers, rows, widths=None):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Inches(0); p.paragraph_format.space_after = Pt(4)
    set_font(p.add_run(title), 12, True)
    t = doc.add_table(rows=1, cols=len(headers)); t.alignment = WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'; t.autofit=False
    for i,h in enumerate(headers): set_cell(t.rows[0].cells[i],h,True,'D9EAF7',10.5,WD_ALIGN_PARAGRAPH.CENTER)
    for row in rows:
        cells=t.add_row().cells
        for i,val in enumerate(row): set_cell(cells[i],val,False,'F7FAFC' if len(t.rows)%2==0 else None,10.5)
    if widths:
        for row in t.rows:
            for i,w in enumerate(widths): row.cells[i].width=Inches(w)
    doc.add_paragraph().paragraph_format.space_after=Pt(1)
    return t

def figure_table(caption, headers, rows, widths=None):
    t=doc.add_table(rows=1,cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'; t.autofit=False
    for i,h in enumerate(headers): set_cell(t.rows[0].cells[i],h,True,'DCE6F1',10.5,WD_ALIGN_PARAGRAPH.CENTER)
    for row in rows:
        cells=t.add_row().cells
        for i,val in enumerate(row): set_cell(cells[i],val,False,'F7FAFC',10.5,WD_ALIGN_PARAGRAPH.CENTER)
    if widths:
        for row in t.rows:
            for i,w in enumerate(widths): row.cells[i].width=Inches(w)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.first_line_indent=Inches(0)
    p.paragraph_format.space_before=Pt(3); p.paragraph_format.space_after=Pt(8)
    set_font(p.add_run(caption),10.5)
    return t

def pagebreak(): doc.add_page_break()

# Title sheet
for _ in range(2): para('', indent=False, line=1)
para('MAHARASHTRA INSTITUTE OF TECHNOLOGY', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('CHHATRAPATI SAMBHAJINAGAR', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('An Autonomous Institute Affiliated to Dr. Babasaheb Ambedkar Marathwada University', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=1.2)
para('', indent=False, line=1)
para('COMMUNITY ENGAGEMENT PROJECT', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('PROJECT REPORT', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('', indent=False, line=1)
para('SCAM OR SMART DEAL?', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('INVESTMENT HYPE AWARENESS WEBSITE', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('', indent=False, line=1)
para('Submitted by', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('Nisha Vinay Thakur  |  102058', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('Bablu Ganesh Ade  |  102014', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('', indent=False, line=1)
para('Second Year B.Tech. Artificial Intelligence and Data Science', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('Division A', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('', indent=False, line=1)
para('Under the guidance of', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('Mr. Pratik Khodwe', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('', indent=False, line=1)
para('ACADEMIC YEAR 2026–2027', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)

# Front matter in roman-numbered section
sec=doc.add_section(WD_SECTION.NEW_PAGE); configure_section(sec,True)
sec._sectPr.append(OxmlElement('w:pgNumType'))
sec._sectPr[-1].set(qn('w:fmt'),'lowerRoman'); sec._sectPr[-1].set(qn('w:start'),'1')
heading('Certificate',2)
body('This is to certify that the Community Engagement Project report entitled “Scam or Smart Deal? Investment Hype Awareness Website” has been submitted by the following students of Second Year B.Tech. Artificial Intelligence and Data Science, Division A, of Maharashtra Institute of Technology, Chhatrapati Sambhajinagar, during Academic Year 2026–2027.')
body('The work presented in this report describes the design and development of a browser-based educational website about warning signs in online investment promotions, fake trading applications, and social-media stock-tip schemes. The project was carried out under the guidance of Mr. Pratik Khodwe.')
table('Student Details', ['Sr. No.','Student Name','Roll No.'], [['1','Nisha Vinay Thakur','102058'],['2','Bablu Ganesh Ade','102014']], [0.8,3.9,1.2])
para('', indent=False, line=1)
for text in ['Project Guide','CEP Coordinator','Head of Department']:
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(36); p.paragraph_format.first_line_indent=Inches(0)
    set_font(p.add_run('________________________                    ' + text),11)

pagebreak(); heading('Acknowledgement',2)
body('We express our sincere gratitude to our project guide, Mr. Pratik Khodwe, for guidance and feedback during the preparation of this Community Engagement Project. His direction helped us shape the project into a focused educational website about investment-scam warning signs and safe verification practices.')
body('We thank the Department of Artificial Intelligence and Data Science and Maharashtra Institute of Technology, Chhatrapati Sambhajinagar, for providing the academic framework in which this project was developed. We also acknowledge the public investor-education materials published by the Securities and Exchange Board of India and the Government of India cybercrime reporting services. These sources informed the educational content and reporting guidance presented on the website.')
body('The project team prepared the website and this report as an educational resource. No community survey, outreach session, participant testing, or impact evaluation was conducted for this report.')

pagebreak(); heading('Sponsorship Letter',2)
para('NOT APPLICABLE', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('This academic project did not receive external sponsorship. No sponsorship letter is therefore included.', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)

pagebreak(); heading('Project Photograph',2)
para('INSERT A SCREENSHOT OF THE PUBLISHED WEBSITE BEFORE FINAL PRINTING', True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('The project website is published at: https://axpitt.github.io/Finance-Scam-Tracker-Cep-Project/', align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
para('A screenshot has not been embedded in this report because a verified page capture was not available during document preparation. Add a direct screenshot of the team’s published website here; do not substitute a recreated mock-up.', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=False)
for _ in range(5): para('',indent=False,line=1)
para('Project website: “Scam or Smart Deal? | Investment Hype Awareness”',italic=True,align=WD_ALIGN_PARAGRAPH.CENTER,indent=False)

pagebreak(); heading('Abstract',2)
abstract=('Online investment promotions can use guaranteed-return claims, urgency, fabricated-looking profit displays, unverified advisers, unfamiliar trading-app links, third-party payment requests, and blocked withdrawals to encourage people to act before checking the facts. This Community Engagement Project developed “Scam or Smart Deal?”, a static multi-page awareness website for students, first-time investors, and community members. The team reviewed investor-education guidance from the Securities and Exchange Board of India (SEBI) and cyber-fraud reporting information from the Government of India, then translated recurring warnings into a red-flag guide, a staged explanation of fake trading-app scams, fictional scenario exercises, a six-question quiz, emergency reporting guidance, and a source directory. The site is implemented with HTML, CSS, and browser-side JavaScript and is published on GitHub Pages. It has no application backend, account system, analytics, or persistent quiz storage; its interactions are designed to run in the browser. The completed deliverable is an educational website, not a financial product or advice service. No survey, community session, usability study, or learning-outcome measurement was conducted. Therefore, this report documents implementation and content scope, but makes no claim that the website has reduced fraud or improved user awareness. Formal usability and accessibility evaluation remain future work.')
assert 150 <= len(abstract.split()) <= 200, len(abstract.split())
body(abstract)
para('Keywords: investment scam awareness; fake trading applications; investor education; financial cyber fraud; static website',italic=True)

pagebreak(); heading('Index / Table of Contents',2)
toc=[('Certificate','i'),('Acknowledgement','ii'),('Sponsorship Letter','iii'),('Project Photograph','iv'),('Abstract','v'),('List of Figures','vi'),('List of Tables','vii'),('List of Graphs','viii'),('Abbreviations','ix'),('Chapter 1  Introduction','1'),('Chapter 2  Literature Survey',''),('Chapter 3  Problem Definition and Objectives',''),('Chapter 4  Methodology and System Design',''),('Chapter 5  Website Implementation',''),('Chapter 6  Results and Discussion',''),('Chapter 7  Conclusion and Future Scope',''),('References','')]
table('Contents', ['Section','Page'], toc,[5.4,1.0])
para('Page numbers for chapters and references should be refreshed in the Table of Contents in Word after the final screenshot and pagination are added.',italic=True,indent=False)

pagebreak(); heading('List of Figures',2)
table('List of Figures', ['Figure No.','Title of Figure','Page No.'], [['4.1','Conceptual architecture of the awareness website',''],['5.1','Website page and learning-flow map',''],['6.1','Evidence boundary for project results','']], [1.0,4.5,0.8])
pagebreak(); heading('List of Tables',2)
table('List of Tables', ['Table No.','Title of Table','Page No.'], [['1.1','Project scope and boundaries',''],['2.1','Summary of reviewed guidance and literature',''],['3.1','Project objectives and deliverables',''],['4.1','Development stages and evidence',''],['5.1','Implemented website modules',''],['6.1','Implementation outcomes and evaluation status','']], [1.0,4.5,0.8])
pagebreak(); heading('List of Graphs',2)
para('No graphs are included. The project did not collect survey, usage, or learning-assessment data from which a graph could be produced.',indent=False)
pagebreak(); heading('Abbreviations',2)
table('Abbreviations', ['Abbreviation','Expansion'], [['AI','Artificial Intelligence'],['CSS','Cascading Style Sheets'],['CEP','Community Engagement Project'],['HTML','HyperText Markup Language'],['I4C','Indian Cyber Crime Coordination Centre'],['JS','JavaScript'],['SEBI','Securities and Exchange Board of India'],['SCORES','SEBI Complaints Redress System'],['URL','Uniform Resource Locator'],['UI','User Interface']], [1.4,4.8])

# Chapters restart in Arabic pagination
sec=doc.add_section(WD_SECTION.NEW_PAGE); configure_section(sec,True)
sec._sectPr.append(OxmlElement('w:pgNumType')); sec._sectPr[-1].set(qn('w:fmt'),'decimal'); sec._sectPr[-1].set(qn('w:start'),'1')

# Chapter 1
heading('Chapter 1  Introduction',chapter=True)
heading('1.1 Background',3)
body('The internet has made financial information and investment offers easy to encounter through social networks, video platforms, messaging groups, advertisements, and app listings. This access can help people learn, but it also creates opportunities for promotional claims to reach users outside formal financial channels. A post may present a promoter as an expert, display supposed profits, promise unusually high or assured returns, or urge a person to join a private group immediately. A polished interface, large follower count, testimonial, or screenshot should not be treated as independent proof of legitimacy.')
body('SEBI’s investor-education material advises caution around assured or near-certain returns, unusually high returns, unregistered entities, complex strategies that are not understood, missing documentation, and pressure to act quickly [1]. Its fake trading-app advisory describes a progression in which social-media promotions and trust-building lead a user to an unfamiliar app, displayed profits encourage more deposits, and withdrawal attempts are blocked or accompanied by demands for additional fees [2]. These public warnings give a concrete foundation for a short, action-focused awareness resource.')
heading('1.2 Community Context',3)
body('The intended audience is college students, first-time investors, and community members who may encounter online investment promotions. The project does not claim that this audience has a measured knowledge gap: the team did not conduct a needs-assessment survey. Instead, the chosen community-facing problem is defined from the documented presence of online investment-scam patterns in official investor warnings. The website offers general prompts for pausing, checking claims independently, and finding official information.')
heading('1.3 Project Overview',3)
body('“Scam or Smart Deal? | Investment Hype Awareness” is a static, multi-page educational website. Its pages cover a home overview, red flags, the stages of a fake trading-app scam, a fictional Scam Spotter challenge, a quiz, actions to take if money was sent, project background, and official sources. The site is published at the GitHub Pages URL listed on the title-related evidence page and in the references. The local project uses HTML for page structure, CSS for presentation, and JavaScript for navigation and browser-side interactions.')
heading('1.4 Scope and Boundaries',3)
table('Table 1.1  Project Scope and Boundaries',['Included in the project','Outside the project scope'],[['Plain-language awareness of investment-promotion warning signs','Personalised investment or legal advice'],['Fictional examples and short learning interactions','Verification or adjudication of real people, firms, or offers'],['Links to SEBI and Government of India information','Investment recommendations, trading, or brokerage services'],['Browser-side interactions without an account','Backend storage, reporting intake, or user profiling'],['Emergency signposting for suspected cyber financial fraud','A promise that reporting will recover money']], [3.1,3.1])
heading('1.5 Report Structure',3)
body('Chapter 2 surveys regulatory guidance and research relevant to investment scams and digital awareness. Chapter 3 states the problem, aim, objectives, and constraints. Chapter 4 describes the development method and conceptual design. Chapter 5 records the website pages and implementation approach. Chapter 6 reports implementation evidence and limits without inventing user-study findings. Chapter 7 concludes the project and identifies future work.')

# Chapter 2 Literature Survey: expanded to satisfy the stated 8–10-page target.
heading('Chapter 2  Literature Survey',chapter=True)
heading('2.1 Purpose and Review Approach',3)
body('This literature survey establishes the content basis for an educational website about investment hype and fake trading applications. It is a focused narrative review, not a systematic review. The source set prioritises public investor guidance issued by SEBI, the Government of India cybercrime reporting portal, and published empirical research on short online financial-fraud education. The review asks four practical questions: what warning signs should the website teach; how do reported fake-app patterns unfold; what should a user do to verify an offer or respond to a suspected fraud; and what can existing education research support without overstating its findings?')
body('Official advisories serve as the primary source for the Indian investor-protection context and the website’s emergency links. Academic research provides a cautious rationale for presenting concise educational content but cannot validate this particular website. The sources have different purposes: an advisory identifies risks and actions, while an experiment estimates intervention effects in a specific population and setting. The project therefore uses official materials to ground factual messages and uses research findings only to discuss design considerations and evaluation needs.')
heading('2.2 Investment Risk and Claims of Certainty',3)
body('SEBI’s “How to Spot a Scam” guidance starts from a basic investment principle: securities-market investments involve risk, so claims of assured, guaranteed, or near-certain returns deserve suspicion [1]. The page also identifies unusually high returns regardless of market conditions, an entity that is not appropriately registered, a strategy too complex for the investor to understand, inadequate documentation, and an instruction to act immediately as warning signs. These signals help form a practical checklist because they focus attention on the claim, the promoter, the supporting information, and the pressure surrounding the decision.')
body('The checklist must be taught as a set of reasons to pause and investigate, not as a scoring rule that proves fraud. A single signal does not establish that a real person or offer is fraudulent. Conversely, a professional-looking website, registration claim, or absence of an obvious warning sign does not guarantee that an investment is suitable or safe. The site’s language should therefore distinguish “red flag” from “proof.” This distinction is central to responsible financial education: a quick checklist helps users ask better questions, but does not replace independent due diligence or formal advice.')
body('SEBI’s guidance on factors to consider before investing expands this point by asking investors to consider goals, risk tolerance, time horizon, asset allocation, diversification, and the limitations of past performance [3]. For the awareness website, this material is relevant because scam messaging often short-circuits the process of understanding risk. A person who is pressured to act at once may not stop to consider whether the product is understood, whether the risk fits their circumstances, or whether the evidence is independently verifiable. The website avoids explaining how to select a security; it focuses on resisting pressure and checking the source.')
heading('2.3 Social-Media Promoters and “Guru” Claims',3)
body('Social-media investment promotion mixes educational content, personal branding, entertainment, and commercial persuasion. SEBI’s investor-awareness material about “Stock Market Guru” scams warns users to be cautious about claims of expertise and investment success promoted through online channels [4]. An audience may use the visible popularity of a promoter, testimonials, or screenshots as a shortcut for credibility. Yet these indicators can be self-published, selectively presented, or difficult to verify from the post itself. The website therefore uses fictional examples and points learners toward independent checks rather than asking them to judge a promoter’s trustworthiness from appearance.')
body('The content design also avoids naming or depicting real social-media personalities. A student awareness resource should not make unsupported allegations or risk confusing a warning example with a real accusation. Fictional posts can isolate patterns such as a guaranteed daily profit claim, limited-time access to a private group, a request to pay for “activation,” or an app download link supplied by the promoter. The scenario then explains why those details deserve scrutiny and what safer next step is available.')
body('SEBI’s investor material identifies unregistered entities and pushy sales tactics as concerns [1]. Registration checks should be carried out through official regulator or exchange information reached independently. A link in a promotional message can lead to an imitation site, and the use of a regulator’s name or logo is not by itself proof that the message is genuine. The website frames verification as checking the exact entity, service, and platform through an official source. It does not claim that registration alone guarantees investment performance, prevents impersonation, or makes every product suitable for every user.')
heading('2.4 Fake Trading Applications as a Sequence of Decisions',3)
body('SEBI’s fake trading-app advisory is especially relevant to the project because it presents a sequence rather than a single warning sign [2]. The described stages begin with an attractive social-media advertisement or messaging-group invitation. A promoter may build trust by sharing analysis, supposed performance history, screenshots, or early successful tips. The user is then directed to a fake trading application, where an apparent profit display may encourage further deposits. Pressure to invest more can follow. When the user tries to withdraw, the platform may give excuses, block the transaction, or demand more fees. The app may ultimately stop working.')
body('A stage-based presentation helps the learner see how small decisions can connect. The initial post may look like an invitation to learn; a testimonial may appear to confirm the promoter; a displayed balance may seem to show a successful investment. Each step can increase confidence and commitment, even though the evidence may be controlled by the same unverified source. By tracing the sequence, a learner can identify more than one opportunity to pause: before clicking the link, before installing an app, before sending money, before borrowing to add funds, and when withdrawal conditions change.')
body('The SEBI advisory flags unverified app or APK links, payments to third-party accounts, unrealistic promises, and social-media stock tips as reasons for caution [2]. It points users toward checking platform legitimacy through exchange information or SEBI investor resources. The project reflects these points in a dedicated page explaining the stages of the pattern and in its red-flag and scenario modules. The explanations remain educational; the website does not scan devices, inspect apps, or authenticate any platform.')
heading('2.5 Ponzi-Style Offers and Withdrawal Barriers',3)
body('SEBI’s caution-to-investor guidance describes Ponzi schemes as arrangements that use money from later participants to pay earlier participants, while promising high or unusually consistent returns [5]. The guidance identifies guaranteed high returns, unregistered investments or sellers, lack of transparency, and difficulty receiving payments as warning indicators. This source broadens the project’s context beyond fake trading interfaces: investment fraud may rely on a promise and a payment structure even when there is no app at all.')
body('Withdrawal barriers are especially useful as a teaching example because they may occur after trust has been built. A user may see an account balance rise on a screen, then be told that tax, verification, unlocking, or processing fees must be paid before funds can be released. The website’s emergency page can explain that a displayed balance is not independent proof that the money is invested or withdrawable. It should not tell users to pay a further fee to recover funds. If a person suspects a cyber financial fraud, the site directs them to prompt official reporting and their bank or payment provider rather than to further engagement with the promoter.')
body('The wording must avoid making every delayed payment or failed transfer equivalent to a Ponzi scheme. A warning pattern is a reason to preserve relevant information, stop following unverified instructions, and use appropriate official channels. The project is not a diagnostic tool and does not provide legal classification. The distinctions in the cited official materials help keep the lessons precise and avoid turning general awareness guidance into accusations against particular entities.')
heading('2.6 Due Diligence and the Limits of Checks',3)
body('SEBI’s due-diligence material describes research into the business, business model, financial condition, available information, and risk-return profile before an investment decision [6]. Its investor support resources also provide routes to check the registration status of market intermediaries [7]. These resources support the project’s practical instruction to leave a social-media link and visit a regulator or exchange website independently. Users should look for exact name, registration category, and service, rather than relying on a badge or screenshot supplied by a promoter.')
body('Verification is not a guarantee. It can establish limited facts about an entity or platform at the time of checking, but it cannot predict returns or make a product appropriate for a particular person. Registration status may also be impersonated: a scammer can use a real firm’s name while directing the user to a different account or application. Consequently, a responsible awareness website should encourage users to compare details carefully and to seek trusted professional help when uncertain. The website confines itself to signposting, not to making the check on the user’s behalf.')
body('The project also avoids giving stock picks, return projections, market timing advice, or instructions to invest. This boundary is consistent with its educational purpose and reduces the risk that a user will mistake a student website for a regulated financial service. A clear disclaimer should appear near the informational content. Source links should be labelled with the issuing organisation and page purpose so that users can identify official material and understand why the link is offered.')
heading('2.7 Reporting and Immediate Response in India',3)
body('The National Cyber Crime Reporting Portal is a Government of India channel for reporting cybercrime. Its public information identifies helpline 1930 for reporting financial cyber fraud and provides an online reporting route [8]. The website’s “If Money Was Sent” page is intended to put this information in a visible, action-oriented place. It encourages prompt contact with the bank or payment provider and use of official reporting channels. These are signposts; the static website does not send a complaint, transfer evidence, contact a bank, or provide case-specific advice.')
body('The wording must not promise that calling the helpline will recover the amount. Reporting enables the relevant authorities and financial institutions to consider the incident, but outcomes depend on facts and official processes. The user should preserve transaction details and relevant communications when making a real report, while avoiding the disclosure of sensitive data on the awareness website. The project collects none of these details because it has no form or reporting intake.')
body('A securities-market grievance and a cyber financial fraud report may involve different channels. SEBI’s SCORES platform is an investor grievance redress system for matters within its remit [9]. The cybercrime portal and 1930 are relevant to suspected cyber financial fraud. The site provides links to both types of official resources and should not conflate them. Users should follow the instructions of the appropriate authority and first contact the relevant intermediary where required by the official process.')
heading('2.8 Digital Learning and Scenario-Based Explanations',3)
body('A short digital lesson can organise information into a memorable pattern: identify a claim, notice a pressure tactic, decide what information is missing, and choose a safer next step. A static website is suitable for such content because it can present text, examples, feedback, and references without asking a learner to create an account. Fictional scenarios also let a learner practise applying a checklist without exposing real financial information or naming alleged victims and perpetrators.')
body('The project’s Scam Spotter challenge follows this approach. A learner reads a fictional investment message, selects a response, and receives an explanation. Immediate feedback can connect a signal to its reason for concern. The quiz uses multiple-choice items to revisit key concepts. This structure can support practice, but a quiz score is not a validated measure of financial capability. Correctly answering a question in a quiet learning setting does not prove that someone will act safely under pressure or recognise every real-world scam.')
body('Research by Burke, Kieffer, Mottola, and Perez-Arce examined short online educational interventions designed to reduce susceptibility to financial fraud [10]. Their study used a representative sample of U.S. adults and compared concise text or video education with a control condition. The authors reported reduced expressed susceptibility after the intervention, with longer-term persistence depending on a reminder. The study suggests that concise fraud education can be worth evaluating and that reinforcement may matter. It does not establish that this Indian student website has an effect, nor that results from the U.S. study transfer directly to this project’s audience or to every form of investment fraud.')
body('The design implication is modest: clear, repeated cues and feedback are reasonable learning features to implement, while impact claims require direct evaluation. If this website is later demonstrated to a community group, evaluation should record participant numbers, date, method, consent approach, and limitations. A suitable pre/post learning check would need to be planned and reviewed in accordance with college requirements. The current report includes none of those outcomes because no survey or user study was conducted.')
heading('2.9 Privacy, Accessibility, and Trust in an Awareness Site',3)
body('An awareness resource can itself create risk if it asks people to submit sensitive financial stories or account details. The site is designed without a login, backend, database, analytics, or persistent quiz storage. Scenario responses and quiz state are intended to remain in page memory and reset when the page is reloaded. This minimises the amount of information handled by the project. The report describes these architectural properties from the local source files; no independent privacy audit or network capture is claimed.')
body('Accessibility also matters because a community resource should be usable with different input methods and screen sizes. The project source includes semantic HTML landmarks, labelled navigation controls, visible focus styling, reduced-motion preferences, and live regions for interaction feedback. JavaScript includes keyboard handling for the mobile navigation and dropdowns. These are implementation features, not proof of conformance to a formal accessibility standard. A future accessibility review should test the deployed pages with keyboard-only navigation, screen-reader software, zoom, and mobile layouts, then document issues and corrections.')
body('Trust depends on factual accuracy, legible presentation, predictable links, and clear limits. Official sources should be easy to find and checked periodically. The design should not imitate a trading terminal or display fictional market data as if live. The project has no live price feed, broker integration, investment calculator, or trading feature. These omissions help maintain a clear distinction between an educational site and a financial service. They also keep implementation manageable for a small student team.')
heading('2.10 Review Synthesis and Design Implications',3)
body('The reviewed sources converge on a set of behaviours relevant to the website: treat assured or unusually high returns with caution; be wary of urgency and unverifiable authority; research the promoter and platform through official sources reached independently; do not treat screenshots or displayed profits as proof; recognise unverified apps, third-party payment instructions, and withdrawal barriers as warning patterns; and seek official help promptly when cyber financial fraud is suspected [1–9]. These points support a simple learning sequence from recognition to action.')
body('The literature also sets limits on what can be claimed. Regulatory warnings are not a dataset measuring prevalence among the project’s intended audience. The U.S. education experiment is not a local evaluation. A quiz is not a validated predictor of real-world behaviour. No student survey, usability study, or community demonstration was conducted. The project’s evidence is therefore the developed website and its documented content structure, not a measured change in awareness or fraud incidence.')
body('Table 2.1 summarises how the reviewed sources informed the website. The mapping is thematic: it indicates the content rationale for a module, not a claim that the module has been experimentally validated.')
table('Table 2.1  Summary of Reviewed Guidance and Literature',['Source group','Relevant message','Website design use'],[['SEBI scam guidance [1]','Guaranteed returns, pressure, unregistered promoters, and poor documentation are reasons to pause.','Red-flag checklist and verification prompts.'],['SEBI fake-app advisory [2]','Social-media hook can lead through trust-building, fake app, displayed profit, more deposits, and blocked withdrawal.','Stage-by-stage “How It Works” page.'],['SEBI investment guidance [3,6,7]','Independent research and official checks support informed decisions; checks have limits.','Source directory and explicit educational boundaries.'],['SEBI caution and SCORES [5,9]','Ponzi warning signs and investor grievance routes require accurate signposting.','Withdrawal warning and distinct complaint links.'],['Government cybercrime portal [8]','1930 and online reporting are official routes for suspected financial cyber fraud.','“If Money Was Sent” response page.'],['Burke et al. [10]','Concise fraud education may improve recognition in the studied U.S. setting; reminders may support persistence.','Motivates short scenarios and future evaluation, not an impact claim.']], [1.65,2.7,2.15])

# Chapter 3
heading('Chapter 3  Problem Definition and Objectives',chapter=True)
heading('3.1 Problem Definition',3)
body('People who encounter investment promotions through social media or messaging channels may see claims of assured returns, urgency, supposed expert success, unfamiliar applications, third-party payments, or barriers to withdrawal. A concise community-facing resource is needed to explain why these patterns deserve caution, how to check information through official sources, and where to find reporting guidance if a person suspects cyber financial fraud.')
heading('3.2 Aim',3)
body('To develop a simple, privacy-conscious website that helps learners recognise common warning signs in online investment promotions and practise safer next steps using official investor-education information.')
heading('3.3 Objectives',3)
for x in ['Review official SEBI guidance and Government of India cyber-fraud information relevant to online investment scams.','Present warning signs in plain language and distinguish a warning sign from proof that a specific offer is fraudulent.','Explain the commonly described fake trading-app sequence using an accessible, stage-based presentation.','Develop fictional scenarios and a short browser-side quiz that give immediate explanatory feedback.','Provide visible links to official verification, grievance, and cyber-fraud reporting resources.','Keep the website static and avoid accounts, backend storage, analytics, or collection of identity and financial data.','Document implementation accurately and identify evaluation work that remains incomplete.']: bullet(x)
heading('3.4 Scope and Constraints',3)
body('The project covers investment hype, social-media stock-tip promotions, fake trading applications, misleading profit displays, and withdrawal barriers. It provides general awareness information and official links. It does not verify live offers, investigate complaints, provide personalised financial advice, facilitate trading, or guarantee recovery. Examples are educational and must not be treated as evidence about a real person or company. No survey, awareness session, participant feedback, or learning assessment was conducted. These constraints limit the report’s results to the deliverable and its implementation scope.')
table('Table 3.1  Project Objectives and Deliverables',['Objective','Corresponding deliverable'],[['Translate official warnings','Red-flags and fake-app guidance pages.'],['Enable practice','Scam Spotter scenarios and six-question quiz.'],['Support safe next steps','Emergency response page and official source links.'],['Limit data handling','Static front end without accounts or persistent quiz data.'],['Maintain evidence integrity','Report implementation; label evaluation as not conducted.']], [3.0,3.5])

# Chapter 4
heading('Chapter 4  Methodology and System Design',chapter=True)
heading('4.1 Development Method',3)
body('The project used a small, iterative website-development workflow. First, the team established the educational topic and bounded the site to investment-scam awareness. Second, official investor and cybercrime materials were reviewed to identify recurring signals and safe next steps. Third, these messages were organised into a set of short pages and fictional activities. Fourth, the pages were implemented using HTML, CSS, and browser-side JavaScript. The completed files were configured as a multi-page Vite project and published on GitHub Pages. This report records the implemented pages and source files; it does not claim a formal usability or community evaluation.')
table('Table 4.1  Development Stages and Evidence',['Stage','Activity','Available evidence'],[['1. Topic definition','Set the focus on investment-promotion scams and fake apps.','Project brief and website content.'],['2. Source review','Use SEBI and Government of India investor/cybercrime information.','Sources page and references.'],['3. Content organisation','Arrange warnings, scenarios, quiz, and reporting information.','Eight HTML page files.'],['4. Implementation','Build page structure, styling, navigation, and interactions.','HTML, CSS, JavaScript, Vite configuration.'],['5. Publication','Publish the static project on GitHub Pages.','URL supplied by the project team.'],['6. User evaluation','Survey, community session, usability test, or learning assessment.','Not conducted; no results reported.']], [1.2,2.6,2.8])
heading('4.2 System Architecture',3)
body('The architecture is client-side. HTML files contain page structure and content. A shared CSS asset defines typography, colour, layout, responsive behaviour, and focus treatments. A shared JavaScript file manages navigation, dropdowns, scenario responses, quiz state, and interface feedback. During development, Vite supports a multi-page build; the published output consists of static assets delivered to the browser. External links lead to official sources but are opened only when a user chooses them.')
figure_table('Fig. 4.1  Conceptual architecture of the awareness website',['Content layer','Presentation layer','Interaction layer','Published delivery'],[['HTML pages\nWarnings, scenarios, quiz, sources','Shared CSS\nResponsive layout and focus styling','Browser JavaScript\nNavigation and local feedback','Static GitHub Pages\nNo project backend']], [1.6,1.6,1.6,1.6])
heading('4.3 User Flow and Learning Pattern',3)
body('The intended learning path begins with the home page, where a learner can select a topic. The red-flags page introduces observable warning patterns. The fake-app page shows how an apparently profitable platform can be used to solicit further deposits. The Scam Spotter page asks the learner to interpret fictional messages. The quiz revisits concepts and provides immediate feedback. The emergency page explains where to find official help if money has already been sent. The source directory supports independent reading.')
heading('4.4 Privacy and Data Handling',3)
body('The site is designed without user accounts, a server-side database, analytics, or a form that collects reports. Quiz choices are handled in page memory. The local source code contains no intentional persistent score storage such as local storage. These design choices reduce collection of personal information. They do not, by themselves, establish a formal privacy certification or independent network audit. Users should not enter personal or financial details into the site.')
heading('4.5 Content Review Principles',3)
for x in ['Use official sources for factual descriptions of scam patterns and reporting routes.','Use fictional examples and avoid identifying real individuals or businesses as scammers.','Present warning signs as reasons to verify, not as proof or a legal judgment.','Keep reporting guidance separate from investment guidance and do not promise recovery.','State that the website is educational and does not provide personalised financial advice.','Keep external sources visible so readers can verify information independently.']: bullet(x)

# Chapter 5
heading('Chapter 5  Website Implementation',chapter=True)
heading('5.1 Technology and Project Structure',3)
body('The project is implemented as a static front end using HTML, CSS, and vanilla JavaScript. Vite is configured for a multi-page build with separate entries for the eight site pages. No server-side application or database is included. The project source also contains a README and a compiled distribution folder. The public deployment URL supplied by the team is https://axpitt.github.io/Finance-Scam-Tracker-Cep-Project/.')
heading('5.2 Implemented Pages',3)
table('Table 5.1  Implemented Website Modules',['Page / file','Purpose and principal content'],[['Home — index.html','Introduces the “Scam or Smart Deal?” project and directs users to learning modules.'],['Red Flags — red-flags.html','Presents warning signs such as guaranteed returns, urgency, unverified claims, suspicious links, payment requests, and withdrawal barriers.'],['How It Works — how-it-works.html','Explains the staged pattern described in SEBI fake trading-app guidance.'],['Scam Spotter — scam-spotter.html','Uses fictional investment-promotion examples and interactive choices with explanations.'],['Quiz — quiz.html','Provides six short questions with browser-side answer feedback and scoring.'],['If Money Sent — if-money-sent.html','Signposts prompt bank/payment-provider contact and official cyber-fraud reporting routes, including 1930.'],['About CEP — about-cep.html','Explains project background, intended audience, scope, and educational boundary.'],['Sources — sources.html','Lists official investor-education and reporting sources.']], [1.7,4.9])
heading('5.3 Interaction Design',3)
body('The shared JavaScript file supports a mobile-navigation toggle, dropdown menus, keyboard dismissal with Escape, scenario selection and explanation, quiz progress and feedback, and page-level interface helpers. Quiz and scenario interactions are designed to run in the browser rather than submit answers to a server. Refreshing the page is intended to clear transient quiz state. These behaviours are described from the implementation files; this report does not claim that every interaction was independently exercised across browsers or devices.')
heading('5.4 Responsive Design and Accessibility Features',3)
body('The stylesheet includes layouts intended for desktop, tablet, and phone widths, visible keyboard focus styling, reduced-motion preferences, and a consistent visual theme. The HTML uses structural landmarks and ARIA labels or live feedback regions in interactive areas. JavaScript uses expanded/collapsed state on navigation controls and returns focus after closing a mobile menu with Escape. These source-level features are useful starting points for accessible interaction, but the project has not undergone a formal WCAG audit or assistive-technology test. The report therefore describes implemented provisions rather than declaring conformance.')
heading('5.5 Published Educational Flow',3)
figure_table('Fig. 5.1  Website page and learning-flow map',['Discover','Recognise','Practise','Respond','Verify'],[['Home / About','Red Flags / How It Works','Scam Spotter / Quiz','If Money Sent','Sources']], [1.3,1.3,1.3,1.3,1.3])
body('The page sequence moves from understanding the topic to recognising patterns, practising decisions, finding incident-response information, and checking official sources. Users can also navigate directly to any page. The structure is designed for short self-guided use and does not depend on a facilitator, account, or stored progress.')

# Chapter 6
heading('Chapter 6  Results and Discussion',chapter=True)
heading('6.1 Implemented Results',3)
body('The primary result is a published, eight-page static awareness website supported by shared CSS and JavaScript. The pages cover a home overview, red flags, the fake trading-app sequence, fictional scenario practice, a six-question quiz, emergency reporting signposts, project information, and source references. The site’s content is based on public official materials cited in this report. The local project includes a Vite multi-page configuration and a production distribution folder. The team supplied the public GitHub Pages URL recorded in this report.')
body('The project also establishes a clear technical boundary: it is an educational front end and does not provide brokerage, live market information, personalised advice, or complaint intake. The absence of a backend and persistent quiz storage reduces project complexity and avoids creating a repository of sensitive financial or identity details. It also means the website cannot save progress, analyse visitor behaviour, or report incidents on a user’s behalf.')
heading('6.2 Evidence and Evaluation Status',3)
table('Table 6.1  Implementation Outcomes and Evaluation Status',['Area','What this report can state','Status'],[['Website pages','Eight HTML pages and shared styling/JavaScript exist in the project.','Implemented in source.'],['Public deployment','A GitHub Pages URL was supplied by the team.','URL recorded; visual capture not embedded.'],['Quiz and scenarios','Browser-side learning interactions are present in the source.','Implemented; no participant results.'],['Survey / outreach','No survey or awareness session was conducted.','Not conducted.'],['Usability testing','No formal user test is available.','Not conducted.'],['Learning impact','No pre/post measure or outcome data is available.','Not measured.'],['Privacy audit','Source is structured without backend collection features.','No independent audit claimed.']], [1.4,3.6,1.5])
heading('6.3 Interpretation',3)
body('The implementation demonstrates that a focused investor-awareness resource can be organised as a compact static website. Its strongest project evidence is the presence of the page modules, client-side learning interactions, and official source links. The design translates advisory content into a sequence of recognition, practice, and response. That is a design outcome, not evidence of improved awareness or reduced exposure to fraud.')
body('The research reviewed in Chapter 2 provides a rationale for evaluating brief online education, but findings from other populations cannot be attributed to this website. Because no user study was conducted, the team cannot report whether the language is understood, whether navigation is easy, whether the quiz is helpful, or whether users remember the advice. The project also lacks a verified screenshot in the report and has not documented a browser-by-browser test record. These gaps should be addressed before claiming community impact.')
heading('6.4 Limitations',3)
for x in ['The website content is general awareness material and may not cover every investment-fraud pattern.','The project did not collect survey responses, participant feedback, usability observations, or learning outcomes.','The report does not include a verified screenshot of the deployed pages.','Accessibility provisions were identified in source, but formal accessibility conformance was not tested.','Links and official procedures can change and should be rechecked before future use.','The static site cannot submit complaints, verify a live entity, or recover funds.']: bullet(x)
figure_table('Fig. 6.1  Evidence boundary for project results',['Documented in this report','Not measured or claimed'],[['Website structure and source files\nContent modules and technical scope\nPublic URL supplied by team','Survey or outreach findings\nUsability or accessibility validation\nChange in knowledge or fraud outcomes']], [3.2,3.2])

# Chapter 7
heading('Chapter 7  Conclusion and Future Scope',chapter=True)
heading('7.1 Conclusion',3)
body('The Community Engagement Project developed “Scam or Smart Deal? | Investment Hype Awareness,” a static multi-page website that explains warning signs in online investment promotions and fake trading-app patterns. It uses a red-flag guide, staged scam explanation, fictional scenario practice, a six-question quiz, incident-response signposting, and an official source directory. The content draws on SEBI investor education and Government of India cyber-fraud reporting information. The project demonstrates a small, privacy-conscious front-end approach that does not require accounts, a database, or a custom backend.')
body('The report records the website implementation and its boundaries. It does not report a survey, outreach event, usability study, or measured learning result because none was conducted. Accordingly, the project’s educational benefit remains an intended outcome rather than a measured result. The website should be presented as an awareness resource, not as financial advice or a guarantee against fraud.')
heading('7.2 Future Scope',3)
for x in ['Insert a genuine screenshot of the deployed site and verify the public pages before final printing.','Conduct a small, voluntary usability review with informed participants and report the actual method, sample size, and limitations.','If permitted by the college, evaluate learning with a short pre/post check and present only the observed results.','Prepare Marathi and Hindi versions after review by fluent speakers.','Test keyboard operation, screen-reader feedback, zoom, reduced motion, and mobile layouts; record fixes.','Review SEBI and Government of India links periodically and record the date of each content check.','Use non-identifying feedback to improve clarity; do not collect account data, transaction identifiers, or personal loss details through the website.']: bullet(x)

# References
heading('References',2)
refs=[
'[1] Securities and Exchange Board of India (SEBI), “How to Spot a Scam,” SEBI Investor. Available: https://investor.sebi.gov.in/spot-any-scam.html. Accessed: 3 November 2026.',
'[2] Securities and Exchange Board of India (SEBI), “Beware of Fake Trading App Scams!” investor-awareness advisory. Available: https://investor.sebi.gov.in/pdf/Fake%20trading%20app%20scam%20Landscape.pdf. Accessed: 3 November 2026.',
'[3] Securities and Exchange Board of India (SEBI), “Factors to Consider Before Investing,” SEBI Investor. Available: https://investor.sebi.gov.in/investment-thingsbeforeinv.html. Accessed: 3 November 2026.',
'[4] Securities and Exchange Board of India (SEBI), “Stock Market Guru Scams,” SEBI Investor. Available: https://investor.sebi.gov.in/pdf/Stock%20Market%20Guru%20Scams%20final.pdf. Accessed: 3 November 2026.',
'[5] Securities and Exchange Board of India (SEBI), “Caution to Investor: Caution Against Ponzi Schemes and Unregistered Investment Advisers,” SEBI Investor. Available: https://investor.sebi.gov.in/cautiontoinvestor.html. Accessed: 3 November 2026.',
'[6] Securities and Exchange Board of India (SEBI), “Due Diligence,” SEBI Investor. Available: https://investor.sebi.gov.in/due_diligence.html. Accessed: 3 November 2026.',
'[7] Securities and Exchange Board of India (SEBI), “Investor Support,” SEBI Investor. Available: https://investor.sebi.gov.in/investor-support.html. Accessed: 3 November 2026.',
'[8] Government of India, Ministry of Home Affairs, Indian Cyber Crime Coordination Centre, “National Cyber Crime Reporting Portal.” Available: https://www.cybercrime.gov.in/. Accessed: 3 November 2026.',
'[9] Securities and Exchange Board of India (SEBI), “SCORES: SEBI Complaints Redress System.” Available: https://scores.sebi.gov.in/. Accessed: 3 November 2026.',
'[10] J. Burke, C. Kieffer, G. Mottola, and F. Perez-Arce, “Can educational interventions reduce susceptibility to financial fraud?,” Journal of Economic Behavior & Organization, vol. 198, pp. 250–266, 2022. doi: 10.1016/j.jebo.2022.03.028.',
'[11] Finance Scam Tracker CEP Project, “Scam or Smart Deal? | Investment Hype Awareness,” project website. Available: https://axpitt.github.io/Finance-Scam-Tracker-Cep-Project/. Accessed: 3 November 2026.'
]
for ref in refs:
    p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.4); p.paragraph_format.first_line_indent=Inches(-.4)
    p.paragraph_format.line_spacing=1.5; p.paragraph_format.space_after=Pt(4)
    set_font(p.add_run(ref),11.5)

# Metadata and save
doc.core_properties.title='Scam or Smart Deal? Investment Hype Awareness Website — CEP Project Report'
doc.core_properties.subject='Community Engagement Project, Academic Year 2026–2027'
doc.core_properties.author='Nisha Vinay Thakur and Bablu Ganesh Ade'
doc.core_properties.keywords='CEP, investment scam awareness, SEBI, fake trading applications'
doc.save(OUT)
print(OUT)
print('abstract_word_count=',len(abstract.split()))
