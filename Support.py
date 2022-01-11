class Support:
    count_support=0
    def __init__(self,name,email,outlet, platform, order_id, subject, enquiry):
        super().__init__(name,email,order_id,outlet,platform,enquiry)
        Support.count_id+=1
        self.__order_id = order_id
        self.__name = name
        self.__email = email
        self.__outlet = outlet
        self.__platform = platform
        self.__subject = subject
        self.__enquiry = enquiry

    def get_order_id(self):
        return self.__order_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_outlet(self):
        return self.__outlet

    def get_platform(self):
        return self.__platform

    def get_subject(self):
        return self.__subject

    def get_enquiry(self):
        return self.__enquiry



    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_outlet(self, outlet):
        self.__outlet = outlet

    def set_platform(self, platform):
        self.__platform = platform

    def set_subject(self, subject):
        self.__subject = subject

    def set_enquiry(self, enquiry):
        self.__enquiry = enquiry
