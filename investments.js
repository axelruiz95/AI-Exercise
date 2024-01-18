function reserveMoney() {
    let savings = 0;

    for (let month = 1; month <= 12; month++) {
        try {
            let monthlyContribution = parseFloat(prompt(`Enter the amount to reserve for month ${month}: $`));
            if (isNaN(monthlyContribution)) {
                throw new Error("Invalid input. Please enter a valid numeric value.");
            }

            // Apply a 2% growth each month
            savings += monthlyContribution;
            savings *= 1.02;

            console.log(`Total savings after month ${month}: $${savings.toFixed(2)}`);
        } catch (error) {
            console.log(error.message);
            month--; // Repeat the current iteration if there's an error
        }
    }
}

reserveMoney();
