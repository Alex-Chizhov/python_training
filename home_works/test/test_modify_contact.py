from model.info_contact import Infos
import random

def test_mod_somecontact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_(Infos(firstname='test'))
    old_conts = db.get_contact_list()
    contact = random.choice(old_conts)
    app.contact.edit_contact_by_id(contact.id)
    new_conts = db.get_contact_list()
    assert len(old_conts) == len(new_conts)
    if check_ui:
        assert sorted(new_conts, key=Infos.id_or_max) == sorted(app.contact.get_conts_lst(), key=Infos.id_or_max)

