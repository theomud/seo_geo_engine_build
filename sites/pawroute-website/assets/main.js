// Engine runtime — mobile nav + quote form (no backend; mailto/WhatsApp handoff).
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Quote form: assemble a message and hand off via WhatsApp / mailto. No data stored.
  document.querySelectorAll('form[data-quote]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var lines = [];
      d.forEach(function (v, k) { if (v) lines.push(k.replace(/_/g, ' ') + ': ' + v); });
      var msg = 'New pet relocation enquiry%0A' + lines.join('%0A');
      var wa = form.getAttribute('data-whatsapp');
      var email = form.getAttribute('data-email');
      if (wa) {
        window.open('https://wa.me/' + wa + '?text=' + msg, '_blank');
      } else if (email) {
        window.location.href = 'mailto:' + email + '?subject=Pet relocation enquiry&body=' + msg;
      }
      var ok = form.querySelector('[data-ok]');
      if (ok) ok.hidden = false;
    });
  });
})();
