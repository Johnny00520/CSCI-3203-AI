import java.util.ArrayList;
import java.util.List;

public class CustomState {

    public static int count = 0;
    boolean visited = false;
    private CustomState predecessor;
    private List<CustomState> adjacencyList;

    int cont1; // Cap = 40
    int cont2; // Cap = 40
    int cont3; // Cap = 5
    int cont4; // Cap = 4

    CustomState(int container1, int container2, int container3, int container4) {
        predecessor = null;
        adjacencyList = new ArrayList<>();
        this.cont1 = container1;
        this.cont2 = container2;
        this.cont3 = container3;
        this.cont4 = container4;
        count++;
    }

    public CustomState getPredecessor() {
        return predecessor;
    }

    public void setPredecessor(CustomState predecessor) {
        this.predecessor = predecessor;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof CustomState) {
            CustomState s = (CustomState) obj;
            if(this.cont1 == s.cont1 && this.cont2 == s.cont2 && this.cont3 == s.cont3 && this.cont4 == s.cont4) {
                return true;
            }
            if (this.cont1 == s.cont2 && this.cont2 == s.cont1 && this.cont3 == s.cont3 && this.cont4 == s.cont4) {
                return true;
            }
        }
        return false;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("--------------------\n");
        sb.append("NODE :: container 1 : " + cont1 + "/40\n" +
                "        container 2 : " + cont2 + "/40\n" +
                "        container 3 : " + cont3 + "/5\n" +
                "        container 4 : " + cont4 + "/4");
        sb.append("\n Adjacency List");
        for (CustomState adj : getAdjacencyList()) {
            sb.append(" -> NODE:" + adj.cont1 + "," + adj.cont2 + "," + adj.cont3 + "," + adj.cont4);
        }
        sb.append("\n--------------------");
        sb.append("\n");
        return sb.toString();
    }

    public List<CustomState> getAdjacencyList() {
        return adjacencyList;
    }

    public boolean isValid() {
        if (cont1 > 40 || cont1 < 0) {
            return false;
        }
        if (cont2 > 40 || cont2 < 0) {
            return false;
        }
        if (cont3 > 5 || cont3 < 0) {
            return false;
        }
        if (cont4 > 4 || cont4 < 0) {
            return false;
        }
        if (cont1 + cont2 + cont3 + cont4 != 80) {
            return false;
        }
        return true;
    }

}
