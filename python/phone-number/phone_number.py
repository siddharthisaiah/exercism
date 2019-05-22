class Phone(object):
    def __init__(self, phone_number):
        self.number = self.clean_number(phone_number)

        if self.invalid_phone_length():
            raise ValueError("Invalid phone number length")

        if self.invalid_area_code():
            raise ValueError("Invalid Area Code")

        if self.invalid_exchange_code():
            raise ValueError("Invalid Exchange Code")

    def clean_number(self, number):
        number = ''.join(d for d in number if d.isdigit())
        if number[0] == "1": return number[1:]
        return number


    def invalid_area_code(self):
        return self.number[0] == "0" or self.number[0] == "1"

    def invalid_phone_length(self):
        length = len(self.number)
        return length > 10 or length < 10

    def invalid_exchange_code(self):
        return self.number[3] == "0" or self.number[3] == "1"

    
    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return "({area_code}) {exchange_code}-{subscriber_num}".format(
            area_code=self.number[:3],
            exchange_code=self.number[3:6],
            subscriber_num=self.number[6:])
