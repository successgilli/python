class Tab:
    menu = {
        "rice": 10,
        "beans": 5,
        "wine": 12,
        "chicken": 6,
        "water": 3
    }

    def __init__(self):
        self.total = 0
        self.items = []
    
    def add_item(self):
        while True:
            item = input('insert an item')
            self.items.append(item)
            self.total += self.menu[item]
            add_more = input('add more? (y/n)')

            if add_more != 'y': break

    def print_items(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = tax + service + self.total

        for item in self.items:
            print(f"{item:20} ${self.menu[item]}")
        print(f"{'Total':20} ${total}")
