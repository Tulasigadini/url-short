document.addEventListener('DOMContentLoaded', function() {
    const copyBtn = document.getElementById('copy-btn');
    const shortUrl = document.getElementById('short-url');

    if (copyBtn && shortUrl) {
        copyBtn.addEventListener('click', function() {
            navigator.clipboard.writeText(shortUrl.textContent).then(() => {
                alert('Short URL copied to clipboard!');
            }).catch(err => {
                console.error('Failed to copy: ', err);
            });
        });
    }
});