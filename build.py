#!/usr/bin/env python3
"""Generates the static SmartVersa site skeleton. Run: python3 build.py"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = ROOT  # pages live at repo root for GitHub Pages

LOGO_SVG = '<img src="assets/logo-icon-gold.png" alt="SmartVersa shield logo" style="height:36px;width:auto;">'

# Official-style social icons (simple line-mark glyphs), themed gold, used to link out to profiles
SOCIAL_ICONS = {
    "linkedin": """<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M4.98 3.5C4.98 4.88 3.88 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.22 8.24h4.56V23H.22V8.24zM8.1 8.24h4.37v2.01h.06c.61-1.15 2.1-2.37 4.33-2.37 4.63 0 5.48 3.05 5.48 7.01V23h-4.56v-6.99c0-1.67-.03-3.81-2.32-3.81-2.33 0-2.69 1.82-2.69 3.7V23H8.1V8.24z"/></svg>""",
    "facebook": """<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5.02 3.66 9.18 8.44 9.94v-7.03H7.9v-2.91h2.54V9.85c0-2.5 1.49-3.89 3.77-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.91h-2.34V22c4.78-.76 8.44-4.92 8.44-9.94z"/></svg>""",
    "instagram": """<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2.5" y="2.5" width="19" height="19" rx="5"/><circle cx="12" cy="12" r="4.3"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg>""",
    "whatsapp": """<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.79.47 3.47 1.28 4.93L2 22l5.32-1.39a9.9 9.9 0 0 0 4.72 1.2h.01c5.46 0 9.9-4.45 9.9-9.9C21.96 6.45 17.5 2 12.04 2zm0 18.09h-.01a8.2 8.2 0 0 1-4.18-1.14l-.3-.18-3.16.83.84-3.08-.19-.32a8.18 8.18 0 0 1-1.25-4.29c0-4.53 3.69-8.22 8.24-8.22 2.2 0 4.27.86 5.82 2.42a8.16 8.16 0 0 1 2.41 5.81c0 4.54-3.69 8.17-8.22 8.17zm4.51-6.13c-.25-.12-1.47-.72-1.7-.81-.23-.08-.39-.12-.56.13-.17.25-.64.81-.78.97-.14.17-.29.19-.53.06-.25-.12-1.04-.38-1.99-1.22-.73-.65-1.23-1.46-1.37-1.71-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.14.16-.25.25-.41.08-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.48-.41-.42-.56-.42-.14-.01-.31-.01-.48-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.08 0 1.22.89 2.4 1.02 2.57.12.17 1.75 2.67 4.24 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.08.14-1.18-.06-.11-.23-.17-.48-.29z"/></svg>""",
}

NAV_LINKS = [
    ("Home", "index.html"),
    ("Programs", "programs.html"),
    ("About", "about.html"),
    ("Resources", "resources.html"),
    ("FAQ", "faq.html"),
    ("Contact", "contact.html"),
]

def nav(active=""):
    links = "\n".join(
        f'<a href="{href}"{" style=\"color:var(--gold-2)\"" if label==active else ""}>{label}</a>'
        for label, href in NAV_LINKS
    )
    mobile_links = "\n".join(f'<a href="{href}">{label}</a>' for label, href in NAV_LINKS)
    return f"""
<nav class="navbar">
  <div class="container">
    <a href="index.html" class="brand">{LOGO_SVG}<span>SMART <span class="gold-text">VERSA</span></span></a>
    <div class="nav-links">{links}</div>
    <div class="nav-cta">
      <a href="login.html" class="btn btn-outline" style="padding:9px 18px;">Login</a>
      <a href="contact.html" class="btn btn-primary" style="padding:9px 18px;">Apply Now</a>
    </div>
    <button class="hamburger" onclick="document.getElementById('mobileMenu').classList.toggle('open')" aria-label="Menu">☰</button>
  </div>
  <div class="mobile-menu" id="mobileMenu">
    {mobile_links}
    <a href="login.html">Login</a>
    <a href="contact.html" class="btn btn-primary" style="margin-top:10px;text-align:center;">Apply Now</a>
  </div>
</nav>"""

