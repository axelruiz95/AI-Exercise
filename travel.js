function depositMoney() {
    let balance = 0;
    let monthsPassed = 0;
  
    const intervalId = setInterval(() => {
      balance += 1000;
      monthsPassed++;
  
      console.log(`1000 pesos deposited. Current balance: ${balance} pesos.`);
  
      if (monthsPassed === 12) {
        clearInterval(intervalId);
        console.log("Funds have been deposited for 12 months. Program terminated.");
      }
    }, 30 * 24 * 60 * 60 * 1000);
  }
  
  depositMoney();
  