#!/usr/bin/env python3
from build import page, write, breadcrumb_schema

# ============================================================
# RESOURCES HUB (index of all resource sub-pages)
# ============================================================
RESOURCE_PAGES = [
    ("blog", "Blog", "Practical articles on skills, careers, and industry trends.", "📰"),
    ("case-studies", "Case Studies", "Real student projects and the outcomes they led to.", "📊"),
    ("career-guides", "Career Guides", "Role-by-role breakdowns of what it takes to get hired.", "🧭"),
    ("project-ideas", "Project Ideas", "Portfolio-ready project ideas by skill track.", "💡"),
    ("skill-roadmaps", "Skill Roadmaps", "Step-by-step learning paths for each track.", "🗺️"),
    ("glossary", "Learning Glossary", "Plain-English definitions of terms you'll hear in each field.", "📖"),
    ("interview-prep", "Interview Preparation", "Question banks and mock-interview frameworks.", "🎤"),
    ("tools", "Tools", "Free and low-cost tools we recommend for each track.", "🛠️"),
    ("downloads", "Downloads", "Templates, cheat sheets, and checklists to download.", "📥"),
    ("support", "Support", "Raise a ticket or check the status of an existing one.", "🎫"),
    ("ai-mentor", "AI Mentor", "Chat with our WhatsApp-based AI Mentor anytime.", "🤖"),
    ("certificate-verification", "Verify a Certificate", "Confirm the authenticity of a SmartVersa certificate.", "✅"),
]

hub_cards = "".join(f"""
      <a href="{slug}.html" class="card" style="display:block;">
        <div class="icon">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </a>""" for slug, title, desc, icon in RESOURCE_PAGES)

resources_body = f"""
<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 44px;">
      <div class="eyebrow">Resources Hub</div>
      <h1>Free resources for your learning journey</h1>
      <p>Guides, templates, and roadmaps — no login required.</p>
    </div>
    <div class="grid grid-3">{hub_cards}</div>
  </div>
</section>
"""
write("resources.html", page(
    "Resources Hub", "Free learning resources from SmartVersa: blog, case studies, career guides, project ideas, roadmaps, glossary, interview prep, tools, and downloads.",
    "Resources", resources_body, canonical="resources.html", schema=breadcrumb_schema([("Home", ""), ("Resources", "resources.html")])
))

# ---- Sample content per resource page (a few real starter items each) ----

BLOG_POSTS = [
    ("How to Build a Data Analytics Portfolio With No Experience", "Career Guides", "5 min read"),
    ("SEO Basics Every Digital Marketer Should Know in 2026", "Digital Marketing", "6 min read"),
    ("Python vs Excel: When to Use Which for Data Work", "Data Analytics", "4 min read"),
    ("What Recruiters Actually Look For in an AI/ML Resume", "Career Guides", "7 min read"),
]

def blog_body():
    cards = "".join(f"""
      <div class="card">
        <span class="tag-pill">{cat}</span>
        <h3>{title}</h3>
        <p style="font-size:.85rem;color:var(--text-low);">{read}</p>
      </div>""" for title, cat, read in BLOG_POSTS)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Blog</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Blog</div>
      <h1>Articles on skills, careers, and industry trends</h1>
    </div>
    <div class="grid grid-2">{cards}</div>
  </div>
</section>"""
write("blog.html", page("Blog", "Practical articles on skills, careers, and industry trends from the SmartVersa team.", "Resources", blog_body(), canonical="blog.html"))

CASE_STUDIES = [
    ("From Zero to First Dashboard in 6 Weeks", "Data Analytics", "Karan Sethi built a sales-performance dashboard that's now the centerpiece of his interviews."),
    ("Launching a Live Ad Campaign Mid-Course", "Digital Marketing", "Rohit Malik ran a real Meta Ads campaign during week 5 and used the results in his portfolio."),
    ("Building an ML Capstone Alongside Final-Year Exams", "AI & Data Science", "Priya Yadav balanced university exams with a full ML capstone using recorded classes."),
]
def case_studies_body():
    cards = "".join(f"""
      <div class="card">
        <span class="tag-pill">{track}</span>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>""" for title, track, desc in CASE_STUDIES)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Case Studies</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Case Studies</div>
      <h1>Real student projects and outcomes</h1>
    </div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>"""
write("case-studies.html", page("Case Studies", "Real SmartVersa student projects and the outcomes they led to.", "Resources", case_studies_body(), canonical="case-studies.html"))

