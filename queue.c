#include <stdio.h>
#include <stdlib.h>

#include "queue.h"

queue *create_queue() {
  queue *q = (queue *) malloc(sizeof(queue));
  q->tail = 0;
  q->front = 0;
  return q;
}

void add_item(queue *q, queue_item *item) {
  q->items[q->tail % MAX_QUEUE_SIZE] = item;
  q->tail++;
}

queue_item *remove_item(queue *q) {
  if (q->tail == q->front) {
    return NULL;
  }
  return q->items[q->front++];
}

/*int main(int argc, char **argv) {
  queue *q = create_queue();
  add_item(q, (queue_item*) 1);
  add_item(q, (queue_item*) 2);
  add_item(q, (queue_item*) 3);
  add_item(q, (queue_item*) 4);
  printf("%d", (int)remove_item(q));
  printf("%d", (int)remove_item(q));
  printf("%d", (int)remove_item(q));
  printf("%d", (int)remove_item(q));
  add_item(q, (queue_item*) 5);
  printf("%d", (int)remove_item(q));
  }*/
