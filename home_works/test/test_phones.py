import re

def test_phones_on_hp(app):
    contact_from_hp        = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_hp.all_phones_on_hp   ==  merge_like_phones_on_hp(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home   == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work   == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub('[() -]','',s)

def merge_like_phones_on_hp(contact):
    return '\n'.join(filter(lambda x: x!= "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home,contact.mobile,contact.work,contact.phone2]))))