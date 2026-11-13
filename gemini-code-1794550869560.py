import pandas as pd

def calculate_store_kpis(df_merged, df_targets, report_period, compare_period):
    # Xử lý đồng bộ hàng trả (Return): Doanh thu và giá vốn ghi âm nếu Status == 'Returned'
    df_merged['Multiplier'] = df_merged['Status'].apply(lambda x: -1 if x == 'Returned' else 1)
    
    df_merged['Net_Revenue'] = df_merged['Quantity'] * df_merged['Unit_Price'] * df_merged['Multiplier']
    df_merged['Net_COGS'] = df_merged['Quantity'] * df_merged['Unit_Cost'] * df_merged['Multiplier']
    df_merged['Gross_Profit'] = df_merged['Net_Revenue'] - df_merged['Net_COGS']
    df_merged['Return_Value'] = df_merged.apply(
        lambda r: abs(r['Net_Revenue']) if r['Status'] == 'Returned' else 0, axis=1
    )

    # Lọc đúng kỳ báo cáo (Apples-to-Apples)
    df_current = df_merged[df_merged['Period'] == report_period]
    df_prev = df_merged[df_merged['Period'] == compare_period]

    # Tổng hợp theo cửa hàng
    curr_summary = df_current.groupby('Store_ID').agg(
        Net_Revenue=('Net_Revenue', 'sum'),
        Gross_Profit=('Gross_Profit', 'sum'),
        Return_Value=('Return_Value', 'sum')
    ).reset_index()

    prev_summary = df_prev.groupby('Store_ID').agg(
        Prev_Revenue=('Net_Revenue', 'sum')
    ).reset_index()

    # Ghép với mục tiêu (Target) và kỳ trước
    report = pd.merge(curr_summary, df_targets[df_targets['Period'] == report_period], on='Store_ID', how='left')
    report = pd.merge(report, prev_summary, on='Store_ID', how='left')

    # Tính các tỷ lệ quản trị
    report['Target_Completion_%'] = (report['Net_Revenue'] / report['Target_Revenue'] * 100).round(2)
    report['Gross_Margin_%'] = (report['Gross_Profit'] / report['Net_Revenue'] * 100).round(2)
    report['Return_Rate_%'] = (report['Return_Value'] / (report['Net_Revenue'] + report['Return_Value']) * 100).round(2)
    report['Growth_%'] = ((report['Net_Revenue'] - report['Prev_Revenue']) / report['Prev_Revenue'] * 100).round(2)

    return report.sort_values(by='Target_Completion_%', ascending=True)