typedef void* list_item;

typedef struct list {
  int item;
  struct list* next;
} list;

list *create_list(int item);
void add_tail(list *list, int item);
void add_head(list *list, int item);
void add_item(list *list, int item);
void remove_item(list *list, int item); // This is some great pointer fuckery. 
void remove_all(list *list, int item);

void print_list(list *list);
void print_list_reverse(list *list);

list *reverse(list *list);
list *reverse1(list *list); // For LL problems, visualize first edge cases, then in the middle

list *add_numbers(list *list1, list *list2);

int get_nth(list *list, int n);
