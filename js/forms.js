document.querySelectorAll('form[data-demo]').forEach(function (f) {
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var m = f.querySelector('[data-match]');
    if (m && m.value !== document.getElementById(m.dataset.match).value) { m.setCustomValidity('Passwords do not match'); m.reportValidity(); return; }
    if (f.dataset.next) { location.href = f.dataset.next; return; }
    var box = f.querySelector('.msg'); box.className = 'msg good show'; box.textContent = f.dataset.ok || 'Done.';
  });
  var m = f.querySelector('[data-match]');
  if (m) m.addEventListener('input', function () { m.setCustomValidity(''); });
});
