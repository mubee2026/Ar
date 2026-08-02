document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".ar-menu-toggle");
  const menu = document.querySelector(".ar-nav-links");

  if (!toggle || !menu) return;

  const closeMenu = () => {
    menu.classList.remove("open");
    document.body.classList.remove("mobile-menu-open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.textContent = "☰";
  };

  const openMenu = () => {
    menu.classList.add("open");
    document.body.classList.add("mobile-menu-open");
    toggle.setAttribute("aria-expanded", "true");
    toggle.textContent = "×";
  };

  toggle.setAttribute("aria-expanded", "false");

  toggle.addEventListener("click", () => {
    if (menu.classList.contains("open")) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  menu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("click", (event) => {
    if (
      window.innerWidth <= 960 &&
      menu.classList.contains("open") &&
      !menu.contains(event.target) &&
      !toggle.contains(event.target)
    ) {
      closeMenu();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 960) closeMenu();
  });
});