CAREER_GUIDES = [
    ("Breaking Into Data Analytics", "What skills, tools, and portfolio pieces actually matter for entry-level analytics roles."),
    ("A Realistic Path Into AI & Data Science", "What to learn first, what to skip, and how long it realistically takes."),
    ("Getting Your First Digital Marketing Role", "The skills clients and employers ask for most, and how to demonstrate them."),
]
def career_guides_body():
    cards = "".join(f"""
      <div class="card"><h3>{title}</h3><p>{desc}</p></div>""" for title, desc in CAREER_GUIDES)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Career Guides</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Career Guides</div>
      <h1>Role-by-role breakdowns of what it takes to get hired</h1>
    </div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>"""
write("career-guides.html", page("Career Guides", "Role-by-role career guides for Data Analytics, AI & Data Science, and Digital Marketing.", "Resources", career_guides_body(), canonical="career-guides.html"))

PROJECT_IDEAS = [
    ("Personal Finance Dashboard", "Data Analytics", "Build a dashboard tracking spend categories from a sample bank statement."),
    ("Local Business SEO Audit", "Digital Marketing", "Audit and improve the on-page SEO of a small local business site."),
    ("Movie Recommendation Model", "AI & Data Science", "A simple content-based recommender using a public movie dataset."),
    ("Automation Script for Repetitive Files", "Python Programming", "Automate renaming/sorting a folder of files using Python."),
]
def project_ideas_body():
    cards = "".join(f"""
      <div class="card"><span class="tag-pill">{track}</span><h3>{title}</h3><p>{desc}</p></div>""" for title, track, desc in PROJECT_IDEAS)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Project Ideas</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Project Ideas</div>
      <h1>Portfolio-ready project ideas by track</h1>
    </div>
    <div class="grid grid-2">{cards}</div>
  </div>
</section>"""
write("project-ideas.html", page("Project Ideas", "Portfolio-ready project ideas across Data Analytics, Digital Marketing, AI & Data Science, and Python.", "Resources", project_ideas_body(), canonical="project-ideas.html"))

ROADMAPS = [
    ("Data Analytics Roadmap", "Excel → SQL → Visualization → Storytelling with data."),
    ("AI & Data Science Roadmap", "Python → Statistics → ML fundamentals → Capstone project."),
    ("Digital Marketing Roadmap", "SEO fundamentals → Content → Paid ads → Analytics."),
]
def roadmaps_body():
    cards = "".join(f"""
      <div class="card"><h3>{title}</h3><p>{desc}</p></div>""" for title, desc in ROADMAPS)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Skill Roadmaps</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Skill Roadmaps</div>
      <h1>Step-by-step learning paths</h1>
    </div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>"""
write("skill-roadmaps.html", page("Skill Roadmaps", "Step-by-step skill roadmaps for Data Analytics, AI & Data Science, and Digital Marketing.", "Resources", roadmaps_body(), canonical="skill-roadmaps.html"))

GLOSSARY = [
    ("API", "A set way for two pieces of software to talk to each other."),
    ("Dataset", "A structured collection of data used for analysis or training a model."),
    ("SEO", "Search Engine Optimization — improving a site so it ranks higher in search results."),
    ("Machine Learning", "Teaching a computer to find patterns in data instead of coding every rule by hand."),
    ("CTR", "Click-Through Rate — the percentage of people who click an ad or link after seeing it."),
    ("Wireframe", "A simple, low-detail sketch of a screen layout used early in design."),
]
def glossary_body():
    items = "".join(f"""<div class="card"><h3>{term}</h3><p>{definition}</p></div>""" for term, definition in GLOSSARY)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Glossary</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Learning Glossary</div>
      <h1>Plain-English definitions</h1>
    </div>
    <div class="grid grid-3">{items}</div>
  </div>
</section>"""
write("glossary.html", page("Learning Glossary", "Plain-English definitions of terms used in Data Analytics, AI, Digital Marketing, and more.", "Resources", glossary_body(), canonical="glossary.html"))

INTERVIEW_TOPICS = [
    ("Data Analytics Interview Questions", "SQL joins, dashboard walkthroughs, and how to explain a project end-to-end."),
    ("AI & Data Science Interview Questions", "Core ML concepts, model evaluation, and explaining your capstone project."),
    ("Digital Marketing Interview Questions", "Campaign metrics, channel strategy, and case-study style questions."),
]
def interview_prep_body():
    cards = "".join(f"""<div class="card"><h3>{t}</h3><p>{d}</p></div>""" for t, d in INTERVIEW_TOPICS)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Interview Preparation</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Interview Preparation</div>
      <h1>Question banks and mock-interview frameworks</h1>
    </div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>"""
write("interview-prep.html", page("Interview Preparation", "Interview question banks and mock-interview frameworks for Data Analytics, AI & Data Science, and Digital Marketing.", "Resources", interview_prep_body(), canonical="interview-prep.html"))

TOOLS = [
    ("Google Sheets", "Free spreadsheet tool — great starting point before SQL/Power BI."),
    ("VS Code", "Free code editor used throughout the Python and Web Dev tracks."),
    ("Canva", "Free design tool useful for marketing creatives and social posts."),
    ("Figma", "Free-tier design tool used in the UI/UX track."),
]
def tools_body():
    cards = "".join(f"""<div class="card"><h3>{t}</h3><p>{d}</p></div>""" for t, d in TOOLS)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Tools</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Tools</div>
      <h1>Free and low-cost tools we recommend</h1>
    </div>
    <div class="grid grid-4">{cards}</div>
  </div>
</section>"""
write("tools.html", page("Tools", "Free and low-cost tools SmartVersa recommends across Data Analytics, Web Dev, Marketing, and UI/UX.", "Resources", tools_body(), canonical="tools.html"))

