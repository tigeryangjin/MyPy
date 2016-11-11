class Test():
    def prt(self, username, password):
        self.username = username
        self.password = password
        print(self.username, self.password)


t = Test()
t.prt('tiger', '1979')
