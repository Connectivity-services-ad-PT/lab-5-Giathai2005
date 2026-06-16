# Readiness Checklist – Lab 05

Đây là danh sách kiểm tra (checklist) để đảm bảo stack Docker Compose đã sẵn sàng trước khi nộp bài.

---

## ✅ Database ready
- [x] Container DB đã chạy và trạng thái `healthy`
- [x] Kiểm tra bằng lệnh:
  ```bash
  docker exec -it fit4110-db-lab05 pg_isready -U lab05