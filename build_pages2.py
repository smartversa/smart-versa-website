#!/usr/bin/env python3
from build import page, write, FAQ_SCRIPT, breadcrumb_schema, faqpage_schema, FIREBASE_CONFIG_JS

# ============================================================
# CONTACT
# ============================================================
contact_body = """
<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">Get In Touch</div>
      <h1>Let's talk about your next step</h1>
      <p>Fill out the form and our team will reach out within one business day — or reach us directly below.</p>
    </div>

    <div class="grid grid-2" style="align-items:start;">
      <div class="form-shell">
        <form id="applyForm">
          <label for="name">Full Name</label>
          <input type="text" id="name" name="name" placeholder="Your full name" required>

          <label for="email">Email</label>
          <input type="email" id="email" name="email" placeholder="you@example.com" required>

          <label for="phone">Phone</label>
          <input type="tel" id="phone" name="phone" placeholder="+91 XXXXX XXXXX" required>

          <label for="course">Course Interested In</label>
          <select id="course" name="course" required>
            <option value="">Select a program</option>
            <option>AI &amp; Data Science</option>
            <option>Python Programming</option>
            <option>Data Analytics</option>
            <option>Digital Marketing</option>
            <option>UI/UX Design (Waitlist)</option>
            <option>Web Development (Waitlist)</option>
            <option>HR Course (Waitlist)</option>
          </select>

          <label for="message">Message</label>
          <textarea id="message" name="message" rows="4" placeholder="Tell us a bit about your goals"></textarea>

          <button type="submit" class="btn btn-primary btn-block" style="margin-top:22px;">Submit Application</button>
          <div class="form-msg" id="formMsg"></div>
          <p class="form-note">Submissions are securely stored. We only use your details to follow up about your application.</p>
        </form>
      </div>

      <div>
        <div class="card" style="margin-bottom:18px;">
          <h3>Email</h3>
          <p><a href="mailto:team@smartversa.in">team@smartversa.in</a></p>
        </div>
        <div class="card" style="margin-bottom:18px;">
          <h3>Call</h3>
          <p><a href="tel:+919306539879">+91 93065 39879</a></p>
        </div>
        <div class="card" style="margin-bottom:18px;">
          <h3>WhatsApp</h3>
          <p><a href="https://wa.me/919306539879">Message us on WhatsApp</a></p>
        </div>
        <div class="card">
          <h3>Support Hours</h3>
          <p>9 AM – 8 PM, Monday to Saturday</p>
        </div>
      </div>
    </div>
  </div>
</section>

<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

  __FIREBASE_CONFIG__
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);

  const form = document.getElementById('applyForm');
  const msg = document.getElementById('formMsg');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
      name: form.name.value,
      email: form.email.value,
      phone: form.phone.value,
      course: form.course.value,
      message: form.message.value,
      status: 'new',
      createdAt: serverTimestamp(),
    };
    try {
      await addDoc(collection(db, "leads"), data);
      msg.textContent = "Thanks! Your application has been received — we'll be in touch within 1 business day.";
      msg.className = "form-msg success";
      form.reset();
    } catch (err) {
      console.error(err);
      msg.textContent = "Something went wrong. Please try WhatsApp or email instead.";
      msg.className = "form-msg error";
    }
  });
</script>
"""
contact_body = contact_body.replace("__FIREBASE_CONFIG__", FIREBASE_CONFIG_JS)
write("contact.html", page(
    "Contact", "Get in touch with SmartVersa. Apply for a program, ask a question, or reach us by phone, email, or WhatsApp.",
    "Contact", contact_body, canonical="contact.html"
))

