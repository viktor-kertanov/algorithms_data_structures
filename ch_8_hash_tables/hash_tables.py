class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
    

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        
        return my_hash


    def set_item(self, key, value):
        index = self.__hash(key)
        
        if not self.data_map[index]:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])


    def get_item(self, key):
        index = self.__hash(key)
        cell_data = self.data_map[index]
        
        if not cell_data:
            return None
        
        for element in cell_data:
            if key == element[0]:
                return element[1]
        
        return None


    def keys(self):
        keys = []
        for data_cell in self.data_map:
            if data_cell:
                for data in data_cell:
                    keys.append(data[0])
        return keys


    def print_table(self):
        for address, data in enumerate(self.data_map):
            print(f"{address}: {data}")


def item_in_common_1(list_1, list_2):
    for i in list_1:
        for j in list_2:
            if i == j:
                print(f"{i} = {j}")
                return True
    return False


def item_in_common_2(list_1, list_2):
    dict_1 = {el: True for el in list_1}
    for i in list_2:
        if i in dict_1:
            return True
    return False


if __name__ == '__main__':
    list_1 = [1, 3, 7, 9]
    list_2 = [2, 4, 6, 8]
    print(item_in_common_2(list_1, list_2))



    hash_table = HashTable(size=7)
    hash_table.set_item('cat', 111)
    hash_table.set_item('dog', 222)
    hash_table.set_item('sog', 333)
    hash_table.set_item('mag', 444)
    hash_table.set_item('rag', 555)
    hash_table.set_item('vag', 666)
    hash_table.set_item('nag', 777)
    hash_table.set_item('jug', 888)
    hash_table.set_item('lug', 999)

    hash_table.print_table()

    print('-'*10)
    key = 'dog'
    value = hash_table.get_item(key)
    print(f"The value for key '{key}' is {value}")
    
    print('-'*10)
    print(hash_table.keys())
    print('Hello_world')