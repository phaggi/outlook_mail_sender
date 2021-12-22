import win32com.client as win32
from win32com.client.gencache import EnsureDispatch




def get_maillist(maillistname: str):
    """

    :param maillistname: str name of Group contacts at Outlook
    :return: string of addresses (des = ;) of Group contacts
    (empty if Group 'maillistname' not found)
    """
    outlook = EnsureDispatch("Outlook.Application")
    olNamespace = outlook.GetNamespace("MAPI")
    olFolder = olNamespace.GetDefaultFolder(10)
    olConItems = olFolder.Items
    mail_list = []
    for olItem in olConItems:
        if "_DistListItem" in str(type(olItem)) and olItem.DLName == maillistname:
            counter = olItem.MemberCount
            while bool(counter):
                mail_list.append(olItem.GetMember(counter).Address)
                counter -= 1
    if bool(mail_list):
        result = ';'.join(mail_list)
    else:
        result = ''
    return result

if __name__ == '__main__':
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = get_maillist('test1')
    mail.Subject = 'testmail'
    print(mail.Recipients.ResolveAll())
    print(mail.To)
    mail.Send()
