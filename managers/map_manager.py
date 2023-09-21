import random


def generate_able_edges(pre_nodes, nodes):
    able_edges = []

    for pre_node in pre_nodes:
        for node in nodes:
            if abs(pre_node - node) <= 1:
                able_edges.append([pre_node, node])

    return able_edges


def select_random_elements(arr, n):
    if n >= len(arr):
        return arr

    selected_elements = random.sample(arr, n)
    return selected_elements


def remove_value(my_list, value):
    """Remove the first occurrence of a value in a list if it exists."""
    if value in my_list:
        my_list.remove(value)


def print_map(nodes, edges):
    def initialize_map():
        # 가로와 세로 크기 계산
        map_width = MapManager.MAX_NODE + ((MapManager.MAX_NODE - 1) * MapManager.MAP_SPACE_GAP)
        map_height = MapManager.MAX_LEVEL + ((MapManager.MAX_LEVEL - 1) * MapManager.MAP_SPACE_GAP)

        # 초기 맵 생성
        map_grid = [['□' for _ in range(map_width)] for _ in range(map_height)]

        # 노드 추가
        for i in range(len(nodes)):  # 0, 1
            level = (i) * MapManager.MAP_SPACE_GAP + i
            for j in nodes[i]:
                node = j + (j - 1) * MapManager.MAP_SPACE_GAP
                map_grid[level][node - 1] = '■'  # 0 ,0 0,2 2,0

        for level in range(len(edges)):
            start_y = level + level * MapManager.MAP_SPACE_GAP
            for i in edges[level]:
                start_x = i[0] + (i[0] - 1) * MapManager.MAP_SPACE_GAP - 1
                dir = i[1] - i[0]
                for gap_index in range(1, MapManager.MAP_SPACE_GAP + 1):
                    map_grid[start_y + gap_index][start_x + gap_index * dir] = '◆'

        return map_grid

    # 테스트 용 빈 맵 생성
    map_grid = initialize_map()

    # 맵 출력
    for row in map_grid:
        print(''.join(row))


class MapManager:
    # Make Edge
    START_NODE_NUMBER = 4
    MAX_LEVEL = 12
    MAX_NODE = 7
    EDGE_LINE_NUMBER = 6
    MAX_NODE_BY_LEVEL = 4
    MAX_EDGE_BY_LEVEL = 6
    MAP_SPACE_GAP = 3

    def __init__(self):
        self.map = self.make_map()

    def generate_able_nodes(self, pre_node):
        able_nodes = set()

        for node in pre_node:
            possible_nodes = [node - 1, node, node + 1]
            for n in possible_nodes:
                if 1 <= n <= self.MAX_NODE:
                    able_nodes.add(n)

        return list(able_nodes)

    def make_load(self):
        pass

    def make_map(self):
        """
            1. 이전 레벨 노드를 참조해서 가능한 노드 집합을 만듬
            2. 해당 노드 집합 중에서 MAX_NODE_BY_LEVEL 이하에 노드를 채택함
            3. 이전 노드 와 현제 노드 집합중에서 연결 가능한 엣지 집합을 만듬
            4. 해당 집합 중에서 MAX_EDGE_BY_LEVEL 이하에 엣지를 채택함

        game_map_able_node = [
            [[4],
            [3,4,5],
            [2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6,7],
            [1,2,3,4,5,6,7],
            [1,2,3,4,5,6,7],
            [1,2,3,4,5,6,7],
        
        game_map_node = [
            [[4],
            [3,4,5],
            [2,3,4,5],
            [3,4,5,7],
            [4,3,2,1]]
        game_map_able_edge = [
            [(4,3),(4,4),(4,5)],
            [(3,2),(3,3),(3,4),(4,3) ...]
            
            ]
        
        game_map_edge = [
            []
            
            ]
        """
        nodes_list = []
        edges_list = []
        pre_nodes = []
        # level 개수 만큼
        for level_index in range(MapManager.MAX_LEVEL):
            able_nodes = []
            nodes = []
            able_edges = []
            edges = []
            if level_index == 0:
                nodes = [MapManager.START_NODE_NUMBER]
                pre_nodes = nodes
                nodes_list.append(nodes)
                continue
            else:
                # 가능한 노드 집합
                able_nodes = self.generate_able_nodes(pre_nodes)
                # 가능한 노드 집합 중에서 n개 뽑기
                is_possible_nodes = []
                while True:
                    nodes = select_random_elements(able_nodes, MapManager.MAX_NODE_BY_LEVEL)
                    is_possible_nodes = pre_nodes.copy()
                    for i in nodes:
                        remove_value(is_possible_nodes, i+1)
                        remove_value(is_possible_nodes, i)
                        remove_value(is_possible_nodes, i-1)
                    if not is_possible_nodes:
                        break
                nodes_list.append(nodes)
                # 가능한 엣지 구하기
                # n개 뽑기
                able_edges = generate_able_edges(pre_nodes, nodes)
                is_possible_pre_nodes = []
                while True:
                    edges = select_random_elements(able_edges, MapManager.MAX_EDGE_BY_LEVEL)
                    is_possible_nodes = nodes.copy()
                    is_possible_pre_nodes = pre_nodes.copy()
                    for i in edges:
                        remove_value(is_possible_pre_nodes, i[0])
                        remove_value(is_possible_nodes, i[1])
                    if not is_possible_pre_nodes and not is_possible_nodes:
                        break
            edges_list.append(edges)
            pre_nodes = nodes

        return  nodes_list, edges_list


e = MapManager()
print_map(e.map[0],e.map[1])