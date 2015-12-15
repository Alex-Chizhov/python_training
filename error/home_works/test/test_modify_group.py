from model.group import Group


def test_modify_gname(app):
	old_groups = app.group.get_group_list()
	group = Group(name= 'New Group')
	group.id = old_groups[0].id
	app.group.modify_first_group(group)
	new_groups = app.group.get_group_list()
	assert len(old_groups) == len(new_groups)
	old_groups[0]= group
	assert  sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)










def test_modify_group_name(app):
	if app.group.count() == 0:
		app.group.creator(Group(name ='New Name Test'))
	if app.group.count_modify('group_name') == 0:
		app.group.fill_group_form(Group(name ='1111New neme1111'))
		app.group.click_update()
		#app.group.modify_first_group(Group(name="New group"))  Решил не удалять пока




def test_modify_group_header(app):
	if app.group.count() == 0:
		app.group.creator(Group(header ='New header Test'))
	if app.group.count_modify('group_header') == 0:
		app.group.fill_group_form(Group(header ='222New header222'))
		app.group.click_update()
