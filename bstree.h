typedef struct bstree {
  struct bstree *left;
  struct bstree *right;
  int value;
} bstree;

// Basic operations
bstree *create_bstree(int value);
int add(bstree *t, int value);
int find(bstree *t, int value);


// Traversal operations
void print_dfs(bstree *tree);
void print_bfs(bstree *tree);

