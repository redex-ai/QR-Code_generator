document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('qr-form');
  const urlInput = document.getElementById('url-input');

  form.addEventListener('submit', function(event) {
    const urlValue = urlInput.value.trim();
    if (!isValidHttpUrl(urlValue)) {
      event.preventDefault();
      alert('Please enter a valid URL.');
    }
  });

  function isValidHttpUrl(string) {
    let url;

    try {
      url = new URL(string);
    } catch (_) {
      return false;  
    }

    return url.protocol === 'http:' || url.protocol === 'https:';
  }
});