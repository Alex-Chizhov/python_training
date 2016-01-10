from model.info_contact import Infos


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact =(Infos(firstname="qq", middelname="qq", lastname="qq", nickname="qq", title="qq", company="qq",
								address="ww", home="11", mobile="22", fax="22", homepage="wewr.ru", day_Birthday="[7]",
								month_Birthday="[10]", year_Birthday="1980", day_Anniversary="[18]", month_Anniversary="[7]",
								email='asf@mail.ru',email2='1233@mail.ru',email3='!!!!@mail.ru',
								year_Anniversary="2000", address2="12", phone2="12", notes="12", work ='qwe', photo ="C:\\Users\\Alex\\Documents\\GitHub\\python_training\\home_work_3\\avatar.jpg"))
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Infos.id_or_max) == sorted(new_contacts, key=Infos.id_or_max)
