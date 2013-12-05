from nose.tools import *
from abakaffe.lib import Abakaffe
from datetime import timedelta


class test_status_suite():

    def test_no_coffee_today(self):
        time_delta = timedelta(1)
        eq_("Det er ingen som har traktet kaffe i dag.",
                    Abakaffe.get_status(time_delta))
