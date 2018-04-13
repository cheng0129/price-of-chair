from src.common.database import Database
from src.models.alerts.alert import Alert


# Database.initialize()
# # print("something has to be changed")
# alerts_needing_update = Alert.find_needing_update()
#
#
# for alert in alerts_needing_update:
#     # print("email sent for test!")
#     alert.load_item_price()
#     alert.send_email_if_price_reached()

def runASample():
    Database.initialize()
    print("something has to be changed")
    alerts_needing_update = Alert.find_needing_update()

    for alert in alerts_needing_update:
        print("email sent for test!")
        alert.load_item_price()
        alert.send_email_if_price_reached()
