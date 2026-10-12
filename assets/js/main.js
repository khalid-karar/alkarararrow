(function () {
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header: gains a solid edge once the page scrolls.
  var header = d.querySelector('header.site');
  function onScroll() { if (header) header.classList.toggle('scrolled', window.scrollY > 8); }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  // Scroll reveal: elements fade up once as they enter the viewport.
  if (reduce || !('IntersectionObserver' in window)) { root.classList.remove('js'); return; }
  var sel = '.hero .wrap > div > *, .hero-art, .page-hero .wrap > *, section .wrap > .stack, section .wrap > h2,' +
            ' .card, .principle, .rows > div, .work, .cta .wrap > *, section .wrap > .btns, .prose > *';
  var els = d.querySelectorAll(sel);
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
  els.forEach(function (el) {
    var i = Array.prototype.indexOf.call(el.parentNode.children, el);
    el.style.setProperty('--d', Math.min(i, 5) * 90 + 'ms');
    el.classList.add('rv'); io.observe(el);
  });
})();
