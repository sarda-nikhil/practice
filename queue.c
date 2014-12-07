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

int is_empty(queue *q) {
  return q->tail == q->front;
}

void next_greater_element(int *numbers, int n) {
  int current_max = numbers[0];

  queue *q = create_queue();

  for (int i = 1; i < n; i++) {
    if (numbers[i] > current_max) {
      current_max = numbers[i];
      add_item(q, (queue_item *) current_max);
    }
  }

  add_item(q, (queue_item *) -1);

  int flip = 0;
  current_max = (int) remove_item(q);
  
  for (int i = 0; i < n; i++) {    
    if (current_max <= numbers[i]) {
      if (flip == 0) {
	printf("%d ", -1);
      } else {
	current_max = (int) remove_item(q);
	flip = 0;
      }
    }

    if (current_max > numbers[i]) {
      flip = 1;
      printf("%d ", current_max);
    }
  }
}

/*int _main(int argc, char **argv) {
  queue *q = create_queue();

  int n[4] = {13, 7, 6, 12};
  next_greater_element(n, 4);
  }*/