FOOTER = f"""
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="index.html" class="brand">{LOGO_SVG}<span>SMART <span class="gold-text">VERSA</span></span></a>
        <p style="margin-top:14px;">Learn Smart. Grow Faster. Practical, mentor-led online programs in AI &amp; Data Science, Digital Marketing, and more — built for Indian students who want real, job-ready skills.</p>
        <div class="social-row">
          <a href="#" aria-label="LinkedIn">{SOCIAL_ICONS['linkedin']}</a>
          <a href="#" aria-label="Facebook">{SOCIAL_ICONS['facebook']}</a>
          <a href="#" aria-label="Instagram">{SOCIAL_ICONS['instagram']}</a>
          <a href="https://wa.me/919306539879" aria-label="WhatsApp">{SOCIAL_ICONS['whatsapp']}</a>
        </div>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="programs.html">All Programs</a></li>
          <li><a href="blog.html">Blog</a></li>
          <li><a href="case-studies.html">Case Studies</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Courses</h4>
        <ul>
          <li><a href="course-ai-data-science.html">AI &amp; Data Science</a></li>
          <li><a href="course-python.html">Python Programming</a></li>
          <li><a href="course-data-analytics.html">Data Analytics</a></li>
          <li><a href="course-digital-marketing.html">Digital Marketing</a></li>
          <li><a href="course-uiux.html">UI/UX Design</a></li>
          <li><a href="course-webdev.html">Web Development</a></li>
          <li><a href="course-hr.html">HR Course</a></li>
        </ul>
      </div>
      <div>
        <h4>Support</h4>
        <ul>
          <li><a href="mailto:team@smartversa.in">team@smartversa.in</a></li>
          <li><a href="tel:+919306539879">+91 93065 39879</a></li>
          <li><a href="https://wa.me/919306539879">WhatsApp Us</a></li>
          <li><a href="support.html">Raise a Support Ticket</a></li>
          <li><a href="ai-mentor.html">AI Mentor</a></li>
          <li><a href="certificate-verification.html">Verify a Certificate</a></li>
          <li>Support hours: 9 AM – 8 PM</li>
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="privacy-policy.html">Privacy Policy</a></li>
          <li><a href="terms.html">Terms &amp; Conditions</a></li>
          <li><a href="refund-policy.html">Refund Policy</a></li>
          <li><a href="cancellation-policy.html">Cancellation Policy</a></li>
          <li><a href="internship-agreement.html">Internship Agreement</a></li>
          <li><a href="certificate-verification.html">Certificate Verification Policy</a></li>
          <li><a href="disclaimer.html">Disclaimer</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 SmartVersa. MSME Registered. All rights reserved.</div>
      <div>
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms.html">Terms &amp; Conditions</a>
        <a href="disclaimer.html">Disclaimer</a>
      </div>
    </div>
  </div>
</footer>
<div class="mobile-sticky">
  <a href="tel:+919306539879" class="call">📞 Call</a>
  <a href="https://wa.me/919306539879" class="wa">💬 WhatsApp</a>
  <a href="contact.html" class="apply">Apply Now</a>
</div>
<a href="https://wa.me/919306539879" class="floating-wa">💬</a>
"""

HEAD_TAIL = """
<meta name="google-site-verification" content="E3SW3D3uMtXXo7o4abZ7pyE-CGt5ZZI89i-NgZmnV2M">
<link rel="icon" type="image/x-icon" href="assets/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/favicon-180.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/favicon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-C5MPGJYCT5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-C5MPGJYCT5');
</script>
"""

# Real Firebase config (from the SmartVersa Firebase console) — shared across pages that need Auth/Firestore.
FIREBASE_CONFIG_JS = """const firebaseConfig = {
  apiKey: "AIzaSyC9Ix2P-UGwwqZTBZVv2LpXVv60gEWi_LM",
  authDomain: "smartversa-deac8.firebaseapp.com",
  projectId: "smartversa-deac8",
  storageBucket: "smartversa-deac8.firebasestorage.app",
  messagingSenderId: "995974015593",
  appId: "1:995974015593:web:5ef1cbcbd8238cb39410f8",
  measurementId: "G-E6242NLGVF"
};"""

