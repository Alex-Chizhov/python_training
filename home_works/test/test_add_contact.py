from model.info_contact import Infos

def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Infos.id_or_max) == sorted(new_contacts, key=Infos.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean, new_contacts), key=Infos.id_or_max) == sorted(app.contact.get_contact_list(), key=Infos.id_or_max)
