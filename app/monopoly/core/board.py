from django.utils.translation import gettext as _
from land import *


class Board(object):

    def __init__(self):
        self._lands = []
        self.generate_lands()

    def get_lands(self):
        return self._lands

    def get_land(self, index):
        return self._lands[index]

    def generate_lands(self):
        self._lands.append(Land(0, _("Start"), StartLand(START_REWARD)))
        self._lands.append(Land(1, _("Warner Hall"), ConstructionLand(60)))
        self._lands.append(Land(2, _("Community Chest"), ChestLand()))
        self._lands.append(Land(3, _("UC"), ConstructionLand(60)))
        self._lands.append(Land(4, _("Union Grill"), TaxLand(200)))
        self._lands.append(Land(5, _("AB route"), Infra(200)))
        self._lands.append(Land(6, _("College of Fine Art"), ConstructionLand(100)))
        self._lands.append(Land(7, _("Chance"), ChanceLand()))
        self._lands.append(Land(8, _("Posner Hall"), ConstructionLand(100)))
        self._lands.append(Land(9, _("Hunt Library"), ConstructionLand(120)))
        self._lands.append(Land(10, _("AIV Jail"), VisitingJailLand(0)))
        self._lands.append(Land(11, _("Doherty Hall"), ConstructionLand(140)))
        self._lands.append(Land(12, _("Entropy+"), Infra(150)))
        self._lands.append(Land(13, _("Gasling Stadium"), ConstructionLand(140)))
        self._lands.append(Land(14, _("Margaret Morrison Carnegie Hall"), ConstructionLand(160)))
        self._lands.append(Land(15, _("Escort"), Infra(200)))
        self._lands.append(Land(16, _("Hamerschlag Hall"), ConstructionLand(180)))
        self._lands.append(Land(17, _("Community Chest"), ChestLand()))
        self._lands.append(Land(18, _("Roberts Engineering Hall"), ConstructionLand(180)))
        self._lands.append(Land(19, _("Porter Hall"), ConstructionLand(200)))
        self._lands.append(Land(20, _("Parking"), ParkingLand()))
        self._lands.append(Land(21, _("Gates Center"), ConstructionLand(220)))
        self._lands.append(Land(22, _("Chance"), ChanceLand()))
        self._lands.append(Land(23, _("Newell-Simon Hall"), ConstructionLand(220)))
        self._lands.append(Land(24, _("Wean Hall"), ConstructionLand(240)))
        self._lands.append(Land(25, _("PTC"), Infra(200)))
        self._lands.append(Land(26, _("Baker Hall"), ConstructionLand(260)))
        self._lands.append(Land(27, _("Fence"), ConstructionLand(260)))
        self._lands.append(Land(28, _("iNoodle"), Infra(150)))
        self._lands.append(Land(29, _("Purnell Center"), ConstructionLand(280)))
        self._lands.append(Land(30, _("AIV Jail"), JailLand(1)))
        self._lands.append(Land(31, _("Hamburg Hall"), ConstructionLand(300)))
        self._lands.append(Land(32, _("Collaborative Innovation Center"), ConstructionLand(300)))
        self._lands.append(Land(33, _("Community Chest"), ChestLand()))
        self._lands.append(Land(34, _("Cyert Hall"), ConstructionLand(320)))
        self._lands.append(Land(35, _("Monorail"), Infra(200)))
        self._lands.append(Land(36, _("Chance"), ChanceLand()))
        self._lands.append(Land(37, _("Information Networking Institute"), ConstructionLand(350)))
        self._lands.append(Land(38, _("Pasta Vilaggio"), TaxLand(100)))
        self._lands.append(Land(39, _("Mellon Institute"), ConstructionLand(400)))


    def get_grid_num(self):
        return len(self._lands)


def test():
    b = Board()
    assert b.get_land(1).get_position() == 1
    assert b.get_land(10).get_content().get_type() == LandType.JAIL


if __name__ == "__main__":
    test()
