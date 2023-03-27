import csv


def file_saver(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        users_list = args[0]._users
        with open('database.user.csv', 'w') as file:
            csv_writer = csv.DictWriter(f=file, delimiter='|', fieldnames=users_list[0].as_dict().keys())
            csv_writer.writeheader()
            for user in users_list:
                csv_writer.writerow(user.as_dict())
        return res
    return wrapper




