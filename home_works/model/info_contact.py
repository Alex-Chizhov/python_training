__author__ = 'Alex'
from sys import maxsize

class Infos:

    def __init__(self, firstname = None ,middelname = None,lastname = None,nickname = None, title = None,company = None,address = None,home = None,mobile = None,
                          fax= None,homepage = None,day_Birthday= None,month_Birthday= None,year_Birthday= None,day_Anniversary= None,
                          month_Anniversary= None,year_Anniversary= None,address2= None,phone2= None,notes= None,work= None,photo= None,id=None):


        self.firstname         = firstname
        self.middelname        = middelname
        self.lastname          = lastname
        self.nickname          = nickname
        self.title             = title
        self.company           = company
        self.address            = address
        self.home              = home
        self.mobile            = mobile
        self.fax               = fax
        self.homepage          = homepage
        self.day_Birthday      = day_Birthday
        self.month_Birthday    = month_Birthday
        self.year_Birthday     = year_Birthday
        self.day_Anniversary   = day_Anniversary
        self.month_Anniversary = month_Anniversary
        self.year_Anniversary  = year_Anniversary
        self.address2          = address2
        self.phone2            = phone2
        self.notes             = notes
        self.work              = work
        self.photo             = photo
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.lastname, self.firstname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize