#!/usr/bin/env python3
from build import (page, write, feature_cards, course_cards, testimonial_cards,
                    FEATURES, COURSES, TESTIMONIALS, FAQ_SCRIPT,
                    breadcrumb_schema, course_schema, faqpage_schema)

# ============================================================
# HOME
# ============================================================
home_body = f"""
<section class="hero">
  <div class="container">
    <div class="eyebrow">MSME Registered · Practical Online Learning</div>
    <h1>Learn Smart. Grow <span class="gold-text">Faster.</span></h1>
    <p class="lead">Mentor-led, project-based programs in AI &amp; Data Science, Digital Marketing, and more —
    built for Indian students who want real skills and a real portfolio, not another certificate that sits in a folder.</p>
    <div class="hero-cta">
      <a href="programs.html" class="btn btn-primary">Explore Programs</a>
      <a href="contact.html" class="btn btn-outline">Talk to Us</a>
    </div>
  </div>
  <div class="container trust-strip">
    <span class="trust-pill">MSME Registered</span>
    <span class="trust-pill">500+ Students Trained</span>
    <span class="trust-pill">Lifetime Access</span>
    <span class="trust-pill">Mentor Support</span>
    <span class="trust-pill">Certificate Included</span>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 44px;">
      <div class="eyebrow">Why SmartVersa</div>
      <h2>Built for people who want to <span class="gold-text">actually get hired</span></h2>
      <p>Every program is designed around one outcome: work you can show, and skills you can defend in an interview.</p>
    </div>
    <div class="grid grid-5">{feature_cards(FEATURES)}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 44px;">
      <div class="eyebrow">Pick Your Track</div>
      <h2>Programs built around real outcomes</h2>
    </div>
    <div class="grid grid-4">{course_cards(COURSES)}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 44px;">
      <div class="eyebrow">The Process</div>
      <h2>Your journey with us</h2>
    </div>
    <div class="steps">
      <div class="step"><div class="num">01</div><h4>Enroll</h4><p style="font-size:.85rem;">Pick a track and secure your seat.</p></div>
      <div class="step"><div class="num">02</div><h4>Learn</h4><p style="font-size:.85rem;">Go through recorded classes at your pace.</p></div>
      <div class="step"><div class="num">03</div><h4>Complete Projects</h4><p style="font-size:.85rem;">Apply what you learn to real assignments.</p></div>
      <div class="step"><div class="num">04</div><h4>Get Certificate</h4><p style="font-size:.85rem;">Receive your verifiable certificate.</p></div>
      <div class="step"><div class="num">05</div><h4>Become Job Ready</h4><p style="font-size:.85rem;">Resume, LinkedIn, and interview prep support.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt2">
  <div class="container stats-row">
    <div class="stat"><div class="num">500+</div><div class="label">Students Trained</div></div>
    <div class="stat"><div class="num">20+</div><div class="label">Mentor Sessions / Batch</div></div>
    <div class="stat"><div class="num">6</div><div class="label">Live Programs</div></div>
    <div class="stat"><div class="num">100%</div><div class="label">Recorded + Lifetime Access</div></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 44px;">
      <div class="eyebrow">Student Stories</div>
      <h2>What our students say</h2>
    </div>
    <div class="grid grid-3" id="testimonialGrid">{testimonial_cards(TESTIMONIALS[:6])}</div>
    <div class="show-more-wrap">
      <button class="btn btn-outline" id="showMoreBtn" onclick="document.getElementById('moreTestimonials').style.display='grid';this.style.display='none';">Show More Reviews</button>
    </div>
    <div class="grid grid-3" id="moreTestimonials" style="display:none;margin-top:22px;">{testimonial_cards(TESTIMONIALS[6:])}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 44px;">
      <div class="eyebrow">The Comparison</div>
      <h2>SmartVersa vs other platforms</h2>
    </div>
    <div class="table-scroll">
      <table class="compare-table">
        <tr><th>Feature</th><th>SmartVersa</th><th>Typical Video Platforms</th></tr>
        <tr><td>Mentor support</td><td class="yes">✓ Included</td><td class="no">✗ Rarely</td></tr>
        <tr><td>Live industry projects</td><td class="yes">✓ Yes</td><td class="no">✗ Toy exercises</td></tr>
        <tr><td>Resume &amp; LinkedIn help</td><td class="yes">✓ Included</td><td class="no">✗ Not offered</td></tr>
        <tr><td>Lifetime access</td><td class="yes">✓ Yes</td><td class="no">Often time-limited</td></tr>
        <tr><td>Certificate</td><td class="yes">✓ Free, included</td><td class="no">Often paid add-on</td></tr>
        <tr><td>Placement guidance</td><td class="yes">✓ Yes</td><td class="no">✗ Rarely</td></tr>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 30px;">
      <div class="eyebrow">Trust &amp; Safety</div>
      <h2>Why students trust SmartVersa</h2>
    </div>
    <div class="badges-strip">
      <div class="badge-item"><span class="dot">●</span> MSME Registered</div>
      <div class="badge-item"><span class="dot">●</span> Secure Payments</div>
      <div class="badge-item"><span class="dot">●</span> Lifetime Access</div>
      <div class="badge-item"><span class="dot">●</span> Mentor Support</div>
      <div class="badge-item"><span class="dot">●</span> Certificate Included</div>
      <div class="badge-item"><span class="dot">●</span> Industry Projects</div>
      <div class="badge-item"><span class="dot">●</span> Recorded Classes</div>
      <div class="badge-item"><span class="dot">●</span> Beginner Friendly</div>
    </div>
  </div>
</section>

<section class="section section--alt2" style="text-align:center;">
  <div class="container">
    <h2>Ready to build something real?</h2>
    <p style="max-width:520px;margin:0 auto 26px;">Seats are limited every batch to keep mentor support meaningful. Apply today.</p>
    <div class="hero-cta">
      <a href="programs.html" class="btn btn-primary">View All Programs</a>
      <a href="contact.html" class="btn btn-outline">Contact Us</a>
    </div>
  </div>
</section>
"""

