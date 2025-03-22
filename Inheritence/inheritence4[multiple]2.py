class father:
        def gardening(self):
                print("I enjoy gardening")

class mother:
        def cooking(self):
                print("I love cooking")


class child(father, mother):
        def sports(self):
                father.gardening(self)
                mother.cooking(self)
                print("I enjoy sports")

c=child()
c.sports()




