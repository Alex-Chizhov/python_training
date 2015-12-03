from model.info_contact import Infos








def test_modify_contact_firstname(app):
	app.contact.modify_first_contact(Infos(firstname="New firstname"))

def test_modify_contact_month_Anniversary(app):
	app.contact.modify_first_contact(Infos(month_Anniversary="[6]"))

