from collections import deque
import pygame
import heapq
import itertools
import time
#Cấu hình cho game
WIDTH, HEIGHT = 320, 690 
TILE_SIZE = WIDTH // 3     
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (173, 215, 230)
RED = (255, 99, 70)
GREEN = (144, 238, 144)
GRAY = (200, 200, 200)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8 Puzzle Solver")
clock = pygame.time.Clock()

# Khởi tạo trạng thái đầu và đích
INITIAL_STATE = ("2", "6", "5", "", "8", "7", "4", "3", "1")
# INITIAL_STATE = ("1", "2", "3", "4", "", "5", "6", "7", "8")
# INITIAL_STATE = ("1", "2", "3", "", "5", "6", "4", "7", "8")

GOAL_STATE = ("1", "2", "3", "4", "5", "6", "7", "8", "")

#Thiết kế giao diện game
def draw_board(state, message="", runtime = None):
    screen.fill(WHITE)
    if len(state) != 9:
        print(f"⚠️ Lỗi: Kích thước của state không phải là 9, mà là {len(state)}.")
        return
    for i in range(3):
        for j in range(3):
            value = state[i*3+j]
            x,y = j*TILE_SIZE, i*TILE_SIZE
            color = BLUE if value != "" else  WHITE
            pygame.draw.rect(screen, color, (x , y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, BLACK,(x , y, TILE_SIZE, TILE_SIZE),2)

            if value != "":
                font = pygame.font.Font(None,44)
                text = font.render(value, True, BLACK)
                text_rect = text.get_rect(center=(x+TILE_SIZE//2, y+TILE_SIZE//2))
                screen.blit(text,text_rect)

    draw_button(20, HEIGHT - 315, 85, 35, "0 Ob", GREEN)
    draw_button(120, HEIGHT - 315, 85, 35, "QLearning", GREEN)
    draw_button(220, HEIGHT - 315, 85, 35, "Reset", RED)

    draw_button(20, HEIGHT - 270, 85, 35, "BBSS", GREEN)
    draw_button(120, HEIGHT - 270, 85, 35, "POS", GREEN)
    draw_button(220, HEIGHT - 270, 85, 35, "CSP", GREEN)

    draw_button(20, HEIGHT - 225, 85, 35, "Simulated", GREEN)
    draw_button(120, HEIGHT - 225, 85, 35, "Genetic", GREEN)
    draw_button(220, HEIGHT - 225, 85, 35, "And-Or", GREEN)

    draw_button(20, HEIGHT - 180, 85, 35, "Steepest", GREEN)
    draw_button(120, HEIGHT - 180, 85, 35, "Stochastic", GREEN)
    draw_button(220, HEIGHT - 180, 85, 35, "Beam", GREEN)


    draw_button(20, HEIGHT - 135, 85, 35, "A*", GREEN)
    draw_button(120, HEIGHT - 135, 85, 35, "IDA*", GREEN)
    draw_button(220, HEIGHT - 135, 85, 35, "Simple", GREEN)


    draw_button(20, HEIGHT - 90, 85, 35, "BFS", GREEN)
    draw_button(120, HEIGHT - 90, 85, 35, "DFS", GREEN)
    draw_button(220, HEIGHT - 90, 85, 35, "IDS", GREEN)

    draw_button(20, HEIGHT - 45, 85, 35, "UCS", GREEN)
    draw_button(120, HEIGHT - 45, 85, 35, "Greedy", GREEN)
    draw_button(220, HEIGHT - 45, 85, 35, "Thoát", BLACK)

    font = pygame.font.Font(None, 30)
    text = font.render(message, True, BLACK)
    screen.blit(text, (20, HEIGHT - 360))
    if runtime is not None:
        font = pygame.font.Font(None, 30)
        runtime_text = f"Thoi gian chay: {runtime:.3f} s"
        runtime_surface = font.render(runtime_text, True, BLACK)
        screen.blit(runtime_surface, (20, HEIGHT - 340))

    pygame.display.flip()


def draw_button(x, y, width, height, text, color):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    is_hover = x <= mouse_x <= x + width and y <= mouse_y <= y + height

    pygame.draw.rect(screen, GRAY if is_hover else color, (x, y, width, height), border_radius=8)
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2, border_radius=8)
    font = pygame.font.Font(None, 25)
    text_render = font.render(text, True, WHITE if color == BLACK else BLACK)
    text_rect = text_render.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_render, text_rect)

#Hàm hỗ trợ
def get_blank_index(state):
    if "" not in state:
        print("⚠️ Lỗi: state không chứa ô trống:", state)
        return -1  # hoặc có thể raise lỗi nếu bạn muốn dừng hẳn
    return state.index("")


def get_neighbors(index):
    moves = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 
        3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8], 
        6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
    }
    return moves[index]

