from django.utils.translation import gettext as _


class MoveResultType(object):
    BUY_LAND_OPTION = 0
    PAYMENT = 1
    REWARD = 2
    STOP_ROUND = 3
    CONSTRUCTION_OPTION = 4
    NOTHING = 5

    @staticmethod
    def get_description(val):
        ret = [
            _("is choosing to buy or not. "),
            _("should make a payment. "),
            _("is rewarded a fortune. "),
            _("is stopped for one round. "),
            _("is choosing to build a new building or not. "),
            _("Nothing actually happened. ")
        ]
        return ret[val]
