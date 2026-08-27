#include <iostream>
#include <string>

class Database {
public:
    void execute(const std::string& query) {
        std::cout << query << '\n';
    }
};

int main() {
    Database db;

    std::string name;
    std::cout << "Enter username: ";
    std::getline(std::cin, name);

    std::string query =
        "SELECT id, username, email FROM users WHERE username = '" +
        name + "'";

    db.execute(query);

    return 0;
}
