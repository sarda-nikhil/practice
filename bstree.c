#include <stdlib.h>
#include <stdio.h>

#include "bstree.h"
#include "queue.h"

bstree *create_bstree(int value) {
  bstree *t = (bstree *) malloc(sizeof(bstree));
  if (t == NULL) {
    return t;
  }

  t->value = value;
  
  return t;
}

int add(bstree* t, int value) {
  if (t->value > value) {
    if (t->left == NULL) {
      t->left = create_bstree(value);
      if (t->left != NULL)
	return 0;
    } else {
      return add(t->left, value);
    }
  } else {
    if (t->right == NULL) {
      t->right = create_bstree(value);
      if (t->right != NULL)
	return 0;
    } else {
      return add(t->right, value);
    }
  }
  return 1;
}

int add_with_level(bstree* t, int value, int level) {
  if (t->value > value) {
    if (t->left == NULL) {
      t->left = create_bstree(value);
      t->left->level = level + 1;
      if (t->left != NULL)
	return 0;
    } else {
      return add_with_level(t->left, value, level+1);
    }
  } else {
    if (t->right == NULL) {
      t->right = create_bstree(value);
      t->right->level = level + 1;
      if (t->right != NULL)
	return 0;
    } else {
      return add_with_level(t->right, value, level+1);
    }
  }
  return 1;
}

int find(bstree *t, int value) {
  if (t->value == value) {
    return 1;
  }
  if (t->value > value) {
    if (t->left == NULL) {
      return 0;
    } else {
      return find(t->left, value);
    }
  } else {
    if (t->right == NULL) {
      return 0;
    } else {
      return find(t->right, value);
    }
  }
  return 0;
}

int find_min(bstree *t) {
  while (t->left != NULL) {
    t = t->left;
  }

  return t->value;
}

void print_dfs(bstree *tree) {
  if (tree == NULL)
    return;
  
  printf("%d\n", tree->value);
  print_dfs(tree->left);
  print_dfs(tree->right);
}

void print_bfs(bstree *tree) {
  if (tree == NULL)
    return;

  queue *q = create_queue();
  add_item(q, (queue_item*) tree);

  bstree *t;
  do {
    t = (bstree*) remove_item(q);
    if (t == NULL) {
      break;
    }
    printf("%d\n", t->value);

    if (t->left != NULL) {
      add_item(q, (queue_item*) t->left);
    }

    if (t->right != NULL) {
      add_item(q, (queue_item*) t->right);
    }

  } while (1);
}

void print_bfs_sameline(bstree *tree) {
  const char *d = '\0';

  if (tree == NULL)
    return;

  queue *q = create_queue();
  add_item(q, (queue_item *) tree);

  bstree *t;

  int level = 0;

  do {
    queue_item *q_item = remove_item(q);

    t = (bstree*) q_item;
    if (t == NULL) {
      break;
    }
    
    if (t->level > level) {
      level = t->level;
      printf("\n");
    }

    printf("%d ", t->value);

    if (t->left != NULL) {
      add_item(q, (queue_item*) t->left);
    }

    if (t->right != NULL) {
      add_item(q, (queue_item*) t->right);
    }
    
  } while (1);
}

void print_bfs_sameline1(bstree *tree) {
  char d = 'd';

  if (tree == NULL)
    return;

  queue *q = create_queue();
  add_item(q, (queue_item *) tree);
  add_item(q, (queue_item *) d);

  do {
    queue_item *q_item = remove_item(q);

    if ((char) q_item == 'd') {
      printf("\n");
      if (is_empty(q))
	break;
      add_item(q, (queue_item *) d);
      continue;
    }

    bstree *t = (bstree*) q_item;
    if (t == NULL) {
      break;
    }

    printf("%d ", t->value);

    if (t->left != NULL) {
      add_item(q, (queue_item*) t->left);
    }

    if (t->right != NULL) {
      add_item(q, (queue_item*) t->right);
    }
    
  } while(1);
  
}

void print_inorder(bstree *tree) {
  if (tree == NULL) {
    return;
  }

  print_inorder(tree->left);
  printf("%d ", tree->value);
  print_inorder(tree->right);
}

void print_preorder(bstree *tree) {
  if (tree == NULL) {
    return;
  }

  printf("%d ", tree->value);
  print_preorder(tree->left);
  print_preorder(tree->right);
}

