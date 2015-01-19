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

// EPI 8.1
list *merge(list *l1, list *l2) {
  if (l1 == NULL) {
    return l2;
  } else if (l2 == NULL) {
    return l1;
  }

  list *start = NULL;
  list *curr = NULL;

  if (l1->item > l2->item) {
    start = l2;
    l2 = l2->next;
  } else {
    start = l1;
    l1 = l1->next;
  }
  curr = start;

  while (l1 != NULL && l2 != NULL) {
    if (l1->item > l2->item) {
      curr->next = l2;
      l2 = l2->next;
    } else {
      curr->next = l1;
      l1 = l1->next;
    }

    curr = curr->next;

    if (l1 == NULL) {
      curr->next = l2;
    } else if (l2 == NULL) {
      curr->next = l1;
    }
  }

  return start;
}

// EPI 8.2
list *reverse_nonrec(list *l1) {
  if (l1 == NULL) {
    return l1;
  }

  list *prev = l1;
  list *curr = l1->next;
  list *temp = NULL;
  prev->next = NULL;

  while (curr != NULL) {
    temp = curr;
    curr = curr->next;
    temp->next = prev;
    prev = temp;
  }

  return prev;
}

// EPI 8.3
// Revisit this problem. This does not handle cases where k = 0
// This is needed for the next problem
list *reverse_sublist(list *l1, int k, int f) {
  list *sublist_start = l1;
  list *sublist_end = NULL;
  list *sublist_next = NULL;

  if (l1 == NULL) {
    return l1;
  }

  for (int i = 0; i < k - 1; i++) {
    sublist_start = sublist_start->next;
    if (sublist_start == NULL) {
      return NULL;
    }
  }

  sublist_end = sublist_start;

  for (int i = 0; i < f - 1; i++) {
    sublist_end = sublist_end->next;
    if (sublist_end == NULL) {
      return NULL;
    }
  }

  sublist_next = sublist_end->next;
  sublist_end->next = NULL;

  sublist_start->next = reverse_nonrec(sublist_start->next);

  while (sublist_start->next != NULL) {
    sublist_start = sublist_start->next;
  }
  sublist_start->next = sublist_next;

  return l1;
}



int main(int argc, char **argv) {
  list *l1 = create_list(2);
  add_item(l1, 5);
  add_item(l1, 7);
  add_item(l1, 9);
  add_item(l1, 11);
  add_item(l1, 13);
  add_item(l1, 15);
  add_item(l1, 17);
  add_item(l1, 19);
  add_item(l1, 21);
  add_item(l1, 23);

  print_list(reverse_sublist(l1, 0, 3));
}
