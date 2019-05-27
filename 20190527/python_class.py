class BusinessCard:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    # All methods should have self as it's first argument.
    def print_info(self):
        print('-----------------------')
        print('Name: ', self.name)
        print('E-mail: ', self.email)
        print('Address: ', self.address)
        print('-----------------------')


member1 = BusinessCard('shin', 'donggyu9410@gmail.com', 'gongneung')
member1.print_info()
