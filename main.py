import flight_search
import data_manager
import notification_manager


def check(info):
    if int(info[0]) <= city['lowestPrice']:
        return True
    else:
        return False


search = flight_search.FlightSearch()
data = data_manager.DataManager()
sms = notification_manager.NotificationManager()

all_data_to_search = data.read_all()
receivers = data.read_users()

for city in all_data_to_search:
    iata_code = search.iata(city["city"])
    info = search.find_plane(iata_code)

    try:
        if check(info):
            sms.send_emails(info, receivers)
    except TypeError:
        info = search.find_plane(iata_code, max_stopovers=2)
        if info is not None:
            if check(info):
                sms.send_emails(info, receivers)
    else:
        pass
