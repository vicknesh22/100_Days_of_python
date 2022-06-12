class User:

    def __init__(self, u_id, name):
        # initialize the attributes
        self.id = u_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "random_guy")
user_2 = User("002", "New_Guy")
# user_1.id = "001"
# user_1.name = "random_guy"

print(user_1.name)
user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)

print(user_2.following)
print(user_2.followers)
# adding methods example