void print_postorder(bstree *tree) {
  if (tree == NULL) {
    return;
  }

  print_postorder(tree->left);
  print_postorder(tree->right);
  printf("%d ", tree->value);
}

void print_left_boundary(bstree *tree) {
  if (tree == NULL) {
    return;
  }

  if (tree->left != NULL) {
    print_left_boundary(tree->left);
  } else {
    print_left_boundary(tree->right);
  }

  printf("%d ", tree->value);
}

void print_right_boundary(bstree *tree) {
  if (tree == NULL) {
    return;
  }

  printf("%d ", tree->value);

  if (tree->right != NULL) {
    print_right_boundary(tree->right);
  } else {
    print_right_boundary(tree->left);
  }

}

void print_boundary(bstree *tree) {
  // When printing the boundary we need to go bottom up
  print_left_boundary(tree->left);
  printf("%d ", tree->value);
  // When printing the right side we need to go top down
  print_right_boundary(tree->right);
}

/*void print_inorder_succpred(bstree *tree, bstree *parent, int value) {
  if (tree == NULL) {
    return;
  }

  if (tree->value == value) {
    if (tree->left == NULL
    
  } else {
  }
  }*/

int check_bst(bstree *tree, int min, int max) {
  if (tree == NULL) {
    return 1;
  }

  printf("%d %d %d\n", tree->value, min, max);

  if (tree->value < min && tree->value > max) {
    return 1;
  }

  return check_bst(tree->left, min, tree->value) && check_bst(tree->right, tree->value, max);
}

bstree *lca(bstree *tree, int n1, int n2) {
  if (tree == NULL) {
    return NULL;
  }

  if (n1 <= tree->value && n2 >= tree->value) {
    return find(tree, n1) && find(tree, n2) ? tree : NULL;
  }

  if (n1 < tree->value && n2 < tree->value) {
    return lca(tree->left, n1, n2);
  } else {
    return lca(tree->right, n1, n2);
  }
}

int k = 0;
int getkth(bstree *tree, int kth) {
  if (tree == NULL) {
    return NULL;
  }

  int left = getkth(tree->left, kth);
  if (left != NULL)
    return left;

  if (k == kth)
    return tree->value;
  else {
    k++;
  }

  int right = getkth(tree->right, kth);
  if (right != NULL)
    return right;

  return NULL;
}

void print_range(bstree *tree, int n1, int n2) {
  if (tree == NULL) {
    return;
  }

  if (tree->value >= n1)
    print_range(tree->left, n1, n2);

  if (tree->value >= n1 && tree->value <= n2) {
    printf("%d ", tree->value);
  }

  if (tree->value <= n2)
    print_range(tree->right, n1, n2);
}

int is_identical(bstree *tree1, bstree *tree2) {
  if (tree1 == NULL && tree2 == NULL) {
    return 1;
  }

  if ((tree1 == NULL && tree2 != NULL) || (tree1 == NULL && tree2 != NULL)) {
    return 0;
  }

  if (tree1->value == tree2->value) {
    return 1 && is_identical(tree1->left, tree2->left) && is_identical(tree1->right, tree2->right);
  }

  return 0;
}

int pred = 0;
void add_greater_bst(bstree *tree1) {
  if (tree1 == NULL) {
    return;
  }

  add_greater_bst(tree1->right);
  tree1->value += pred;
  pred = tree1->value;
  add_greater_bst(tree1->left);
}

void sorted_merge_print(bstree *tree1, bstree *tree2) {
  if (tree1 == NULL && tree2 == NULL) {
    return;
  }

  if (tree1 == NULL) {
    sorted_merge_print(tree1, tree2->left);
    printf("%d ", tree2->value);
    sorted_merge_print(tree1, tree2->right);
    return;
  }

  if (tree2 == NULL) {
    return;
  }

  if (tree1->value < tree2->value) {
    sorted_merge_print(tree1->left, tree2);
    printf("%d ", tree1->value);
    sorted_merge_print(tree1->right, tree2);
  } else {
    sorted_merge_print(tree1, tree2->left);
    printf("%d ", tree2->value);
    sorted_merge_print(tree1, tree2->right);
  }
}

int main(int argc, char **argv) {
  bstree *t = create_bstree(50);
  add_with_level(t, 30, 0);
  add_with_level(t, 70, 0);
  add_with_level(t, 20, 0);
  add_with_level(t, 40, 0);
  add_with_level(t, 60, 0);
  add_with_level(t, 80, 0);

  print_boundary(t);
}