write("index.html", page(
    "Home", "SmartVersa — practical, mentor-led online programs in AI & Data Science, Digital Marketing and more. MSME registered, lifetime access, free certificate.",
    "Home", home_body, canonical=""
))

# ============================================================
# ABOUT
# ============================================================
about_body = """
<section class="section">
  <div class="container prose">
    <div class="eyebrow">About Us</div>
    <h1>Built by two people who wanted the course <span class="gold-text">they never got</span></h1>
    <p>SmartVersa was founded by Vinay and Kusum with a simple frustration: most online courses are either too
    theoretical to be useful, or too expensive to be accessible. We started SmartVersa as an MSME-registered
    education platform to close that gap — practical, mentor-supported, project-based programs priced for students,
    not corporates.</p>

    <h2>Our Mission</h2>
    <p>To make industry-relevant skills — in AI &amp; Data Science, Digital Marketing, and beyond — accessible to
    every student willing to put in the work, regardless of their college or city.</p>

    <h2>MSME Registration</h2>
    <p>SmartVersa is registered as a Micro, Small &amp; Medium Enterprise (MSME) in India, reflecting our commitment
    to operating as a transparent, accountable business — not an anonymous course reseller.</p>

    <h2>Who's Behind SmartVersa</h2>
    <p><strong>Kusum</strong> — Co-founder, leads curriculum design and product for SmartVersa's technical
    programs. Background in Data Science &amp; Analytics with Python, machine learning, and data visualization,
    including IBM certifications in the field.</p>
    <p><strong>Vinay</strong> — Co-founder, leads business growth and operations for SmartVersa.</p>

    <h2>How We're Different</h2>
    <ul>
      <li>Every program includes real mentor sessions, not just pre-recorded videos.</li>
      <li>Assignments are built around real datasets and real campaigns, not toy examples.</li>
      <li>We help with the parts that actually get you hired: resume, LinkedIn, and interview prep.</li>
    </ul>

    <div style="text-align:center;margin-top:40px;">
      <a href="programs.html" class="btn btn-primary">Explore Our Programs</a>
    </div>
  </div>
</section>
"""
about_schema = breadcrumb_schema([("Home", ""), ("About Us", "about.html")])
write("about.html", page(
    "About Us", "Meet the founders of SmartVersa and learn about our mission to make practical, mentor-led education accessible to Indian students.",
    "About", about_body, canonical="about.html", schema=about_schema
))

# ============================================================
# PROGRAMS LISTING
# ============================================================
programs_body = f"""
<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 44px;">
      <div class="eyebrow">All Programs</div>
      <h1>Pick the track that fits where you want to go</h1>
      <p>Every program includes mentor support, real projects, and a free certificate on completion.</p>
    </div>
    <div class="grid grid-4">{course_cards(COURSES)}</div>
  </div>
</section>
"""
write("programs.html", page(
    "Programs", "Browse all SmartVersa programs: AI & Data Science, Python, Data Analytics, Digital Marketing, UI/UX, Web Development, and HR.",
    "Programs", programs_body, canonical="programs.html"
))

