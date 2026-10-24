TRAINS = [  # name, route, departs, duration, category, fare
    ('Nilgiri Whistle', 'Mettupalayam → Ooty', '07:10', '4h 40m', 'Heritage', 650),
    ('Konkan Sunrise', 'Chennai → Goa', '18:45', '21h 10m', 'Overnight', 2850),
    ('Pink City Limited', 'Delhi → Jaipur', '06:05', '4h 30m', 'Scenic', 1450),
    ('Tea Hills Express', 'Kochi → Munnar', '08:30', '5h 15m', 'Weekend', 890),
    ('Valley Arrow', 'Jammu → Srinagar', '09:20', '6h 50m', 'Scenic', 3400),
    ('Backwater Slow', 'Alappuzha → Kollam', '10:00', '3h 05m', 'Weekend', 420),
]
CATS = '<option value="">All categories</option><option>Scenic</option><option>Overnight</option><option>Heritage</option><option>Weekend</option>'
PRICES = '<option value="">Any price</option><option value="lo">Under ₹1,000</option><option value="mid">₹1,000 – ₹3,000</option><option value="hi">Above ₹3,000</option>'


def build(page):
    # ---------------------------------------------------------- HOME
    slides = [('slide-1', 'See India at train speed', 'Window seats on the country\'s prettiest lines, booked in two minutes.'),
              ('slide-2', 'Overnight, and awake by the sea', 'Sleeper berths, chai at dawn and a coastline you will not forget.'),
              ('slide-3', 'Weekend lines, weekday fares', 'Hill stations and backwaters from ₹420.')]
    sl = ''.join(f'<div class="slide{" on" if i == 0 else ""}" style="background-image:url(img/{im}.svg)"><div><h1>{h}</h1><p>{p}</p><a class="btn" href="routes.html">Explore routes</a></div></div>' for i, (im, h, p) in enumerate(slides))
    cards = ''.join(f'<a class="rc" href="routes.html#{i}"><img src="img/{im}.svg" alt="{n}"><div><h3>{n}</h3><p class="mono">{r} · from ₹{f}</p></div></a>'
                    for i, (im, (n, r, _, _, _, f)) in enumerate(zip(['travel-munnar', 'travel-goa', 'travel-jaipur'], [TRAINS[3], TRAINS[1], TRAINS[2]])))
    page('index.html', 'Home', f'''
<section class="slider" id="slider">{sl}<button class="arrow l" id="prev" aria-label="Previous">‹</button><button class="arrow r" id="next" aria-label="Next">›</button><div class="dots" id="dots"></div></section>
<section class="finder"><div class="wrap"><form action="routes.html" method="get" class="find">
  <input type="text" name="q" placeholder="Search routes, stations or offers..." aria-label="Search">
  <select name="cat" aria-label="Category">{CATS}</select><select name="price" aria-label="Price range">{PRICES}</select>
  <button class="btn dark">Find trains</button></form></div></section>
<section class="block"><div class="wrap">
  <span class="eyebrow">Welcome aboard</span><h2 id="hello">Welcome to Junction 41</h2>
  <p class="lede">We run six scenic lines and sell them honestly: real timetables, real fares, no hidden fees.
  <button class="btn ghost" id="hb" type="button">Hover for a greeting</button></p>
  <div class="cols" style="margin-top:2rem">{cards}</div></div></section>''',
         nav='index.html', js=['slider', 'home'],
         css='''.slider{position:relative;height:70vh;min-height:380px;overflow:hidden;background:#000;border-bottom:4px solid var(--ink)}
.slide{position:absolute;inset:0;background-size:cover;background-position:center;display:grid;place-items:center;text-align:center;color:#fff;opacity:0;transition:opacity .9s}.slide::before{content:"";position:absolute;inset:0;background:rgba(10,10,8,.5)}
.slide.on{opacity:1}.slide div{position:relative;max-width:780px;padding:0 1.4rem}.slide h1{font-size:clamp(2.6rem,7vw,5rem);text-shadow:4px 4px 0 var(--signal)}.slide p{font-size:1.3rem}
.arrow{position:absolute;top:50%;transform:translateY(-50%);background:rgba(0,0,0,.5);color:#fff;border:2px solid #fff;font-size:2rem;width:48px;height:48px;cursor:pointer;z-index:3}.arrow:hover{background:var(--signal)}.l{left:14px}.r{right:14px}
.dots{position:absolute;bottom:16px;left:0;right:0;display:flex;justify-content:center;gap:.5rem;z-index:3}.dots i{width:30px;height:5px;background:#fff6;cursor:pointer}.dots i.on{background:var(--amber)}
.finder{background:var(--amber);border-bottom:4px solid var(--ink)}.find{display:flex;gap:.7rem;padding:1rem 0;flex-wrap:wrap}.find input,.find select{flex:1;min-width:170px;border:2px solid var(--ink)!important;background:#fffdf5!important;padding:.65rem .9rem!important;border-radius:30px!important;width:auto!important}.find input{flex:2}
.find .btn{border-radius:30px}.lede{font-size:1.25rem;max-width:60ch}.rc{display:block;text-decoration:none;color:var(--ink);border:2px solid var(--ink);background:#fbf6ea;box-shadow:6px 6px 0 var(--ink);transition:.2s}.rc:hover{transform:translate(-3px,-3px);box-shadow:9px 9px 0 var(--signal)}
.rc img{width:100%;aspect-ratio:3/2;object-fit:cover;border-bottom:2px solid var(--ink)}.rc div{padding:1rem 1.2rem}.rc h3{margin-bottom:.3rem}''')

    # ---------------------------------------------------------- ROUTES
    rows = ''.join(f'<tr data-cat="{c}" data-fare="{f}" id="{i}"><td><strong>{n}</strong></td><td>{r}</td><td>{d}</td><td>{du}</td><td>{c}</td><td>₹{f:,}</td></tr>' for i, (n, r, d, du, c, f) in enumerate(TRAINS))
    shots = [('nature-forest', 'Nilgiri Whistle', 'A narrow-gauge toy train climbs through pine and tea, crossing 250 bridges on the way to Ooty.'),
             ('nature-lake', 'Backwater Slow', 'Glide past coconut palms and still green water, with houseboats for company.'),
             ('nature-desert', 'Pink City Limited', 'Golden-hour dunes and sandstone forts, framed by a wide window.'),
             ('nature-alpine', 'Valley Arrow', 'Snow ridges and apple orchards on the climb into Kashmir.')]
    g = ''.join(f'<div class="shot"><img src="img/{i}.svg" alt="{h}"><div><h3>{h}</h3><p>{d}</p><a href="book.html">Book this line →</a></div></div>' for i, h, d in shots)
    page('routes.html', 'Routes', f'''
<section class="block"><div class="wrap"><span class="eyebrow">Timetable</span><h2>All departures</h2>
<p class="mono" id="count"></p>
<table id="tt"><thead><tr><th>Train</th><th>Route</th><th>Departs</th><th>Duration</th><th>Type</th><th>Fare</th></tr></thead><tbody>{rows}</tbody></table></div></section>
<section class="block"><div class="wrap"><span class="eyebrow">The lines</span><h2>Four views from the window seat</h2><div class="gallery">{g}</div></div></section>
<section class="block"><div class="wrap cols">
 <div class="ticket"><h3>Trip fare calculator</h3><p>Planning a multi-leg trip? Enter each leg's fare.</p>
  <form id="fare" novalidate class="stack"><div class="f"><label for="l1">Leg 1 (₹)</label><input id="l1" type="number" min="0"></div>
  <div class="f"><label for="l2">Leg 2 (₹)</label><input id="l2" type="number" min="0"></div><div class="f"><label for="l3">Leg 3 (₹)</label><input id="l3" type="number" min="0"></div>
  <button class="btn" type="submit">Calculate</button><div class="msg" id="fareOut"></div></form></div>
 <div class="ticket"><h3>Scenic preview</h3><img id="trv" src="img/travel-goa.svg" alt="Destination" class="vw"><p class="mono">N next · P previous · Space names it · click here first</p><p class="mono" id="trvMsg" style="min-height:1.4em"></p></div>
</div></section>''', nav='routes.html', no='→', heading='Routes & timetable',
         blurb='Filter by what you typed on the home page, browse the lines, add up a multi-leg fare, or flip through the views with your keyboard.',
         tags=['table', 'URL search filter', 'div gallery', 'keydown'], js=['routes'],
         css='''.gallery{display:flex;flex-direction:column;gap:2rem}.shot{display:grid;grid-template-columns:3fr 2fr;border:2px solid var(--ink);background:#fbf6ea;box-shadow:7px 7px 0 var(--ink)}
.shot:nth-child(even){grid-template-columns:2fr 3fr}.shot:nth-child(even) img{order:2}.shot img{width:100%;height:100%;min-height:240px;object-fit:cover}.shot div{padding:1.8rem;align-self:center}
.stack{display:grid;gap:1rem}.vw{width:100%;aspect-ratio:3/2;object-fit:cover;border:3px solid var(--ink);margin-bottom:.8rem}tr.hide{display:none}@media(max-width:700px){.shot,.shot:nth-child(even){grid-template-columns:1fr}.shot:nth-child(even) img{order:0}table{font-size:.85rem}}''')

    # ---------------------------------------------------------- JOURNAL
    arts = [('Signal upgrade ends decade of delays', 'The new colour-light system went live overnight. Engineers expect the morning run to clear nearly a quarter faster, with fewer red stops on the hill line.'),
            ('Chai counters return to platforms', 'After a two-year pause, licensed tea stalls are back on every Junction 41 station, brewing in clay cups from first light.'),
            ('Monsoon timetable in force', 'Expect a few extra minutes between stations while crews inspect low-lying stretches. Live boards will show every revised time.'),
            ('Window seats now bookable', 'Passengers can pick left or right side on all scenic lines, so the best view is no longer luck.'),
            ('Heritage walk returns Saturday', 'The clock tower, goods shed and signal cabin: a two-hour guided walk through the junction\'s history. Bring water and a camera.'),
            ('Rail Fest opens registrations', 'Workshops on signalling, ticketing software and photography return this November. Seats are limited and fill quickly.')]
    html = ''.join(f'<article><h3>{h}</h3><p>{p}</p><p>{p.split(".")[0]}. Travellers have welcomed the change, with more detail due in the coming days.</p></article>' for h, p in arts)
    page('journal.html', 'Journal', f'''
<section class="block"><div class="wrap"><div class="masthead"><h2>The Junction Journal</h2><span class="mono" id="today">Today</span><span class="mono">News from the line</span></div>
<div class="paper"><h1 class="main-head">Trains run on time as new signals go live</h1>
<p class="lead">The long-awaited upgrade promises smoother mornings for thousands of commuters and holidaymakers across all six lines.</p>{html}</div></div></section>
<script>document.getElementById('today').textContent=new Date().toLocaleDateString('en-IN',{{weekday:'long',day:'numeric',month:'long',year:'numeric'}});</script>''',
         nav='journal.html', no='N', heading='The Journal', blurb='Notices and stories from the network. Three columns on a desktop, one on your phone.',
         tags=['column-count', 'column-rule', '@media'],
         css='''.masthead{display:flex;justify-content:space-between;align-items:baseline;border-top:6px double var(--ink);border-bottom:2px solid var(--ink);padding:.8rem 0;flex-wrap:wrap;gap:.5rem}.masthead h2{margin:0;font-size:3rem}
.paper{column-count:3;column-gap:2.4rem;column-rule:2px solid var(--ink);margin-top:1.6rem;text-align:justify;hyphens:auto}.paper article{break-inside:avoid;margin-bottom:1.4rem}.paper h3{font-size:1.5rem}
.main-head{column-span:all;border-bottom:4px solid var(--signal);padding-bottom:.4rem;text-align:left}.lead{column-span:all;font:italic 1.35rem/1.4 var(--body);text-align:left;border-bottom:1px solid var(--ink);padding-bottom:1rem}
.paper article:first-of-type p:first-of-type::first-letter{float:left;font:700 4rem/.8 var(--display);margin:.1em .1em 0 0;color:var(--signal)}@media(max-width:800px){.paper{column-count:1;column-rule:none}.masthead h2{font-size:2.1rem}}''')

    # ---------------------------------------------------------- ABOUT
    page('about.html', 'About', '''
<section class="block"><div class="wrap cols">
 <div><p><b>Junction 41</b> is a rail travel service built around one idea: the journey is the destination.
 We run <i>six scenic lines</i> across India, each with a <u>fixed timetable</u>, honest fares and a window seat for every <mark>booked</mark> passenger.</p>
 <p>Our onboard water is filtered to the last drop (H<sub>2</sub>O, nothing else), and every coach is cleaned to a standard of 10<sup>3</sup> checks a month.</p>
 <h3>What we offer</h3>
 <ul><li>Scenic lines<ul><li>Nilgiri Whistle</li><li>Valley Arrow</li><li>Pink City Limited</li></ul></li>
     <li>Comfort<ul><li>Window-seat booking</li><li>Sleeper berths</li><li>Chai at dawn</li></ul></li>
     <li>Support<ul><li>Special assistance</li><li>24-hour helpline</li></ul></li></ul>
 <h3>Fleet</h3>
 <table><thead><tr><th>Class</th><th>Seats / coach</th><th>Meals</th></tr></thead><tbody>
  <tr><td>Sleeper</td><td>72</td><td>Chai &amp; snacks</td></tr><tr><td>AC Chair</td><td>78</td><td>Full meal</td></tr><tr><td>Vista Dome</td><td>40</td><td>Full meal</td></tr></tbody></table>
 <p style="margin-top:1rem">Timetable rules follow the <a href="https://indianrailways.gov.in" target="_blank" rel="noopener">Indian Railways</a> framework.</p></div>
 <div style="display:flex;flex-direction:column;align-items:center;gap:1.6rem">
  <div class="idcard"><img src="img/avatar.svg" alt="@@NAME@@" width="150" height="150"><h3>@@NAME@@</h3><p>Web design student</p><p class="mono">@@DEPT@@<br>Vellore Institute of Technology</p></div>
  <p class="mono" style="max-width:280px;text-align:center">Designed and coded as a front-end project. CGPA <mark>9.10</mark> · Reg. @@REG@@</p></div>
</div></section>''', nav='about.html', no='i', heading='About Junction 41',
         blurb='Who runs the trains, what is on offer, and who built this website.', tags=['nested lists', 'text formatting', 'sub / sup', 'div profile card'],
         css='.idcard{border:4px solid var(--ink);background:#fbf6ea;padding:1.6rem;text-align:center;width:280px;box-shadow:8px 8px 0 var(--signal)}.idcard img{margin:0 auto 1rem;border:3px solid var(--ink);border-radius:50%}.idcard h3{margin-bottom:.3rem}')
