# 🧩 8-Puzzle Solver
### 📝 Họ và Tên: Trương Thanh Thành | MSSV: 23133069  

## 📌 Mục lục
- Giới thiệu  
- Tính năng  
- Thuật toán hỗ trợ  
- Cài đặt  
- Hình ảnh minh họa  
- Tài liệu tham khảo

## 📖 Giới thiệu
Trò chơi 8-Puzzle sử dụng một bảng 3×3 bao gồm 8 ô được đánh số từ 1 đến 8 và một ô trống.
Mục tiêu của trò chơi là sắp xếp lại các ô sao cho khớp với cấu hình đích (thường là các số theo thứ tự từ 1 đến 8, với ô trống nằm ở cuối).
Người chơi có thể trượt một trong bốn ô liền kề (trái, phải, trên, dưới) vào vị trí ô trống để thay đổi trạng thái của bảng.

## ✨ Tính năng
- Giao diện trực quan được xây dựng bằng Pygame, dễ sử dụng và thân thiện với người dùng
- Hỗ trợ đa dạng thuật toán tìm kiếm:
  + Tìm kiếm không thông tin (Uninformed Search): Breadth-First Search (BFS), Depth-First Search (DFS), Iterative Deepening Search (IDS), Uniform Cost Search (UCS)
  + Tìm kiếm có thông tin (Informed Search): Greedy Search, A*, Iterative Deepening A* (IDA)
  + Tìm kiếm cục bộ (Local Search): Simple Hill Climbing, Steepest-Ascent Hill Climbing, Stochastic Hill Climbing, Beam Search, Genetic Algorithm
  + Bài toán ràng buộc: Constraint Satisfaction Problems (CSPs)
  + Môi trường phức tạp (Complex Environments): Search with nondeterministic actions (cây AND-OR), Search with no observation, Belief state search, Searching with partially observation
  + Học tăng cường (Reinforcement Learning): Q-Learning
- Hiển thị trực tiếp quá trình giải.
- Tính thời gian chạy thuật toán.
- Thống kê kết quả.
- Chức năng reset giúp quay lại trạng thái ban đầu để chọn lại thuật toán, để có thể dễ dàng thấy quá trình chạy các thuật toán mà so sánh.

## ⚙️ Cài đặt
Chạy trong môi trường Python với các thư viện:
- pygame – để xây dựng giao diện đồ họa
- heapq, collections, itertools, time – hỗ trợ thuật toán tìm kiếm
Cài đặt thư viện (nếu chưa có):
<pre><code>pip install pygame </code></pre>

### 1. Cấu hình và khởi tạo  
![image](https://github.com/user-attachments/assets/f6d7f73b-b1a9-476e-93e9-7a2fbaed8b4d)
### 2. Vẽ bảng trò chơi và nút lựa chọn
Thiết kế bảng trò chơi bằng hàm draw_board(state, message="", runtime=None)
- Hiển thị bảng 3x3 cho trạng thái hiện tại.
- Các ô được tô màu và có số tương ứng.
- Hiển thị thời gian chạy thuật toán.
- Vẽ các nút tương tác với thuật toán như: A*, BFS, DFS, Genetic, QLearning, Thoát, Reset,...
Tạo các nút lựa chọn thông qua hàm draw_button(x, y, width, height, text, color)
### 3. Các hàm hỗ trợ xử lý logic
- get_blank_index(state): tìm vị trí ô trống ("")
- get_neighbors(index): trả về các vị trí có thể hoán đổi với ô trống
- swap_positions(state, blank_index, move): hoán đổi hai ô
- manhattan_distance(state): tính khoảng cách Manhattan (heuristic)
### 4. Xử lý chọn thuật toán
- Các sự kiện chuột được xử lý để xác định người dùng chọn thuật toán nào thông qua nút bấm. Ví dụ:
  <pre><code>if 20 <= x <= 105 and HEIGHT - 90 <= y <= HEIGHT - 55:
    selected_algorithm = "bfs" </code></pre>
- Thực thi thuật toán. Ví dụ:
  <pre><code>if selected_algorithm == "bfs":
    solution_path = bfs_solve(INITIAL_STATE) </code></pre>
    
## 🖼️ Hình ảnh minh họa 

![8-puzzle-test](https://github.com/user-attachments/assets/cb0ad6b2-0e04-48b6-9e82-ab4c6f310b16)

## 📚 Tài liệu tham khảo
1. Artificial Intelligence: A Modern Approach – Stuart Russell & Peter Norvig
2. https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/  
3. https://github.com/rmssoares/8Puzzle-StateSpaceSearches
