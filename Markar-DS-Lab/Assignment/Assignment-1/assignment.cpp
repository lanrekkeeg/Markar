#include<iostream>
using namespace std;

struct node {
	int data;
	node *left;
	node *right;
};

class BST {

private:
	node *root;

public:
    BST() {
		root = NULL;
		
	}

	bool check_left(node *temp) {
		if (temp->left == NULL) {
			return true;
		}
		else return false;
	}

	bool check_right(node *temp) {
		if (temp->right == NULL)
			return true;
		else return false;
	}

	bool is_greater(int val, int val_1) {
		if (val > val_1)
			return true;
		else return false;
	}

	node* Create(int data) {
		node *Node = new node();
		Node->data = data;
		Node->left == NULL;
		Node->right == NULL;
		return Node;
	}

	void Insertion(node *temp, int data) {
		if (root == NULL) {
			root = Create(data);
			return;
		}
		if (is_greater(temp->data, data)) {
			if (check_left(temp)) {
				temp->left = Create(data);
				return;
			}
			else Insertion(temp->left, data);

		}
		else {
			if (check_right(temp)) {
				
				temp->right = Create(data);
				temp->right->left = temp->right->right = NULL;
				return;
			}
			else Insertion(temp->right, data);
		}

	}

	node *Get_Root() {
		return root;
	}

	void print(node *temp) {
		if (temp == NULL)
			return;
		print(temp->left);
		cout << temp->data << " ";
		print(temp->right);
	}


	
  
    // ***************Part A*******************
    int count_nodes(node* iter, int val, int count=0){
        //   YOUR CODE HERE /////
        return 0;
    }

 
 /*
    // ****************Part-B********************
    int left_most_node(node *root_iter){
        // YOUR CODE HERE

    }
*/

 /*    
    // **********************PART-C********************
    int right_leaves(node* root_iter){
        // YOUR CODE HERE
    }
*/

/*
    // *********************PART-D******************
    int min_diff(node *root_iter,int diff=0){
        // YOUR CODE HERE
        }

*/
};

int main() {
	BST bst;
	bst.Insertion(bst.Get_Root(), 8);
    bst.Insertion(bst.Get_Root(), 5);
    bst.Insertion(bst.Get_Root(), 6);
    bst.Insertion(bst.Get_Root(), 20);
    bst.Insertion(bst.Get_Root(), 10);
    bst.Insertion(bst.Get_Root(), 12);
    bst.print(bst.Get_Root());

}