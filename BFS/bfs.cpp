#include <vector>
#include <iostream>
#include <unordered_set>

using namespace std;

// Node class
class Node {
	public:
		vector<Node*> neighbours;
		int number;
		Node(int);
		void add_edge(Node*);
};

Node::Node(int x) {
	number = x;
} // constructor

void Node::add_edge(Node *nb) {
	this->neighbours.push_back(nb);
} // adds an edge by adding a reference to the neigbour


// Graph class
class Graph {
	public:
		vector<Node> nodes;
		Graph(int);
		int bfsearch(int, int);
};

Graph::Graph(int n) {
	for (int i = 1; i <= n; i++) {
		class Node *new_node = new class Node(i);
		nodes.push_back(*new_node);
	}
} // constructor

int Graph::bfsearch(int from, int to) {
	// performs a breadth-first search to return the number of nodes
	// between from and to, or -1 if they are not connected
	if (from == to) {
		return 0;
	}
	unordered_set<int> visited;
	unordered_set<Node*> current;
	unordered_set<Node*> added_this_cycle;
	current.insert(&this->nodes[from-1]);
	visited.insert(from);
	int result = 0;
	bool added = true;
	while (added) {
		++result;
		added_this_cycle.clear();
		added = false;
		for (auto x: current) {              // for each nodes
			for (auto y: x->neighbours) { // for each of its neighbours
				if (y->number == to) {
					return result;
				} else if (visited.count(y->number)) {
					continue;   // we have seen this edge before
				} else {
					visited.insert(y->number);
					added_this_cycle.emplace(y);
					added = true;
				}
			}
		}
		current = added_this_cycle;
	}
	return -1;
}

int main(void) {
	// parsing first line to get info on the graph
	int n, num_edges;
	cin >> n >> num_edges;

	// creating graph
	Graph *curr_graph = new Graph(n);

	// adding connections
	for (int i = 0; i < num_edges; i++) {
		int a, b;
		cin >> a >> b;
		curr_graph->nodes[a-1].add_edge(&curr_graph->nodes[b-1]); // [(a|b)-1] to convert 1 based indices to 0
	}

	for (int i = 1; i <= n; i++) {
		cout << curr_graph->bfsearch(1, i) << " ";
	}
	cout << endl;
}
