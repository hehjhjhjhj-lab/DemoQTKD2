from langchain_community.llms import Ollama

def generate_management_insights(kpi_df, product_mix_summary):
    # Kết nối tới Local LLM chạy qua Ollama
    llm = Ollama(model="qwen2.5:7b", temperature=0.2)
    
    data_str = kpi_df.to_markdown(index=False)
    
    prompt = f"""
    Bạn là Chuyên gia Phân tích Kinh doanh cấp cao của chuỗi 18 cửa hàng bán lẻ Phúc An.
    Dưới đây là bảng tổng hợp chỉ số kinh doanh đã được làm sạch và đối soát chuẩn kỳ:
    
    {data_str}
    
    Cơ cấu nhóm sản phẩm chính tại các cửa hàng yếu:
    {product_mix_summary}
    
    Nhiệm vụ của bạn:
    1. Xác định TOP 3 cửa hàng cần Giám đốc Kinh doanh hỗ trợ ưu tiên nhất (không chỉ nhìn vào doanh thu thấp mà phải xét biên lợi nhuận gộp thấp, tỷ lệ hoàn thành mục tiêu kém hoặc tỷ lệ đổi trả cao bất thường).
    2. Chỉ ra nguyên nhân gốc rễ (tác động của đổi trả, cơ cấu hàng biên lãi thấp).
    3. Đề xuất hành động cụ thể cho từng cửa hàng trong 3 cửa hàng đó.
    Trình bày ngắn gọn, súc tích, đi thẳng vào số liệu để báo cáo Giám đốc.
    """
    
    response = llm.invoke(prompt)
    return response