from pages_a import TRAINS
GENDER = ''.join(f'<label><input type="radio" name="gender" value="{g}" required> {g}</label>' for g in ['Female', 'Male', 'Other'])
TOPTS = ''.join(f'<option value="{f}">{n} · {r}</option>' for n, r, d, du, c, f in TRAINS)
STEPS = '''.steps{display:flex;margin-bottom:2rem;font:600 1rem var(--display);letter-spacing:.1em;text-transform:uppercase}.steps a{flex:1;text-align:center;padding:.7rem .4rem;border:2px solid var(--ink);margin-left:-2px;text-decoration:none;color:var(--ink);background:#fbf6ea}.steps .now{background:var(--amber)}.steps a:hover{background:var(--paper-2)}'''
def steps(n):
    return '<div class="steps">' + ''.join(f'<a href="{h}"{" class=now" if i == n else ""}>{t}</a>' for i, (h, t) in enumerate([('book.html', '1 · Passenger'), ('payment.html', '2 · Payment'), ('summary.html', '3 · Basket')])) + '</div>'
STATES = '<option value="">Select state</option>' + ''.join(f'<option>{s}</option>' for s in ['Tamil Nadu', 'Kerala', 'Karnataka', 'Telangana', 'Maharashtra', 'Delhi'])


def build(page):
    # ---------------------------------------------------------- BOOK (step 1)
    prefs = ''.join(f'<label><input type="checkbox" name="pref" value="{p}"> {p}</label>' for p in ['Window seat', 'Lower berth', 'Vegetarian meal', 'Extra luggage', 'Travel insurance'])
    page('book.html', 'Book', f'''
<section class="block"><div class="wrap">{steps(0)}
<form class="pass" id="bk" novalidate>
  <div class="f"><label for="tr">Train</label><select id="tr" required><option value="">Choose a train</option>{TOPTS}</select><span class="err" data-for="tr"></span></div>
  <div class="f"><label for="dt">Travel date</label><input id="dt" type="date" required><span class="err" data-for="dt"></span></div>
  <div class="f"><label for="px">Passengers</label><input id="px" type="number" min="1" max="6" value="1" required></div>
  <div class="f"><label for="nm">Passenger name</label><input id="nm" required maxlength="40" placeholder="As on ID, letters only"><span class="err" data-for="nm"></span></div>
  <div class="f"><label for="jp">Junction Pass no. (if any)</label><input id="jp" maxlength="8" placeholder="JN123456"><span class="err" data-for="jp"></span></div>
  <div class="f"><label for="em">Email</label><input id="em" type="email" required placeholder="you@example.com"><span class="err" data-for="em"></span></div>
  <div class="f"><label for="mb">Mobile</label><input id="mb" type="tel" maxlength="10" required placeholder="10 digits"><span class="err" data-for="mb"></span></div>
  <div class="f"><label for="db">Date of birth</label><input id="db" type="date" required></div>
  <fieldset class="f"><legend>Gender</legend><div class="opts">{GENDER}</div></fieldset>
  <fieldset class="f full"><legend>Preferences</legend><div class="opts">{prefs}</div></fieldset>
  <div class="actions"><button class="btn" type="submit">Confirm details</button><button class="btn ghost" type="reset" id="rs">Reset</button></div>
  <div class="msg full" id="out"></div></form>
<div id="result" style="margin-top:2rem"></div></div></section>''',
         nav='book.html', no='1', heading='Book a seat', blurb='Tell us who is travelling. Every field is checked in your browser before anything moves on.',
         tags=['regex test()', 'arrays', 'DOM table', 'sessionStorage'], js=['book'], css=STEPS)

    # ---------------------------------------------------------- PAYMENT (step 2)
    page('payment.html', 'Payment', f'''
<section class="block"><div class="wrap">{steps(1)}
<form class="pass" data-demo data-next="summary.html" id="pay">
  <fieldset class="f full"><legend>Pay with</legend><div class="opts">
  {''.join(f'<label><input type="radio" name="pm" value="{m}" required{" checked" if m == "Credit Card" else ""}> {m}</label>' for m in ['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Pay at station'])}</div></fieldset>
  <div class="f card"><label for="ch">Card holder</label><input id="ch" placeholder="Name on card"></div>
  <div class="f card"><label for="cn">Card number</label><input id="cn" inputmode="numeric" maxlength="19" placeholder="XXXX XXXX XXXX XXXX"></div>
  <div class="f card"><label for="ex">Expiry</label><input id="ex" type="month"></div>
  <div class="f card"><label for="cv">CVV</label><input id="cv" type="password" maxlength="4" placeholder="•••"></div>
  <div class="f upi" hidden><label for="up">UPI ID</label><input id="up" placeholder="name@bank"></div>
  <div class="f"><label for="bs">Billing state</label><select id="bs" required>{STATES}</select></div>
  <div class="f"><label for="bp">PIN code</label><input id="bp" type="number" min="100000" max="999999" required placeholder="6 digits"></div>
  <label class="opts f full" style="font-size:1rem"><input type="checkbox" required> I accept the fare rules and cancellation policy</label>
  <div class="actions"><a class="btn ghost" href="book.html">← Back</a><button class="btn" type="submit">Review basket →</button></div></form></div></section>
<script>
var pay=document.getElementById('pay');
function sync(){{var m=pay.pm.value,card=/Card/.test(m);document.querySelectorAll('.card').forEach(function(e){{e.hidden=!card;e.querySelector('input').required=card;}});
 document.querySelector('.upi').hidden=m!=='UPI';document.getElementById('up').required=m==='UPI';}}
pay.addEventListener('change',sync);sync();</script>''',
         nav='book.html', no='2', heading='Payment', blurb='Fields appear only for the method you pick.', tags=['radio', 'month', 'password', 'conditional fields'], js=['forms'], css=STEPS)

    # ---------------------------------------------------------- SUMMARY (step 3)
    page('summary.html', 'Basket', f'''
<section class="block"><div class="wrap">{steps(2)}
<table><thead><tr><th>Item</th><th>Qty</th><th>Price</th><th>Total</th></tr></thead><tbody id="rows"></tbody>
<tfoot><tr><th colspan="3" style="text-align:right">Total amount</th><th id="grand">₹0</th></tr></tfoot></table>
<p style="margin-top:1.4rem"><button class="btn" id="place">Place Order</button> <a class="btn ghost" href="index.html">Cancel</a></p>
<div class="msg" id="m"></div></div></section>''', nav='book.html', no='3', heading='Your basket',
         blurb='Fares, reservation fee and tax, worked out from the booking you just made.', tags=['table', 'tfoot', 'sessionStorage'], js=['summary'], css=STEPS)

    # ---------------------------------------------------------- ACCOUNT (login)
    page('account.html', 'Sign in', '''
<section class="block"><div class="wrap cols">
<form class="pass" data-auth novalidate style="grid-template-columns:1fr">
  <div class="f"><label for="u">Username or email</label><input id="u" maxlength="50" placeholder="e.g. rail_fan or you@mail.com" autocomplete="username"></div>
  <div class="f"><label for="pw">Password</label><input id="pw" type="password" maxlength="30" placeholder="8+ characters" autocomplete="current-password"></div>
  <fieldset class="f"><legend>I am a</legend><div class="opts"><label><input type="radio" name="role" checked> Traveller</label><label><input type="radio" name="role"> Station staff</label></div></fieldset>
  <label class="opts" style="font-size:1rem"><input type="checkbox"> Remember me</label>
  <div class="actions"><button class="btn" type="submit">Sign in</button><button class="btn ghost" type="reset">Clear</button></div><div class="msg"></div>
  <p><a href="#">Forgot password?</a> · <a href="book.html">Create new account</a></p></form>
<div class="ticket dark"><h3>Station announcement</h3><p>New here? Press play for a thirty-second guide to signing in, then pick your role and enter your details.</p>
 <audio controls preload="none" style="width:100%"><source src="media/announcement.mp3" type="audio/mpeg"></audio></div></div></section>''',
         nav='trips.html', no='↩', heading='Sign in', blurb='Username and password are checked for emptiness and strength with regular expressions.', tags=['regex', 'radio', 'checkbox', '&lt;audio&gt;'], js=['auth'])

    # ---------------------------------------------------------- CAREERS
    page('careers.html', 'Careers', f'''
<section class="block"><div class="wrap cols">
<form class="pass" data-demo data-ok="Application received. We will write to you soon." id="emp">
  <div class="f"><label for="n">Full name</label><input id="n" required minlength="3" maxlength="40" pattern="[A-Za-z ]+" placeholder="Letters and spaces"></div>
  <div class="f"><label for="eid">Employee ID</label><input id="eid" required maxlength="7" placeholder="EMP1234"><span class="err" id="eidErr"></span></div>
  <div class="f"><label for="e">Email address</label><input id="e" type="email" required placeholder="you@company.com"></div>
  <div class="f"><label for="m">Mobile number</label><input id="m" type="tel" required pattern="[0-9]{{10}}" maxlength="10" placeholder="10 digits"></div>
  <div class="f"><label for="p1">Password</label><input id="p1" type="password" required minlength="8" maxlength="20" placeholder="Min 8 characters"></div>
  <div class="f"><label for="p2">Confirm password</label><input id="p2" type="password" required minlength="8" data-match="p1" placeholder="Repeat password"></div>
  <div class="f"><label for="d">Date of birth</label><input id="d" type="date" required></div>
  <div class="f"><label for="dep">Department</label><select id="dep" required><option value="">Select</option><option>Operations</option><option>Signalling</option><option>Customer care</option><option>Engineering</option></select></div>
  <fieldset class="f"><legend>Employment type</legend><div class="opts"><label><input type="radio" name="et" required> Full-Time</label><label><input type="radio" name="et"> Part-Time</label><label><input type="radio" name="et"> Intern</label></div></fieldset>
  <fieldset class="f"><legend>Gender</legend><div class="opts">{GENDER}</div></fieldset>
  <div class="f full"><label for="ph">Profile photo</label><input id="ph" type="file" accept="image/*"></div>
  <div class="actions"><button class="btn" type="submit">Submit</button><button class="btn ghost" type="reset">Reset</button></div><div class="msg full"></div></form>
<div class="ticket dark"><h3>Meet the crew</h3><video controls poster="img/slide-2.svg" preload="metadata" style="width:100%"><source src="media/welcome.mp4" type="video/mp4"></video>
 <p style="margin-top:1rem">A short welcome from the operations team. Employee IDs look like <span class="mono">EMP1234</span>.</p></div></div></section>''',
         nav='about.html', no='★', heading='Join the crew', blurb='Staff registration using HTML5 validation, plus a live check on the employee ID format.', tags=['email', 'tel', 'date', 'file', 'pattern', 'minlength', '&lt;video&gt;'], js=['forms', 'careers'])

    # ---------------------------------------------------------- ASSIST
    page('assist.html', 'Assistance', f'''
<section class="block clinic"><div class="wrap">
<form class="rx" data-demo data-ok="Request received. A station officer will meet you at the platform.">
 <input type="hidden" name="rid" value="SA-2026-0041">
 <div class="f"><label for="a1">Passenger name</label><input id="a1" type="text" required></div>
 <div class="f"><label for="a2">Email</label><input id="a2" type="email" required></div>
 <div class="f"><label for="a3">Account password</label><input id="a3" type="password" minlength="8" required></div>
 <div class="f"><label for="a4">Contact number</label><input id="a4" type="tel" pattern="[0-9]{{10}}" required placeholder="10 digits"></div>
 <div class="f"><label for="a5">Age</label><input id="a5" type="number" min="0" max="120" required></div>
 <div class="f"><label for="a6">Date of birth</label><input id="a6" type="date" required></div>
 <div class="f"><label for="a7">Reporting time at platform</label><input id="a7" type="time" required></div>
 <div class="f"><label for="a8">Journey date &amp; time</label><input id="a8" type="datetime-local" required></div>
 <div class="f"><label for="a9">Doctor's note / reference link</label><input id="a9" type="url" placeholder="https://"></div>
 <div class="f"><label for="b1">Search station</label><input id="b1" type="search" placeholder="Station name"></div>
 <div class="f"><label for="b2">Preferred seat-cover colour</label><input id="b2" type="color" value="#1e6a4b" style="width:100%;height:42px"></div>
 <div class="f"><label for="b3">Medical certificate</label><input id="b3" type="file"></div>
 <div class="f"><label for="b4">Mobility support level: <output id="ov">5</output> / 10</label><input id="b4" type="range" min="0" max="10" value="5" oninput="ov.value=this.value"></div>
 <div class="f"><label for="b5">Blood group</label><select id="b5"><option value="">Select</option><option>A+</option><option>A-</option><option>B+</option><option>B-</option><option>O+</option><option>O-</option><option>AB+</option><option>AB-</option></select></div>
 <fieldset class="f"><legend>Gender</legend><div class="opts">{GENDER}</div></fieldset>
 <fieldset class="f"><legend>Support needed</legend><div class="opts"><label><input type="checkbox"> Wheelchair</label><label><input type="checkbox"> Porter</label><label><input type="checkbox"> Medical kit</label><label><input type="checkbox"> Escort</label></div></fieldset>
 <div class="f full"><label for="b6">Pick-up address</label><textarea id="b6" rows="3" placeholder="House, street, city"></textarea></div>
 <div class="actions"><button class="btn" type="submit">Submit</button><button class="btn ghost" type="reset">Reset</button>
  <input type="image" src="img/confirm.svg" alt="Confirm request" width="170" height="44" style="margin-left:auto"></div><div class="msg full"></div></form></div></section>''',
         nav='about.html', no='+', heading='Special assistance', blurb='Request help at the platform. This one form uses every HTML5 input type, laid out on a CSS grid.',
         tags=['time', 'datetime-local', 'url', 'search', 'color', 'range', 'hidden', 'image button', 'grid'], js=['forms'],
         css='''.clinic{background:linear-gradient(135deg,#cfe6d8 0%,#efe6d2 55%,#f8d9a0 100%)}.rx{background:#fff;border:2px solid var(--ink);border-radius:18px;box-shadow:0 18px 40px rgba(23,21,15,.25);padding:2rem 2.2rem;margin:0 auto;max-width:900px;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.2rem 1.8rem;border-top:12px solid var(--green)}''')

    # ---------------------------------------------------------- FEST
    page('fest.html', 'Rail Fest', f'''
<section class="block"><div class="wrap">
<div class="cols" style="margin-bottom:2rem">
 <div class="ticket dark"><h3>Promo reel</h3><video controls poster="img/slide-1.svg" preload="metadata" style="width:100%"><source src="media/welcome.mp4" type="video/mp4"></video></div>
 <div class="ticket dark"><h3>Message from the organisers</h3><p>Listen before you register.</p><audio controls preload="none" style="width:100%"><source src="media/announcement.mp3" type="audio/mpeg"></audio></div></div>
<form class="pass" id="fest" novalidate>
 <div class="f"><label for="fn">Participant name</label><input id="fn" required maxlength="40" placeholder="Letters and spaces"><span class="err" data-for="fn"></span></div>
 <div class="f"><label for="fr">Register number</label><input id="fr" required maxlength="9" placeholder="REG123456"><span class="err" data-for="fr"></span></div>
 <div class="f"><label for="fm">VIT email ID</label><input id="fm" required placeholder="username@vit.ac.in"><span class="err" data-for="fm"></span></div>
 <div class="f"><label for="fb">Mobile number</label><input id="fb" type="tel" required maxlength="10" placeholder="10 digits"><span class="err" data-for="fb"></span></div>
 <div class="f"><label for="fe">Event date</label><input id="fe" type="date" required value="2026-11-14"></div>
 <div class="f"><label for="fd">Department</label><select id="fd" required><option value="">Select</option><option>Computer Science</option><option>Electronics</option><option>Mechanical</option><option>Civil</option></select><span class="err" data-for="fd"></span></div>
 <fieldset class="f full"><legend>Workshop interests (pick at least one)</legend><div class="opts">
  <label><input type="checkbox" name="int" value="Web Development"> Web Development</label><label><input type="checkbox" name="int" value="Artificial Intelligence"> Artificial Intelligence</label>
  <label><input type="checkbox" name="int" value="Cyber Security"> Cyber Security</label><label><input type="checkbox" name="int" value="Cloud Computing"> Cloud Computing</label></div><span class="err" data-for="int"></span></fieldset>
 <div class="f full"><label for="fi">Student ID card</label><input id="fi" type="file" accept="image/*,.pdf"></div>
 <div class="actions"><button class="btn" type="submit">Register</button><button class="btn ghost" type="reset" id="rs">Reset</button></div><div class="msg full" id="out"></div></form>
<div id="result" style="margin-top:2rem"></div></div></section>''',
         nav='journal.html', no='◆', heading='Rail Fest registration', blurb='Workshops on signalling, software and photography. Pick your interests and register with your VIT email.',
         tags=['regex', 'checkbox rule', 'array', 'result table', '&lt;video&gt;', '&lt;audio&gt;'], js=['fest'])
