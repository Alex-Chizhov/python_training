from model.info_contact import Infos
from random import randrange


def test_modify_some_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Infos(firstname = "AAAA", lastname="BBBBB", day_Birthday="[2]")
    if app.contact.count() == 0:
        app.contact.create(contact)
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Infos.id_or_max) == sorted(new_contacts, key=Infos.id_or_max)

