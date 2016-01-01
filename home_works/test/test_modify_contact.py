from model.info_contact import Infos



def test_add_modify_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Infos(firstname = "AAAA", lastname="BBBBB", day_Birthday="[2]")
    if app.contact.count() == 0:
        app.contact.create(contact)
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Infos.id_or_max) == sorted(new_contacts, key=Infos.id_or_max)

