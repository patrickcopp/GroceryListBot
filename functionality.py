def add(list, message):
    list.append(message[5:])

def list(list):
    print(str(list))

def clear(list):
    list.clear()

def remove(list, message):
    item = message[8:]
    if item in list:
        list.remove(item)
        return True
    return False
