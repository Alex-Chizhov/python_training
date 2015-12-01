class GroupHelper:

	def __init__(self,app):
		self.app = app

	def return_to_group_page(self):
		wd = self.app.wd
		wd.find_element_by_link_text("group page").click()

	def creator(self, group):
		wd = self.app.wd
		# open_gp
		wd.find_element_by_link_text("groups").click()
		# init_group_creator
		wd.find_element_by_name("new").click()
		self.fill_group_form(group)
		# sumbit_creation_group
		wd.find_element_by_name("submit").click()
		self.return_to_group_page()

	def fill_group_form(self, group):
		wd = self.app.wd
		self.change_field_value('group_name', group.name)
		self.change_field_value('group_header', group.header)
		self.change_field_value('group_footer', group.footer)

	def change_field_value(self, field_name, text):
		wd = self.app.wd
		if text is not None:
			wd.find_element_by_name(field_name).click()
			wd.find_element_by_name(field_name).clear()
			wd.find_element_by_name(field_name).send_keys(text)

	def delete_first_group(self):
		wd = self.app.wd
		# link group page
		wd.find_element_by_link_text("groups").click()
		self.select_first_group()
		# Delite
		wd.find_element_by_name("delete").click()
		self.return_to_group_page()


	def select_first_group(self):
		wd = self.app.wd
		wd.find_element_by_name("selected[]").click()

	def modify_first_group(self, new_group_data):
		wd = self.app.wd
		wd.find_element_by_link_text("groups").click()
		self.select_first_group()
		# open modification form
		wd.find_element_by_name("edit").click()
		# fill form
		self.fill_group_form(new_group_data)
		# sumbit modification
		wd.find_element_by_name("update").click()
		self.return_to_group_page()