def swap_positions(state, blank_index, move):
    state = list(state)
    state[blank_index], state[move] = state[move], state[blank_index]
    return tuple(state)

def manhattan_distance(state):
    distance = 0
    for i, value in enumerate(state):
        if value == "":
            continue
        target_index = GOAL_STATE.index(value)
        x1, y1 = i % 3, i // 3
        x2, y2 = target_index % 3, target_index // 3
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

#Thuật toán Greedy Search
def greedy_search_solve(initial_state):
    queue = [(manhattan_distance(initial_state), initial_state, [])]
    visited = set()
    visited.add(initial_state)

    while queue:
        _, current_state, path = heapq.heappop(queue)

        if current_state == GOAL_STATE:
            return path

        blank_index = get_blank_index(current_state)

        for move in get_neighbors(blank_index):
            new_state = swap_positions(current_state, blank_index, move)
            if new_state not in visited:
                visited.add(new_state)
                heapq.heappush(queue, (manhattan_distance(new_state), new_state, path + [new_state]))

    return None

#Thuật toán IDS
def ids_solve(initial_state):
    def dfs_limited(state, path, depth, limit):
        if state == GOAL_STATE:
            return path
        if depth == limit:
            return None

        blank_index = get_blank_index(state)
        for move in get_neighbors(blank_index):
            new_state = swap_positions(state, blank_index, move)
            if new_state not in path:  
                result = dfs_limited(new_state, path + [new_state], depth + 1, limit)
                if result:
                    return result
        return None

    limit = 0
    while True:
        result = dfs_limited(initial_state, [], 0, limit)
        if result:
            return result
        limit += 1

#Thuật toán UCS
def ucs_solve(initial_state):
    queue = [(0, initial_state, [])]
    visited = set()
    visited.add(initial_state)

    while queue:
        cost, current_state, path = heapq.heappop(queue)

        if current_state == GOAL_STATE:
            return path

        blank_index = get_blank_index(current_state)

        for move in get_neighbors(blank_index):
            new_state = swap_positions(current_state, blank_index, move)
            if new_state not in visited:
                visited.add(new_state)
                heapq.heappush(queue, (cost + 1, new_state, path + [new_state]))

    return None

