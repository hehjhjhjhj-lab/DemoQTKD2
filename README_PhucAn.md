# README -- Báo cáo BI & AI Agent chuỗi bán lẻ Phúc An

## 1. Giới thiệu

Tài liệu này giới thiệu dự án phân tích hiệu quả kinh doanh và kiến trúc
tự động hóa AI Agent cho **Chuỗi bán lẻ Phúc An**, gồm 18 cửa hàng tại
Hà Nội và TP. Hồ Chí Minh.

-   **Học phần:** AI301 -- AI Agent & Business Intelligence
-   **Kỳ báo cáo:** Tháng 04/2026
-   **Kỳ dữ liệu phân tích:** 01/01/2026 -- 30/04/2026
-   **Dữ liệu kiểm thử được đề cập trong báo cáo:** 6.000 dòng giao dịch
-   **Tệp dữ liệu nguồn được đề cập:**
    `PhucAn_6000_DonHang_18CuaHang.xlsx`
-   **Ngày thực thi ghi trong báo cáo:** 11/11/2026

## 2. Mục tiêu dự án

Dự án hướng đến việc thay thế quy trình ghép và xử lý dữ liệu thủ công
bằng một quy trình BI có hỗ trợ AI Agent, nhằm:

-   Kiểm tra chất lượng dữ liệu và phát hiện giao dịch trùng lặp.
-   Loại trừ đơn hủy, đơn chờ xử lý và các bản ghi chưa đủ căn cứ.
-   Chuẩn hóa cách tính doanh thu thuần, lợi nhuận gộp và tỷ lệ đổi trả.
-   Phân tích hiệu quả theo cửa hàng và sản phẩm.
-   Xác định các cửa hàng cần ưu tiên hỗ trợ.
-   Tạo cơ sở dữ liệu đáng tin cậy cho dashboard và quyết định quản trị.

## 3. Phạm vi dữ liệu

Phúc An có 18 cửa hàng, gồm 13 cửa hàng tại miền Bắc và 5 cửa hàng tại
miền Nam. Báo cáo phân tích 5 sản phẩm thuộc 3 nhóm ngành:

  Mã sản phẩm   Sản phẩm             Nhóm ngành
  ------------- -------------------- ------------
  SP001         Tai nghe Bluetooth   Điện tử
  SP002         Nồi cơm điện tử      Gia dụng
  SP003         Áo khoác gió         Thời trang
  SP004         Quạt tích điện       Gia dụng
  SP005         Bàn phím cơ          Điện tử

## 4. Quy trình xử lý và phân tích

Quy trình đề xuất gồm 7 bước:

1.  **Tiếp nhận dữ liệu thô:** Nạp dữ liệu POS, danh mục sản phẩm và
    danh mục cửa hàng.
2.  **Kiểm định và khử trùng lặp:** Phát hiện bản ghi trùng, đơn hủy, dữ
    liệu thiếu và đơn chờ xử lý.
3.  **Duyệt ngoại lệ (HITL-1):** Kế toán và chuyên viên BI xem xét các
    trường hợp thiếu thông tin hoặc đang chờ xử lý.
4.  **Tính toán chỉ số:** Tính doanh thu mua mới, giá trị đổi trả, doanh
    thu thuần, giá vốn, lợi nhuận gộp, biên lợi nhuận và tỷ lệ đổi trả.
5.  **Chẩn đoán:** Xếp hạng cửa hàng dựa trên doanh thu, biến động theo
    tháng và tỷ lệ đổi trả.
6.  **Phê duyệt quản trị (HITL-2):** Ban điều hành xác nhận mục tiêu và
    quyết định phương án can thiệp.
7.  **Xuất bản và giám sát:** Cập nhật dashboard, gửi cảnh báo và giao
    nhiệm vụ cải thiện.

### Các tác tử AI được đề xuất

-   **AI Data Quality & Deduplication Agent:** Kiểm tra dữ liệu, phát
    hiện trùng lặp và phân loại ngoại lệ.
-   **AI Financial Metric Engine:** Tính toán các chỉ số tài chính theo
    quy tắc thống nhất.
-   **AI Prescriptive Diagnostics Agent:** Phân tích, chấm điểm và xếp
    hạng cửa hàng cần hỗ trợ.

Các quyết định liên quan đến chứng từ ngoại lệ, mục tiêu kinh doanh và
ngân sách vẫn cần con người phê duyệt.

