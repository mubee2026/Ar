
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".ar-menu-toggle");
  const menu = document.querySelector(".ar-nav-links");

  if (toggle && menu) {
    toggle.addEventListener("click", () => menu.classList.toggle("open"));
  }
});
