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

  

    int  _count(node *random){
    if (random==NULL) return -1;
    int left = 1+ _count(random->left);
    int right = 1+ _count(random->right);
    return left+right;
    }
    // Part A
    int count_nodes(node* iter, int val, int count=0){
        if (iter == NULL)return count;
       
        count= count_nodes(iter->left, val, count);
        if (iter->data == val){
            int al =  _count(iter)+1;
            cout<<"Root is: "<<val<<endl<<"nodes under: "<<al<<endl;
            return al;
        }

        count = count_nodes(iter->right, val,count);
        return count;
    
    }

  //  int mix_count(node* root_iter, int node_val){
   //     return count_nodes(root_iter,)
   // }

    // Part-B
    int find_left_most(node *root_iter, int level, int height, string child="nill"){
        if (root_iter == root && root->left == NULL && root->right == NULL)
            return 1;
        if (root_iter==NULL)
            return 0;
        if(root_iter->left != NULL){
            //cout<<"Node: "<<root_iter->data<< " height is: "<<level<<endl;
            level++;
            height = find_left_most(root_iter->left, level,height, "left");
            level--;
        }
         if (child == "left" && root_iter->left==NULL && root_iter->right == NULL){
                // returing current state height
                //level--;
                //child = "nill";
                cout<<"Found leftmost at height: "<<level<<endl;
                cout<<"Curent height: "<<height<<endl;
                cout<<"Node is "<<root_iter->data<<endl;

                if (height<level){
                    cout<<"Latest Height: "<<height<<endl;
                    height= level;
                    return height;}
                else return height;
        }
        

        if(root_iter->right != NULL){
            //cout<<"Node: "<<root_iter->data<< " height is: "<<level<<endl;
            level++;
            height = find_left_most(root_iter->right, level,height, "right");
            level--;
        }

       
        return height;
    }
    
    int left_most_node(node *root_iter){
        return find_left_most(root,0,0);

    }

     int count_right_leaves(node *root_iter, int count, string child="nill"){
        if (root_iter==NULL)
            return 0;
        if(root_iter->left != NULL){
            count = count_right_leaves(root_iter->left ,count, "left");
        }
        if (child == "right" && root_iter->left==NULL && root_iter->right == NULL){
                count+=root_iter->data;
                return count;
        }
        if(root_iter->right != NULL){
            count = count_right_leaves(root_iter->right,count, "right");
        }

        return count;
    }
    // PART-C
    int right_leaves(node* root_iter){
        return count_right_leaves(root_iter, 0, "nill");
    }

    int get_min(int val1, int val2){
        if (val1 == 0)
        return val2;
        if (val2 ==0)
        return val1;
        if (val1>val2)return val2;
        else return val1;
    }

    int min_diff(node *root_iter,int diff=0){
        if (root_iter == NULL)return 0;

        diff = min_diff(root_iter->left,diff);
        diff = min_diff(root_iter->right, diff);
        int diff_left=0,diff_right=0, temp_min;
        if (root_iter->left!=NULL)
            diff_left = root_iter->data - root_iter->left->data;
        if (root_iter->right != NULL)
            diff_right = root_iter->right->data - root_iter->data;
        if (diff_left == 0)
            return get_min(diff, diff_right);
        else if (diff_right == 0)
            return get_min(diff, diff_left);
        else{
            int min_tmp = get_min(diff_right, diff_left);
            return get_min(min_tmp, diff);
        }
        
        /*
        if (diff_left>diff_right){ 
            int diff1 = diff_left - diff_right;
            return get_min(diff1, diff);
            }
        else {
            int diff2 = diff_right-diff_left;
            return get_min(diff2, diff);
        */

    }
};


//###############PART A #####################



//################PART B####################
int main() {
	BST bst;
	node *root = NULL;
	bst.Insertion(bst.Get_Root(), 8);
	//root = bst.Get_Root();
    
    //bst.Insertion(root, 100);
    //bst.Insertion(root, 200);
    //bst.Insertion(root, 145);
    //bst.Insertion(root, 74);
    //bst.Insertion(root, 50);
    bst.Insertion(bst.Get_Root(), 5);
    bst.Insertion(bst.Get_Root(), 6);
    bst.Insertion(bst.Get_Root(), 20);
    bst.Insertion(bst.Get_Root(), 10);
    bst.Insertion(bst.Get_Root(), 12);



    //bst.Insertion(root, 1);
   // bst.Insertion(root, 4);
   // bst.Insertion(root, 7);
   // bst.Insertion(root, 6);
  //  bst.Insertion(root, 5);
   // bst.Insertion(root, 25);
   // bst.Insertion(root, 18);
   // bst.Insertion(root, 17);
   // bst.Insertion(root, 16);
  //  bst.Insertion(root, 15);
  //  bst.Insertion(root, 13);
    //bst.Insertion(root, 4);

    /*
	bst.Insertion(root, 5);
    //bst.Insertion(root, 3);
    //bst.Insertion(root, 4);
	bst.Insertion(root, 20);
    
	bst.Insertion(root, 18);
	bst.Insertion(root, 17);
	bst.Insertion(root, 6);
    bst.Insertion(root, 16);
    bst.Insertion(root, 15);
    bst.Insertion(root, 32);
    bst.Insertion(root, 33);
    bst.Insertion(root, 34);
    bst.Insertion(root, 35);
    bst.Insertion(root, 27);
    bst.Insertion(root, 28);
    bst.Insertion(root, 24);
    bst.Insertion(root, 25);
    bst.Insertion(root, 19);
    */
	bst.print(bst.Get_Root());
	cout << endl << "'''''''''''''''''" << endl;
   // cout<<bst.count_nodes(bst.Get_Root(),20)<<endl;
    //cout<<bst._count(root);
    //cout<<bst.find_left_most(root,0,0)<<endl;
    cout<<bst.right_leaves(bst.Get_Root())<<endl;
    //cout<<bst.min_diff(root, 0);
}