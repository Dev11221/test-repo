#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <sqlite3.h>

using namespace std;

void login(sqlite3* db) {
    string username, password;

    cout << "Username: ";
    cin >> username;

    cout << "Password: ";
    cin >> password;

    string query =
        "SELECT * FROM users WHERE username='" +
        username +
        "' AND password='" +
        password + "';";

    cout << "[DEBUG] Executing: " << query << endl;

    sqlite3_stmt* stmt;

    if (sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr) == SQLITE_OK) {
        if (sqlite3_step(stmt) == SQLITE_ROW) {
            cout << "Login successful!\n";
        } else {
            cout << "Login failed.\n";
        }
    }

    sqlite3_finalize(stmt);
}

void vulnerableCopy() {
    char buffer[16];

    cout << "Enter some text: ";
    cin >> buffer;

    cout << "You entered: " << buffer << endl;
}

void vulnerableCommand() {
    string filename;

    cout << "Enter filename: ";
    cin >> filename;

    string command = "cat " + filename;

    cout << "[DEBUG] Running command: " << command << endl;

    system(command.c_str());
}

void vulnerableFileAccess() {
    string filename;

    cout << "Enter file name: ";
    cin >> filename;

    string path = "./files/" + filename;

    cout << "[DEBUG] Opening: " << path << endl;

    FILE* file = fopen(path.c_str(), "r");

    if (file) {
        cout << "File opened successfully.\n";
        fclose(file);
    } else {
        cout << "Could not open file.\n";
    }
}

int vulnerableRandom() {
    return rand();
}

int main() {
    sqlite3* db = nullptr;

    if (sqlite3_open("lab.db", &db) != SQLITE_OK) {
        cerr << "Could not open database.\n";
        return 1;
    }

    cout << "\n=== C++ Lab ===\n";
    cout << "1. Login\n";
    cout << "2. Input\n";
    cout << "3. Command\n";
    cout << "4. File\n";
    cout << "5. Random\n";

    int choice;
    cin >> choice;

    switch (choice) {
        case 1:
            login(db);
            break;
        case 2:
            vulnerableCopy();
            break;
        case 3:
            vulnerableCommand();
            break;
        case 4:
            vulnerableFileAccess();
            break;
        case 5:
            cout << "Generated value: " << vulnerableRandom() << endl;
            break;
        default:
            cout << "Invalid choice.\n";
    }

    sqlite3_close(db);
    return 0;
}
