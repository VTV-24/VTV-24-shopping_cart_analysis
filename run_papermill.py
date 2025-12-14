import papermill as pm
import os

# Tạo thư mục output nếu chưa có
os.makedirs("notebooks/runs", exist_ok=True)

KERNEL_NAME = "venv"   # 🔴 kernel đã đăng ký bằng ipykernel

# =====================================================
# 1. Preprocessing + EDA
# =====================================================
pm.execute_notebook(
    "notebooks/preprocessing_and_eda.ipynb",
    "notebooks/runs/preprocessing_and_eda_run.ipynb",
    parameters=dict(
        DATA_PATH="data/raw/online_retail.csv",
        COUNTRY="United Kingdom",
        OUTPUT_DIR="data/processed",

        # Tắt bớt plot khi chạy batch
        PLOT_REVENUE=False,
        PLOT_TIME_PATTERNS=False,
        PLOT_PRODUCTS=False,
        PLOT_CUSTOMERS=False,
        PLOT_RFM=False,
    ),
    kernel_name=KERNEL_NAME,
)

# =====================================================
# 2. Basket Preparation
# =====================================================
pm.execute_notebook(
    "notebooks/basket_preparation.ipynb",
    "notebooks/runs/basket_preparation_run.ipynb",
    parameters=dict(
        CLEANED_DATA_PATH="data/processed/cleaned_uk_data.csv",
        BASKET_BOOL_PATH="data/processed/basket_bool.parquet",

        INVOICE_COL="InvoiceNo",
        ITEM_COL="Description",
        QUANTITY_COL="Quantity",
        THRESHOLD=1,
    ),
    kernel_name=KERNEL_NAME,
)

# =====================================================
# 3. Apriori Modelling
# =====================================================
pm.execute_notebook(
    "notebooks/apriori_modelling.ipynb",
    "notebooks/runs/apriori_modelling_run.ipynb",
    parameters=dict(
        BASKET_BOOL_PATH="data/processed/basket_bool.parquet",
        RULES_OUTPUT_PATH="data/processed/rules_apriori_filtered.csv",

        # Tham số Apriori
        MIN_SUPPORT=0.01,
        MAX_LEN=3,

        # Generate rules
        METRIC="lift",
        MIN_THRESHOLD=1.0,

        # Lọc luật
        FILTER_MIN_SUPPORT=0.01,
        FILTER_MIN_CONF=0.3,
        FILTER_MIN_LIFT=1.2,
        FILTER_MAX_ANTECEDENTS=2,
        FILTER_MAX_CONSEQUENTS=1,

        # Số luật để vẽ
        TOP_N_RULES=20,

        # Tắt plot khi chạy batch
        PLOT_TOP_LIFT=False,
        PLOT_TOP_CONF=False,
        PLOT_SCATTER=False,
        PLOT_NETWORK=False,
    ),
    kernel_name=KERNEL_NAME,
)

print("✅ Đã chạy xong toàn bộ pipeline Papermill")
