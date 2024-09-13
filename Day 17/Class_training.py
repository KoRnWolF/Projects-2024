class User:

    def __init__(self, usr_id, usr_name):
        self.id = usr_id
        self.user_name = usr_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.follower += 1


user_1 = User("1234", "Jack")
user_2 = User("5678", "James")

user_1.follow(user_2)
print(user_1.following)
print(user_2.follower)



