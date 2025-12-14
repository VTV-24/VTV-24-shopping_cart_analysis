# 🛒 Shopping Cart Analysis – Apriori (Lab 1)

## 📌 Giới thiệu
Dự án này thực hiện **phân tích giỏ hàng (Market Basket Analysis)** trên bộ dữ liệu **Online Retail** bằng thuật toán **Apriori** nhằm khai thác **các tập mục phổ biến** và **luật kết hợp**.  
Bài làm được xây dựng theo dạng **pipeline tự động** sử dụng **Jupyter Notebook + Papermill**.


---

## 🔍 Các bước thực hiện

### 1️⃣ Tiền xử lý & EDA
- Làm sạch dữ liệu:
  - Loại bỏ hóa đơn hủy (InvoiceNo bắt đầu bằng `C`)
  - Loại bỏ giá trị thiếu, số lượng âm
- Lọc dữ liệu theo **United Kingdom**
- Phân tích sơ bộ doanh thu, khách hàng, sản phẩm

📓 Notebook: `preprocessing_and_eda.ipynb`

---

### 2️⃣ Chuẩn bị dữ liệu giỏ hàng
- Chuyển dữ liệu sang dạng **basket boolean matrix**
  - Hàng: hóa đơn
  - Cột: sản phẩm
  - Giá trị: 0/1
- Lưu dữ liệu dưới dạng `.parquet` để tối ưu tốc độ

📓 Notebook: `basket_preparation.ipynb`

---

### 3️⃣ Khai thác luật kết hợp với Apriori
- Áp dụng thuật toán **Apriori** từ thư viện `mlxtend`
- Do kích thước dữ liệu lớn (hơn 18.000 sản phẩm), nhóm đã:
  - Giữ lại **TOP N sản phẩm phổ biến nhất**
  - Lấy mẫu các giao dịch đại diện
- Thiết lập tham số:
  - `min_support`: 0.02 – 0.05
  - `max_len`: 2
  - `low_memory=True` để giảm tiêu thụ RAM
- Sinh luật kết hợp và lọc theo:
  - Support
  - Confidence
  - Lift

📓 Notebook: `apriori_modelling.ipynb`

---
### 4️⃣ Phân tích ảnh hưởng của tham số
- Khi tăng min_support:

  - Số luật giảm

  - Luật mạnh và phổ biến hơn

- Khi tăng min_confidence:

  - Luật đáng tin cậy hơn

  - Có thể bỏ sót các mối quan hệ ít xuất hiện

- Khi tăng min_lift:

  - Chỉ giữ lại các mối liên hệ thực sự có ý nghĩa

- Nhận xét giúp hiểu rõ sự đánh đổi giữa:

  - Độ phổ biến

  - Độ tin cậy

  - Độ mạnh của luật

---
### 5️⃣ Trực quan hóa kết quả

- Dự án sử dụng tối thiểu 2 biểu đồ, bao gồm:

  - Bar chart: Top luật kết hợp theo Lift

  - Scatter plot: Mối quan hệ giữa Support – Confidence – Lift

  - (Tuỳ chọn) Network graph để minh họa mối liên kết giữa các sản phẩm

- Mỗi biểu đồ đều kèm diễn giải ý nghĩa nhằm hỗ trợ việc ra quyết định.
---

## ⚙️ Chạy toàn bộ pipeline

Pipeline được tự động hóa bằng **Papermill**.

```bash
python run_papermill.py



