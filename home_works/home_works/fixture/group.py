from model.group import Group
class GroupHelper:

	def __init__(self,app):
		self.app = app

	def return_to_group_page(self):
		wd = self.app.wd
		wd.find_element_by_link_text("group page").click()

	def open_groups_page(self):
		wd = self.app.wd
		if not (wd.current_url.endswith("/group.php") and len (wd.find_elements_by_name("new")) > 0):
			wd.find_element_by_link_text("groups").click()



	def creator(self, group):
		wd = self.app.wd
		self.open_groups_page()
		# init_group_creator
		wd.find_element_by_name("new").click()
		self.fill_group_form(group)
		# sumbit_creation_group
		wd.find_element_by_name("submit").click()
		self.return_to_group_page()
		self.group_cache = None


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
		self.open_groups_page()
		self.select_first_group()
		# Delite
		wd.find_element_by_name("delete").click()
		self.return_to_group_page()
		self.group_cache = None


	def delete_by_index(self,index):
		wd = self.app.wd
		# link group page
		self.open_groups_page()
		self.select_group_by_index(index)
		# Delite
		wd.find_element_by_name("delete").click()
		self.return_to_group_page()
		self.group_cache = None

	def select_group_by_index(self,index):
		wd = self.app.wd
		wd.find_elements_by_name("selected[]")[index].click()


	def select_first_group(self):
		wd = self.app.wd
		wd.find_element_by_name("selected[]").click()

	#def modify_first_group(self, new_group_data):
		#wd = self.app.wd
		#self.open_groups_page()
		#self.select_first_group()
		# open modification form
		#wd.find_element_by_name("edit").click()
		# fill form
		#self.fill_group_form(new_group_data)
		#self.click_update()
		#self.return_to_group_page()

	def modify_first_group(self, new_group):
		self.modify_by_index(0)

	def modify_by_index(self, index,new_group):
		wd = self.app.wd
		self.open_groups_page()
		self.select_group_by_index(index)
		# click edit button
		wd.find_element_by_name("edit").click()
		#modify group form
		self.fill_group_form(new_group)
		#submit modify
		wd.find_element_by_name("update").click()
		# return to group page
		self.open_groups_page()
		self.group_cache = None


	def click_update(self):
		wd = self.app.wd
		# sumbit modification
		wd.find_element_by_name("update").click()

	def count(self):
		wd = self.app.wd
		self.open_groups_page()
		return len(wd.find_elements_by_name("selected[]"))

	def count_modify(self,field_name):
		wd = self.app.wd
		self.open_groups_page()
		self.select_first_group()
		wd.find_element_by_name("edit").click()
		return len(wd.find_element_by_name(field_name).get_attribute("value"))


	group_cache = None

	def get_group_list(self):
		if self.group_cache is None:
			wd = self.app.wd
			self.open_groups_page()
			self.group_cache = []
			for element in wd.find_elements_by_css_selector('span.group'):
				text = element.text
				id = element.find_element_by_name("selected[]").get_attribute("value")
				self.group_cache.append(Group(name = text, id = id))
		return list(self.group_cache)