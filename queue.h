#define MAX_QUEUE_SIZE 100

typedef void* queue_item;

typedef struct queue {
  queue_item items[MAX_QUEUE_SIZE];
  int tail;
  int front;
} queue;

queue *create_queue();
void add_item(queue *q, queue_item *item);
queue_item *remove_item(queue *q);
int is_empty(queue *q);

void next_greater_element(int *numbers, int n); // Got fucked


