import time

def deposit_money():
    balance = 0
    months_passed = 0

    while months_passed < 12:
        balance += 1000
        months_passed += 1
        print(f'1000 pesos deposited. Current balance: {balance} pesos.')
        
        time.sleep(30 * 24 * 60 * 60)

    print("Funds have been deposited for 12 months. Program terminated.")

if __name__ == "__main__":
    deposit_money()