// 1. Filter timetable from home-page search (?q=&cat=&price=)
var p = new URLSearchParams(location.search), q = (p.get('q') || '').toLowerCase(), cat = p.get('cat') || '', pr = p.get('price') || '';
var rows = document.querySelectorAll('#tt tbody tr'), shown = 0;
rows.forEach(function (r) {
  var fare = +r.dataset.fare, band = fare < 1000 ? 'lo' : fare <= 3000 ? 'mid' : 'hi';
  var ok = (!q || r.textContent.toLowerCase().indexOf(q) > -1) && (!cat || r.dataset.cat === cat) && (!pr || band === pr);
  r.classList.toggle('hide', !ok); if (ok) shown++;
});
document.getElementById('count').textContent = (q || cat || pr) ? shown + ' train(s) match your search' : rows.length + ' trains on the network';
// 2. Fare calculator
document.getElementById('fare').addEventListener('submit', function (e) {
  e.preventDefault(); var out = document.getElementById('fareOut'), v = ['l1', 'l2', 'l3'].map(function (id) { return document.getElementById(id).value; });
  if (v.some(function (x) { return x === '' || +x < 0; })) { out.className = 'msg bad show'; out.textContent = 'Enter a fare (0 or more) for every leg.'; return; }
  var t = v.reduce(function (a, b) { return a + +b; }, 0);
  out.className = 'msg good show'; out.innerHTML = 'Total: ₹' + t.toLocaleString('en-IN') + '<br>Average per leg: ₹' + (t / 3).toFixed(2);
});
// 3. Scenic viewer (keyboard)
var places = [['travel-goa', 'Goa coast'], ['travel-jaipur', 'Jaipur'], ['travel-munnar', 'Munnar hills'], ['travel-kashmir', 'Kashmir valley']], k = 0;
var im = document.getElementById('trv'), tm = document.getElementById('trvMsg');
function show(n) { k = (n + places.length) % places.length; im.src = 'img/' + places[k][0] + '.svg'; tm.textContent = ''; }
document.addEventListener('keydown', function (e) {
  if (/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) return;
  var c = e.key.toLowerCase();
  if (c === 'n') show(k + 1); else if (c === 'p') show(k - 1);
  else if (e.key === ' ') { e.preventDefault(); tm.textContent = 'Destination: ' + places[k][1]; }
});
