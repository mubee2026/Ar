
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');
if (toggle && nav) toggle.addEventListener('click', () => nav.classList.toggle('open'));

document.querySelectorAll('[data-year]').forEach(el => {
  el.textContent = new Date().getFullYear();
});

document.querySelectorAll('form[data-demo-form]').forEach(form => {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const box = form.querySelector('.form-message');
    if (box) {
      box.hidden = false;
      box.textContent = 'Thank you. Connect this form to the AR Solutions sales email or CRM before publishing.';
    }
  });
});
