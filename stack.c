#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "stack.h"
#include "queue.h"

stack *create_stack() {
  stack *s = (stack *) malloc(sizeof(stack));
  return s;
}

void push(stack *s, stack_item *item) {
  s->items[s->top++] = item;
}

stack_item* pop(stack *s) {
  if (s->top == 0) {
    return NULL;
  }

  return s->items[--s->top];
}

int is_stack_empty(stack *s) {
  return s->top == 0;
}

char *reversed(char *c, int n) {
  stack *s = create_stack();

  for (int i = 0; i < n - 1; i++) {
    push(s, (stack_item *)c[i]);
  }

  int i = 0;
  while(!is_stack_empty(s)) {
    c[i++] = (char)pop(s);
  }

  return c;
}

void reverse_stack(stack *s) {
  queue *temp = create_queue();
  while (!is_stack_empty(s)) {
    int item = (int)pop(s);
    add_item(temp, (queue_item *) item);
  }
  while(!is_empty(temp)) {
    int item = remove_item(temp);
    push(s, (stack_item *) item);
  }
}

int main(int argc, char **argv) {
  stack *s = create_stack();
  push(s, (stack_item *) 1);
  push(s, (stack_item *) 2);
  push(s, (stack_item *) 3);
  push(s, (stack_item *) 4);
  reverse_stack(s);
  printf("%d", (int) pop(s));
  printf("%d", (int) pop(s));
  printf("%d", (int) pop(s));
  printf("%d", (int) pop(s));
}
