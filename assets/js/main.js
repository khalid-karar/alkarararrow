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

// Mobile menu
(function () {
  var btn = document.querySelector('.menu-btn'), nav = document.getElementById('site-nav');
  if (!btn || !nav) return;
  btn.hidden = false;
  function set(open) {
    nav.classList.toggle('open', open); btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.setAttribute('aria-label', open ? btn.dataset.close : btn.dataset.open);
  }
  btn.addEventListener('click', function () { set(!nav.classList.contains('open')); });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) set(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
})();

// Contact forms: send to the configured endpoint, or fall back to the visitor's email app.
(function () {
  document.querySelectorAll('form.form').forEach(function (form) {
    var status = form.querySelector('.status'), btn = form.querySelector('button[type="submit"]');
    function say(msg, ok) { status.textContent = msg; status.className = 'status ' + (ok ? 'ok' : 'bad'); }
    function valid() {
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (el) {
        var bad = el.type === 'checkbox' ? !el.checked : !el.value.trim() || (el.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value));
        el.setAttribute('aria-invalid', bad ? 'true' : 'false'); if (bad) ok = false;
      });
      if (!ok) { say(form.dataset.req, false); var first = form.querySelector('[aria-invalid="true"]'); if (first) first.focus(); }
      return ok;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('[name="_gotcha"]').value) return; // bot
      if (!valid()) return;
      var data = new FormData(form), endpoint = form.dataset.endpoint;
      if (!endpoint) {
        var lines = []; ['name', 'organisation', 'email', 'phone', 'division'].forEach(function (k) { if (data.get(k)) lines.push(k + ': ' + data.get(k)); });
        var body = lines.join('\n') + '\n\n' + data.get('message');
        location.href = 'mailto:' + form.getAttribute('action').replace('mailto:', '') + '?subject=' + encodeURIComponent(form.dataset.subject) + '&body=' + encodeURIComponent(body);
        return;
      }
      btn.disabled = true; say(form.dataset.sending, true);
      fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); say(form.dataset.ok, true); })
        .catch(function () { say(form.dataset.err, false); })
        .then(function () { btn.disabled = false; });
    });
  });
})();
