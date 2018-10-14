# 컨택트 클래스의 설정
class Contact:
    def __init__(self,name,phone_number,e_mail,addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print('name:', self.name)
        print('phone_number :', self.phone_number)
        print('e_mail ;', self.e_mail)
        print('Address:', self.addr)

# 연락처 입력 동작 (contact input)
def set_contact():
    name = input('name:')
    phone_number = input('phone number:')
    e_mail = input('e mail:')
    addr = input('address:')
    contact = Contact(name,phone_number,e_mail,addr)
    return contact

# 출력 동작 실행 (contact output)
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

# 연락처 삭제하기  (delete contact)
def remove_contact(contact_list,name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

# 메인 메뉴 동작 (main menu)
def print_menu():
    print('1.연락처 입력')
    print('2 연락처 출력')
    print('3 연락처 삭제')
    print('4 종료')
    menu = input('메뉴선택:')
    return int(menu)

# 입력된 데이터 저장하기 (프로그래밍 종료시에는 데이터가 다 사라지기 떄문에
# 그 이유는 컨택트 클래스의 인스턴스 메모리에 데이터들이 저장되다가 종료시 사라지기에
# 따로 파일로 데이터베이스를 저장하는 것이다)
def store_contact(contact_list):
    f = open('contact.txt','w')
    for contact in contact_list:
        f.write(contact.name +'\n')
        f.write(contact.phone_number +'\n')
        f.write(contact.e_mail +'\n')
        f.write(contact.addr +'\n')
    f.close()

# 저장된 파일의 데이터를 다시 불러오기
def load_contact(contact_list):
    with open('contact.txt','r') as f:
        lines = f.readlines()
        num = len(lines)/4
        num = int(num)
    for i in range(num):
         name = lines[4*i].rstrip('\n')
         phone = lines[4*i+1].rstrip('\n')
         email = lines[4*i+2].rstrip('\n')
         addr = lines[4*i+3].rstrip('\n')
         contact = Contact(name,phone,email,addr)
         contact_list.append(contact)

# 동작 실행 (rum)
def run():
    contact_list =[]
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("name:")
            remove_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break

if __name__ == '__main__':
    run()
