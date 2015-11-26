
def test_delite_group(app):
	app.session.login( username="admin", password="secret")
	app.contact.delete_first_contact()
	app.session.logout()

