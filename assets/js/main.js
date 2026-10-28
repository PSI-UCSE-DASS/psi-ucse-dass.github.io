(function () {
  var raiz = document.documentElement;

  // Modo claro / oscuro
  var temaBtn = document.querySelector('.tema-btn');
  if (temaBtn) temaBtn.addEventListener('click', function () {
    var t = raiz.dataset.theme === 'dark' ? 'light' : 'dark';
    raiz.dataset.theme = t;
    try { localStorage.setItem('tema', t); } catch (e) {}
  });

  // Menú móvil
  var menuBtn = document.querySelector('.menu-btn');
  var menu = document.getElementById('menu');
  if (menuBtn && menu) menuBtn.addEventListener('click', function () {
    var abierto = menuBtn.getAttribute('aria-expanded') === 'true';
    menuBtn.setAttribute('aria-expanded', String(!abierto));
    menu.classList.toggle('abierto', !abierto);
  });

  // Video pitch con carga diferida
  document.querySelectorAll('.video-facade').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1&rel=0';
      f.title = 'Video pitch';
      f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      f.className = 'video-iframe';
      b.replaceWith(f);
    });
  });

  // Zoom del poster en pantalla completa
  var dlg = document.querySelector('dialog.zoom');
  var link = document.querySelector('[data-zoom]');
  if (dlg && link && dlg.showModal) {
    var img = dlg.querySelector('img');
    var lienzo = dlg.querySelector('.zoom__lienzo');
    link.addEventListener('click', function (e) {
      e.preventDefault();
      img.src = link.href;
      img.alt = link.querySelector('img').alt;
      lienzo.classList.remove('ampliado');
      dlg.showModal();
    });
    img.addEventListener('click', function () { lienzo.classList.toggle('ampliado'); });
    dlg.querySelector('.zoom__cerrar').addEventListener('click', function () { dlg.close(); });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
  }

  // Compartir y copiar
  document.querySelectorAll('[data-compartir]').forEach(function (b) {
    b.addEventListener('click', function () {
      var url = b.dataset.compartir;
      if (navigator.share) { navigator.share({ title: document.title, url: url }).catch(function () {}); }
      else if (navigator.clipboard) { navigator.clipboard.writeText(url).then(function () { b.textContent = 'Enlace copiado'; }); }
    });
  });
  document.querySelectorAll('[data-copiar]').forEach(function (b) {
    b.addEventListener('click', function () {
      var el = document.querySelector(b.dataset.copiar);
      if (el && navigator.clipboard) navigator.clipboard.writeText(el.innerText).then(function () { b.textContent = 'Cita copiada'; });
    });
  });
})();
