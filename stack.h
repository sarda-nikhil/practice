#define MAX_STACK_SIZE 100

typedef void* stack_item;

typedef struct stack {
  stack_item items[MAX_STACK_SIZE];
  int top;
} stack;

stack *create_stack();
void push(stack *s, stack_item* item);
stack_item* pop(stack *s);
int is_stack_empty(stack *s);

// gfg

char *reversed(char *s, int n);

void reverse_stack(stack *s);
