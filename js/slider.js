(function () {
  var s = document.querySelectorAll('#slider .slide'), d = document.getElementById('dots'), i = 0, t;
  if (!s.length) return;
  s.forEach(function (_, k) { var e = document.createElement('i'); e.onclick = function () { go(k); }; d.appendChild(e); });
  function go(k) { i = (k + s.length) % s.length; s.forEach(function (x, j) { x.classList.toggle('on', j === i); d.children[j].classList.toggle('on', j === i); }); clearInterval(t); t = setInterval(function () { go(i + 1); }, 5500); }
  document.getElementById('prev').onclick = function () { go(i - 1); };
  document.getElementById('next').onclick = function () { go(i + 1); };
  go(0);
})();