# ============================================================
# COURSE PAGE TEMPLATE
# ============================================================
def course_page(c):
    soon = c.get("soon", False)
    hero_cta = (
        f'<a href="contact.html" class="btn btn-primary">Join Waitlist</a>'
        if soon else
        f'<a href="contact.html" class="btn btn-primary">Apply Now — {c["price"]}</a>'
    )
    price_line = c["price"] if soon else f'{c["price"]} <span style="font-size:.9rem;color:var(--text-low);">/ {c["duration"]}</span>'
    curriculum_items = "".join(f"<li>{b}</li>" for b in c["bullets"])

    weeks = []
    n_weeks = 4 if soon else int(c["duration"].split()[0])
    for i in range(1, min(n_weeks, 8) + 1):
        weeks.append(f"""
        <div class="week-item">
          <h4>Week {i}</h4>
          <p style="font-size:.88rem;margin:0;">Core concepts, guided practice, and a hands-on task for week {i} of the {c['name']} track.</p>
        </div>""")

    related = [x for x in COURSES if x["slug"] != c["slug"]][:3]
    related_html = course_cards(related)

    soon_banner = f"""
    <div class="card" style="margin-bottom:32px;text-align:center;">
      <p style="margin:0;color:var(--gold-2);">🚀 This program is launching soon. Join the waitlist to get early-bird pricing and be first to know when seats open.</p>
    </div>""" if soon else ""

    body = f"""
<section class="section" style="padding-top:52px;">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / <a href="programs.html">Programs</a> / {c['name']}</div>
    <div class="eyebrow">{"Launching Soon" if soon else "Program"}</div>
    <h1>{c['name']}</h1>
    <p class="lead" style="max-width:640px;">{c['blurb']}</p>
    <div class="price" style="font-family:var(--font-display);font-size:1.8rem;color:var(--gold-2);margin-bottom:20px;">{price_line}</div>
    <div class="hero-cta" style="justify-content:flex-start;">
      {hero_cta}
      <a href="contact.html" class="btn btn-outline">Ask a Question</a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    {soon_banner}
    <h2>What you'll learn</h2>
    <ul style="color:var(--text-mid);max-width:640px;">{curriculum_items}</ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Week-by-week roadmap</h2>
    <div style="max-width:640px;">{''.join(weeks)}</div>
  </div>
</section>

<section class="section section--alt2">
  <div class="container grid grid-2">
    <div>
      <h2>Who can apply</h2>
      <p>Open to students and early professionals with no prior experience required — we start from the basics and
      build up. A laptop and consistent weekly time (4–6 hours) are all you need.</p>
    </div>
    <div>
      <h2>Career outcomes</h2>
      <p>Graduates leave with a portfolio project, a rewritten resume and LinkedIn profile, and interview practice
      specific to roles in this track.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container prose" style="text-align:center;">
    <h2>Certificate</h2>
    <p>On completing all assignments, you receive a free, verifiable SmartVersa certificate of completion.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <h2 style="text-align:center;">Frequently asked questions</h2>
    <div style="max-width:700px;margin:0 auto;">
      <div class="faq-item"><div class="faq-q">Do I need prior experience?<span class="chev">▾</span></div><div class="faq-a"><p>No — this program is built to start from zero and build up with weekly guided practice.</p></div></div>
      <div class="faq-item"><div class="faq-q">Is the certificate recognized?<span class="chev">▾</span></div><div class="faq-a"><p>You receive a verifiable SmartVersa certificate on completion, included at no extra cost.</p></div></div>
      <div class="faq-item"><div class="faq-q">What if I miss a live mentor session?<span class="chev">▾</span></div><div class="faq-a"><p>All sessions are recorded, and you get lifetime access to rewatch them anytime.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="text-align:center;">Related programs</h2>
    <div class="grid grid-3">{related_html}</div>
  </div>
</section>

<section class="section section--alt2" style="text-align:center;">
  <div class="container">
    <h2>{"Join the waitlist" if soon else f"Ready to start {c['name']}?"}</h2>
    <div class="hero-cta">{hero_cta}</div>
  </div>
</section>
{FAQ_SCRIPT}
"""
    course_faq = [
        ("Do I need prior experience?", "No, this program is built to start from zero and build up with weekly guided practice."),
        ("Is the certificate recognized?", "You receive a verifiable SmartVersa certificate on completion, included at no extra cost."),
        ("What if I miss a live mentor session?", "All sessions are recorded, and you get lifetime access to rewatch them anytime."),
    ]
    page_schema = "\n".join([
        breadcrumb_schema([("Home", ""), ("Programs", "programs.html"), (c["name"].replace("&amp;", "&"), f"{c['slug']}.html")]),
        course_schema(c["name"].replace("&amp;", "&"), c["blurb"], c["price"], c["slug"]),
        faqpage_schema(course_faq),
    ])
    write(f"{c['slug']}.html", page(
        c["name"].replace("&amp;", "&"),
        f"{c['blurb']} Mentor-led, project-based, MSME-registered SmartVersa program.",
        "Programs", body, canonical=f"{c['slug']}.html", schema=page_schema
    ))

for c in COURSES:
    course_page(c)

print("Home, About, Programs, and all course pages generated.")
