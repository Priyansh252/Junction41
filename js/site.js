(function () {
  var b = document.getElementById('menuBtn'), n = document.getElementById('nav');
  if (b) b.addEventListener('click', function () { n.classList.toggle('open'); });
})();
