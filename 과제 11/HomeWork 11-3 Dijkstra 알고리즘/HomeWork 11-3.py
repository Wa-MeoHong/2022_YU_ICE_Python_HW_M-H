# 파일명 : HomeWork 11-3.py
# 프로그램 목적 및 기능:  Dijkstra 알고리즘을 사용한 최단 거리 경로 탐색
# 프로그램 작성자 : 신대홍(2022년 5월 22일)
# 최종 Update : Version 1.0.0, 2022년 5월 22일(신대홍)
# =======================================================================
#     수정자          날짜        버전        수정내용
# =======================================================================
#     신대홍     2022/05/22     v1.0.0       최초작성

from mydijkstra import *

def main():
    G = WeightedGraph()
    initGraph(G) # G의 초기값 설정 
    nodes = G.getNode_NMs() #노드들을 G에 집어넣고
    edges = G.getWEdges() #edges를 G에 집어 넣는다.
    #노드와 엣지 출력
    print("Nodes : ", nodes)
    print("Edges : ")
    G.printEdges()

    print("\nConnectivity : ") # 연결 현황을 보여줌
    G.printConnectivity()
    print()
    path_Dijkstra, path_cost = Dijkstra(G, "GJ", "SC")
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}".format("GJ", "SC", path_Dijkstra, path_cost))
    path_Dijkstra, path_cost = Dijkstra(G, "SC", "GJ")
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}".format("SC", "GJ", path_Dijkstra, path_cost))
    path_Dijkstra, path_cost = Dijkstra(G, "SL", "BS")
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}".format("SL", "BS", path_Dijkstra, path_cost))
    path_Dijkstra, path_cost = Dijkstra(G, "BS", "SL")
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}".format("BS", "SL", path_Dijkstra, path_cost))
#
if __name__ == "__main__":
    main()