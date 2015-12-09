from model.group import Group

def test_delete_group(app):
	if app.group.count() == 0:
		app.group.creator(Group(name ='New Name Test'))
	app.group.delete_first_group()

