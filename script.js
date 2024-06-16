document.getElementById('wine-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const formProps = Object.fromEntries(formData);

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formProps)
    });

    const result = await response.json();
    document.getElementById('result').innerText = 'Predicted Quality: ' + result.quality;
});