#!/usr/bin/env python3
from build import page, write, breadcrumb_schema, FIREBASE_CONFIG_JS

def legal_page(slug, title, body_html, breadcrumb_name=None):
    bc = breadcrumb_schema([("Home", ""), (breadcrumb_name or title, f"{slug}.html")])
    body = f"""
<section class="section">
  <div class="container prose">
    <div class="breadcrumb"><a href="index.html">Home</a> / {breadcrumb_name or title}</div>
    <div class="eyebrow">Legal</div>
    <h1>{title}</h1>
    {body_html}
  </div>
</section>"""
    write(f"{slug}.html", page(
        title, f"SmartVersa {title.lower()} — read the full terms.", "", body,
        canonical=f"{slug}.html", extra_head='<meta name="robots" content="noindex">', schema=bc
    ))

# ============================================================
# CANCELLATION POLICY
# ============================================================
legal_page("cancellation-policy", "Cancellation Policy", """
<p><em>Last updated: July 2026</em></p>
<p>This Cancellation Policy explains how you can cancel an enrollment before or shortly after a batch begins,
and is separate from our <a href="refund-policy.html">Refund Policy</a>, which governs money-back eligibility.</p>
<h2>Cancelling Before a Batch Starts</h2>
<p>You may cancel your enrollment any time before your batch's start date by emailing
<a href="mailto:team@smartversa.in">team@smartversa.in</a> with your registered email and course name. Your seat
will be released and a refund will be processed per our Refund Policy.</p>
<h2>Cancelling After a Batch Starts</h2>
<p>Cancellations within 7 days of the batch start date, and before more than 20% of the content has been accessed,
are accepted. Beyond this window, see our Refund Policy for eligibility.</p>
<h2>Batch Rescheduling by SmartVersa</h2>
<p>If SmartVersa reschedules or cancels a batch, affected students will be offered a seat in the next available
batch or a full refund, their choice.</p>
<h2>How to Cancel</h2>
<ul>
  <li>Email <a href="mailto:team@smartversa.in">team@smartversa.in</a> or message us on
  <a href="https://wa.me/919306539879">WhatsApp</a> with your registered email and course name</li>
  <li>You'll receive confirmation within 2 business days</li>
</ul>
""")

# ============================================================
# INTERNSHIP AGREEMENT
# ============================================================
legal_page("internship-agreement", "Internship Agreement", """
<p><em>Last updated: July 2026</em></p>
<p>This Internship Agreement applies to students who undertake an internship component as part of a SmartVersa
program or as a separate arrangement with SmartVersa.</p>
<h2>Scope of the Internship</h2>
<p>The internship is a learning-focused engagement intended to give the intern practical, supervised experience.
Specific duration, project scope, and mentor assignment will be confirmed in writing (email) before the internship
begins.</p>
<h2>Intern Responsibilities</h2>
<ul>
  <li>Complete assigned tasks within agreed timelines</li>
  <li>Maintain confidentiality of any non-public business information shared during the internship</li>
  <li>Communicate promptly with your assigned mentor regarding progress or blockers</li>
</ul>
<h2>SmartVersa's Responsibilities</h2>
<ul>
  <li>Provide mentor guidance and clear task scope</li>
  <li>Issue a certificate/letter of completion where the internship is successfully completed</li>
</ul>
<h2>Intellectual Property</h2>
<p>Unless otherwise agreed in writing, work products created solely for internal SmartVersa use during the
internship remain SmartVersa's property; personal portfolio pieces built primarily for the intern's own learning
remain the intern's own work, subject to written confirmation from SmartVersa.</p>
<h2>Stipend / Compensation</h2>
<p>Where applicable, stipend terms (if any) will be specified separately in writing and are not implied by this
Agreement alone.</p>
<h2>Termination</h2>
<p>Either party may end the internship early with written notice, in which case any certificate issued will
reflect the actual duration completed.</p>
<h2>Contact</h2>
<p>Questions about internship terms can be sent to <a href="mailto:team@smartversa.in">team@smartversa.in</a>.</p>
""")

