#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class Temp {
private:
    string id, name, author, search;
    fstream file;

public:
    void addBook();
    void showAll();
    void extractBook();
};

void Temp::addBook() {
    cout << "\nEnter Book ID: ";
    getline(cin, id);

    cout << "Enter Book Name: ";
    getline(cin, name);

    cout << "Enter Author Name: ";
    getline(cin, author);

    file.open("bookdata.txt", ios::out | ios::app);

    file << id << "*" << name << "*" << author << endl;

    file.close();

    cout << "\nBook Added Successfully!\n";
}

void Temp::showAll() {
    file.open("bookdata.txt", ios::in);

    if (!file) {
        cout << "\nNo Book Records Found!\n";
        return;
    }

    cout << "\n--------------------------------------------------------\n";
    cout << "Book ID\t\tBook Name\t\tAuthor\n";
    cout << "--------------------------------------------------------\n";

    while (getline(file, id, '*')) {
        getline(file, name, '*');
        getline(file, author);

        cout << id << "\t\t" << name << "\t\t" << author << endl;
    }

    file.close();
}

void Temp::extractBook() {
    cout << "\nEnter Book ID to Search: ";
    getline(cin, search);

    file.open("bookdata.txt", ios::in);

    if (!file) {
        cout << "\nNo Book Records Found!\n";
        return;
    }

    bool found = false;

    while (getline(file, id, '*')) {
        getline(file, name, '*');
        getline(file, author);

        if (search == id) {
            cout << "\nBook Found Successfully!\n";
            cout << "---------------------------------\n";
            cout << "Book ID    : " << id << endl;
            cout << "Book Name  : " << name << endl;
            cout << "Author Name: " << author << endl;
            cout << "---------------------------------\n";

            found = true;
            break;
        }
    }

    if (!found) {
        cout << "\nBook Not Found!\n";
    }

    file.close();
}

int main() {
    Temp obj;
    char choice;

    while (true) {
        cout << "\n========== LIBRARY MANAGEMENT SYSTEM ==========\n";
        cout << "1. Show All Books\n";
        cout << "2. Search Book by ID\n";
        cout << "3. Add Book\n";
        cout << "4. Exit\n";
        cout << "==============================================\n";

        cout << "Enter Choice: ";
        cin >> choice;
        cin.ignore();

        switch (choice) {
            case '1':
                obj.showAll();
                break;

            case '2':
                obj.extractBook();
                break;

            case '3':
                obj.addBook();
                break;

            case '4':
                cout << "\nProgram Closed Successfully!\n";
                return 0;

            default:
                cout << "\nInvalid Choice! Try Again.\n";
        }
    }

    return 0;
}