var h = document.getElementById('hello'), hb = document.getElementById('hb'), orig = h.textContent;
hb.addEventListener('mouseover', function () { h.textContent = 'Welcome to VIT!'; });
hb.addEventListener('mouseout', function () { h.textContent = orig; });
