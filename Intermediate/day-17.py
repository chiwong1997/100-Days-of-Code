class User:
    # initialize i.e. the constructor function - this is called everytime you create
    # a new object from this class
    def __init__(self, id, username):
        # initialize/create starting values for our attributes
        self.id = id
        self.username = username
        # we can also provide a default value for an attribute
        self.followers = 0
        self.following = 0

    # adding methods to a class - the things that our object does
    # note that methods always have self as their first parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1

# we can create a User object called user_1, and then add attributes for that object 
# remember that an attribute is just a variable that belongs to an object
# in this case, we are adding attributes id and username to the user_1 object  

user_1 = User("001", "Chi")
user_1.id = "001"
user_1.username = "Chi"

print(user_1.username)

# we don't want to have to do this every time we create a new user object
# this is where the constructor comes in (__init__ method)

user_2 = User("002", "Angela")
print(user_2.id)
print(user_2.username)
user_2.id = "004"
print(user_2.id)
print(user_2.followers)

# user_1 object, using the follow method from the user_1 object, to follow user_2
# what happens here is that user_1 is passed into the self parameter of the follow method
# and user_2 is passed into the user parameter of the follow method
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)