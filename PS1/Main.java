import java.util.ArrayList;
import java.util.List;

public class Main {

    private static List<CustomState> states = new ArrayList<>();
    private static List<CustomState> targetStates = new ArrayList<>();
    private static int pSpace = 0;
    private static int graphSize = 0;

    public static void main(String[] args) {

        // Instantiate all valid states as a single node
        createNodes();
        // Create edges between all states that are achievable
        // from each other
        generateGraph();
        // Check that the graph was generated properly
        System.out.println("Graph verified: " + verifyGraph());
        // Print the problem space
        System.out.println("Problem Space: " + pSpace);
        // Find the initial state in the graph
        CustomState initialState = findNode(new CustomState(40, 40, 0, 0));
        // Start DFS from the given initial state
        depthFirstSearch(initialState);
        // Demonstrate a sample sequence of moves that traverses from
        // the initial state to the target state
//        printPath(initialState, targetStates.get(0));
        // Verify that DFS visited all nodes
        System.out.println("Nodes visited by DFS: " + graphSize);
        printGraph();
    }

    private static boolean isTarget(CustomState s) {
        return (s.cont3 == 2 && s.cont4 == 2);
    }

    private static CustomState findNode(CustomState s) {
        for (CustomState node : states) {
            if (node.equals(s)) {
                return node;
            }
        }
        return null;
    }

    private static void printPath(CustomState start, CustomState end) {
        System.out.println(end.toString());
        if(!start.equals(end)) {
            printPath(start, end.getPredecessor());
        }
    }

    /**
     * @param start - The starting state of the containers. In the case of the problem given
     *                      This is 40/40 quarts in container 1, 40/40 quarts in container 2, 0/5
     *                      quarts in container 3, and 0/4 quarts in container 4. This function
     *                      maintains an ordered list of the nodes traversed to get to the target
     *                      state called "path".
     * @return True if the target state is found, false if the target state is unachievable from the starting state
     */
    private static boolean depthFirstSearch(CustomState start) {
        if (isTarget(start)) {
            start.visited = true;
            System.out.println("Found target state");
            targetStates.add(start);
            return true; // Target state found
        } else {
            for (CustomState s : start.getAdjacencyList()) {
                if (!s.visited) {
                    graphSize++;
                    s.visited = true;
                    s.setPredecessor(start);
                    depthFirstSearch(s);
                }
            }
        }
        return false; // Target state not in graph
    }

    private static boolean verifyGraph() {
        List<CustomState> distinctStates = new ArrayList<>();
        for (CustomState node : states) {
            if (distinctStates.contains(node)) {
                return false;
            }
            distinctStates.add(node);
            if (node.getAdjacencyList().contains(node)) {
                return false;
            }
            for (CustomState adj : node.getAdjacencyList()) {
                if (!adj.getAdjacencyList().contains(node)) {
                    return false;
                }
            }
        }
        return true;
    }

    private static void printGraph() {
        for (CustomState  s : states) {
            System.out.println(s.toString());
        }
    }

    private static void createNodes() {
        for (int cont1 = 31; cont1 <= 40; cont1++) {
            for (int cont2 = 31; cont2 <= 40; cont2++) {
                for (int cont3 = 0; cont3 <= 5; cont3++) {
                    for (int cont4 = 0; cont4 <= 4; cont4 ++) {
                        if (cont1 + cont2 + cont3 + cont4 == 80) {
                            CustomState newState = new CustomState(cont1, cont2, cont3, cont4);
                            if (newState.isValid() && !states.contains(newState)) {
                                states.add(newState);
                                pSpace++;
                            }
                        }
                    }
                }
            }
        }
    }

    private static void generateGraph() {
        System.out.println("Generating graph...");
        for (CustomState state : states) {
            for (CustomState potentialAdj : states) {
                if (adjacent(state, potentialAdj)) {
                    state.getAdjacencyList().add(potentialAdj);
                }
            }
        }
    }

    private static boolean checkDiffs(int focus, int a, int b, int c) {
        if (focus == 0 && a == 0 && b == 0 && c == 0) return false;
        if (Math.abs(focus) == 1) {
            if (a == -focus && b == 0 && c == 0) {
                return true;
            } else if (a == 0 && b == -focus && c == 0) {
                return true;
            }else if ((a == 0 && b == 0 && c == -focus)) {
                return true;
            }
        }
        return false;
    }

    private static boolean adjacent(CustomState s1, CustomState s2) {
        int diff1 = s1.cont1 - s2.cont1;
        int diff2 = s1.cont2 - s2.cont2;
        int diff3 = s1.cont3 - s2.cont3;
        int diff4 = s1.cont4 - s2.cont4;
        if(s1.isValid() && s2.isValid()) {
            if (checkDiffs(diff1, diff2, diff3, diff4)) {
                return true;
            } else if (checkDiffs(diff2, diff1, diff3, diff4)) {
                return true;
            } else if (checkDiffs(diff3, diff1, diff2, diff4)) {
                return true;
            } else if (checkDiffs(diff4, diff1, diff2, diff3)) {
                return true;
            }
        }
        return false;
//            if (diff1 == -1) {
//                if (diff2 == 1 && diff3 == 0 && diff4 ==0) {
//                    return true;
//                } else if (diff2 == 0 && diff3 == 1 && diff4 ==0) {
//                    return true;
//                } else if (diff2 == 0 && diff3 == 0 && diff4 == 1) {
//                    return true;
//                }
//            } else if (diff1 == 1) {
//                if (diff2 == -1 && diff3 == 0 && diff4 ==0) {
//                    return true;
//                } else if (diff2 == 0 && diff3 == -1 && diff4 ==0) {
//                    return true;
//                } else if (diff2 == 0 && diff3 == 0 && diff4 == -1) {
//                    return true;
//                }
//            }
//            if (diff2 == -1) {
//                if (diff1 == 1 && diff3 == 0 && diff4 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff3 == 1 && diff4 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff3 == 0 && diff4 == 1) {
//                    return true;
//                }
//            } else if (diff2 == 1) {
//                if (diff1 == -1 && diff3 == 0 && diff4 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff3 == -1 && diff4 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff3 == 0 && diff4 == -1) {
//                    return true;
//                }
//            }
//            if (diff3 == -1) {
//                if (diff1 == 1 && diff2 == 0 && diff4 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff2 == 1 && diff4 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff2 == 0 && diff4 == 1) {
//                    return true;
//                }
//            } else if (diff3 == 1) {
//                if (diff1 == -1 && diff2 == 0 && diff4 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff2 == -1 && diff4 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff2 == 0 && diff4 == -1) {
//                    return true;
//                }
//            }
//            if (diff4 == -1) {
//                if (diff1 == 1 && diff2 == 0 && diff3 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff2 == 1 && diff3 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff2 == 0 && diff3 == 1) {
//                    return true;
//                }
//            } else if (diff4 == 1) {
//                if (diff1 == -1 && diff2 == 0 && diff3 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff2 == -1 && diff3 ==0) {
//                    return true;
//                } else if (diff1 == 0 && diff2 == 0 && diff3 == -1) {
//                    return true;
//                }
//            }
    }

}
