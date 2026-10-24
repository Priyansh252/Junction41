var d; try { d = JSON.parse(sessionStorage.getItem('j41')); } catch (e) {}
d = d || { name: 'Guest', train: 'Nilgiri Whistle · Mettupalayam → Ooty', fare: 650, pax: 1, prefs: [] };
var lines = [[d.train, d.pax, d.fare], ['Reservation fee', d.pax, 40]];
if (d.prefs.indexOf('Vegetarian meal') > -1) lines.push(['Vegetarian meal', d.pax, 180]);
if (d.prefs.indexOf('Travel insurance') > -1) lines.push(['Travel insurance', d.pax, 49]);
if (d.prefs.indexOf('Extra luggage') > -1) lines.push(['Extra luggage', 1, 150]);
var sub = 0, html = '';
lines.forEach(function (l) { var t = l[1] * l[2]; sub += t; html += '<tr><td>' + l[0] + '</td><td>' + l[1] + '</td><td>₹' + l[2] + '</td><td>₹' + t + '</td></tr>'; });
var gst = Math.round(sub * 0.05); html += '<tr><td>GST (5%)</td><td>1</td><td>₹' + gst + '</td><td>₹' + gst + '</td></tr>';
document.getElementById('rows').innerHTML = html; document.getElementById('grand').textContent = '₹' + (sub + gst).toLocaleString('en-IN');
document.getElementById('place').onclick = function () { var m = document.getElementById('m'); m.className = 'msg good show'; m.textContent = 'Order placed for ' + d.name + '. Your e-ticket is on its way.'; };
