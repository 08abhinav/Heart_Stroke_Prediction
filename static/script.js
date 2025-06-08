document.getElementById('strokeForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  const resultText = document.getElementById('resultText');
  const resultModal = document.getElementById('resultModal');

  try {
    const response = await fetch('/predict-stroke', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();

    if (data.error) {
      resultText.innerHTML = `<span class="text-red-500">${data.error}</span>`;
    } else {
      resultText.innerHTML = `<span class="text-green-600">Risk: ${data.risk_category} (${data.risk_percent}%)</span>`;
    }

    resultModal.classList.remove('hidden');
  } catch (error) {
    resultText.innerHTML = `<span class="text-red-500">Error: ${error.message}</span>`;
    resultModal.classList.remove('hidden');
  }
});

function closeModal() {
  document.getElementById('resultModal').classList.add('hidden');
}
