import pandas as pd

def clean_and_validate_data(df_trans, df_costs):
    logs = []
    initial_rows = len(df_trans)
    
    # 1. Loại bỏ trùng lặp theo mã giao dịch (Transaction_ID)
    df_clean = df_trans.drop_duplicates(subset=['Transaction_ID'], keep='first').copy()
    dup_count = initial_rows - len(df_clean)
    logs.append(f"Đã loại bỏ {dup_count} dòng giao dịch trùng lặp.")
    
    # 2. Lọc bỏ đơn hàng bị hủy (Status == 'Cancelled')
    cancelled_count = len(df_clean[df_clean['Status'] == 'Cancelled'])
    df_clean = df_clean[df_clean['Status'] != 'Cancelled']
    logs.append(f"Đã loại bỏ {cancelled_count} đơn hàng bị hủy.")
    
    # 3. Ghép giá vốn và kiểm tra điểm dừng Human-in-the-Loop (thiếu giá vốn)
    df_merged = pd.merge(df_clean, df_costs, on='Product_ID', how='left')
    missing_cost_skus = df_merged[df_merged['Unit_Cost'].isna()]['Product_ID'].unique().tolist()
    
    return df_merged, logs, missing_cost_skus