# ============================================================
# DISCLAIMER
# ============================================================
legal_page("disclaimer", "Disclaimer", """
<p><em>Last updated: July 2026</em></p>
<h2>Educational Purpose</h2>
<p>All content on this website and within SmartVersa programs is provided for educational purposes. While we aim
for accuracy and currency, technology, tools, and best practices in fields like AI, marketing, and web development
change quickly — always verify critical details against current, authoritative sources before making
professional decisions based on course content.</p>
<h2>No Guarantee of Outcomes</h2>
<p>SmartVersa provides placement guidance, resume support, and interview preparation, but does not guarantee
employment, income, or specific career outcomes. Results depend on individual effort, market conditions, and
factors outside our control.</p>
<h2>Third-Party Tools and Links</h2>
<p>Course material may reference third-party tools, platforms, or websites (e.g. Google Sheets, Figma, Canva).
SmartVersa is not responsible for the availability, pricing, or policies of these third-party services.</p>
<h2>Testimonials</h2>
<p>Student testimonials reflect individual experiences and are not a guarantee that others will have the same
results.</p>
<h2>Limitation of Liability</h2>
<p>To the fullest extent permitted by law, SmartVersa is not liable for indirect or consequential losses arising
from use of this website or enrollment in our programs.</p>
<h2>Contact</h2>
<p>Questions about this disclaimer can be sent to <a href="mailto:team@smartversa.in">team@smartversa.in</a>.</p>
""")

# ============================================================
# CERTIFICATE VERIFICATION (policy + lookup tool)
# ============================================================
cert_bc = breadcrumb_schema([("Home", ""), ("Certificate Verification", "certificate-verification.html")])
cert_body = """
<section class="section">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / Certificate Verification</div>
    <div style="text-align:center;max-width:640px;margin:0 auto 36px;">
      <div class="eyebrow">Verify a Certificate</div>
      <h1>Certificate Verification</h1>
      <p>Employers and institutions can confirm whether a SmartVersa certificate is genuine by entering the
      certificate ID below.</p>
    </div>

    <div class="form-shell" style="margin-bottom:60px;">
      <form id="verifyForm">
        <label for="certId">Certificate ID</label>
        <input type="text" id="certId" placeholder="e.g. SV-2026-AIDS-0342" required>
        <button type="submit" class="btn btn-primary btn-block" style="margin-top:18px;">Verify Certificate</button>
        <div class="form-msg" id="verifyMsg"></div>
      </form>
    </div>

    <div class="prose">
      <h2>Certificate Verification Policy</h2>
      <p><em>Last updated: July 2026</em></p>
      <h3>Issuance</h3>
      <p>Certificates are issued only on successful completion of all required assignments and the final project
      for a given program. Each certificate carries a unique Certificate ID.</p>
      <h3>Verification</h3>
      <p>Anyone — students, employers, or institutions — can verify a certificate's authenticity using the tool
      above by entering the Certificate ID exactly as printed. A valid match will show the student's name (as
      registered), program name, and completion date.</p>
      <h3>Invalid or Not Found Results</h3>
      <p>If a Certificate ID doesn't match our records, it may be mistyped, revoked, or not genuine. Contact
      <a href="mailto:team@smartversa.in">team@smartversa.in</a> for manual verification support.</p>
      <h3>Revocation</h3>
      <p>SmartVersa reserves the right to revoke a certificate found to have been obtained through plagiarism,
      fraud, or violation of our Terms &amp; Conditions.</p>
      <h3>Data Shown</h3>
      <p>Only the minimum information needed to confirm authenticity (name, program, completion date, status) is
      shown to verifiers — no contact details or private student data are displayed.</p>
    </div>
  </div>
</section>

<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

  __FIREBASE_CONFIG__
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);

  const form = document.getElementById('verifyForm');
  const msg = document.getElementById('verifyMsg');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = document.getElementById('certId').value.trim();
    try {
      const snap = await getDoc(doc(db, "certificates", id));
      if (snap.exists()) {
        const d = snap.data();
        msg.textContent = `Valid certificate — ${d.name || 'Student'}, ${d.program || 'Program'}, completed ${d.completionDate || ''}.`;
        msg.className = "form-msg success";
      } else {
        msg.textContent = "No certificate found with that ID. Double-check it, or contact support for manual verification.";
        msg.className = "form-msg error";
      }
    } catch (err) {
      console.error(err);
      msg.textContent = "Couldn't complete verification. Please try again or contact support.";
      msg.className = "form-msg error";
    }
  });
</script>
"""
cert_body = cert_body.replace("__FIREBASE_CONFIG__", FIREBASE_CONFIG_JS)
write("certificate-verification.html", page(
    "Certificate Verification", "Verify the authenticity of a SmartVersa certificate using its Certificate ID, and read our certificate verification policy.",
    "", cert_body, canonical="certificate-verification.html", schema=cert_bc
))

