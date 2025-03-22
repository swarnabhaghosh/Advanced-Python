class remote_control:
        def __init__(self):
                self.channels=["star sports", "HBO" "ESPN", "BBC", "POGO", "CN", "HUNGAMA"]
                self.index=-1
        def __iter__(self):
                return self
        def __next__(self):
                try:
                        self.index+=1
                        if self.index == len(self.channels):
                                raise StopIteration #it will not work because here the list ends and return StopIteration exception
                        return self.channels[self.index]
                except StopIteration as e:
                        return("Iteration is stopped")
        
r=remote_control()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
