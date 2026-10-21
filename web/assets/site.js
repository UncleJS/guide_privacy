/* Online Privacy Guide - tiny site script. No dependencies. */
(function () {
  'use strict';

  var THEME_KEY = 'privacy-guide-theme';
  var root = document.documentElement;

  // Theme toggle (dark is the default; the saved choice is applied in <head>).
  var toggle = document.getElementById('theme-toggle');
  function setLabel() {
    if (!toggle) return;
    var dark = root.getAttribute('data-theme') !== 'light';
    toggle.textContent = dark ? 'Light mode' : 'Dark mode';
    toggle.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
  }
  setLabel();
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
      setLabel();
    });
  }

  // Mobile menu.
  var menu = document.getElementById('menu-toggle');
  if (menu) {
    menu.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      menu.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Checklists: remember ticked items on this device only.
  var page = location.pathname.split('/').pop() || 'index.html';
  var boxes = document.querySelectorAll('li.task input[type="checkbox"]');
  Array.prototype.forEach.call(boxes, function (box, i) {
    var key = 'privacy-guide-check:' + page + ':' + i;
    try { box.checked = localStorage.getItem(key) === '1'; } catch (e) {}
    box.addEventListener('change', function () {
      try {
        if (box.checked) localStorage.setItem(key, '1');
        else localStorage.removeItem(key);
      } catch (e) {}
    });
  });
})();