# ============================================================
# SUPPORT / TICKET SYSTEM
# ============================================================
support_bc = breadcrumb_schema([("Home", ""), ("Support", "support.html")])
support_body = """
<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Support</div>
      <h1>Raise a Support Ticket</h1>
      <p>Describe your issue and we'll get back to you by email. You'll receive a ticket ID to track your request.</p>
    </div>

    <div class="grid grid-2" style="align-items:start;">
      <div class="form-shell">
        <form id="ticketForm">
          <label for="tName">Full Name</label>
          <input type="text" id="tName" required>

          <label for="tEmail">Email</label>
          <input type="email" id="tEmail" required>

          <label for="tCategory">Category</label>
          <select id="tCategory" required>
            <option value="">Select a category</option>
            <option>Enrollment / Payment</option>
            <option>Course Access</option>
            <option>Certificate</option>
            <option>Technical Issue</option>
            <option>Refund / Cancellation</option>
            <option>Other</option>
          </select>

          <label for="tPriority">Priority</label>
          <select id="tPriority">
            <option>Low</option>
            <option selected>Normal</option>
            <option>High</option>
          </select>

          <label for="tMessage">Describe the issue</label>
          <textarea id="tMessage" rows="5" required></textarea>

          <button type="submit" class="btn btn-primary btn-block" style="margin-top:20px;">Submit Ticket</button>
          <div class="form-msg" id="ticketMsg"></div>
          <p class="form-note">Typical first response time: within 1 business day, 9 AM – 8 PM.</p>
        </form>
      </div>
      <div>
        <div class="card" style="margin-bottom:18px;">
          <h3>Check Ticket Status</h3>
          <p style="margin-bottom:12px;">Have a ticket ID already? Enter it to check status.</p>
          <input type="text" id="ticketLookup" placeholder="e.g. SV-TCK-00231" style="margin-bottom:10px;">
          <button class="btn btn-outline btn-block" id="lookupBtn">Check Status</button>
          <p class="form-msg" id="lookupMsg" style="margin-top:12px;"></p>
        </div>
        <div class="card">
          <h3>Prefer to talk directly?</h3>
          <p><a href="https://wa.me/919306539879">WhatsApp us</a> or call
          <a href="tel:+919306539879">+91 93065 39879</a>, 9 AM – 8 PM.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import { getFirestore, doc, setDoc, getDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

  __FIREBASE_CONFIG__
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);

  function genTicketId() {
    // Public read access is granted by exact ID (see firestore.rules), so this must be
    // hard to brute-force — 12 random alphanumeric chars via crypto, not a 5-digit number.
    const bytes = new Uint8Array(9);
    crypto.getRandomValues(bytes);
    const b64 = btoa(String.fromCharCode(...bytes)).replace(/[+/=]/g, '').slice(0, 12).toUpperCase();
    return "SV-TCK-" + b64;
  }

  const form = document.getElementById('ticketForm');
  const msg = document.getElementById('ticketMsg');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const ticketId = genTicketId();
    const data = {
      ticketId,
      name: document.getElementById('tName').value,
      email: document.getElementById('tEmail').value,
      category: document.getElementById('tCategory').value,
      priority: document.getElementById('tPriority').value,
      message: document.getElementById('tMessage').value,
      status: "open",
      createdAt: serverTimestamp(),
    };
    try {
      await setDoc(doc(db, "tickets", ticketId), data);
      msg.textContent = `Ticket submitted! Your ticket ID is ${ticketId} — save this to check status later.`;
      msg.className = "form-msg success";
      form.reset();
    } catch (err) {
      console.error(err);
      msg.textContent = "Couldn't submit ticket. Please try WhatsApp instead.";
      msg.className = "form-msg error";
    }
  });

  document.getElementById('lookupBtn').addEventListener('click', async () => {
    const id = document.getElementById('ticketLookup').value.trim();
    const lookupMsg = document.getElementById('lookupMsg');
    if (!id) { lookupMsg.textContent = "Enter a ticket ID first."; lookupMsg.className = "form-msg error"; return; }
    try {
      const snap = await getDoc(doc(db, "tickets", id));
      if (snap.exists()) {
        const d = snap.data();
        lookupMsg.textContent = `Status: ${d.status || 'open'} — category: ${d.category || 'N/A'}.`;
        lookupMsg.className = "form-msg success";
      } else {
        lookupMsg.textContent = "No ticket found with that ID. Check it and try again.";
        lookupMsg.className = "form-msg error";
      }
    } catch (err) {
      console.error(err);
      lookupMsg.textContent = "Couldn't look up that ticket.";
      lookupMsg.className = "form-msg error";
    }
  });
</script>
"""
support_body = support_body.replace("__FIREBASE_CONFIG__", FIREBASE_CONFIG_JS)
write("support.html", page(
    "Support", "Raise a SmartVersa support ticket or check the status of an existing one.",
    "", support_body, canonical="support.html", schema=support_bc
))

