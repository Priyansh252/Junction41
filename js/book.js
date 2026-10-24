var NAME = /^[A-Za-z ]+$/, PASSNO = /^JN\d{6}$/, MAIL = /^[^\s@]+@[^\s@]+\.[A-Za-z]{2,}$/, MOBILE = /^\d{10}$/;
var f = document.getElementById('bk'), out = document.getElementById('out'), res = document.getElementById('result');
function say(id, t) { var e = f.querySelector('[data-for="' + id + '"]'); if (e) e.textContent = t || ''; }
f.addEventListener('submit', function (e) {
  e.preventDefault(); var bad = 0;
  function chk(id, ok, t) { say(id, ok ? '' : t); if (!ok) bad++; }
  var tr = f.tr.value, nm = f.nm.value.trim(), jp = f.jp.value.trim();
  chk('tr', tr, 'Choose a train.'); chk('dt', f.dt.value, 'Pick a travel date.');
  chk('nm', NAME.test(nm), 'Name: letters and spaces only.'); chk('jp', !jp || PASSNO.test(jp), 'Format: JN followed by 6 digits.');
  chk('em', MAIL.test(f.em.value), 'Enter a valid email.'); chk('mb', MOBILE.test(f.mb.value), 'Exactly 10 digits.');
  if (bad) { out.className = 'msg bad show full'; out.textContent = 'Please fix the highlighted fields.'; res.innerHTML = ''; return; }
  var prefs = []; f.querySelectorAll('input[name=pref]:checked').forEach(function (c) { prefs.push(c.value); });
  var train = f.tr.options[f.tr.selectedIndex].text, fare = +f.tr.value;
  var data = { name: nm, train: train, fare: fare, pax: +f.px.value, date: f.dt.value, prefs: prefs };
  try { sessionStorage.setItem('j41', JSON.stringify(data)); } catch (x) {}
  out.className = 'msg good show full'; out.textContent = 'Details confirmed. Review them below, then continue to payment.';
  res.innerHTML = '<table><thead><tr><th>Passenger</th><th>Train</th><th>Date</th><th>Preferences</th></tr></thead><tbody><tr><td>' + nm + ' ×' + data.pax + '</td><td>' + train + '</td><td>' + data.date + '</td><td>' + (prefs.length ? prefs.join(', ') : 'None') + '</td></tr></tbody></table><p style="margin-top:1rem"><a class="btn" href="payment.html">Continue to payment →</a></p>';
});
f.addEventListener('reset', function () { out.className = 'msg full'; res.innerHTML = ''; f.querySelectorAll('.err').forEach(function (e) { e.textContent = ''; }); });