## 5. Một số kết quả chính trong báo cáo

Theo báo cáo, sau bước kiểm định dữ liệu:

-   Tổng dữ liệu đầu vào: **6.000 dòng**.
-   Dữ liệu được đưa vào tính toán: **4.667 dòng**, gồm 4.070 đơn mua
    mới và 597 đơn đổi trả.
-   Dữ liệu chưa đủ căn cứ đưa vào tính toán: **1.333 dòng**.
-   Doanh thu thuần lũy kế 4 tháng: **10.013.850.000 VNĐ**.
-   Lợi nhuận gộp lũy kế 4 tháng: **4.151.550.000 VNĐ**.
-   Biên lợi nhuận gộp trung bình: **41,46%**.
-   Doanh thu thuần tháng 04/2026: **2.379.650.000 VNĐ**.

### Ba cửa hàng cần ưu tiên hỗ trợ trong tháng 04/2026

  -----------------------------------------------------------------------
  Cửa hàng          Doanh thu thuần   Biến động so với      Tỷ lệ đổi trả
                                              tháng 03 
  -------------- ------------------ ------------------ ------------------
  CH15 -- Quận 3     85.050.000 VNĐ             -47,1%             32,61%

  CH14 -- Bắc Từ    122.050.000 VNĐ             -31,6%             18,98%
  Liêm                                                 

  CH05 -- Thanh     116.750.000 VNĐ             -28,3%             17,49%
  Xuân                                                 
  -----------------------------------------------------------------------

### Một số phát hiện về sản phẩm

-   SP003 -- Áo khoác gió có biên lợi nhuận gộp cao nhất: **58,33%**.
-   SP004 -- Quạt tích điện có biên lợi nhuận gộp **55,56%**.
-   SP001 -- Tai nghe Bluetooth có biên lợi nhuận gộp thấp nhất:
    **28,57%**.
-   SP005 -- Bàn phím cơ có tỷ lệ đổi trả cao nhất: **14,20%**.

## 6. Điểm cần lưu ý và giới hạn dữ liệu

-   Báo cáo cho biết dữ liệu nguồn chưa có bảng chỉ tiêu mục tiêu cho
    từng cửa hàng. Vì vậy, không tự đặt mục tiêu; cần Ban Giám đốc bổ
    sung và phê duyệt tại bước HITL-2.
-   Các bản ghi thiếu thông tin và đơn chờ xử lý cần được bộ phận phụ
    trách xác minh trước khi quyết định ghi nhận.
-   Tệp Excel nguồn và tệp ngoại lệ được nhắc đến trong báo cáo không
    nằm trong bộ tài liệu README này, trừ khi được cung cấp riêng.
-   Các số liệu trong README được tóm lược từ báo cáo Word đi kèm. Khi
    sử dụng cho mục đích kiểm toán hoặc triển khai, cần đối chiếu lại
    với dữ liệu nguồn và quy tắc tính toán chính thức.

## 7. Tài liệu trong dự án

  -------------------------------------------------------------------------------
  Tài liệu                                    Mô tả
  ------------------------------------------- -----------------------------------
  `Bao_Cao_BI_Chuoi_Cua_Hang_PhucAn.docx`     Báo cáo phân tích BI, quy trình AI
                                              Agent, kết quả kinh doanh và đề
                                              xuất hành động

  `PhucAn_6000_DonHang_18CuaHang.xlsx`        Tệp dữ liệu giao dịch nguồn được
                                              báo cáo sử dụng (cần cung cấp
                                              riêng)

  `Danh_Sach_Ngoai_Le_Khong_Du_Can_Cu.xlsx`   Danh sách bản ghi ngoại lệ được báo
                                              cáo đề cập (cần cung cấp riêng)
  -------------------------------------------------------------------------------

## 8. Kết luận

Dự án xây dựng quy trình kết hợp BI và AI Agent để chuẩn hóa dữ liệu,
phân tích hiệu quả kinh doanh và hỗ trợ phát hiện sớm các cửa hàng có
dấu hiệu suy giảm. AI Agent đảm nhiệm các bước kiểm tra và tính toán
theo quy tắc; con người giữ vai trò thẩm định ngoại lệ, xác nhận mục
tiêu và phê duyệt quyết định kinh doanh.
