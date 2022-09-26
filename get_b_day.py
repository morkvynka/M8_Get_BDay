from datetime import datetime, timedelta

# test-list of users
users = [{"name": "Oleksiy", "birthday": datetime(year=1993, month=2, day=16)},
         {"name": "Viktoriia", "birthday": datetime(
             year=1989, month=5, day=18)},
         {"name": "Andriy", "birthday": datetime(year=1995, month=8, day=5)},
         {"name": "Hrystyna", "birthday": datetime(
             year=1990, month=9, day=30)},
         {"name": "Oleg", "birthday": datetime(year=1991, month=1, day=3)},
         {"name": "Dmytro", "birthday": datetime(year=1988, month=6, day=14)},
         {"name": "Dariia", "birthday": datetime(year=1995, month=10, day=5)},
         {"name": "Yaroslava", "birthday": datetime(year=1992, month=10, day=3)}]


def find_days_delta(today: datetime) -> timedelta:

    if today.weekday() == 5:
        days_delta = timedelta(days=6)
    elif today.weekday() == 6:
        days_delta = timedelta(days=5)
    else:
        days_delta = timedelta(days=7)

    return days_delta


def get_birthdays_per_week(users: list):
    bday_users_list = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }
    today = datetime.now()
    delta = find_days_delta(today)
    new_delta = today + delta

    for user in users:
        new_bd_date = datetime(
            year=today.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )

        if today < new_bd_date <= new_delta:
            weekday = new_bd_date.strftime("%A")
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            bday_users_list.get(weekday).append(user.get('name'))

    for key, value in bday_users_list.items():
        if value:
            print(f"{key}: {', '.join(value)}")


if __name__ == '__main__':
    get_birthdays_per_week(users)
