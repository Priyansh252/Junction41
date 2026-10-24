// Signals
var msg = document.getElementById('sigMsg');
document.querySelectorAll('.bulb').forEach(function (b) {
  b.addEventListener('mouseover', function () { b.classList.add('lit'); msg.textContent = b.dataset.msg; });
  b.addEventListener('mouseout', function () { b.classList.remove('lit'); msg.textContent = 'Hover a lamp'; });
});
// Seats
var sm = document.getElementById('seatMsg');
document.querySelectorAll('.seat').forEach(function (s) {
  s.addEventListener('mouseover', function () { sm.textContent = 'Seat ' + s.dataset.s + ' · ' + s.dataset.w + (s.classList.contains('taken') ? ' · taken' : ''); });
  s.addEventListener('mouseleave', function () { sm.textContent = 'Hover a seat. Click to choose.'; });
  s.addEventListener('click', function () { if (!s.classList.contains('taken')) { s.classList.toggle('sel'); var n = document.querySelectorAll('.seat.sel'); sm.textContent = n.length + ' seat(s) selected'; } });
});
// Coach card
var img = document.getElementById('pimg'), info = document.getElementById('pinfo');
img.addEventListener('mouseover', function () { img.classList.add('hot'); info.classList.add('show'); });
img.addEventListener('mouseout', function () { img.classList.remove('hot'); info.classList.remove('show'); });
document.getElementById('pbtn').addEventListener('click', function () { document.getElementById('pdet').textContent = 'Fare ₹1,850 per seat · 12 seats available'; });
