from model.info_contact import Infos
import pytest
import random
import string
from random import randrange

def random_string(prefix,maxline):
    simvol = string.ascii_letters + string.digits + string.punctuation +' '*10
    return prefix +''.join([random.choice(simvol) for i in range (random.randrange(maxline))])



testdata=[Infos(firstname='', lastname='')] + [
    Infos(firstname=random_string('firstname',10), lastname=random_string('lastname',10),email =random_string('email',10), home = random_string('home',10),
                                middelname=random_string('middelname',10), nickname=random_string('nickname',10), title=random_string('title',10), company=random_string('company',10),
								address=random_string('address',10), mobile=random_string('mobile',10), fax=random_string('fax',10), homepage=random_string('homepage',10),
                                day_Birthday=[random.randint(1,31)],day_Anniversary=[random.randint(1,31)],
                                month_Birthday=[random.randint(1,12)],month_Anniversary=[random.randint(1,12)],
								year_Anniversary=[random.randint(1,2016)],year_Birthday=[random.randint(1,2016)],
                                address2=random_string('address2',10), phone2=random_string('phone2',10), notes=random_string('notes',10), work =random_string('work',10),
                                photo ="C:\\Users\\Alex\\Documents\\GitHub\\python_training\\home_work_3\\avatar.jpg")
for i in range (5)
]


@pytest.mark.parametrize('contact',testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Infos.id_or_max) == sorted(new_contacts, key=Infos.id_or_max)