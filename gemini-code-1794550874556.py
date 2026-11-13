import streamlit as st
import pandas as pd
from agents.data_cleaner import clean_and_validate_data
from agents.calc_engine import calculate_store_kpis
from agents.analyst_agent import generate_management_insights

st.set_page_config(page_title="Phúc An - Retail AI Agent", layout="wide")
st.title("📊 Hệ thống AI Agent Phân tích Hiệu quả Chuỗi 18 Cửa hàng")

# Sidebar: Tải dữ liệu & Thiết lập kỳ so sánh
with st.sidebar:
    st.header("1. Dữ liệu đầu vào")
    file_trans = st.file_uploader("Upload Giao dịch (60k dòng CSV/Excel)", type=["csv", "xlsx"])
    file_costs = st.file_uploader("Upload Danh mục & Giá vốn", type=["csv", "xlsx"])
    file_targets = st.file_uploader("Upload Mục tiêu theo kỳ", type=["csv", "xlsx"])
    
    st.header("2. Chuẩn hóa kỳ báo cáo")
    report_period = st.text_input("Kỳ báo cáo (VD: 2026-10)", value="2026-10")
    compare_period = st.text_input("Kỳ so sánh chuẩn (VD: 2026-09)", value="2026-09")

if file_trans and file_costs and file_targets:
    df_trans = pd.read_csv(file_trans) if file_trans.name.endswith('.csv') else pd.read_excel(file_trans)
    df_costs = pd.read_csv(file_costs) if file_costs.name.endswith('.csv') else pd.read_excel(file_costs)
    df_targets = pd.read_csv(file_targets) if file_targets.name.endswith('.csv') else pd.read_excel(file_targets)

    # BƯỚC 1: Làm sạch dữ liệu
    df_clean, logs, missing_skus = clean_and_validate_data(df_trans, df_costs)
    
    st.subheader("🔍 Nhật ký Làm sạch Dữ liệu (Data Cleaning Agent)")
    for log in logs:
        st.info(log)

    # HUMAN-IN-THE-LOOP ĐIỂM 1: Kiểm tra dữ liệu bất thường
    if missing_skus:
        st.error(f"⚠️ CẢNH BÁO HUMAN-IN-THE-LOOP: Phát hiện {len(missing_skus)} mã sản phẩm thiếu giá vốn: {missing_skus}. Vui lòng cập nhật bảng giá vốn hoặc xác nhận bỏ qua trước khi tiếp tục!")
        override = st.checkbox("Tôi đã kiểm tra và cho phép tính tiếp (gán giá vốn = 0 cho mã thiếu)")
        if not override:
            st.stop()

    # BƯỚC 2: Tính toán chỉ số
    kpi_report = calculate_store_kpis(df_clean, df_targets, report_period, compare_period)
    
    st.subheader("📈 Bảng Đối soát Hiệu quả 18 Cửa hàng (Đã chuẩn hóa kỳ)")
    st.dataframe(kpi_report, use_container_width=True)

    # Cảnh báo biến động bất thường (>30%) để con người rà soát
    anomalies = kpi_report[kpi_report['Growth_%'].abs() > 30]
    if not anomalies.empty:
        st.warning(f"💡 Lưu ý kiểm soát: Các cửa hàng sau có biến động doanh thu >30% so với kỳ trước, cần xác minh yếu tố vận hành (sửa chữa, khai trương...): {anomalies['Store_ID'].tolist()}")

    # BƯỚC 3: AI Agent phân tích và đề xuất
    if st.button("🤖 Chạy AI Agent Phân tích & Đề xuất Hỗ trợ"):
        with st.spinner("AI Agent đang phân tích cơ cấu sản phẩm và tác động đổi trả..."):
            # Tóm tắt cơ cấu sản phẩm của top 5 cửa hàng thấp nhất
            weak_stores = kpi_report.head(5)['Store_ID'].tolist()
            mix = df_clean[df_clean['Store_ID'].isin(weak_stores)].groupby(['Store_ID', 'Category'])['Net_Revenue'].sum().to_string()
            
            insights = generate_management_insights(kpi_report, mix)
            st.subheader("🎯 Báo cáo Đề xuất Hành động cho Giám đốc Kinh doanh")
            st.markdown(insights)
            
            # HUMAN-IN-THE-LOOP ĐIỂM 2: Phê duyệt báo cáo
            st.download_button(
                label="✅ Phê duyệt & Xuất Báo cáo Đối soát (CSV)",
                data=kpi_report.to_csv(index=False).encode('utf-8-sig'),
                file_name=f"Bao_Cao_Quan_Tri_PhucAn_{report_period}.csv",
                mime="text/csv"
            )