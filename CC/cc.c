#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* 
 * This struct stores the struct number and its edges in a connectvec
 */
typedef struct Node {
	int number;
	struct ConnectVec *conn_vec;
} Node;

/*
 * This struct stores and returns the edges of each node.
 */
typedef struct ConnectVec {
	size_t len;
	size_t capacity;
	size_t needle;		// used to retain position while iterating
	Node **arr;		
} ConnectVec;

ConnectVec *ConnectVecNew(void) {
	ConnectVec *new = malloc(sizeof(ConnectVec));
	new->len        = 0;
	new->capacity   = 8;
	new->needle     = 0;
	new->arr        = malloc(new->capacity*sizeof(Node*));
	return new;
}

int ConnectVecPush(ConnectVec* conn_vec, Node *target) {
	if (conn_vec->len == conn_vec->capacity) {
		conn_vec->capacity *= 2;
		conn_vec->arr = realloc(conn_vec->arr, conn_vec->capacity*sizeof(Node *));
	}
	conn_vec->arr[conn_vec->len] = target;
	conn_vec->len++;
	return conn_vec->len;
}

Node *ConnectVecYield(ConnectVec *conn_vec) {
	if (conn_vec->needle == conn_vec->len) {
		return NULL;
	} else {
		return conn_vec->arr[conn_vec->needle++];
	}
}

Node *NodeNew(int number) {
	Node *new     = malloc(sizeof(Node));
	new->number   = number;
	new->conn_vec = ConnectVecNew();
	return new;
}

/*
 * This type stores every node
 */
typedef struct {
	int nb_nodes;
	int nb_edges;
	Node **nodes;
} Graph;

Graph *GraphNew(int nb_nodes, int nb_edges) {
	Graph *new    = malloc(sizeof(Graph));
	new->nodes    = malloc(nb_nodes * sizeof(Node*));
	new->nb_nodes = nb_nodes;
	new->nb_edges = nb_edges;
	for (int i = 0; i < nb_nodes; i++) {
		new->nodes[i] = NodeNew(i+1);
	}
	return new;
}

void AddEdge(Node *from, Node *to) {
	ConnectVecPush(from->conn_vec, to);
}

bool all_true(bool *arr, size_t len) {
	for (int i = 0; i < len; i++) {
		if (arr[i] == false) {
			return false;
		}
	}
	return true;
} // check if all the values of a bool array are true

int first_not_visited(bool *arr) {
	size_t x = 0;
	while (true) {
		if (!arr[x]) {
			return x;
		} else {
			++x;
		}
	}
} // returns the first non-true value in a bool array
  // /!\ unsafe and will overflow the array if it is all true
  // only used after all_true() in this program so it's safe



/* 
 * This struct is a linked list that will allow depth-first search.
 */
typedef struct NodeLL {
	struct NodeLL *previous;
	struct NodeLL *next;
	Node   *node;
} NodeLL;

NodeLL *NodeLLNew (Node *node) {
	NodeLL *new   = malloc(sizeof(NodeLL));
	new->previous = NULL;
	new->next     = NULL;
	new->node     = node;
	return new;
}

NodeLL *NodeLLPop (NodeLL *target) {
	if (target->previous == NULL) {
		return NULL;
	} else {
		target->previous->next = NULL;
		return target->previous;
	}
}

NodeLL *NodeLLPush(NodeLL *target, Node* node) {
	target->next = NodeLLNew(node);
	target->next->previous = target;
	return target->next;
}


int main(void) {
	int n, nb_edges;
	scanf("%d %d", &n, &nb_edges);

	Graph *curr_graph = GraphNew(n, nb_edges);
	for (int i = 0; i < nb_edges; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		AddEdge(curr_graph->nodes[a-1], curr_graph->nodes[b-1]);
		AddEdge(curr_graph->nodes[b-1], curr_graph->nodes[a-1]);
	}
	

	bool *visited_nodes = malloc((n+1)*sizeof(bool));
	for (int i = 0; i <= n; i++) {
		visited_nodes[i] = false;
	}

	int curr_node_nb = 0;
	int components = 0;
	while (true) {
		if (all_true(&visited_nodes[1], n)) {
			printf("%d\n", components);
			return 0;
		} else {
			curr_node_nb += first_not_visited(&visited_nodes[curr_node_nb+1]) + 1;   // Current node is the first next non-visited.
			visited_nodes[curr_node_nb] = true;					 // Current node is now visited.
			NodeLL *search_list = NodeLLNew(curr_graph->nodes[curr_node_nb-1]);      // Initiate a search list at the current node.
			while (true) {
				Node *x = ConnectVecYield(search_list->node->conn_vec);          // Yield a connection from the connect vector.
				if (x == NULL) {						 // Result is null if the function has yielded every connection.
					if (search_list->previous == NULL) {			 // If we are at the root of the search list,
						break;						 // start a new one at the next non-visited node.
					} else {
						search_list = NodeLLPop(search_list);            // We have visited every node from the current edge,
						continue;	                                 // so we move back in the search.
					}
				} else {
					if (visited_nodes[x->number]) {                          // If we have visited that node, ignore it.
						continue;
					} else {
						visited_nodes[x->number] = true;		 // If we haven't, we visit it,
						search_list = NodeLLPush(search_list, x);	 // and push it to the list.
					}
			}
		}
		++components;
		}
	}
}
