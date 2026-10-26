# Danh sách để lưu các công việc (mỗi phần tử là một dictionary)
tasks = []

def add_task(task_name):
    """Thêm một công việc mới dưới dạng dictionary vào danh sách."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    """Đánh dấu công việc tại vị trí task_index là đã hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành công việc: '{tasks[task_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

def list_tasks():
    """Hiển thị danh sách công việc kèm trạng thái hoàn thành."""
    print("\nDanh sách công việc:")
    for index, task in enumerate(tasks):
        # Chọn ký hiệu [x] nếu đã hoàn thành, [ ] nếu chưa
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index + 1}. {status} {task['name']}")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    
    # Hiển thị danh sách ban đầu
    list_tasks()
    
    # Đánh dấu công việc đầu tiên (chỉ số 0) là hoàn thành
    complete_task(0)
    
    # Hiển thị lại danh sách sau khi đã cập nhật
    list_tasks()