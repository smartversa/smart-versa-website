#!/usr/bin/env python3
from build import page, write, FIREBASE_CONFIG_JS

# ============================================================
# 404 PAGE (GitHub Pages auto-serves /404.html for unmatched routes)
# ============================================================
notfound_body = """
<section class="section" style="text-align:center;padding:120px 0;">
  <div class="container">
    <div class="eyebrow">Page Not Found</div>
    <h1 style="font-size:4rem;">4<span class="gold-text">0</span>4</h1>
    <p style="max-width:480px;margin:0 auto 28px;">
      The page you're looking for doesn't exist — it may have moved, or the link might be mistyped.
    </p>
    <div class="hero-cta">
      <a href="index.html" class="btn btn-primary">Go to Homepage</a>
      <a href="programs.html" class="btn btn-outline">View Programs</a>
    </div>
  </div>
</section>
"""
write("404.html", page(
    "Page Not Found", "The page you're looking for doesn't exist on SmartVersa.",
    "", notfound_body, extra_head='<meta name="robots" content="noindex">'
))

# ============================================================
# ADMIN PANEL (protected — requires auth + admins/{email} doc)
# ============================================================
admin_body = """
<section class="section">
  <div class="container">
    <div id="authGate" class="card" style="max-width:520px;margin:0 auto;text-align:center;">
      <p>Checking admin access…</p>
    </div>

    <div id="adminContent" style="display:none;">
      <div style="max-width:640px;margin:0 auto 30px;text-align:center;">
        <div class="eyebrow">Admin Panel</div>
        <h1>SmartVersa Admin</h1>
        <p id="adminWho" style="color:var(--text-low);"></p>
      </div>

      <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-bottom:36px;">
        <button class="btn btn-outline admin-tab-btn" data-tab="leads">Leads</button>
        <button class="btn btn-outline admin-tab-btn" data-tab="tickets">Tickets</button>
        <button class="btn btn-outline admin-tab-btn" data-tab="certificates">Certificates</button>
        <button class="btn btn-outline" id="adminLogoutBtn">Log Out</button>
      </div>

      <div id="tab-leads" class="admin-tab">
        <h2>Leads</h2>
        <p style="font-size:.85rem;color:var(--text-low);">Most recent applications from the Contact form.</p>
        <div class="table-scroll">
          <table class="compare-table" id="leadsTable">
            <tr><th>Name</th><th>Email</th><th>Phone</th><th>Course</th><th>Status</th></tr>
            <tr><td colspan="5">Loading…</td></tr>
          </table>
        </div>
      </div>

      <div id="tab-tickets" class="admin-tab" style="display:none;">
        <h2>Support Tickets</h2>
        <div class="table-scroll">
          <table class="compare-table" id="ticketsTable">
            <tr><th>Ticket ID</th><th>Name</th><th>Category</th><th>Priority</th><th>Status</th></tr>
            <tr><td colspan="5">Loading…</td></tr>
          </table>
        </div>
      </div>

      <div id="tab-certificates" class="admin-tab" style="display:none;">
        <h2>Issue a Certificate</h2>
        <div class="form-shell" style="margin-bottom:36px;">
          <form id="issueCertForm">
            <label for="certIdInput">Certificate ID</label>
            <input type="text" id="certIdInput" placeholder="e.g. SV-2026-AIDS-0342" required>

            <label for="certName">Student Name</label>
            <input type="text" id="certName" required>

            <label for="certProgram">Program</label>
            <input type="text" id="certProgram" placeholder="e.g. AI & Data Science" required>

            <label for="certDate">Completion Date</label>
            <input type="date" id="certDate" required>

            <button type="submit" class="btn btn-primary btn-block" style="margin-top:18px;">Issue Certificate</button>
            <div class="form-msg" id="issueCertMsg"></div>
          </form>
        </div>

        <h2>Issued Certificates</h2>
        <div class="table-scroll">
          <table class="compare-table" id="certsTable">
            <tr><th>Certificate ID</th><th>Name</th><th>Program</th><th>Date</th></tr>
            <tr><td colspan="4">Loading…</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
  import {
    getFirestore, collection, getDocs, doc, getDoc, setDoc, query, orderBy, limit
  } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

  __FIREBASE_CONFIG__
  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);
  const db = getFirestore(app);

  const authGate = document.getElementById('authGate');
  const adminContent = document.getElementById('adminContent');

  function esc(s) {
    return (s ?? '').toString().replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }

  async function loadLeads() {
    const tbl = document.getElementById('leadsTable');
    try {
      const q = query(collection(db, "leads"), orderBy("createdAt", "desc"), limit(50));
      const snap = await getDocs(q);
      let rows = '<tr><th>Name</th><th>Email</th><th>Phone</th><th>Course</th><th>Status</th></tr>';
      if (snap.empty) rows += '<tr><td colspan="5">No leads yet.</td></tr>';
      snap.forEach(d => {
        const l = d.data();
        rows += `<tr><td>${esc(l.name)}</td><td>${esc(l.email)}</td><td>${esc(l.phone)}</td><td>${esc(l.course)}</td><td>${esc(l.status)}</td></tr>`;
      });
      tbl.innerHTML = rows;
    } catch (err) {
      console.error(err);
      tbl.innerHTML = '<tr><td colspan="5">Could not load leads. Check Firestore rules/indexes.</td></tr>';
    }
  }

  async function loadTickets() {
    const tbl = document.getElementById('ticketsTable');
    try {
      const q = query(collection(db, "tickets"), orderBy("createdAt", "desc"), limit(50));
      const snap = await getDocs(q);
      let rows = '<tr><th>Ticket ID</th><th>Name</th><th>Category</th><th>Priority</th><th>Status</th></tr>';
      if (snap.empty) rows += '<tr><td colspan="5">No tickets yet.</td></tr>';
      snap.forEach(d => {
        const t = d.data();
        rows += `<tr><td>${esc(t.ticketId || d.id)}</td><td>${esc(t.name)}</td><td>${esc(t.category)}</td><td>${esc(t.priority)}</td><td>${esc(t.status)}</td></tr>`;
      });
      tbl.innerHTML = rows;
    } catch (err) {
      console.error(err);
      tbl.innerHTML = '<tr><td colspan="5">Could not load tickets. Check Firestore rules/indexes.</td></tr>';
    }
  }

  async function loadCertificates() {
    const tbl = document.getElementById('certsTable');
    try {
      const snap = await getDocs(collection(db, "certificates"));
      let rows = '<tr><th>Certificate ID</th><th>Name</th><th>Program</th><th>Date</th></tr>';
      if (snap.empty) rows += '<tr><td colspan="4">No certificates issued yet.</td></tr>';
      snap.forEach(d => {
        const c = d.data();
        rows += `<tr><td>${esc(d.id)}</td><td>${esc(c.name)}</td><td>${esc(c.program)}</td><td>${esc(c.completionDate)}</td></tr>`;
      });
      tbl.innerHTML = rows;
    } catch (err) {
      console.error(err);
      tbl.innerHTML = '<tr><td colspan="4">Could not load certificates.</td></tr>';
    }
  }

  function showTab(tab) {
    document.querySelectorAll('.admin-tab').forEach(el => el.style.display = 'none');
    document.getElementById('tab-' + tab).style.display = 'block';
    document.querySelectorAll('.admin-tab-btn').forEach(b => b.classList.remove('btn-primary'));
    document.querySelector(`.admin-tab-btn[data-tab="${tab}"]`)?.classList.add('btn-primary');
  }
  document.querySelectorAll('.admin-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => showTab(btn.dataset.tab));
  });

  document.getElementById('issueCertForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const msg = document.getElementById('issueCertMsg');
    const certId = document.getElementById('certIdInput').value.trim();
    const data = {
      name: document.getElementById('certName').value,
      program: document.getElementById('certProgram').value,
      completionDate: document.getElementById('certDate').value,
    };
    try {
      await setDoc(doc(db, "certificates", certId), data);
      msg.textContent = `Certificate ${certId} issued.`;
      msg.className = "form-msg success";
      e.target.reset();
      loadCertificates();
    } catch (err) {
      console.error(err);
      msg.textContent = "Couldn't issue certificate — check Firestore rules and your admin status.";
      msg.className = "form-msg error";
    }
  });

  document.getElementById('adminLogoutBtn').addEventListener('click', async () => {
    await signOut(auth);
    window.location.href = 'login.html';
  });

  onAuthStateChanged(auth, async (user) => {
    if (!user) {
      authGate.innerHTML = '<p>You need to be logged in as an admin. Redirecting to login…</p>';
      setTimeout(() => window.location.href = 'login.html', 1000);
      return;
    }
    try {
      const adminSnap = await getDoc(doc(db, "admins", user.email));
      if (!adminSnap.exists()) {
        authGate.innerHTML = '<p>This account does not have admin access.</p>';
        return;
      }
      authGate.style.display = 'none';
      adminContent.style.display = 'block';
      document.getElementById('adminWho').textContent = user.email;
      showTab('leads');
      loadLeads();
      loadTickets();
      loadCertificates();
    } catch (err) {
      console.error(err);
      authGate.innerHTML = '<p>Could not verify admin access. Check your connection and try again.</p>';
    }
  });
</script>
"""
admin_body = admin_body.replace("__FIREBASE_CONFIG__", FIREBASE_CONFIG_JS)
write("admin.html", page(
    "Admin Panel", "SmartVersa internal admin panel for leads, tickets, and certificates.",
    "", admin_body, canonical="admin.html", extra_head='<meta name="robots" content="noindex">'
))

print("404.html and admin.html generated.")
