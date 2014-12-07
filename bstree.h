typedef struct bstree {
  struct bstree *left;
  struct bstree *right;
  int value;
  int level;
} bstree;

// Basic operations
bstree *create_bstree(int value);
int add(bstree *t, int value);
int add_with_level(bstree *t, int value, int level);
int find(bstree *t, int value);
int find_min(bstree *t);

// Traversal operations
void print_dfs(bstree *tree);
void print_bfs(bstree *tree);

void print_inorder(bstree *tree);
void print_preorder(bstree *tree);
void print_postorder(bstree *tree);

// BFS in the same line. One involves keeping track of levels in the nodes
// themselves. Need auxiliary memory. Another keeps track of which level we
// are in using a dummy variable. Note the edge conditions.
void print_bfs_sameline(bstree *tree);
void print_bfs_sameline1(bstree *tree);

// gfg
void print_inorder_succpred(bstree *tree, int value, int min, int max); // got fucked here

int check_bst(bstree *tree, int min, int max);

bstree *lca(bstree *tree, int n1, int n2);

int getkth(bstree *tree, int k); // Clever manipulation of inorder algo. Look again, might not be able to repro

void print_range(bstree *tree, int n1, int n2);

//int is_identical1(int[] tree1, int[] tree2); // got fucked here

void add_greater_bst(bstree *tree1);

void sorted_merge_print(bstree *tree1, bstree *tree2); // got fucked here


