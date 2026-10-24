// Username / password: empty checks + regular expressions
var USER = /^([A-Za-z][A-Za-z0-9_]{3,15}|[^@\s]+@[^@\s]+\.[A-Za-z]{2,})$/;
var PASS = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
document.querySelectorAll('form[data-auth]').forEach(function (f) {
  var inputs = f.querySelectorAll('input:not([type=radio]):not([type=checkbox])'), u = inputs[0], p = inputs[1], box = f.querySelector('.msg');
  f.addEventListener('submit', function (e) {
    e.preventDefault(); var errs = [];
    if (!u.value.trim()) errs.push('Username cannot be empty.');
    else if (!USER.test(u.value.trim())) errs.push('Username: 4-16 letters/digits/underscore starting with a letter, or a valid email.');
    if (!p.value) errs.push('Password cannot be empty.');
    else if (!PASS.test(p.value)) errs.push('Password needs 8+ characters with upper-case, lower-case and a digit.');
    box.className = 'msg show ' + (errs.length ? 'bad' : 'good');
    box.innerHTML = errs.length ? errs.join('<br>') : 'Welcome aboard, ' + u.value.trim() + '!';
  });
  f.addEventListener('reset', function () { box.className = 'msg'; });
});
