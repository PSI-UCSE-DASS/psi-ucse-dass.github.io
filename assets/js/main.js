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
  // Descarga del QR con título y autores debajo (sin JS se descarga el QR solo)
  document.querySelectorAll('[data-qr-descarga]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var img = a.parentNode.querySelector('img');
      if (!img || !img.complete) return;
      e.preventDefault();
      var W = 1200, M = 80, qr = 640, y = M;
      var c = document.createElement('canvas'), x = c.getContext('2d');
      var ff = 'Montserrat, Roboto, Arial, sans-serif';
      var lineas = function (txt, font, ancho) {
        x.font = font;
        var out = [], l = '';
        txt.split(' ').forEach(function (p) {
          var t = l ? l + ' ' + p : p;
          if (x.measureText(t).width > ancho && l) { out.push(l); l = p; } else { l = t; }
        });
        if (l) out.push(l);
        return out;
      };
      var fT = '700 52px ' + ff, fA = '400 40px ' + ff, fU = '400 32px ' + ff;
      var T = lineas(a.dataset.titulo, fT, W - 2 * M), A = lineas(a.dataset.autores, fA, W - 2 * M);
      c.width = W;
      c.height = M + qr + 60 + T.length * 66 + 20 + A.length * 54 + 30 + 44 + M;
      x.fillStyle = '#fff'; x.fillRect(0, 0, c.width, c.height);
      x.imageSmoothingEnabled = false;
      x.drawImage(img, (W - qr) / 2, y, qr, qr); y += qr + 60;
      x.fillStyle = '#0B2A55'; x.textAlign = 'center'; x.textBaseline = 'top';
      x.font = fT; T.forEach(function (l) { x.fillText(l, W / 2, y); y += 66; });
      y += 20; x.fillStyle = '#333'; x.font = fA;
      A.forEach(function (l) { x.fillText(l, W / 2, y); y += 54; });
      y += 30; x.fillStyle = '#555'; x.font = fU; x.fillText(a.dataset.url, W / 2, y);
      c.toBlob(function (b) {
        var u = URL.createObjectURL(b), d = document.createElement('a');
        d.href = u; d.download = a.getAttribute('download'); document.body.appendChild(d); d.click();
        d.remove(); setTimeout(function () { URL.revokeObjectURL(u); }, 1000);
      });
    });
  });
})();
