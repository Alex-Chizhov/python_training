from model.info_contact import Infos

def test_delite_group(app):
	if app.contact.count() == 0:
		app.contact.link_add_new()
		app.contact.fill_form(Infos(firstname="AAAAA"))
		app.contact.input_save_form()
	app.contact.delete_first_contact()



