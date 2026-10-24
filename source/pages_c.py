def build(page):
    # ---------------------------------------------------------- TRIPS (portal)
    page('trips.html', 'My Trips', '''
<section class="block"><div class="wrap">
 <div class="portal"><div class="side" id="side">
  <div class="on" data-t="Welcome back. You have 1 upcoming trip: Nilgiri Whistle, Saturday 07:10.">Dashboard</div>
  <div data-t="Traveller profile: loyalty tier Silver · 2,480 points · Window seat preferred.">Profile</div>
  <div data-t="Bookings: 3 completed, 1 upcoming, 0 cancelled.">Bookings</div>
  <div data-t="Tickets: boarding pass is ready below. Show it at the gate.">Tickets</div>
  <div data-t="Settings: notifications, saved passengers and password live here.">Settings</div></div>
  <div class="main" id="main">Welcome back. You have 1 upcoming trip: Nilgiri Whistle, Saturday 07:10.</div></div>
 <p style="margin:1rem 0"><a class="btn dark" href="account.html">Sign in</a> <a class="btn ghost" href="assist.html">Request assistance</a></p></div></section>
<section class="block"><div class="wrap"><span class="eyebrow">Boarding pass</span>
 <table class="pass-t"><tr><td colspan="3" class="hd">Junction 41 · Boarding Pass</td></tr>
  <tr><td rowspan="2" class="qr"><div aria-hidden="true"></div></td><td><small>Passenger</small><br><strong>@@NAME@@</strong></td><td><small>Train</small><br><strong>Nilgiri Whistle</strong></td></tr>
  <tr><td><small>From → To</small><br><strong>Mettupalayam → Ooty</strong></td><td><small>Departs</small><br><strong>Sat 07:10 · Coach C2 · 14A</strong></td></tr>
  <tr><td colspan="3" class="ft">Gates close 10 minutes before departure. Have a lovely journey.</td></tr></table></div></section>
<script>var it=document.querySelectorAll('#side div'),mn=document.getElementById('main');
it.forEach(function(d){d.addEventListener('click',function(){it.forEach(function(x){x.classList.remove('on')});d.classList.add('on');mn.textContent=d.dataset.t;});});</script>''',
         nav='trips.html', no='◎', heading='My Trips', blurb='Your dashboard and boarding pass. Click the sidebar to switch panels.', tags=['div sidebar layout', 'table layout', 'colspan / rowspan'],
         css='''.portal{display:grid;grid-template-columns:230px 1fr;border:3px solid var(--ink);min-height:260px;box-shadow:8px 8px 0 var(--ink)}.side{background:var(--ink)}
.side div{color:var(--paper);padding:1rem 1.3rem;font:600 1.1rem var(--display);letter-spacing:.1em;text-transform:uppercase;cursor:pointer;border-left:6px solid transparent}.side div:hover{background:#2a2820}.side div.on{border-color:var(--amber);background:#2a2820;color:var(--amber)}
.main{padding:2rem;font:600 1.9rem/1.15 var(--display);text-transform:uppercase;background:#fbf6ea}.pass-t td{vertical-align:top;background:#fbf6ea}.hd,.ft{background:var(--ink)!important;color:var(--paper);font:600 1.1rem var(--display);letter-spacing:.1em;text-transform:uppercase}
.qr{width:140px}.qr div{width:110px;height:110px;background:repeating-conic-gradient(var(--ink) 0 25%,#fff 0 50%) 0 0/22px 22px;border:4px solid var(--ink)}small{font:500 .7rem var(--mono);text-transform:uppercase;color:var(--muted)}
@media(max-width:640px){.portal{grid-template-columns:1fr}}''')

    # ---------------------------------------------------------- LIVE
    seats = ''.join(f'<div class="seat{" taken" if i in (3, 4, 9, 14, 17) else ""}" data-s="{(i // 4) + 1}{"ABCD"[i % 4]}" data-w="{"window" if i % 4 in (0, 3) else "aisle"}"></div>' for i in range(24))
    page('status.html', 'Live', f'''
<section class="block"><div class="wrap cols">
 <div class="ticket"><h3>Find a train</h3><div class="f"><label for="ss">Train name or PNR</label><input id="ss" class="fancy" autocomplete="off" placeholder="Enter to search · Esc to clear"></div>
  <p class="mono" id="ssKey">Key pressed: –</p><p class="mono" id="ssEcho"></p><p class="mono" id="ssMsg" style="color:var(--green)"></p></div>

 <div class="ticket dark"><h3>Line signals</h3><div style="display:flex;gap:1.6rem;align-items:center"><div class="signal-post">
  <div class="bulb r" data-msg="STOP · line occupied"></div><div class="bulb y" data-msg="READY · next train approaching"></div><div class="bulb g" data-msg="GO · line clear"></div></div>
  <p id="sigMsg" class="big" style="color:var(--amber)">Hover a lamp</p></div></div>

 <div class="ticket"><h3>Pick a seat</h3><div class="seats" id="seats">{seats}</div><p class="mono" id="seatMsg" style="min-height:1.4em;margin-top:.6rem">Hover a seat. Click to choose.</p></div>

 <div class="ticket"><h3>Coach class</h3><div class="pcard"><img id="pimg" src="img/travel-munnar.svg" alt="Vista Dome coach" width="400" height="260">
  <div id="pinfo" class="pinfo">Vista Dome · glass roof, 40 seats</div><button class="btn" id="pbtn">View Details</button><p id="pdet" class="mono"></p></div></div>

 <div class="ticket"><h3>Seat-lock PIN</h3><div class="f"><label for="pin">4-digit PIN</label><input id="pin" type="password" maxlength="4" inputmode="numeric" placeholder="••••" autocomplete="off"></div><p class="mono" id="pinMsg"></p></div>

 <div class="ticket"><h3>Quick poll</h3><p><strong>How was your last journey?</strong></p>
  <div id="opts"><div class="opt" tabindex="0">On time, lovely</div><div class="opt" tabindex="0">Slightly late</div><div class="opt" tabindex="0">Needs work</div></div>
  <button class="btn dark" id="sub" style="margin-top:1rem">Submit</button><p class="mono" id="exMsg">Click an option, then press Enter.</p></div>
</div></section>''', nav='status.html', no='●', heading='Live desk',
         blurb='Search a train, check the signals, pick a seat, preview a coach, lock it with a PIN and rate your trip. Mouse and keyboard both work.',
         tags=['mouseover', 'mouseout', 'click', 'keydown', 'keyup', 'event.key'], js=['mouse', 'keys'],
         css='''.big{font:700 1.9rem/1 var(--display);text-transform:uppercase;min-height:2rem}.fancy{border:2px solid var(--ink)!important;padding:.6rem!important;transition:background .3s}.fancy.typing{background:#fff0b8}
.seats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;max-width:260px}.seat{aspect-ratio:1;border:2px solid var(--ink);background:#bfe0cf;cursor:pointer;transition:.15s}.seat:hover{transform:scale(1.1)}.seat.sel{background:var(--signal)}.seat.taken{background:#8a8574;cursor:not-allowed}
.pcard{text-align:center}.pcard img{margin:0 auto 1rem;width:100%;max-width:320px;border:3px solid var(--ink);transition:.3s}.pcard img.hot{transform:rotate(-2deg) scale(1.05);filter:saturate(1.8);box-shadow:8px 8px 0 var(--signal)}
.pinfo{max-height:0;opacity:0;overflow:hidden;transition:.3s;font:500 .85rem var(--mono)}.pinfo.show{max-height:60px;opacity:1;margin-bottom:.8rem}
.opt{border:2px solid var(--ink);padding:.6rem 1rem;margin-bottom:.5rem;cursor:pointer;font-family:var(--mono)}.opt.sel{background:var(--amber)}.opt:hover{background:var(--paper-2)}#sub.hi{background:var(--signal);transform:scale(1.05)}''')