# ============================================================
# LOGIN / SIGNUP
# ============================================================
login_body = """
<section class="section">
  <div class="container">
    <div class="form-shell">
      <div style="text-align:center;margin-bottom:24px;">
        <div class="eyebrow">Student Portal</div>
        <h2 id="formTitle">Log In to Your Account</h2>
      </div>

      <form id="authForm">
        <div id="signupOnly" style="display:none;">
          <label for="fullname">Full Name</label>
          <input type="text" id="fullname" placeholder="Your full name">
        </div>

        <label for="authEmail">Email</label>
        <input type="email" id="authEmail" placeholder="you@example.com" required>

        <label for="authPassword">Password</label>
        <input type="password" id="authPassword" placeholder="••••••••" required>

        <div id="forgotWrap" style="text-align:right;margin-top:8px;">
          <a href="#" id="forgotLink" style="font-size:.82rem;color:var(--gold-2);">Forgot password?</a>
        </div>

        <button type="submit" class="btn btn-primary btn-block" style="margin-top:20px;" id="authSubmit">Log In</button>
        <div class="form-msg" id="authMsg"></div>
      </form>

      <p style="text-align:center;margin-top:20px;font-size:.88rem;">
        <span id="toggleText">Don't have an account?</span>
        <a href="#" id="toggleAuth" style="color:var(--gold-2);">Sign Up</a>
      </p>
    </div>
  </div>
</section>

<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import {
    getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword,
    sendPasswordResetEmail, updateProfile
  } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

  __FIREBASE_CONFIG__
  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);

  let mode = 'login'; // or 'signup'
  const form = document.getElementById('authForm');
  const msg = document.getElementById('authMsg');
  const toggleAuth = document.getElementById('toggleAuth');
  const toggleText = document.getElementById('toggleText');
  const formTitle = document.getElementById('formTitle');
  const signupOnly = document.getElementById('signupOnly');
  const authSubmit = document.getElementById('authSubmit');
  const forgotLink = document.getElementById('forgotLink');

  toggleAuth.addEventListener('click', (e) => {
    e.preventDefault();
    mode = mode === 'login' ? 'signup' : 'login';
    const isSignup = mode === 'signup';
    signupOnly.style.display = isSignup ? 'block' : 'none';
    formTitle.textContent = isSignup ? 'Create Your Account' : 'Log In to Your Account';
    authSubmit.textContent = isSignup ? 'Sign Up' : 'Log In';
    toggleText.textContent = isSignup ? 'Already have an account?' : "Don't have an account?";
    toggleAuth.textContent = isSignup ? 'Log In' : 'Sign Up';
    msg.className = 'form-msg';
  });

  forgotLink.addEventListener('click', async (e) => {
    e.preventDefault();
    const email = document.getElementById('authEmail').value;
    if (!email) { msg.textContent = "Enter your email above first, then click Forgot password."; msg.className = "form-msg error"; return; }
    try {
      await sendPasswordResetEmail(auth, email);
      msg.textContent = "Password reset email sent — check your inbox.";
      msg.className = "form-msg success";
    } catch (err) {
      console.error(err);
      msg.textContent = "Couldn't send reset email. Check the address and try again.";
      msg.className = "form-msg error";
    }
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('authEmail').value;
    const password = document.getElementById('authPassword').value;
    try {
      if (mode === 'signup') {
        const cred = await createUserWithEmailAndPassword(auth, email, password);
        const fullname = document.getElementById('fullname').value;
        if (fullname) await updateProfile(cred.user, { displayName: fullname });
      } else {
        await signInWithEmailAndPassword(auth, email, password);
      }
      msg.textContent = "Success! Redirecting to your dashboard…";
      msg.className = "form-msg success";
      setTimeout(() => window.location.href = "dashboard.html", 800);
    } catch (err) {
      console.error(err);
      msg.textContent = "Couldn't authenticate. Check your details and try again.";
      msg.className = "form-msg error";
    }
  });
</script>
"""
login_body = login_body.replace("__FIREBASE_CONFIG__", FIREBASE_CONFIG_JS)
write("login.html", page(
    "Login / Sign Up", "Log in or create your SmartVersa student account to access your dashboard.",
    "", login_body, canonical="login.html"
))

