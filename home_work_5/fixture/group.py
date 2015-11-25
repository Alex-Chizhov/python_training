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
		# fill_group_form
		wd.find_element_by_name("group_name").click()
		wd.find_element_by_name("group_name").clear()
		wd.find_element_by_name("group_name").send_keys(group.name)
		wd.find_element_by_name("group_header").click()
		wd.find_element_by_name("group_header").clear()
		wd.find_element_by_name("group_header").send_keys(group.header)
		wd.find_element_by_name("group_footer").click()
		wd.find_element_by_name("group_footer").clear()
		wd.find_element_by_name("group_footer").send_keys(group.footer)
		# sumbit_creation_group
		wd.find_element_by_name("submit").click()
		self.return_to_group_page()