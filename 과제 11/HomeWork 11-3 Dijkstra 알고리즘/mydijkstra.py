# 파일명 : mydijkstra.py
# 프로그램 목적 및 기능:  WeightedGraph 등의 클래스를 만들어둔 파일
# 프로그램 작성자 : 신대홍(2022년 5월 22일)

import sys 

class Node(object): # Node 클래스
    def __init__(self, name): # 초기값 설정
        self.name = name

    def getName(self): # 이름 반환
        return self.name

    def __str__(self): #이름 반환(문자열)
        return self.name
#
class Edge(object): # Edge 클래스
    def __init__(self, src_nm, dest_nm): # Edge 초기값
        self.src_nm = src_nm # 출발
        self.dest_nm = dest_nm # 도착

    def getSource_nm(self): # 출발
        return self.src_nm

    def getDestination_nm(self): # 도착
        return self.dest_nm
    
    def __str__(self): # 출력 형식
        return "{:3}=>{:3}".format(self.src_nm, self.dest_nm)
#
class WeightedEdge(Edge): # WeightedEdge 클래스
    def __init__(self, src_nm, dest_nm, weight=1.0): # 초기값 설정
        Edge.__init__(self, src_nm, dest_nm) # Edge(도시간 거리) 초기값 설정
        self.weight = weight # 거리 설정

    def getWeight(self): #거리 반환
        return self.weight 

    def __str__(self): # 출력 형식
        return "{:3}->{:3} ({:3})".format(self.src_nm, self.dest_nm, self.weight)
#
class WeightedGraph(object): #DiGraph 클래스 (WeightedGraph) 그래프 토폴로지
    def __init__(self):
        self.nodes = [] # list of Node(v_id, v_names)
        self.node_names = [] # 노드 이름들
        self.wedges = [] # Weightededge된 리스트
        self.adjacencyList = {} # 딕셔너리 of {src_nm:list of node_names)
        self.edgeWeights = {} # dictionary of {edge(src_nm, dest_nm):weight}

    def addNode(self, node): # 노드 추가
        if node in self.nodes: #만약 노드가 추가되어있다면
            raise ValueError("Duplicated node") #안함
        else: #없으면 추가 및 작업
            self.nodes.append(node)
            node_nm = node.getName()
            self.node_names.append(node_nm)
            self.adjacencyList[node_nm] = []

    def addEdge(self, weighted_edge): # 엣지 추가 
        src_nm = weighted_edge.getSource_nm()
        dest_nm = weighted_edge.getDestination_nm()
        if not (src_nm in self.node_names and dest_nm in self.node_names): #만약에 대응되는 노드가 없으면 X
            raise ValueError("Node not in graph")
        self.wedges.append(weighted_edge) # 노드 추가
        self.adjacencyList[src_nm].append(dest_nm)
        self.edgeWeights[(src_nm, dest_nm)] = weighted_edge.getWeight()

    def getNeighbors(self, node_nm): # 이웃하는 도시
        return self.adjacencyList[node_nm]

    def getAdjacencyList(self): # 이웃하는 도시 리스트
        return self.adjacencyList

    def getNode_NMs(self): #노드 이름들 반환
        return self.node_names

    def getWEdges(self): # 엣지 반환
        return self.wedges

    def getEdgeWeight(self, edge): # 거리를 반환
        if (edge.src_nm, edge.dest_nm) in self.edgeWeights:
            return self.edgeWeights[(edge.src_nm, edge.dest_nm)]
        else:
            None

    def printConnectivity(self): # 연결되어있는 도시 출력
        for node_nm in self.node_names:
            print(" AdjacencyList[{}] = {}".format(node_nm, self.adjacencyList[node_nm]))

    def printEdges(self): #edge 출력
        eCount = 0
        for e in self.wedges:
            print(" {}".format(e), end=', ')
            eCount += 1
            if eCount % 5 == 0:
                print()

    def __str__(self): # 출력형식
        result = ''
        for src in self.nodes:
            for dest in self.wedges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
            return result[:-1]
#
PLUS_INF = sys.maxsize

