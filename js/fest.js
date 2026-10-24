var f = document.getElementById('fest'), out = document.getElementById('out'), res = document.getElementById('result');
var R = { fn: /^[A-Za-z ]+$/, fr: /^REG\d{6}$/, fm: /^[A-Za-z0-9._%+-]+@vit\.ac\.in$/, fb: /^\d{10}$/ };
var T = { fn: 'Letters and spaces only.', fr: 'Must be REG followed by exactly 6 digits.', fm: 'Use the format username@vit.ac.in.', fb: 'Exactly 10 digits.' };
function say(id, t) { var e = f.querySelector('[data-for="' + id + '"]'); e.textContent = t || ''; }
f.addEventListener('submit', function (e) {
  e.preventDefault(); var bad = 0;
  Object.keys(R).forEach(function (id) { var ok = R[id].test(f[id].value.trim()); say(id, ok ? '' : T[id]); if (!ok) bad++; });
  if (!f.fd.value) { say('fd', 'Select a department.'); bad++; } else say('fd');
  var skills = []; f.querySelectorAll('input[name=int]:checked').forEach(function (c) { skills.push(c.value); });
  if (!skills.length) { say('int', 'Pick at least one interest.'); bad++; } else say('int');
  if (bad) { out.className = 'msg bad show full'; out.textContent = 'Registration failed: please correct the errors above.'; res.innerHTML = ''; return; }
  out.className = 'msg good show full'; out.textContent = 'Registration confirmed. See you at the Fest!';
  res.innerHTML = '<table><thead><tr><th>Name</th><th>Department</th><th>Interests</th></tr></thead><tbody><tr><td>' + f.fn.value.trim() + '</td><td>' + f.fd.value + '</td><td>' + skills.join(', ') + '</td></tr></tbody></table>';
});
f.addEventListener('reset', function () { out.className = 'msg full'; res.innerHTML = ''; f.querySelectorAll('.err').forEach(function (e) { e.textContent = ''; }); });
