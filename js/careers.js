var eid = document.getElementById('eid'), er = document.getElementById('eidErr');
eid.addEventListener('input', function () {
  var ok = /^EMP\d{4}$/.test(eid.value);
  eid.setCustomValidity(ok ? '' : 'Use EMP followed by exactly four digits');
  er.textContent = !eid.value ? '' : ok ? '✓ valid ID' : 'Format: EMP + 4 digits (e.g. EMP1234)';
});