def Dijkstra(G, start_nm, end_nm): # 그래프 토폴로지 및 최단거리 경로 탐색 함수
    errorInLoop = False
    nodeAccWeight = {}
    nodeStatus = {}
    prevNodes_nm = {}
    selectedNodes = []
    remainingNodes = []
    for node_nm in G.node_names: # remainingNodes에 먼저 저장 
        e = Edge(start_nm, node_nm) 
        if node_nm == start_nm:
            eWeight = 0
        else:
            eWeight = G.getEdgeWeight(e)
            if eWeight == None:
                eWeight = PLUS_INF
        nodeAccWeight[node_nm] = eWeight
        nodeStatus[node_nm] = False
        prevNodes_nm[node_nm] = start_nm
        if node_nm != start_nm:
            remainingNodes.append(node_nm)
    nodeAccWeight[start_nm] = 0
    nodeStatus[start_nm] = True
    selectedNodes.append(start_nm) #선택된 노드들에 저장
    count = 1

    while len(remainingNodes) != 0: # remainingNode의 개수가 0개가 될때까지
        minAccWeight = PLUS_INF
        minNode = None
        for n in remainingNodes: # 솎아내기
            nAccWeight = nodeAccWeight[n]
            if (nAccWeight != None) and (nAccWeight < minAccWeight):
                minNode, minAccWeight = n, nodeAccWeight[n]
        if minNode == None: # 가장 작은 노드가 없다면
            print("No minNode was selected at this round !!")
            print("Error - graph is not fully connected !!")
            errorInLoop = True
            break #탈출
        else:
            selectedNodes.append(minNode) 
            minAccWeight = nodeAccWeight[minNode]
            for rn in remainingNodes:
                if rn == minNode:
                    continue
                e = Edge(minNode, rn)
                eWeight = G.getEdgeWeight(e)
                if eWeight == None:
                    continue
                if nodeAccWeight[rn] > minAccWeight + eWeight:
                    nodeAccWeight[rn] = minAccWeight + eWeight
                    prevNodes_nm[rn] = minNode
            if minNode == end_nm:
                break
            remainingNodes.remove(minNode) # remianingNodes에서 요소를 제거해간다.
        count += 1
    if errorInLoop == True:
        return None

    path = [end_nm] #남은 노드들을 찾는다.
    cur_node_nm = end_nm
    while cur_node_nm in selectedNodes: #selectedNodes에 있다면
        if cur_node_nm == start_nm: # start_nm(출발지)와 같다면
            break #탈출
        else:
            cur_node_nm = prevNodes_nm[cur_node_nm] #아니면 path에 넣는다.
            path.insert(0,cur_node_nm)
    return path, nodeAccWeight[end_nm]

def initGraph(G): # 노드 초기값 설정
    node_names = ["SL", "CC", "SC", "SW", "WJ", "GR", "DJ", "DG", "PH", "GJ", "BS"]
    w_edges = [ WeightedEdge("SL", "CC", 71), WeightedEdge("CC", "SL", 71),\
                WeightedEdge("SL", "SW", 34), WeightedEdge("SW", "SL", 34),\
                WeightedEdge("CC", "SC", 79), WeightedEdge("SC", "CC", 79),\
                WeightedEdge("CC", "WJ", 47), WeightedEdge("WJ", "CC", 47),\
                WeightedEdge("SC", "GR", 42), WeightedEdge("GR", "SC", 42),\
                WeightedEdge("SW", "WJ", 84), WeightedEdge("WJ", "SW", 84),\
                WeightedEdge("WJ", "GR", 91), WeightedEdge("GR", "WJ", 91),\
                WeightedEdge("GR", "PH", 200), WeightedEdge("PH", "GR", 200),\
                WeightedEdge("DJ", "SW", 109), WeightedEdge("SW", "DJ", 109),\
                WeightedEdge("GJ", "DJ", 138), WeightedEdge("DJ", "GJ", 138),\
                WeightedEdge("GJ", "DG", 170), WeightedEdge("DG", "GJ", 170),\
                WeightedEdge("WJ", "DG", 174), WeightedEdge("DG", "WJ", 174),\
                WeightedEdge("DJ", "DG", 120), WeightedEdge("DG", "DJ", 120),\
                WeightedEdge("DG", "PH", 66), WeightedEdge("PH", "DG", 66),\
                WeightedEdge("DG", "BS", 87), WeightedEdge("BS", "DG", 87),\
                WeightedEdge("GJ", "BS", 202), WeightedEdge("BS", "GJ", 202),\
                WeightedEdge("BS", "PH", 93), WeightedEdge("PH", "BS", 93) ]
    # 노드들끼리 반대방향으로도 지정해야해서 총 17 * 2개의 요소가 필요
    for i in range(len(node_names)): # 노드의 개수만큼
        v_name = node_names[i]
        node = Node(v_name)
        G.addNode(node) # 노드들을 추가한다.
    for we in w_edges: #에지를 추가한다.
        G.addEdge(we)
    return G