# ============================================================
# DASHBOARD (protected)
# ============================================================
dashboard_body = """
<section class="section">
  <div class="container">
    <div id="authGate" class="card" style="max-width:520px;margin:0 auto;text-align:center;">
      <p>Checking your session…</p>
    </div>

    <div id="dashboardContent" style="display:none;">
      <div style="max-width:640px;margin:0 auto 36px;text-align:center;">
        <div class="eyebrow">Student Dashboard</div>
        <h1>Welcome back, <span class="gold-text" id="studentName">Student</span></h1>
        <p id="studentEmail" style="color:var(--text-low);"></p>
      </div>
      <div class="grid grid-3">
        <div class="card">
          <h3>Enrolled Program</h3>
          <p id="enrolledProgram">No active enrollment yet — apply to a program to see it here.</p>
        </div>
        <div class="card">
          <h3>Certificate Status</h3>
          <p>Not yet issued — complete all assignments to unlock your certificate.</p>
        </div>
        <div class="card">
          <h3>Account</h3>
          <button class="btn btn-outline btn-block" id="logoutBtn">Log Out</button>
        </div>
      </div>
    </div>
  </div>
</section>

<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

  __FIREBASE_CONFIG__
  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);

  const authGate = document.getElementById('authGate');
  const dashboardContent = document.getElementById('dashboardContent');

  function renderLoggedIn(user) {
    authGate.style.display = 'none';
    dashboardContent.style.display = 'block';
    document.getElementById('studentName').textContent = user.displayName || 'Student';
    document.getElementById('studentEmail').textContent = user.email || '';
  }

  function redirectToLogin() {
    authGate.innerHTML = '<p>You need to be logged in to view this page. Redirecting to login…</p>';
    setTimeout(() => window.location.href = 'login.html', 1000);
  }

  onAuthStateChanged(auth, (user) => {
    if (user) { renderLoggedIn(user); } else { redirectToLogin(); }
  });

  document.getElementById('logoutBtn')?.addEventListener('click', async () => {
    await signOut(auth);
    window.location.href = 'login.html';
  });
</script>
"""
dashboard_body = dashboard_body.replace("__FIREBASE_CONFIG__", FIREBASE_CONFIG_JS)
write("dashboard.html", page(
    "Dashboard", "Your SmartVersa student dashboard — view enrollment and certificate status.",
    "", dashboard_body, canonical="dashboard.html",
    extra_head='<meta name="robots" content="noindex">'
))

# ============================================================
# FAQ
# ============================================================
faq_items = [
    ("Do I need prior experience to join a program?", "No. Every SmartVersa program is designed to start from the basics, with guided weekly practice to build you up to job-ready skills."),
    ("Are the classes live or recorded?", "Classes are recorded so you can learn at your own pace, with live mentor sessions layered on top for guidance and doubt-solving."),
    ("How long do I have access to the course material?", "Lifetime access — you can revisit recordings and resources anytime after enrolling."),
    ("Is there a certificate at the end?", "Yes, a free verifiable certificate of completion is included in every program at no extra cost."),
    ("What is the refund policy?", "See our full Refund Policy page for eligibility windows and process."),
    ("How do I apply?", "Fill out the application form on our Contact page, or reach out directly via WhatsApp or call."),
    ("Is SmartVersa a registered business?", "Yes, SmartVersa is MSME-registered in India."),
    ("Do you offer placement guarantees?", "We provide placement guidance — resume help, LinkedIn optimization, and interview prep — but do not guarantee job placement."),
]
faq_html = "".join(f"""
      <div class="faq-item">
        <div class="faq-q">{q}<span class="chev">▾</span></div>
        <div class="faq-a"><p>{a}</p></div>
      </div>""" for q, a in faq_items)

faq_body = f"""
<section class="section">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <div class="eyebrow">FAQ</div>
      <h1>Frequently asked questions</h1>
    </div>
    <div style="max-width:760px;margin:0 auto;">{faq_html}</div>
  </div>
</section>
{FAQ_SCRIPT}
"""
faq_schema = "\n".join([breadcrumb_schema([("Home", ""), ("FAQ", "faq.html")]), faqpage_schema(faq_items)])
write("faq.html", page(
    "FAQ", "Answers to common questions about SmartVersa programs, certificates, refunds, and enrollment.",
    "FAQ", faq_body, canonical="faq.html", schema=faq_schema
))

print("Contact, Login, Dashboard, and FAQ generated.")
