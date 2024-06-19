from django.utils.translation import gettext as _


class ModalTitleType():
    @staticmethod
    def get_description(val):
        ret = [
            _("Purchase Land"),
            _("Make a Payment"),
            _("Get Reward"),
            _("Stop One Round"),
            _("Build a House"),
            _("Nothing actually happened")
        ]
        return ret[val]
