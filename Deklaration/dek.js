document.getElementById("taxForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const income = parseFloat(document.getElementById("income").value);
  const resultDiv = document.getElementById("result");

  if (isNaN(income) || income < 0) {
    resultDiv.textContent = "Ange en giltig inkomst.";
    return;
  }

  let tax = 0;

  // Förenklad skatteberäkning
  if (income <= 20000) {
    tax = 0;
  } else if (income <= 400000) {
    tax = income * 0.3;
  } else {
    tax = income * 0.5;
  }

  resultDiv.innerHTML = `Din beräknade skatt är <strong>${Math.round(tax).toLocaleString()} kr</strong>.`;
});

// Kontaktformulär (förenklad validering)
document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  alert("Tack för ditt meddelande! Vi återkommer inom kort.");
  this.reset();
});
