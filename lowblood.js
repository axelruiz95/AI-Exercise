function checkBloodPressure(pressure) {
    if (pressure < 90) {
      return "Low blood pressure. It is recommended to consult a doctor.";
    } else if (pressure >= 90 && pressure <= 120) {
      return "Normal blood pressure.";
    } else {
      return "High blood pressure. It is recommended to consult a doctor.";
    }
  }
  
  try {
    const enteredPressure = parseFloat(prompt("Enter the blood pressure value:"));
    const resultMessage = checkBloodPressure(enteredPressure);
    console.log(resultMessage);
  } catch (error) {
    console.log("Please enter a valid numeric value.");
  }
  