class Business(object):
    businesses=[]

    def __init__(self):
        self.business_counter = 0


    def create(self, data):
        new_business = data
        new_business['business_id'] = self.business_counter = self.business_counter+ 1

        self.__class__.all_users.append(new_business)
        return new_business

    def get_all_users (self):
        return self.__class__.businesses


