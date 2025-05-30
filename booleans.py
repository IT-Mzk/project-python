# print(10>9)
# print(10==9)
# print(10!=9)
# print(10<9)

# x="hello"
# y= 15
# print(bool(x))
# print(bool(y))
# print(bool(["apple", "banana", "cherry"])) 

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))  

x=100
print(isinstance(x, float))