#Thuật toán BFS
def bfs_solve(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state == GOAL_STATE:
            return path

        blank_index = get_blank_index(current_state)

        for move in get_neighbors(blank_index):
            new_state = swap_positions(current_state, blank_index, move)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

#Thuật toán DFS 
def dfs_solve(initial_state):
    stack = [(initial_state, [], 0)]  
    visited = set()
    visited.add(initial_state)

    while stack:
        current_state, path, depth = stack.pop()

        if current_state == GOAL_STATE:
            return path

        if depth >= 50:  
            continue

        blank_index = get_blank_index(current_state)

        for move in reversed(get_neighbors(blank_index)):  
            new_state = swap_positions(current_state, blank_index, move)

            if new_state not in visited:
                visited.add(new_state)
                stack.append((new_state, path + [new_state], depth + 1))

    return None

#Thuật toán A*
def a_star_solve(initial_state):
    queue = [(manhattan_distance(initial_state), 0, initial_state, [])]  # (f, g, state, path)
    visited = set()
    visited.add(initial_state)

    while queue:
        _, g, current_state, path = heapq.heappop(queue)

        if current_state == GOAL_STATE:
            return path

        blank_index = get_blank_index(current_state)

        for move in get_neighbors(blank_index):
            new_state = swap_positions(current_state, blank_index, move)
            if new_state not in visited:
                visited.add(new_state)
                new_g = g + 1
                new_f = new_g + manhattan_distance(new_state)
                heapq.heappush(queue, (new_f, new_g, new_state, path + [new_state]))

    return None

#Thuật toán IDA*
def ida_star_solve(initial_state):
    def search(path, g, threshold):
        current_state = path[-1]
        f = g + manhattan_distance(current_state)

        if f > threshold:
            return f 

        if current_state == GOAL_STATE:
            return path

        min_threshold = float('inf')

        blank_index = get_blank_index(current_state)
        for move in get_neighbors(blank_index):
            new_state = swap_positions(current_state, blank_index, move)

            if new_state not in path:
                result = search(path + [new_state], g + 1, threshold)
                if isinstance(result, list):
                    return result  
                min_threshold = min(min_threshold, result)

        return min_threshold

    threshold = manhattan_distance(initial_state)
    path = [initial_state]

    while True:
        result = search(path, 0, threshold)
        if isinstance(result, list):
            return result  
        if result == float('inf'):
            return None  
        threshold = result  # Cập nhật giới hạn mới

# Thuật toán Simple Hill Climbing
def simple_hill_climbing_solve(initial_state):
    current_state = initial_state
    path = [current_state]
    
    while True:
        blank_index = get_blank_index(current_state)
        neighbors = [swap_positions(current_state, blank_index, move) for move in get_neighbors(blank_index)]
        
        # Tìm trạng thái có Manhattan distance nhỏ nhất
        best_state = min(neighbors, key=manhattan_distance, default=None)
        
        if best_state and manhattan_distance(best_state) < manhattan_distance(current_state):
            current_state = best_state
            path.append(current_state)
        else:
            break 

    return path if current_state == GOAL_STATE else None

def steepest_ascent_hill_climbing_solve(initial_state):
    current_state = initial_state
    path = [current_state]

    while True:
        blank_index = get_blank_index(current_state)
        neighbors = [swap_positions(current_state, blank_index, move) for move in get_neighbors(blank_index)]

        # Tìm trạng thái tốt nhất trong tất cả các trạng thái lân cận
        best_state = min(neighbors, key=manhattan_distance, default=None)

        if best_state and manhattan_distance(best_state) < manhattan_distance(current_state):
            current_state = best_state
            path.append(current_state)
        else:
            break

    return path if current_state == GOAL_STATE else None

import random

def stochastic_hill_climbing_solve(initial_state):
    current_state = initial_state
    path = [current_state]

    while True:
        blank_index = get_blank_index(current_state)
        neighbors = [swap_positions(current_state, blank_index, move) for move in get_neighbors(blank_index)]
        
        # Lọc ra các trạng thái tốt hơn hiện tại
        better_neighbors = [state for state in neighbors if manhattan_distance(state) < manhattan_distance(current_state)]

        if better_neighbors:
            current_state = random.choice(better_neighbors)  # Chọn ngẫu nhiên 1 trạng thái tốt hơn
            path.append(current_state)
        else:
            break 
    return path if current_state == GOAL_STATE else None

#Thuật toán Beam
def beam_search_solve(initial_state, beam_width=2):
    from heapq import heappush, heappop

    frontier = [(manhattan_distance(initial_state), [initial_state])]

    while frontier:
        new_frontier = []

        for _, path in frontier:
            current_state = path[-1]
            if current_state == GOAL_STATE:
                return path[1:]

            blank_index = get_blank_index(current_state)
            for move in get_neighbors(blank_index):
                new_state = swap_positions(current_state, blank_index, move)
                if new_state not in path:
                    new_path = path + [new_state]
                    heappush(new_frontier, (manhattan_distance(new_state), new_path))

        # Chỉ giữ lại beam_width phần tử tốt nhất
        frontier = sorted(new_frontier, key=lambda x: x[0])[:beam_width]

    return None

#Thuật toán Simulated Annealing
def simulated_annealing_solve(initial_state):
    import math
    import random

    current_state = initial_state
    path = [current_state]
    temperature = 100.0
    cooling_rate = 0.99

    while temperature > 0.1:
        if current_state == GOAL_STATE:
            return path[1:]

        blank_index = get_blank_index(current_state)
        neighbors = [swap_positions(current_state, blank_index, move) for move in get_neighbors(blank_index)]
        next_state = random.choice(neighbors)

        delta_e = manhattan_distance(current_state) - manhattan_distance(next_state)

        if delta_e > 0 or random.random() < math.exp(delta_e / temperature):
            current_state = next_state
            path.append(current_state)

        temperature *= cooling_rate

    return path if current_state == GOAL_STATE else None

#Thuật toán Genetic 

def is_solvable(state):
    state_list = [int(x) for x in state if x != ""]
    inversions = 0
    for i in range(len(state_list)):
        for j in range(i + 1, len(state_list)):
            if state_list[i] > state_list[j]:
                inversions += 1
    return inversions % 2 == 0

def genetic_algorithm_solve(initial_state, population_size=50, generations=1000):
    import random

    def fitness(state):
        return -manhattan_distance(state)

    def is_valid_state(state):
        return (
            isinstance(state, tuple)
            and len(state) == 9
            and sorted(state) == ["", "1", "2", "3", "4", "5", "6", "7", "8"]
        )

    def mutate(state):
        if not is_valid_state(state):
            return state
        blank_index = get_blank_index(state)
        neighbors = get_neighbors(blank_index)
        new_state = list(state)
        move = random.choice(neighbors)
        new_state[blank_index], new_state[move] = new_state[move], new_state[blank_index]
        return tuple(new_state)

    def crossover(parent1, parent2):
        child = list(parent1)
        start, end = sorted(random.sample(range(9), 2))
        child[start:end] = parent2[start:end]
        remaining = [x for x in parent2 if x not in child[start:end]]
        j = 0
        for i in range(9):
            if i < start or i >= end:
                child[i] = remaining[j]
                j += 1
        child = tuple(child)
        if is_solvable(child):
            return child
        return parent1

    # Khởi tạo quần thể
    population = [initial_state]
    while len(population) < population_size:
        state = initial_state
        for _ in range(10):
            blank = get_blank_index(state)
            state = swap_positions(state, blank, random.choice(get_neighbors(blank)))
        if is_solvable(state) and state not in population:
            population.append(state)

    best_state = initial_state
    best_path = [best_state]
    for _ in range(generations):
        population.sort(key=fitness, reverse=True)
        if population[0] == GOAL_STATE:
            return best_path + [GOAL_STATE]
        if fitness(population[0]) > fitness(best_state):
            best_state = population[0]
            best_path.append(best_state)

        next_generation = population[:10]  # Giữ 20% tốt nhất
        while len(next_generation) < population_size:
            p1, p2 = random.sample(population[:20], 2)
            child = crossover(p1, p2)
            if random.random() < 0.1:  # Xác suất đột biến 0.1
                child = mutate(child)
            if is_solvable(child):
                next_generation.append(child)
        population = next_generation

    return None

def and_or_search_solve(initial_state, max_depth=50):
    stack = [(initial_state, [initial_state], 0)]
    visited = set()

    while stack:
        current_state, path, depth = stack.pop()

        if current_state == GOAL_STATE:
            return path

        if depth >= max_depth:
            continue

        visited.add(current_state)
        blank_index = get_blank_index(current_state)

        for move in get_neighbors(blank_index):
            new_state = swap_positions(current_state, blank_index, move)
            if new_state not in visited:
                stack.append((new_state, path + [new_state], depth + 1))

    return []


def belief_based_search_solve(initial_state):
    queue = [(0, initial_state, [])]
    visited = set([initial_state])

    while queue:
        _, current_state, path = heapq.heappop(queue)
        if current_state == GOAL_STATE:
            return path
        blank_index = get_blank_index(current_state)
        for move in get_neighbors(blank_index):
            new_state = swap_positions(current_state, blank_index, move)
            if new_state not in visited:
                visited.add(new_state)
                belief_score = sum(1 for i in range(9) if new_state[i] == GOAL_STATE[i])
                priority = -belief_score  # Ưu tiên nhiều vị trí đúng hơn
                heapq.heappush(queue, (priority, new_state, path + [new_state]))
    return None

def generate_all_states():
    tiles = ["1", "2", "3", "4", "5", "6", "7", "8", ""]
    return list(itertools.permutations(tiles))


# Hàm xác định các hành động hợp lệ từ trạng thái hiện tại
def get_possible_actions(state):
    """Trả về danh sách các chỉ số ô có thể di chuyển vào vị trí ô trống."""
    blank_index = state.index("") 

    possible_moves = []
    
    # Kiểm tra các ô xung quanh ô trống (trái, phải, lên, xuống)
    if blank_index % 3 != 0:  # Có ô bên trái
        possible_moves.append(blank_index - 1)
    if blank_index % 3 != 2:  # Có ô bên phải
        possible_moves.append(blank_index + 1)
    if blank_index // 3 != 0:  # Có ô bên trên
        possible_moves.append(blank_index - 3)
    if blank_index // 3 != 2:  # Có ô bên dưới
        possible_moves.append(blank_index + 3)
    
    return possible_moves

def move_state(state, move):
    blank_index = state.index("") 
    return swap_positions(state, blank_index, move)


def partial_observable_search(start_state, goal_state):
    from collections import deque

    def observe(state):
        # Quan sát: chỉ thấy các ô xung quanh gạch trắng
        zero_index = state.index("")
        row, col = divmod(zero_index, 3)
        visible = set()
        visible.add(zero_index)
        if row > 0: visible.add(zero_index - 3)
        if row < 2: visible.add(zero_index + 3)
        if col > 0: visible.add(zero_index - 1)
        if col < 2: visible.add(zero_index + 1)
        return tuple(state[i] for i in visible)

    def is_consistent(state, observation):
        return observe(state) == observation

    initial_obs = observe(start_state)
    belief_states = [s for s in generate_all_states() if is_consistent(s, initial_obs)]

    visited = set()
    queue = deque([(belief_states[0], [belief_states[0]])])

    while queue:    
        current_state, path = queue.popleft()
        visited.add(current_state)

        if current_state == goal_state:
            return path

        for move in get_possible_actions(current_state):
            next_state = move_state(current_state, move)
            if next_state not in visited:
                next_obs = observe(next_state)
                # Lọc lại belief states
                belief_states = [s for s in generate_all_states() if is_consistent(s, next_obs)]
                queue.append((next_state, path + [next_state]))
                break  # chỉ đi 1 bước vì chỉ quan sát được ít
    return None

from collections import deque

def csp_solve(start_state):
    visited = set()
    path = []
    max_depth = 50  # Giới hạn chiều sâu

    def is_consistent(state):
        # Không cần kiểm tra quá phức tạp, chỉ kiểm tra đã visited chưa
        return state not in visited

    def backtrack(state, depth):
        if depth > max_depth:
            return False
        if state == GOAL_STATE:
            path.append(state)
            return True

        visited.add(state)
        blank_index = get_blank_index(state)

        for move in get_neighbors(blank_index):
            new_state = swap_positions(state, blank_index, move)
            if is_consistent(new_state):
                if backtrack(new_state, depth + 1):
                    path.append(state)
                    return True

        visited.remove(state)  # Cho phép backtrack thử lại sau nếu cần
        return False

    found = backtrack(start_state, 0)
    return path[::-1] if found else None


def search_with_no_observation(initial_state):
    from collections import deque

    belief_states = set([initial_state])  # Tập hợp trạng thái có thể xảy ra
    path = []  # Chứa các tập trạng thái theo từng bước

    while True:
        path.append(belief_states.copy())

        # Kiểm tra nếu tất cả đều là trạng thái đích
        if all(state == GOAL_STATE for state in belief_states):
            return path  # Trả về các bước belief states

        new_belief_states = set()

        for state in belief_states:
            blank_index = get_blank_index(state)
            for move in get_neighbors(blank_index):
                new_state = swap_positions(state, blank_index, move)
                new_belief_states.add(new_state)

        if new_belief_states == belief_states:
            break  # Không thể thu hẹp nữa → thất bại

        belief_states = new_belief_states

    return None


# Cài đặt Q-learning
import pickle
import os
def q_learning(
    episodes=200000,
    alpha=0.1,         # learning rate
    gamma=0.9,         # discount factor
    epsilon=1.0,        # exploration rate
    epsilon_min=0.05,
    epsilon_decay=0.9995
):
    goal_state = ("1", "2", "3", "4", "5", "6", "7", "8", "")
    all_states = generate_all_states()
    Q = {}  # Q-table: {(state, action): value}

    for ep in range(episodes):
        state = random.choice(all_states)
        steps = 0
        max_steps = 1000
        
        while state != goal_state and steps < max_steps:
            blank_index = get_blank_index(state)
            actions = get_neighbors(blank_index)

            # Epsilon-greedy policy
            if random.random() < epsilon:
                action = random.choice(actions)
            else:
                q_values = [Q.get((state, a), 0) for a in actions]
                max_q = max(q_values)
                best_actions = [a for a, q in zip(actions, q_values) if q == max_q]
                action = random.choice(best_actions)

            next_state = swap_positions(state, blank_index, action)
            reward = 100 if next_state == goal_state else -1

            old_q = Q.get((state, action), 0)
            next_qs = [Q.get((next_state, a), 0) for a in get_neighbors(get_blank_index(next_state))]
            max_next_q = max(next_qs) if next_qs else 0

            # Q-learning update rule
            Q[(state, action)] = old_q + alpha * (reward + gamma * max_next_q - old_q)

            state = next_state
            steps += 1
            
         # Giảm epsilon dần (chuyển từ khám phá -> khai thác)
        if epsilon > epsilon_min:
            epsilon *= epsilon_decay

        if ep % 5000 == 0:
            print(f"Tập {ep} hoàn thành")

    print("✅ Q-learning hoàn tất!")
    return Q

if not os.path.exists("q_table.pkl"):
    print("🔄 Chưa có Q-table, đang huấn luyện...")
    Q_table = q_learning()
    with open("q_table.pkl", "wb") as f:
        pickle.dump(Q_table, f)
    print("✅ Đã lưu Q-table vào q_table.pkl")
else:
    print("✅ Đã có Q-table sẵn, không cần huấn luyện lại.")

def get_best_path(Q, initial_state, goal_state, max_steps=1000):
    path = [initial_state]
    current_state = initial_state

    for _ in range(max_steps):
        if current_state == goal_state:
            break

        blank_index = get_blank_index(current_state)
        actions = get_neighbors(blank_index)

        # Lấy action có Q-value cao nhất
        q_values = [Q.get((current_state, a), -float("inf")) for a in actions]
        max_q = max(q_values)

        if max_q == -float("inf"):
            # Không có hành động nào được biết trong Q-table
            break

        # Chọn action tốt nhất (có Q-value cao nhất)
        best_actions = [a for a, q in zip(actions, q_values) if q == max_q]
        action = random.choice(best_actions)

        next_state = swap_positions(current_state, blank_index, action)

        if next_state in path:
            # Phát hiện lặp vô hạn
            break

        path.append(next_state)
        current_state = next_state

    if current_state == goal_state:
        return path
    else:
        return None  # Không tìm được đường đi đến đích


def main():
    selected_algorithm = None
    while True:
        draw_board(INITIAL_STATE, "")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if 20 <= x <= 105 and HEIGHT - 90 <= y <= HEIGHT - 55:
                    selected_algorithm = "bfs"
                elif 120 <= x <= 205 and HEIGHT - 90 <= y <= HEIGHT - 55:
                    selected_algorithm = "dfs"
                elif 220 <= x <= 305 and HEIGHT - 90 <= y <= HEIGHT - 55:
                    selected_algorithm = "ids"
                elif 20 <= x <= 105 and HEIGHT - 45 <= y <= HEIGHT - 10:
                    selected_algorithm = "ucs"
                elif 120 <= x <= 205 and HEIGHT - 45 <= y <= HEIGHT - 10:
                    selected_algorithm = "greedy"
                elif 220 <= x <= 305 and HEIGHT - 45 <= y <= HEIGHT - 10:
                    pygame.quit()
                    return
                elif 20 <= x <= 105 and HEIGHT - 135 <= y <= HEIGHT - 100:
                    selected_algorithm = "a*"
                elif 120 <= x <= 205 and HEIGHT - 135 <= y <= HEIGHT - 100:
                    selected_algorithm = "ida*"
                elif 220 <= x <= 305 and HEIGHT - 135 <= y <= HEIGHT - 100:
                    selected_algorithm = "simple"
                elif 20 <= x <= 105 and HEIGHT - 180 <= y <= HEIGHT - 145:
                    selected_algorithm = "steepest"
                elif 120 <= x <= 205 and HEIGHT - 180 <= y <= HEIGHT - 145:
                    selected_algorithm = "stochastic"
                elif 220 <= x <= 305 and HEIGHT - 180 <= y <= HEIGHT - 145:
                    selected_algorithm = "beam"
                elif 20 <= x <= 105 and HEIGHT - 225 <= y <= HEIGHT - 190:
                    selected_algorithm = "simulated"
                elif 120 <= x <= 205 and HEIGHT - 225 <= y <= HEIGHT - 190:
                    selected_algorithm = "genetic"
                elif 220 <= x <= 305 and HEIGHT - 225 <= y <= HEIGHT - 190:
                    selected_algorithm = "and-or"
                elif 20 <= x <= 105 and HEIGHT - 270 <= y <= HEIGHT - 235:
                    selected_algorithm = "bbss"
                elif 120 <= x <= 205 and HEIGHT - 270 <= y <= HEIGHT - 235:
                    selected_algorithm = "pos"
                elif 220 <= x <= 305 and HEIGHT - 270 <= y <= HEIGHT - 235:
                    selected_algorithm = "csp"
                elif 20 <= x <= 105 and HEIGHT - 315 <= y <= HEIGHT - 280:
                    selected_algorithm = "0 ob"
                elif 120 <= x <= 205 and HEIGHT - 315 <= y <= HEIGHT - 280:
                    selected_algorithm = "q-learning"
                elif 220 <= x <= 305 and HEIGHT - 315 <= y <= HEIGHT - 280:
                    draw_board(INITIAL_STATE, "")

        if selected_algorithm:
            break

        clock.tick(30)
    start_time = time.perf_counter()
    if selected_algorithm == "bfs":
        solution_path = bfs_solve(INITIAL_STATE)

    elif selected_algorithm == "dfs":
        solution_path = dfs_solve(INITIAL_STATE)
    elif selected_algorithm == "a*":
        solution_path = a_star_solve(INITIAL_STATE)
    elif selected_algorithm == "ids":
        solution_path = ids_solve(INITIAL_STATE)
    elif selected_algorithm == "ucs":
        solution_path = ucs_solve(INITIAL_STATE)
    elif selected_algorithm == "greedy":
        solution_path = greedy_search_solve(INITIAL_STATE)
    elif selected_algorithm == "ida*":
        solution_path = ida_star_solve(INITIAL_STATE)
    elif selected_algorithm == "simple":
        solution_path = simple_hill_climbing_solve(INITIAL_STATE)
    elif selected_algorithm == "steepest":
        solution_path = steepest_ascent_hill_climbing_solve(INITIAL_STATE)
    elif selected_algorithm == "stochastic":
        solution_path = stochastic_hill_climbing_solve(INITIAL_STATE)
    elif selected_algorithm == "beam":
        solution_path = beam_search_solve(INITIAL_STATE)
    elif selected_algorithm == "simulated":
        solution_path = simulated_annealing_solve(INITIAL_STATE)
    elif selected_algorithm == "genetic":
        solution_path = genetic_algorithm_solve(INITIAL_STATE)
    elif selected_algorithm == "and-or":
        solution_path = and_or_search_solve(INITIAL_STATE)
    elif selected_algorithm == "bbss":
        solution_path = belief_based_search_solve(INITIAL_STATE)
    elif selected_algorithm == "pos":
        solution_path = partial_observable_search(INITIAL_STATE, GOAL_STATE)
    elif selected_algorithm == "csp":
        solution_path = csp_solve(INITIAL_STATE)
    elif selected_algorithm == "0 ob":
        solution_path = search_with_no_observation(INITIAL_STATE)
    elif selected_algorithm == "q-learning":
        try:
            # Tải Q-table đã huấn luyện từ file
            with open("q_table.pkl", "rb") as f:
                Q = pickle.load(f)
            
            # Tìm đường đi tốt nhất từ Q-table
            solution_path = get_best_path(Q, INITIAL_STATE, GOAL_STATE)

        except FileNotFoundError:
            draw_board(INITIAL_STATE, "⚠️ Không tìm thấy q_table.pkl", 0)
            solution_path = None
    else:
        return
    
    end_time = time.perf_counter()  # Kết thúc đo thời gian
    runtime = end_time - start_time  # Tính thời gian chạy (giây)
    if solution_path:
        for state in solution_path:
            
            draw_board(state, f"Dang giai bang {selected_algorithm.upper()}...", runtime)
            pygame.time.delay(250)
        draw_board(GOAL_STATE, "Done.....", runtime)
        print(solution_path)
        print("So Buoc:", len(solution_path))
    else:
        draw_board(INITIAL_STATE, "Khong tim duoc duong di!", runtime)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  
                if 220 <= x <= 305 and HEIGHT - 45 <= y <= HEIGHT - 10:
                    pygame.quit()
                    return
                elif 220 <= x <= 305 and HEIGHT - 315 <= y <= HEIGHT - 280:
                    main()

        clock.tick(30)
    

if __name__ == "__main__":
    main()
