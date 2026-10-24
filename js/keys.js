// Train search
var ss = document.getElementById('ssKey') && document.getElementById('ss');
var key = document.getElementById('ssKey'), echo = document.getElementById('ssEcho'), sm = document.getElementById('ssMsg');
ss.addEventListener('keydown', function (e) {
  key.textContent = 'Key pressed: ' + (e.key === ' ' ? 'Space' : e.key);
  ss.classList.add('typing');
  if (e.key === 'Enter') sm.textContent = 'Searching for: ' + ss.value + '…';
  if (e.key === 'Escape') { ss.value = ''; echo.textContent = ''; sm.textContent = ''; ss.classList.remove('typing'); }
});
ss.addEventListener('keyup', function () { echo.textContent = ss.value ? 'You typed: ' + ss.value : ''; if (!ss.value) ss.classList.remove('typing'); });
// PIN
var pin = document.getElementById('pin'), pm = document.getElementById('pinMsg');
pin.addEventListener('keydown', function (e) {
  if (e.key === 'Enter') { pm.textContent = 'PIN Submitted Successfully'; return; }
  if (e.key.length > 1) return; // Backspace, arrows, Tab...
  if (!/\d/.test(e.key)) { e.preventDefault(); pm.textContent = 'Warning: digits only'; return; }
  pm.textContent = 'PIN Entry Started';
});
// Poll
var opts = document.querySelectorAll('.opt'), sub = document.getElementById('sub'), ex = document.getElementById('exMsg'), chosen = null;
opts.forEach(function (o) {
  o.addEventListener('click', function () { opts.forEach(function (x) { x.classList.remove('sel'); }); o.classList.add('sel'); chosen = o; ex.textContent = 'Selected: ' + o.textContent + '. Press Enter to submit.'; });
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Enter' && document.activeElement !== ss && document.activeElement !== pin) ex.textContent = chosen ? 'Answer Submitted Successfully' : 'Please select an option first';
});
sub.addEventListener('mouseover', function () { sub.classList.add('hi'); });
sub.addEventListener('mouseout', function () { sub.classList.remove('hi'); });
sub.addEventListener('click', function () { ex.textContent = chosen ? 'Answer Submitted Successfully' : 'Please select an option first'; });
