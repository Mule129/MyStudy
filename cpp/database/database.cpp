#include <string>
#include <iostream>

#include "database.h"


// 엔트리를 생성한다.
Entry *create(Type type, std::string key, void *value) {
    Entry *entry = new Entry;
    entry->type = type;
    entry->key = key;

    switch (type) {
    case INT:
        entry->value = (int*)value;
        break;
    case DOUBLE:
        entry->value = (double*)value;
        break;
    case STRING:
        entry->value = (std::string*)value;
        break;
    case ARRAY:
        entry->value = (Array*)value;
        break;
    default:
        return nullptr;
    }

    return entry;
}


// 데이터베이스를 초기화한다.
void init(Database &database) {
    database.entry = new Entry*[DEFALTSIZE];
    for (int i = 0; i < DEFALTSIZE; i++) {
        database.entry[i] = nullptr;
    }
    database.index = 0;
    database.maxSize = DEFALTSIZE;
}

// 데이터베이스에 엔트리를 추가한다.
void add(Database &database, Entry *entry) {
    bool check = false;

    for (int i = 0; i < database.index; i++) {  // key duplication check
        if (database.entry[i]->key == entry->key) {  
            database.entry[i] = entry;
            check = true;
        }
    }
    
    if (check == true) {
        return;
    }

    database.entry[database.index] = entry;
    database.index++;
    
    if (database.maxSize <= database.index-1) {
        database.maxSize = database.maxSize * 2;
        Entry** dump = new Entry*[database.maxSize];
        for (int i = 0; i < database.index; i++) {
            dump[i] = database.entry[i];
        }
        delete[] database.entry;
        database.entry = dump;
    }
}

// 데이터베이스에서 키에 해당하는 엔트리를 찾는다.
Entry *get(Database &database, std::string &key) {
    for (int i = 0; i < database.index; i++) {
        if (database.entry[i]->key == key) {
            return database.entry[i];
        }
    }
    return nullptr;
}

// 데이터베이스에서 키에 해당하는 엔트리를 제거한다.
void remove(Database &database, std::string &key) {
    for (int i = 0; i < database.index; i++) {
        if (database.entry[i]->key == key) {
            delete &database.entry[i];
            database.entry[i] = database.entry[i+1];
            database.index--;
            
            return;
        }
    }
}

// 데이터베이스를 해제한다.
void destroy(Database &database) {
    delete[] database.entry;
    delete &database;
}
