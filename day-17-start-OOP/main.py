class User:
    # constructor
    def __init__(self, user_id, username):
        self.user_id = (user_id,)
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user1 = User("001", "Luat")
user2 = User("002", "Nguyen")

user1.follow(user2)
print("user1 er: ", user1.follower)
print("user1 ing: ", user1.following)
print("user2 er: ", user2.follower)
print("user2 ing: ", user2.following)
