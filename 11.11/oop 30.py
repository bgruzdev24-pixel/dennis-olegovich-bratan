class SecureNote:
    def __init__(self, content, password):
        self.__content = content
        self.__password = password

    def reveal(self, password):
        if password == self.__password:
            print(self.__content)
        else:
            print("Неверный пароль")


note = SecureNote("Помнишь пароль", "1234")

note.reveal("0000") 
note.reveal("1234") 