DOWNLOADS = [
    ("Resume Template (Entry-Level Tech)", "DOCX"),
    ("30-Day Learning Planner", "PDF"),
    ("SQL Cheat Sheet", "PDF"),
    ("SEO Audit Checklist", "PDF"),
]
def downloads_body():
    rows = "".join(f"""
      <div class="card" style="display:flex;justify-content:space-between;align-items:center;">
        <div><h3 style="margin-bottom:2px;">{name}</h3><p style="margin:0;font-size:.8rem;">{fmt} file</p></div>
        <a href="contact.html" class="btn btn-outline" style="padding:9px 16px;">Request</a>
      </div>""" for name, fmt in DOWNLOADS)
    return f"""
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Downloads</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Downloads</div>
      <h1>Templates, cheat sheets, and checklists</h1>
    </div>
    <div class="grid grid-2">{rows}</div>
  </div>
</section>"""
write("downloads.html", page("Downloads", "Free downloadable templates, cheat sheets, and checklists from SmartVersa.", "Resources", downloads_body(), canonical="downloads.html"))

# ============================================================
# LEGAL PAGES
# ============================================================
def legal_page(slug, title, body_html):
    body = f"""
<section class="section">
  <div class="container prose">
    <div class="eyebrow">Legal</div>
    <h1>{title}</h1>
    {body_html}
  </div>
</section>"""
    write(f"{slug}.html", page(title, f"SmartVersa {title.lower()}.", "", body, canonical=f"{slug}.html", extra_head='<meta name="robots" content="noindex">'))

legal_page("privacy-policy", "Privacy Policy", """
<p><em>Last updated: July 2026</em></p>
<p>This Privacy Policy explains how SmartVersa ("we", "us") collects, uses, and protects your personal information
when you use our website and enroll in our programs.</p>
<h2>Information We Collect</h2>
<ul>
  <li>Contact details you submit via our forms (name, email, phone number)</li>
  <li>Account details when you sign up (email, authentication credentials via our auth provider)</li>
  <li>Usage data collected through analytics tools</li>
</ul>
<h2>How We Use Your Information</h2>
<ul>
  <li>To respond to enrollment inquiries and provide program access</li>
  <li>To send relevant updates about your enrollment</li>
  <li>To improve our website and course offerings</li>
</ul>
<h2>Data Storage &amp; Security</h2>
<p>Form submissions and account data are stored securely through our backend provider. Passwords are never stored
in plain text. Access to student data is restricted to authorized SmartVersa staff.</p>
<h2>Your Rights</h2>
<p>You may request access to, correction of, or deletion of your personal data at any time by contacting
team@smartversa.in.</p>
<h2>Contact</h2>
<p>Questions about this policy can be sent to <a href="mailto:team@smartversa.in">team@smartversa.in</a>.</p>
""")

legal_page("terms", "Terms &amp; Conditions", """
<p><em>Last updated: July 2026</em></p>
<h2>Use of Our Services</h2>
<p>By enrolling in a SmartVersa program or using this website, you agree to these Terms &amp; Conditions.</p>
<h2>Enrollment</h2>
<p>Enrollment is confirmed upon successful application and payment where applicable. Seats per batch are limited
and allocated on a first-come basis.</p>
<h2>Course Access</h2>
<p>Enrolled students receive lifetime access to recorded course content and associated resources, subject to
continued availability of our hosting platform.</p>
<h2>Conduct</h2>
<p>Course materials are for personal learning use only and may not be redistributed, resold, or publicly
republished without written permission.</p>
<h2>Changes to Programs</h2>
<p>SmartVersa may update curriculum, mentors, or scheduling to improve program quality. Core learning outcomes will
remain consistent with what was advertised at the time of enrollment.</p>
<h2>Limitation of Liability</h2>
<p>SmartVersa provides career guidance and placement support but does not guarantee employment outcomes.</p>
<h2>Contact</h2>
<p>Questions about these terms can be sent to <a href="mailto:team@smartversa.in">team@smartversa.in</a>.</p>
""")

legal_page("refund-policy", "Refund Policy", """
<p><em>Last updated: July 2026</em></p>
<h2>Eligibility</h2>
<p>Refund requests are considered within 7 days of enrollment, provided less than 20% of the course content has
been accessed.</p>
<h2>How to Request a Refund</h2>
<p>Email <a href="mailto:team@smartversa.in">team@smartversa.in</a> with your registered email and reason for the
request. Our team will respond within 3 business days.</p>
<h2>Processing Time</h2>
<p>Approved refunds are processed to the original payment method within 7–10 business days.</p>
<h2>Non-Refundable Cases</h2>
<ul>
  <li>Requests made after the 7-day window</li>
  <li>Cases where more than 20% of course content has already been accessed</li>
  <li>Certificates already issued</li>
</ul>
""")

print("Resources hub, resource sub-pages, and legal pages generated.")
