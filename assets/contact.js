// Reveal only when Netlify has processed and registered the static HTML form.
// Email links remain available with JavaScript disabled or form detection off.
const form = document.getElementById('opportunity-form');
if (form && !form.hasAttribute('data-netlify') && form.querySelector('[name="form-name"]')) {
  form.hidden = false;
}
