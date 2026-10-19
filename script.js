const menuButton = document.querySelector('.menu-toggle');
const primaryNavigation = document.querySelector('.primary-nav');

if (menuButton && primaryNavigation) {
  menuButton.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!isOpen));
    menuButton.classList.toggle('active', !isOpen);
    primaryNavigation.classList.toggle('open', !isOpen);
  });

  primaryNavigation.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.classList.remove('active');
      primaryNavigation.classList.remove('open');
    });
  });
}

document.querySelectorAll('[data-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});
