

def test_delite_group(app):
	app.session.login( username="admin", password="secret")
	app.group.delete_first_group()
	app.session.logout()
