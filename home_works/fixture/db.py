import mysql.connector
from model.group import Group
from model.info_contact import Infos


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True  # Turn off cashing db

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self, clean=False):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname "
                           "from addressbook "
                           "where deprecated= '0000-00-00 00'")
            for row in cursor:
                (id, firstname, lastname) = row
                if clean :
                    list.append(Infos(id=str(id), firstname=firstname.strip(), lastname=lastname.strip()))
                else:
                    list.append(Infos(id=str(id), firstname=firstname, lastname=lastname))

        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()