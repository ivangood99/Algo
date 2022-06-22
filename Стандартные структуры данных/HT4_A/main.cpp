#include <iostream>

using namespace std;

class Node {
public:
    
    int data;
    Node* next;
    
    Node(int data = NULL, Node* next = NULL) {
        this->data = data;
        this->next = next;
    }
};


class Linked_List {
public:
    
    int size;
    Node* head;
    
    Linked_List(int size = 0, Node* head = NULL) {
        this->size = size;
        this->head = head;
    }

    void push(int x) {
        if (this->size == 0) {
            this->head = new Node(x);
        } else {
            this->head = new Node(min(this->head->data, x), this->head);
        }
        this->size++;
    }

    void pop() {
        Node* p = this->head;
        if (this->size == 1) {
            this->head = NULL;
        } else {
            this->head = this->head->next;
        }
        delete p;
        this->size--;
    }
    
    int find_min() {
        return this->head->data;
    }
};


int main() {
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    Linked_List stack = Linked_List();
    int query, elem;
    for (int i = 0; i < n; ++i) {
        cin >> query;
        if (query == 1) {
            cin >> elem;
            stack.push(elem);
        } else if (query == 2) {
            stack.pop();
        } else {
            cout << stack.find_min() << "\n";
        }
    }
    return 0;
}