ORG_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "SmartVersa",
  "alternateName": "Smart Versa",
  "url": "https://smartversa.in/",
  "logo": "https://smartversa.in/assets/logo-full-gold.png",
  "description": "SmartVersa is an MSME-registered online education platform offering practical, mentor-led courses in AI & Data Science, Python, Data Analytics, Digital Marketing, UI/UX Design, Web Development, and HR.",
  "founders": [
    {"@type": "Person", "name": "Vinay"},
    {"@type": "Person", "name": "Kusum"}
  ],
  "areaServed": "IN",
  "sameAs": [],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+91-93065-39879",
    "email": "team@smartversa.in",
    "contactType": "customer service",
    "areaServed": "IN",
    "availableLanguage": ["English", "Hindi"]
  }
}
</script>"""

def breadcrumb_schema(items):
    """items: list of (name, url) tuples in order from Home to current page."""
    entries = ",\n".join(
        f'    {{"@type":"ListItem","position":{i+1},"name":"{name}","item":"https://smartversa.in/{url}"}}'
        for i, (name, url) in enumerate(items)
    )
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
{entries}
  ]
}}
</script>"""

def course_schema(name_plain, description, price, slug):
    price_num = "0"
    is_free_or_soon = "Launching" in price
    price_clean = "0" if is_free_or_soon else price.replace("₹","").replace(",","")
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "{name_plain}",
  "description": "{description}",
  "provider": {{
    "@type": "EducationalOrganization",
    "name": "SmartVersa",
    "sameAs": "https://smartversa.in/"
  }},
  "url": "https://smartversa.in/{slug}.html",
  "offers": {{
    "@type": "Offer",
    "category": "Paid",
    "priceCurrency": "INR",
    "price": "{price_clean}",
    "availability": "https://schema.org/InStock"
  }}
}}
</script>"""

def faqpage_schema(qa_pairs):
    entries = ",\n".join(
        f'''    {{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'''
        for q, a in qa_pairs
    )
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{entries}
  ]
}}
</script>"""

