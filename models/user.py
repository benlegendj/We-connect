
class User(object):
    all_users=[]

    def __init__(self):
        self.user_id_counter = 0


    def create(self, data):
        new_user = data
        new_user['user_id'] = self.user_id_counter = self.user_id_counter+ 1

        self.__class__.all_users.append(new_user)
        return new_user

    def get_all_users (self):
        return self.__class__.all_users