# ============================================================
# AI MENTOR
# ============================================================
mentor_bc = breadcrumb_schema([("Home", ""), ("AI Mentor", "ai-mentor.html")])
mentor_body = """
<section class="hero">
  <div class="container">
    <div class="eyebrow">AI Mentor</div>
    <h1>Ask questions, anytime — <span class="gold-text">on WhatsApp</span></h1>
    <p class="lead">SmartVersa's AI Mentor is a WhatsApp-based assistant that helps you pick the right program,
    answers common curriculum questions, and connects you to a human counsellor when you need one.</p>
    <div class="hero-cta">
      <a href="https://wa.me/919306539879?text=Hi%2C%20I%27d%20like%20to%20talk%20to%20the%20SmartVersa%20AI%20Mentor" class="btn btn-primary">Chat on WhatsApp</a>
      <a href="contact.html" class="btn btn-outline">Talk to a Human Instead</a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container grid grid-3">
    <div class="card">
      <div class="icon">💬</div>
      <h3>Instant Answers</h3>
      <p>Get quick answers on course pricing, duration, and curriculum without waiting for office hours.</p>
    </div>
    <div class="card">
      <div class="icon">🧭</div>
      <h3>Program Guidance</h3>
      <p>Not sure which track fits you? The AI Mentor asks a few questions and points you toward the right course.</p>
    </div>
    <div class="card">
      <div class="icon">🤝</div>
      <h3>Human Handoff</h3>
      <p>For anything specific to your enrollment or payment, the AI Mentor connects you directly to our team.</p>
    </div>
  </div>
</section>

<section class="section" style="text-align:center;">
  <div class="container prose">
    <h2>How it works</h2>
    <p>Message us on WhatsApp using the button above. The AI Mentor will greet you, ask what you're looking for,
    and either answer directly or loop in a SmartVersa counsellor — available during and outside support hours for
    common questions.</p>
  </div>
</section>
"""
write("ai-mentor.html", page(
    "AI Mentor", "Chat with SmartVersa's WhatsApp-based AI Mentor for instant answers on courses, pricing, and guidance.",
    "", mentor_body, canonical="ai-mentor.html", schema=mentor_bc
))

print("Cancellation Policy, Internship Agreement, Disclaimer, Certificate Verification, Support, and AI Mentor pages generated.")
