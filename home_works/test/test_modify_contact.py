from model.info_contact import Infos






def test_modify_contact_firstname(app):
	if app.contact.count() == 0:
		app.contact.link_add_new()
		app.contact.fill_form(Infos(firstname="AAAAA"))
		app.contact.input_save_form()
	if app.contact.count_modify('firstname') == 0:
		app.contact.fill_form(Infos(firstname ='1111'))
		app.contact.click_update()
		#app.contact.modify_first_contact(Infos(firstname="New firstname")) Решил не удалять пока


def test_modify_contact_month_Anniversary(app):
	if app.contact.count() == 0:
		app.contact.link_add_new()
		app.contact.fill_form(Infos(month_Anniversary="[5]"))
		app.contact.input_save_form()
	if app.contact.count_modify_amonth() == 1:
		app.contact.fill_form(Infos(month_Anniversary ="[7]"))
		app.contact.click_update()



	#app.contact.modify_first_contact(Infos(month_Anniversary="[6]"))

