#include <iostream>
#include <string>
#include "database.h"

// template<typename T>
// T getType(const T& value) {
//     return value;
// }

void getAllData(Database &database) {
    for (int i = 0; i < database.index; i++) {
        switch (database.entry[i]->type) {
            case INT:
                std::cout << database.entry[i]->key << ": " << *((int*)database.entry[i]->value) << std::endl;
                break;
            case DOUBLE:
                std::cout << database.entry[i]->key << ": " << *(double*)(database.entry[i]->value) << std::endl;
                break;
            case STRING:
                std::cout << database.entry[i]->key << ": " << *(std::string*)(database.entry[i]->value) << std::endl;
                break;
            case ARRAY:
                std::cout << database.entry[i]->key << ": " << (Array*)(database.entry[i]->value) << std::endl;
                break;
        }
    }
}

Array *addArray(Array *array = new Array) {
    std::string type;
    std::cout << "type (int, double, string, array): ";
    std::cin >> type;
    std::cout << "size: ";
    std::cin >> array->size;
    
    if (type == "int") {
        int dump[array->size];
        for (int i = 0; i < array->size; i++) {
            std::cout << "item[" << i << "]: " ;
            std::cin >> dump[i];
        }
        array->items = dump;
    } else if (type == "double") {
        double dump[array->size];
        for (int i = 0; i < array->size; i++) {
            std::cout << "item[" << i << "]: " ;
            std::cin >> dump[i];
        }
        array->items = dump;
    } else if (type == "string") {
        std::string dump[array->size];
        for (int i = 0; i < array->size; i++) {
            std::cout << "item[" << i << "]: " ;
            std::cin >> dump[i];
        }
        array->items = dump;
    } else if (type == "array") {
        for (int i = 0; i < array->size; i++) {
            std::cout << "item[" << i << "]: " ;
            
            void *dump = addArray();

            if (dump == nullptr) {
                std::cout << "invalid type";
            } else {
                array->items = dump;
            }
        }
    } else {
        return nullptr;
    }
    
    
    return array;
}

void addData(Database &database) {
    std::string key;
    std::string type;
    

    std::cout << "key: ";
    std::cin >> key;

    std::cout << "Type (int, double, string, array): ";
    std::cin >> type;
    std::cout << "Value: ";

    if (type == "int") {
        int value;
        std::cin >> value;
        add(database, create(INT, key, &value));

        std::cout << "database pointer: " << database.entry[0]->value << std::endl;
        std::cout << "database pointer: " << *((int*)database.entry[0]->value) << std::endl;
    } else if (type == "double") {
        double value;
        std::cin >> value;
        add(database, create(DOUBLE, key, &value));
    } else if (type == "string") {
        std::string value;
        std::cin >> value;
        add(database, create(STRING, key, &value));
    } else if (type == "array") {
        Array *array = new Array;
        array = addArray(array);
        if (array == nullptr) {
            std::cout << "invalid type";
        } else {
            add(database, create(ARRAY, key, &array));
        }
    }
    return;
}

// command Mode, input text analyze
void commandMode(Database &database) {
    std::string command;
    std::string key;
    Entry *data;

    while (true) {
        std::cout << "command (list, add, get, del, exit): ";
        std::cin >> command;

        if (command == "list") {
            getAllData(database);
            std::cout << "database pointer: " << database.entry[0]->value << std::endl;
            std::cout << "database pointer: " << *((int*)database.entry[0]->value) << std::endl;
        } else if (command == "add") {
            addData(database);
            std::cout << "database pointer(command): " << database.entry[0]->value << std::endl;
            std::cout << "database pointer(command): " << *((int*)database.entry[0]->value) << std::endl;
        } else if (command == "get") {
            std::cout << "key: ";
            std::cin >> key;
            data = get(database, key);
            if (data == nullptr) {
                std::cout << "not found";
            } else {
                std::cout << data->key << ": " << *((int*)data->value) << std::endl;
                // TODO: type checking for output value
            }
        } else if (command == "del") {
            std::cout << "key: ";
            std::cin >> key;
            data = get(database, key);
            if (data == nullptr) {
                std::cout << "not found";
            } else {
                remove(database, key);
            }
        } else if (command == "exit") {
            return;
        } else {
            std::cout << "invalid command" << std::endl;
        }

        std::cout << std::endl;
    }
}

int main() {
    Database database;

    init(database);

    commandMode(database);

    destroy(database);

    return 0;
}

