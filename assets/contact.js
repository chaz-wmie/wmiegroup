// Reveal only when Netlify has processed and registered the static HTML form.
// Email links remain available with JavaScript disabled or form detection off.
const form = document.getElementById('opportunity-form');
if (form && !form.hasAttribute('data-netlify') && form.querySelector('[name="form-name"]')) {
  form.hidden = false;
}

// Carry the data center CTA's inquiry type into the existing submitted field.
if (form && new URLSearchParams(window.location.search).get('service') === 'data-center-infrastructure') {
  const inquiry = form.querySelector('[name="inquiry"]');
  const industry = form.querySelector('[name="industry"]');
  if (inquiry) inquiry.value = 'AI & Data Center Infrastructure';
  if (industry) industry.value = 'AI & Data Centers';
  // Direct email stays contextual when the optional form is unavailable.
  document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
    link.href += '?subject=' + encodeURIComponent('AI & Data Center Infrastructure Inquiry');
  });
}