def page(title, description, active, body, extra_head="", canonical="", schema=""):
    canonical_tag = f'<link rel="canonical" href="https://smartversa.in/{canonical}">' if canonical else ""
    schema_block = ORG_SCHEMA + ("\n" + schema if schema else "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | SmartVersa</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title} | SmartVersa">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
{canonical_tag}
{HEAD_TAIL}
{extra_head}
{schema_block}
</head>
<body>
{nav(active)}
{body}
{FOOTER}
</body>
</html>"""

def write(filename, html):
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

# ============================================================
# Reusable content blocks
# ============================================================

FEATURES = [
    ("💼", "Live Industry Projects", "Work on real, portfolio-ready projects, not toy exercises."),
    ("🧑‍🏫", "Mentor Support", "1:1 and group mentorship from working professionals."),
    ("📄", "Job-Ready Resume Help", "We help you turn your project work into a resume that gets shortlisted."),
    ("🔗", "LinkedIn Optimization", "A profile audit and rewrite so recruiters actually find you."),
    ("🎤", "Interview Preparation", "Mock interviews and question banks specific to your track."),
    ("📝", "Practical Assignments", "Weekly hands-on tasks that build toward your final project."),
    ("♾️", "Lifetime Access", "Revisit every recording and resource for as long as you need."),
    ("🎥", "Recorded Classes", "Learn at your own pace — pause, rewind, rewatch."),
    ("🏅", "Free Certificate", "A verifiable certificate of completion, included at no extra cost."),
    ("🚀", "Placement Guidance", "Referrals, application strategy, and outreach templates."),
]

COURSES = [
    dict(slug="course-ai-data-science", name="AI &amp; Data Science", price="₹1,299", duration="6 Weeks",
         seats="12 seats left", blurb="Python, statistics, ML fundamentals and a capstone project.",
         bullets=["Python &amp; Pandas foundations", "Statistics for Data Science", "ML models &amp; capstone project"]),
    dict(slug="course-python", name="Python Programming", price="₹999", duration="4 Weeks",
         seats="18 seats left", blurb="Core Python from fundamentals to real automation scripts.",
         bullets=["Syntax, data structures, OOP", "File handling &amp; automation", "Mini-projects each week"]),
    dict(slug="course-data-analytics", name="Data Analytics", price="₹1,499", duration="6 Weeks",
         seats="10 seats left", blurb="Excel, SQL, and dashboarding for real business questions.",
         bullets=["Excel &amp; SQL for analytics", "Dashboards in Power BI", "Real dataset case studies"]),
    dict(slug="course-digital-marketing", name="Digital Marketing", price="₹4,999", duration="8 Weeks",
         seats="15 seats left", blurb="SEO, paid ads, content, and analytics — run a real campaign.",
         bullets=["SEO &amp; content strategy", "Meta &amp; Google Ads basics", "Run a live campaign"]),
    dict(slug="course-uiux", name="UI/UX Design", price="Launching Soon", duration="6 Weeks",
         seats="Waitlist open", blurb="Design thinking, wireframes, and a portfolio-ready case study.",
         bullets=["Design thinking &amp; research", "Wireframes to hi-fi in Figma", "Portfolio case study"], soon=True),
    dict(slug="course-webdev", name="Web Development", price="Launching Soon", duration="8 Weeks",
         seats="Waitlist open", blurb="HTML, CSS, JS and a deployed full-stack project.",
         bullets=["HTML, CSS, JavaScript", "Frontend framework basics", "Deployed capstone project"], soon=True),
    dict(slug="course-hr", name="HR Course", price="Launching Soon", duration="6 Weeks",
         seats="Waitlist open", blurb="Recruitment, HR operations, and people-management basics.",
         bullets=["Recruitment &amp; onboarding", "HR operations &amp; compliance", "People-management basics"], soon=True),
]

TESTIMONIALS = [
    ("Ananya Sharma", "Kurukshetra University · AI & Data Science", "The mentor sessions made the difference — I could actually ask 'why' and get a real answer, not just a video reply.", 5),
    ("Rohit Malik", "GJU Hisar · Digital Marketing", "Ran my first real ad campaign in week 5. That's the part no free YouTube course gives you.", 5),
    ("Priya Yadav", "Chaudhary Devi Lal University · AI & Data Science", "Recorded classes meant I could keep up with college exams and still finish every module.", 4),
    ("Karan Sethi", "Guru Jambheshwar University · Data Analytics", "The dashboard project is genuinely on my resume now — recruiters ask about it in every interview.", 5),
    ("Simran Kaur", "Punjab University · Digital Marketing", "Lifetime access is underrated. I went back to the SEO module three months after finishing.", 5),
    ("Vikas Chaudhary", "Hisar Polytechnic · AI & Data Science", "Straightforward, practical, no fluff. Exactly what I needed alongside my final year project.", 4),
    ("Neha Rathi", "IGNOU · Digital Marketing", "Got my LinkedIn profile rewritten as part of the course — started getting recruiter messages within two weeks.", 5),
    ("Deepak Sharma", "MDU Rohtak · AI & Data Science", "Small enough batches that the mentor actually knew my project by name.", 5),
    ("Anjali Devi", "CDLU Sirsa · Data Analytics", "Went from not knowing what SQL was to writing joins confidently in six weeks.", 4),
]

def stars(n):
    return "★" * n + "☆" * (5 - n)

def testimonial_cards(items):
    out = []
    for name, college, quote, rating in items:
        out.append(f"""
      <div class="card testimonial">
        <div class="stars">{stars(rating)}</div>
        <p class="quote">"{quote}"</p>
        <div class="who">{name}</div>
        <div class="college">{college}</div>
      </div>""")
    return "".join(out)

def feature_cards(items):
    out = []
    for icon, title, desc in items:
        out.append(f"""
      <div class="card">
        <div class="icon">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>""")
    return "".join(out)

def course_cards(items):
    out = []
    for c in items:
        bullets = "".join(f"<li>{b}</li>" for b in c["bullets"])
        price_html = (f'{c["price"]}' if c.get("soon") else f'{c["price"]} <span>/ {c["duration"]}</span>')
        soon_badge = '<span class="soon-badge">Soon</span>' if c.get("soon") else ""
        out.append(f"""
      <div class="course-card">
        <div class="cc-top">
          <h3 style="margin:0;">{c["name"]}{soon_badge}</h3>
          <span class="seats-badge">{c["seats"]}</span>
        </div>
        <div class="cc-body">
          <p style="font-size:.88rem;">{c["blurb"]}</p>
          <div class="price">{price_html}</div>
          <ul>{bullets}</ul>
          <a href="{c["slug"]}.html" class="btn btn-outline btn-block cc-cta">View Details</a>
        </div>
      </div>""")
    return "".join(out)

FAQ_SCRIPT = """
<script>
document.querySelectorAll('.faq-q').forEach(q => {
  q.addEventListener('click', () => q.parentElement.classList.toggle('open'));
});
</script>"""

print("build.py loaded — see build_pages.py for page generation")
