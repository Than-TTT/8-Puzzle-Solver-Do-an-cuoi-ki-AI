# 🧩 8-Puzzle Solver
### 📝 Họ và Tên: Trương Thanh Thành | MSSV: 23133069  

## 📌 Mục lục
- Giới thiệu  
- Tính năng  
- Thuật toán hỗ trợ  
- Cài đặt  
- Hình ảnh minh họa
- Các nhóm thuật toán giải game  
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

## 🪄 Các nhóm thuật toán giải game
### 1. Nhóm thuật toán Uninformed Search (Tìm kiếm không thông tin)
#### Breadth-First Search (BFS)
![BFS](https://github.com/user-attachments/assets/a7854346-2311-47ff-b17b-ea9d19ac02df)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Mở rộng các nút theo từng mức độ (độ sâu) từ trạng thái ban đầu. Tất cả trạng thái ở mức độ hiện tại được khám phá trước khi chuyển sang mức độ sâu hơn. Sử dụng hàng đợi FIFO để lưu các trạng thái chờ khám phá.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo tìm lời giải ngắn nhất (số bước di chuyển ít nhất).  
&nbsp;&nbsp;&nbsp;&nbsp;- Thuật toán đơn giản, dễ triển khai.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ lớn vì phải lưu toàn bộ các trạng thái ở mức độ hiện tại.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể rất chậm với không gian trạng thái lớn.  

#### Depth-First Search (DFS) 
![DFS](https://github.com/user-attachments/assets/72c15527-84a0-4973-9f15-fbc4bb20dbcd)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Khám phá trạng thái bằng cách đi sâu nhất có thể theo một nhánh trước khi quay lại (backtrack) để thử nhánh khác. Sử dụng ngăn xếp LIFO hoặc đệ quy để lưu các trạng thái chờ khám phá. Trong 8-puzzle, DFS di chuyển ô trống theo một hướng cho đến khi gặp ngõ cụt hoặc đạt trạng thái mục tiêu.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm bộ nhớ vì chỉ lưu các trạng thái trên đường đi hiện tại.  
&nbsp;&nbsp;&nbsp;&nbsp;- Nhanh chóng nếu lời giải nằm ở độ sâu nông.  
&nbsp;&nbsp;&nbsp;&nbsp;- Dễ triển khai, đặc biệt với đệ quy.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo tìm lời giải ngắn nhất (có thể đi vào nhánh dài).  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể bị kẹt trong không gian trạng thái lớn hoặc vòng lặp nếu không giới hạn độ sâu.  
&nbsp;&nbsp;&nbsp;&nbsp;- Hiệu suất kém nếu trạng thái mục tiêu ở xa trạng thái ban đầu.  

#### Iterative Deepening Search (IDS)
![IDS](https://github.com/user-attachments/assets/36f64f19-57ba-4ed3-aeb7-2fa195ffe210)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Kết hợp BFS và DFS bằng cách chạy DFS nhiều lần với độ sâu giới hạn tăng dần (1, 2, 3, ...). Mỗi lần chạy DFS chỉ khám phá đến độ sâu cho phép, sau đó tăng độ sâu và lặp lại. Trong 8-puzzle, IDS thử tất cả các bước di chuyển ô trống trong giới hạn độ sâu.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo tìm lời giải ngắn nhất (như BFS).  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm bộ nhớ hơn BFS vì chỉ lưu các trạng thái trên đường đi hiện tại.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phù hợp khi cần lời giải tối ưu trong không gian trạng thái lớn.    
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn thời gian hơn BFS do lặp lại các trạng thái ở các độ sâu thấp hơn.  
&nbsp;&nbsp;&nbsp;&nbsp;- Vẫn chậm với không gian trạng thái rất lớn.  
&nbsp;&nbsp;&nbsp;&nbsp;- Cần quản lý độ sâu để tránh lặp vô hạn.  

#### Uniform Cost Search (UCS)
![UCS](https://github.com/user-attachments/assets/fc1711ec-e70a-4f5e-9971-1f47852567d4)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Mở rộng trạng thái có chi phí đường đi thấp nhất từ trạng thái ban đầu, sử dụng hàng đợi ưu tiên (priority queue). Trong 8-puzzle, mỗi bước di chuyển ô trống có chi phí bằng 1, nên UCS mở rộng trạng thái theo thứ tự chi phí tăng dần, tương tự BFS.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo tìm lời giải ngắn nhất (tối ưu về chi phí).  
&nbsp;&nbsp;&nbsp;&nbsp;- Linh hoạt khi các hành động có chi phí khác nhau.  
&nbsp;&nbsp;&nbsp;&nbsp;- Hiệu quả trong không gian trạng thái có chi phí đồng nhất.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ lớn (tương tự BFS) vì lưu tất cả trạng thái chưa khám phá.  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm hơn BFS trong trường hợp chi phí đồng nhất do quản lý hàng đợi ưu tiên.  
&nbsp;&nbsp;&nbsp;&nbsp;- Không tận dụng heuristic, dẫn đến khám phá nhiều trạng thái không cần thiết.  

### 2. Nhóm thuật toán Informed Search (Tìm kiếm có thông tin)
#### Greedy Best-First Search
![Greedy](https://github.com/user-attachments/assets/423af204-8307-4316-89e8-6dfd0a69e818)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Mở rộng trạng thái có giá trị heuristic thấp nhất (ước lượng khoảng cách đến GOAL_STATE) bằng hàng đợi ưu tiên. Trong 8-puzzle, sử dụng heuristic như số ô sai vị trí (heuristic) hoặc khoảng cách Manhattan (manhattan_distance) để chọn trạng thái gần GOAL_STATE nhất.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Nhanh hơn Uninformed Search nhờ heuristic định hướng tìm kiếm.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm thời gian trong không gian trạng thái lớn.  
&nbsp;&nbsp;&nbsp;&nbsp;- Dễ triển khai với hàng đợi ưu tiên.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo tìm lời giải ngắn nhất (không tối ưu).  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể bị kẹt trong cực trị cục bộ nếu heuristic không tốt.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ để lưu các trạng thái chưa khám phá.  

#### A* Search
![As](https://github.com/user-attachments/assets/347179cf-5614-46d6-980a-c13ce587d814)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Mở rộng trạng thái có tổng chi phí thấp nhất (f(n) = g(n) + h(n)), trong đó g(n) là chi phí từ trạng thái ban đầu và h(n) là giá trị heuristic (như manhattan_distance). Sử dụng hàng đợi ưu tiên để ưu tiên trạng thái có f(n) thấp nhất. Trong 8-puzzle, đảm bảo tìm đường đi ngắn nhất nếu heuristic khả chấp (h(n) ≤ chi phí thực).  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo tìm lời giải ngắn nhất nếu heuristic khả chấp.  
&nbsp;&nbsp;&nbsp;&nbsp;- Hiệu quả hơn BFS nhờ heuristic giảm số trạng thái khám phá.  
&nbsp;&nbsp;&nbsp;&nbsp;- Linh hoạt với các heuristic khác nhau (số ô sai vị trí, Manhattan).    
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ để lưu các trạng thái trong hàng đợi ưu tiên.  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm hơn Greedy nếu không gian trạng thái rất lớn.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào chất lượng heuristic.  

#### Iterative Deepening A* (IDA*)
![IDAs](https://github.com/user-attachments/assets/6a6a37cf-8c98-419e-a3a9-3bc25a8b17bc)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Kết hợp A* với tìm kiếm theo độ sâu, sử dụng ngưỡng f(n) = g(n) + h(n) tăng dần. Chỉ khám phá các trạng thái có f(n) nhỏ hơn ngưỡng, tăng ngưỡng khi không tìm thấy lời giải. Trong 8-puzzle, IDA* tiết kiệm bộ nhớ bằng cách chỉ lưu đường đi hiện tại, sử dụng manhattan_distance làm heuristic.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo tìm lời giải ngắn nhất như A* nếu heuristic khả chấp.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm bộ nhớ hơn A* vì không lưu toàn bộ hàng đợi ưu tiên.  
&nbsp;&nbsp;&nbsp;&nbsp;- Hiệu quả cho không gian trạng thái lớn như 8-puzzle.   
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn thời gian hơn A* do lặp lại các trạng thái ở ngưỡng thấp hơn.  
&nbsp;&nbsp;&nbsp;&nbsp;- Hiệu suất phụ thuộc vào heuristic và bước tăng ngưỡng.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể chậm nếu ngưỡng tăng chậm.  

### 3. Nhóm thuật toán Local Search (Tìm kiếm cục bộ)
#### Simple Hill Climbing

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Bắt đầu từ trạng thái ban đầu, chọn trạng thái láng giềng có heuristic thấp nhất (như heuristic) và tiếp tục cho đến khi không còn láng giềng nào tốt hơn. Trong 8-puzzle, di chuyển ô trống đến vị trí cải thiện trạng thái nhất.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Đơn giản, dễ triển khai.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm bộ nhớ vì chỉ lưu trạng thái hiện tại và láng giềng.  
&nbsp;&nbsp;&nbsp;&nbsp;- Nhanh trong không gian trạng thái nhỏ.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Dễ bị kẹt ở cực trị cục bộ (không đạt GOAL_STATE).  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo tìm lời giải tối ưu hoặc bất kỳ lời giải nào.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào trạng thái ban đầu.  

#### Steepest-Ascent Hill Climbing

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tương tự Simple Hill Climbing, nhưng luôn chọn láng giềng tốt nhất (heuristic thấp nhất) trong tất cả láng giềng có thể. Trong 8-puzzle, kiểm tra tất cả di chuyển của ô trống và chọn di chuyển giảm heuristic nhiều nhất.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Hiệu quả hơn Simple Hill Climbing nhờ xem xét tất cả láng giềng.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm bộ nhớ, chỉ lưu trạng thái hiện tại và láng giềng.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể tìm lời giải nhanh nếu trạng thái ban đầu gần GOAL_STATE.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Dễ bị kẹt ở cực trị cục bộ (không đạt GOAL_STATE).  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo lời giải tối ưu.  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm hơn nếu có nhiều láng giềng cần đánh giá.  

#### Stochastic Hill Climbing

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Chọn ngẫu nhiên một láng giềng tốt hơn trạng thái hiện tại (heuristic thấp hơn) thay vì luôn chọn tốt nhất. Trong 8-puzzle, chọn ngẫu nhiên một di chuyển ô trống cải thiện trạng thái, tiếp tục cho đến khi đạt GOAL_STATE hoặc giới hạn bước.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Thoát khỏi cực trị cục bộ tốt hơn Simple/Steepest nhờ ngẫu nhiên.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm bộ nhớ, chỉ lưu trạng thái hiện tại và láng giềng.  
&nbsp;&nbsp;&nbsp;&nbsp;- Dễ triển khai, phù hợp khi cần lời giải nhanh.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo tìm lời giải tối ưu hoặc bất kỳ lời giải nào.  
&nbsp;&nbsp;&nbsp;&nbsp;- Kết quả phụ thuộc vào yếu tố ngẫu nhiên.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể chậm nếu chọn láng giềng không hiệu quả.  

#### Simulated Annealing

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Bắt đầu từ trạng thái ban đầu, chọn ngẫu nhiên láng giềng và chấp nhận nếu tốt hơn; nếu tệ hơn, chấp nhận với xác suất dựa trên "nhiệt độ" giảm dần (exp(-Δh/T)). Trong 8-puzzle, di chuyển ô trống ngẫu nhiên, giảm nhiệt độ để hội tụ về trạng thái tốt.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Thoát khỏi cực trị cục bộ nhờ chấp nhận trạng thái tệ hơn ở giai đoạn đầu.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể tìm lời giải gần tối ưu với tham số phù hợp.  
&nbsp;&nbsp;&nbsp;&nbsp;- Linh hoạt, điều chỉnh được qua nhiệt độ và tốc độ giảm.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào tham số (nhiệt độ ban đầu, tốc độ giảm).  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo lời giải tối ưu.  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm hơn nếu cần nhiều bước để hội tụ.  

#### Genetic Algorithm

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Duy trì quần thể trạng thái, tiến hóa qua các thế hệ bằng lai ghép (crossover), đột biến (mutation), và chọn lọc dựa trên hàm fitness (như -manhattan_distance). Trong 8-puzzle, trạng thái là các hoán vị, lai ghép tạo trạng thái con, đột biến di chuyển ô trống ngẫu nhiên.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Linh hoạt, có thể xử lý không gian trạng thái phức tạp.  
&nbsp;&nbsp;&nbsp;&nbsp;- Thoát khỏi cực trị cục bộ nhờ đột biến và lai ghép.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể song song hóa để tăng tốc.    
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo lời giải tối ưu hoặc bất kỳ lời giải nào.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào tham số (kích thước quần thể, số thế hệ, tỷ lệ đột biến).  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm hơn (~0.1-0.5 giây) do tính toán trên quần thể lớn.   

#### Beam Search
![BEAM](https://github.com/user-attachments/assets/0d06bbf8-4b67-4176-b5b0-69447565ad27)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Giữ một tập cố định (beam width) các trạng thái tốt nhất theo heuristic, mở rộng chỉ các trạng thái này ở mỗi bước. Trong 8-puzzle, chọn top trạng thái (ví dụ: 3 trạng thái) có heuristic thấp nhất, tiếp tục cho đến khi đạt GOAL_STATE.   
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm bộ nhớ hơn BFS/A* nhờ giới hạn số trạng thái.  
&nbsp;&nbsp;&nbsp;&nbsp;- Nhanh hơn nếu beam width nhỏ.  
&nbsp;&nbsp;&nbsp;&nbsp;- Cân bằng giữa tìm kiếm toàn cục và cục bộ.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo lời giải tối ưu do bỏ qua trạng thái ngoài beam.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào beam width (quá nhỏ dễ bỏ sót lời giải).  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể bỏ lỡ GOAL_STATE nếu heuristic không tốt.    

### 4. Nhóm thuật toán Complex Environment Search (Tìm kiếm trong môi trường phức tạp)
#### AND-OR Search Algorithm
![AND_OR mp4](https://github.com/user-attachments/assets/95d7711a-03ba-4689-bb31-9e46411a2327)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Xây dựng cây tìm kiếm xen kẽ các nút AND (các hành động khả thi) và OR (các trạng thái kết quả). Trong 8-puzzle, tương đương DFS với kiểm tra vòng lặp, khám phá các di chuyển ô trống cho đến khi đạt GOAL_STATE.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Phù hợp với môi trường không xác định hoặc có nhiều kết quả.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tiết kiệm bộ nhớ nếu dùng DFS làm cơ sở.  
&nbsp;&nbsp;&nbsp;&nbsp;- Dễ mở rộng cho các bài toán phức tạp hơn.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Không đảm bảo lời giải ngắn nhất.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể chậm hoặc kẹt trong không gian trạng thái lớn.  
&nbsp;&nbsp;&nbsp;&nbsp;- Triển khai phức tạp hơn DFS thông thường.   

#### Belief State Search
![BBSS](https://github.com/user-attachments/assets/ce13cd2b-caf7-48a3-a36a-5a3edaf85ff2)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Duy trì tập belief_states (các trạng thái có thể), mở rộng tất cả hành động từ mỗi trạng thái, thu hẹp tập bằng heuristic. Trong 8-puzzle, tương tự search_with_no_observation, chọn trạng thái tốt nhất mỗi bước để xây dựng đường đi.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Xử lý môi trường quan sát một phần hoặc không xác định.  
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo lời giải nếu tất cả trạng thái khả thi được giữ.  
&nbsp;&nbsp;&nbsp;&nbsp;- Hiệu quả với heuristic tốt (~0.02 giây).  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ nếu belief_states lớn.  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm hơn nếu không thu hẹp hiệu quả.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào heuristic để chọn trạng thái.   

#### Partially Observable Search

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Duy trì belief_states dựa trên quan sát một phần (ví dụ: ô trống và láng giềng). Mở rộng trạng thái phù hợp với quan sát, sử dụng hàng đợi để theo dõi đường đi. Trong 8-puzzle, lọc trạng thái dựa trên vị trí ô trống và các ô lân cận.   
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Xử lý môi trường quan sát một phần chính xác.
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo lời giải nếu quan sát đủ thông tin.  
&nbsp;&nbsp;&nbsp;&nbsp;- Linh hoạt với các mức độ quan sát.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm (~0.5-1 giây) do lọc belief_states liên tục.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ để lưu các trạng thái khả thi.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào chất lượng quan sát.  

#### No Observation Search

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Duy trì tập belief_states mà không có quan sát mới, mở rộng tất cả hành động và thu hẹp bằng heuristic (như heuristic). Trong 8-puzzle, tương tự search_with_no_observation, chọn trạng thái tốt nhất để đạt GOAL_STATE.    
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Nhanh (~0.02 giây) nhờ heuristic và giới hạn belief_states.  
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo lời giải nếu trạng thái ban đầu khả thi.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phù hợp khi không có quan sát.    
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ nếu belief_states lớn (giới hạn 100 trạng thái).  
&nbsp;&nbsp;&nbsp;&nbsp;- Không hiệu quả nếu cần quan sát một phần.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào heuristic.   

### 5. Nhóm thuật toán Constraint Satisfaction Problem (CSP)
#### Backtracking CSP
![CSP](https://github.com/user-attachments/assets/e01aeeef-fedf-4ac4-ad23-7875669c224f)

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Gán giá trị cho các ô theo thứ tự, quay lui (backtrack) khi vi phạm ràng buộc (ví dụ: giá trị trùng). Trong 8-puzzle, gán số từ 1-8 và ô trống, kiểm tra tính khả thi và di chuyển hợp lệ.   
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Đảm bảo tìm lời giải nếu tồn tại.  
&nbsp;&nbsp;&nbsp;&nbsp;- Linh hoạt với các bài toán CSP phức tạp.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể tối ưu bằng cách sắp xếp biến/ràng buộc.    
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm (~0.1-1 giây) do thử nhiều tổ hợp.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ nếu không gian trạng thái lớn.  

### 6. Nhóm thuật toán Reinforcement Learning
#### Q-Learning  

**Cách chạy:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Học chính sách tối ưu bằng cách cập nhật bảng Q (giá trị hành động-trạng thái) qua các tập huấn luyện, sử dụng công thức Q(s,a) += α * (r + γ * max(Q(s',a')) - Q(s,a)). Trong 8-puzzle, trạng thái là hoán vị, hành động là di chuyển ô trống, phần thưởng -1 mỗi bước và +100 khi đạt GOAL_STATE.  
**Ưu điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Học được chính sách lâu dài mà không cần mô hình môi trường.  
&nbsp;&nbsp;&nbsp;&nbsp;- Linh hoạt với môi trường không xác định.  
&nbsp;&nbsp;&nbsp;&nbsp;- Có thể cải thiện qua nhiều tập huấn luyện.  
**Nhược điểm:**  
&nbsp;&nbsp;&nbsp;&nbsp;- Chậm (~1-10 giây) do cần nhiều tập huấn luyện.  
&nbsp;&nbsp;&nbsp;&nbsp;- Tốn bộ nhớ để lưu bảng Q lớn.  
&nbsp;&nbsp;&nbsp;&nbsp;- Phụ thuộc vào tham số (α, γ, ε) và số tập.  

## 📚 Tài liệu tham khảo
1. Artificial Intelligence: A Modern Approach – Stuart Russell & Peter Norvig
2. https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/  
3. https://github.com/rmssoares/8Puzzle-StateSpaceSearches
