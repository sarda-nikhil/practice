#include <stdlib.h>
#include <stdio.h>

#include "list.h"

list *create_list(int item) {
  list *l = (list *)malloc(sizeof(list));
  l->item = item;
  return l;
}

void add_item(list *list, int item) {
  while (list->next != NULL) {
    list = list->next;
  }

  list->next = create_list(item);
}

void print_list(list *list) {
  if (list == NULL) {
    return;
  }

  do {
    printf("%d ", list->item);
    list = list->next;
  } while (list != NULL);
}

void print_reverse(list *list) {
  if (list == NULL)
    return;

  print_reverse(list->next);
  printf("%d ", list->item);
}

list *head;
list *reverse(list *list) {
  struct list *tmp;
  if (list->next == NULL) {
    head = list;
    return list;
  }
  tmp = reverse(list->next);
  tmp->next = list;
  list->next = NULL;
  return list;
}

list *reverse1(list *list) {
  struct list *tmp, *tmp1;
  tmp = list;

  if (tmp->next == NULL)
    return tmp;

  list = list->next;
  tmp->next = NULL;
  while (list->next != NULL) {
    tmp1 = tmp;
    tmp = list;
    list = list->next;
    tmp->next = tmp1;
  }
  list->next = tmp;
  return list;
}

void remove_item(list *list, int item) {
  // List is empty
  if (list == NULL) {
    return;
  }

  // First element is it
  if (list->item == item) {
    struct list *tmp = list;
    // BOOYAHKASHA
    *list = *list->next;
    return;
  }

  // Start iterating
  struct list *prev = list;
  struct list *curr = list->next;
  while(curr != NULL) {
    if (curr->item == item) {
      prev->next = curr->next;
      return;
    } else {
      prev = curr;
      curr = curr->next;
    }
  }
}

void remove_all(list *list, int item) {
  // List is empty
  if (list == NULL) {
    return;
  }

  // First element is it
  if (list->item == item) {
    struct list *tmp = list;
    // BOOYAHKASHA
    *list = *list->next;
  }

  // Start iterating
  struct list *prev = list;
  struct list *curr = list->next;
  while(curr != NULL) {
    if (curr->item == item) {
      prev->next = curr->next;
    } else {
      prev = curr;
    }
    curr = curr->next;
  }
}


list *add_numbers(list *list1, list *list2) {
  list *tmp = create_list(0);
  list *head = tmp;
  int carry = 0;
  
  while(list1 || list2) {
    if (list1 != NULL && list2 != NULL) {
      tmp->item = (list1->item + list2->item + carry) % 10;
      carry = (list1->item + list2->item + carry) / 10;
      list1 = list1->next;
      list2 = list2->next;
    } else if (list1 != NULL && list2 == NULL) {
      tmp->item = (list1->item + carry) % 10;
      carry = (list1->item + carry) / 10;
      list1 = list1->next;
    } else if (list1 == NULL && list2 != NULL) {
      tmp->item = (list2->item + carry) % 10;
      carry = (list2->item + carry) / 10;
      list2 = list2->next;
    }

    tmp->next = create_list(carry);
    tmp = tmp->next;
  }

  return head;
}

void add_head(list *list, int item) {
  struct list *l = create_list(item);
  l->next = create_list(list->item);
  l->next->next = list->next;
  *list = *l;
}

int get_nth(list *list, int n) {
  while (list != NULL && n > 0) {
    list = list->next;
    n--;
  }

  if (list != NULL)
    return list->item;

  return -1;
}

int main(int argc, char **argv) {
  list *l1 = create_list(1);
  for (int i = 2; i < 10; i++) {
    add_item(l1, i);
    add_item(l1, 5);
  }

  add_head(l1, 42);

  //print_list(l1);

  printf("%d %d", get_nth(l1, 1), get_nth(l1, 0));
}
