#include<iostream>
using namespace std;
struct node {
	int data;
	node *left;
	node *right;
};
class BST {​
private:
	node *root;
​
public:
    BST() {
		root = NULL;
		
	}
​
	bool check_left(node *temp) {
		if (temp->left == NULL) {
			return true;
		}
		else return false;
	}
​
	bool check_right(node *temp) {
		if (temp->right == NULL)
			return true;
		else return false;
	}
​
	bool is_greater(int val, int val_1) {
		if (val > val_1)
			return true;
		else return false;
	}
​
	node* Create(int data) {
		node *Node = new node();
		Node->data = data;
		Node->left == NULL;
		Node->right == NULL;
		return Node;
	}
​
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
​
		}
		else {
			if (check_right(temp)) {
				
				temp->right = Create(data);
				temp->right->left = temp->right->right = NULL;
				return;
			}
			else Insertion(temp->right, data);
		}
​
	}
​
	node *Get_Root() {
		return root;
	}
​
	void print(node *temp) {
		if (temp == NULL)
			return;
		print(temp->left);
		cout << temp->data << " ";
		print(temp->right);
	}
​
  
    // ***************Part A*******************
​
	int mixture(node *iter)
	{
     if (iter == NULL)
	 {
		 return 0;
	 }
	 else
	 {
		 return (mixture(iter->left) + 1 + mixture(iter->right)); 
	 }
​
	}
​
//main Function ... 
    int count_nodes(node* iter, int val, int count=0){
    
​
		 if (iter->data < val)
		{  
			return count_nodes(iter->right,val,count);
		 
		}
​
		if (iter->data > val)
		{ 
			return count_nodes(iter->left,val,count);
                 
		}
        
		if (iter->data == val)
		{
              count++;
			   
              return mixture(iter);
​
		}
              
        return count;
		cout<<endl;
		
    }
​
 // Part A END
​
   // ****************Part-B********************
​
int check_leaf_left(node *temp)
{
	int left ,right;
​
   if (temp == NULL )
   {
	   return 0; //break point
   }
	   
  left=check_leaf_left(temp->left);
​
 right=check_leaf_left(temp->right);
  
//to choose only greater.. 
   
 if (left < right) 
{
	return right+1;
}
  else
{
	return left+1;
}
​
}
    int left_most_node(node *root_iter)
	{ 
		if (root_iter == NULL )
		{  
			return 0;
	 	}
		    else 
​
		 {
       	return check_leaf_left(root_iter)-1;
​
		 }
    }
	
    // **********************PART-C********************
 
    int right_leaves(node *root_iter)
	{
	   int add_r=0;	   
​
               if (root_iter->right != NULL) 
		    { 
				if (root_iter->right->left == NULL && root_iter->right->right == NULL)
			     {
				  add_r += root_iter->right->data;				
			    }
				 add_r += right_leaves(root_iter->right);
		     } 
			    if (root_iter->left != NULL)
             {
	            add_r+= right_leaves(root_iter->left);
​
               }			
           return add_r;
    } 
​
​
    // *********************PART-D******************
    int min_diff(node *root_iter,int diff=0){
        // YOUR CODE HERE
		if (diff==0)
		{
			diff=root_iter->data -root_iter->left->data;
	
		}
		
		
		
		   if (root_iter->left != NULL ) //case 1 both leaf present
		   {			 
			    
				if(root_iter->data  - root_iter->left->data < diff)
					diff = root_iter->data  - root_iter->left->data;
			   
                   diff= min_diff(root_iter->left, diff);
​
		   }
		   		   
		     if (root_iter->right != NULL) //case 2 only right leaf 
		   {
			    
				 			    
				if(root_iter->right->data  - root_iter->data < diff)
					
					diff = root_iter->right->data  - root_iter->data;
			   
			   	  diff=  min_diff(root_iter->right,diff);
		   }	
		   return diff;​
	}  

};
int main() {
	BST bst;
	bst.Insertion(bst.Get_Root(), 10);
    bst.Insertion(bst.Get_Root(), 4);
    bst.Insertion(bst.Get_Root(), 1);
    bst.Insertion(bst.Get_Root(), 8);
    bst.Insertion(bst.Get_Root(), 9);
    bst.Insertion(bst.Get_Root(), 12);
    bst.Insertion(bst.Get_Root(), 24);
    bst.Insertion(bst.Get_Root(), 13);
    
​
    bst.print(bst.Get_Root());
  cout<<endl;
  cout<<bst.count_nodes(bst.Get_Root(),10,0);
  cout<<bst.left_most_node(bst.Get_Root());
  cout<<bst.right_leaves(bst.Get_Root());
  cout<<bst.min_diff(bst.Get_Root(),0);
cout<<endl;
}