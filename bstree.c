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
    printf("%d\n", t->value);

    if (t->left != NULL) {
      add_item(q, (queue_item*) t->left);
    }

    if (t->right != NULL) {
      add_item(q, (queue_item*) t->right);
    }

  } while (t != NULL);
}

int main(int argc, char **argv) {
  bstree *t = create_bstree(10);

  add(t, 5);
  add(t, 15);
  add(t, 6);
  add(t, 14);
  add(t, 4);
  add(t, 16);

  print_dfs(t);

  printf("%d\n", find(t, 5));
  printf("%d\n", find(t, 15));
  printf("%d\n", find(t, 14));
  printf("%d\n", find(t, 16));

  printf("%d\n", find(t, 100));
  printf("%d\n", find(t, -1));
}
