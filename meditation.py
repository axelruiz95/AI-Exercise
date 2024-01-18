import datetime

def meditate_tracker():
    try:
        with open("meditation_history.txt", "r") as file:
            meditation_days = [datetime.datetime.strptime(line.strip(), "%Y-%m-%d").date() for line in file]
    except FileNotFoundError:
        meditation_days = []

    print("Previous meditation days:", meditation_days)
    
    today = datetime.date.today()

    if today in meditation_days:
        print("You've already meditated today. Good job!")
    else:
        print("It's time to meditate!")

        for _ in range(3):
            meditation_date_str = input("Enter the date (YYYY-MM-DD) when you meditated: ")

            try:
                meditation_date = datetime.datetime.strptime(meditation_date_str, "%Y-%m-%d").date()
                
                meditation_days.append(meditation_date)

                with open("meditation_history.txt", "a") as file:
                    file.write(meditation_date.strftime("%Y-%m-%d") + "\n")

                print(f"Meditation recorded for {meditation_date}.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    seven_days_ago = today - datetime.timedelta(days=7)
    recent_meditations = [day for day in meditation_days if seven_days_ago <= day <= today]

    if len(recent_meditations) >= 3:
        print("Congratulations! You've completed three meditations within the last 7 days.")
    else:
        print("You haven't completed three meditations within the last 7 days. Keep going!")

if __name__ == "__main__":
    meditate_tracker()