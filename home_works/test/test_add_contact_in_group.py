from model.group import Group
from model.info_contact import Infos
import random


def test_add_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    index = 0
    for m in groups:
        if m.id == group.id:
            return index
        index = index+1
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Infos(firstname="Firstname"))
    contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.add_contact_in_group(index+1, contact)
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Infos.id_or_max) == sorted(new_contacts, key=Infos.id_or_max)