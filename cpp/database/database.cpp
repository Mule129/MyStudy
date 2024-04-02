#include <string>

#include "database.h"


// 엔트리를 생성한다.
Entry *create(Type type, std::string key, void *value) {
    Entry *entry = new Entry;
    entry->type = type;
    entry->key = key;

    switch (type)
    {
    case INT:
        entry->value = new int(*(int*)value);
        break;
    case DOUBLE:
        entry->value = new double(*(double*)value);
    case STRING:
        entry->value = new std::string(*(std::string*)value);
    case ARRAY:
        entry->value = new Array(*(Array*)value);    
    default:
        break;
    }

    return entry;
}


// 데이터베이스를 초기화한다.
void init(Database &database) {

}

// 데이터베이스에 엔트리를 추가한다.
void add(Database &database, Entry *entry) {

}

// 데이터베이스에서 키에 해당하는 엔트리를 찾는다.
Entry *get(Database &database, std::string &key) {
    Entry *entry;
    return entry;
}

// 데이터베이스에서 키에 해당하는 엔트리를 제거한다.
void remove(Database &database, std::string &key) {

}

// 데이터베이스를 해제한다.
void destroy(Database &database) {

}
