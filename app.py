documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# p [people]
def get_name_by_document_number(user_input):
    for doc in documents:
        if doc["number"] == user_input:
            return doc["name"]
    return user_input

# s [self]
def get_shelf_by_document_number(user_input):
    for key, value in directories.items():
        if user_input in value:
            return key
    return user_input


# l [list]
def show_documents_list():
    for doc in documents:
        return f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"'


# a [add]
def add_document_and_put_on_shelf(input_number, input_name, input_type, input_shelf, notice=f'Полки с таким номером не существует'):
    for doc in documents:
        if doc["number"] == input_number:
            return f'Документ с номером: {input_number} уже существует'
    for key, value in directories.items():
        if input_number not in value and input_shelf in key:
            notice = f'Документ {input_number} добавлен на полку {input_shelf}'
            documents.append({"type": {input_type}, "number": {input_number}, "name": {input_name}})
            directories[input_shelf].append(input_number)
    return notice


# d [delete]
def delete_document_and_put_off_shelf(input_number, notice=f'Документа с таким номером не существует'):
    for doc in documents:
        if doc["number"] == input_number:
            documents.remove(doc)
            for value in directories.values():
                if input_number in value:
                    value.remove(input_number)
                    notice = f'Документ с номером: {input_number} удален'
    return notice

# m [move]
def delete_document_from_one_shelf_and_put_on_another_shelf(input_number, input_shelf, notice=f'Документа и полки с таким номером не существует'):
    for key, value in directories.items():
        if input_number not in value:
            notice = f'Документа с таким номером не существует'
        elif input_shelf not in key:
            notice = f'Полки с таким номером не существует'
        elif input_number in value and input_shelf in key:
            value.remove(input_number)
            directories[input_shelf].append(input_number)
        notice = f'Документа с номером {input_number} удален с полки {key} и перемещен на полку {input_shelf}'
    return notice


# as (add shelf)
def add_shelf(input_shelf, notice=f'Полка с таким номером уже существует'):
    if input_shelf not in directories.keys():
        directories[input_shelf] = []
        notice = f'Полка с номером {input_shelf} создана'
    return notice
