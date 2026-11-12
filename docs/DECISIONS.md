# DECISIONS — Gold Miner Live

Nhật ký quyết định từ các phiên làm việc. Nguồn gốc: `docs/HANDOFF.md`. Cập nhật 12/11/2026.

## Mục tiêu
Tạo cộng đồng trade quanh livestream. Game chỉ trình diễn, MT5 là nguồn sự thật duy nhất.

## Format event (CHỐT)
- Event định kỳ, mỗi buổi 2 tiếng, có kỷ lục độ sâu giữa các buổi.
- Độ sâu theo hướng C: cộng đồng đào chung (chat/like) + kết quả lệnh thật của bro tác động (lời = mở tầng, lỗ = sập hầm).
- Đo kết quả bằng R (bội số rủi ro), không công khai USD.
- Giữ điểm dừng theo rủi ro trong mỗi buổi (lỗ tối đa hoặc số lệnh tối đa), hiển thị công khai. [ĐỀ XUẤT, chờ Bro chốt ngưỡng]

## Thời gian chờ lệnh
- Mini game MVP: Đào chung (`!dig`, `!bomb` có cooldown), thêm túi bí ẩn do chat vote. Điểm không mua được bằng gift.
- Bro giải thích setup, trả lời chat, nhìn lại lệnh trước.

## Lộ trình cuộc thi
| Giai đoạn | Nội dung | Điều kiện qua cửa |
|---|---|---|
| 1 (C) | Bro trade thật, game trình diễn, viewer chơi lớp giải trí | Chạy ổn nhiều buổi demo, có người xem quay lại |
| 2 (A) | Vòng loại bằng sàn ảo (vốn ảo, P/L tính trên giá thật từ MT5), top được bro cấp tài khoản thật (min 50 USD) | Đã hỏi chuyên gia pháp lý, đọc guidelines nền tảng, có bản luật |
| 3 (B) | Viewer tự trade tài khoản thật, xác minh qua dịch vụ bên thứ ba | Chỉ khi 2 giai đoạn trước ổn |

## Luật cứng cho cuộc thi
- Không nhận password của viewer (kể cả investor) vào game, chat hay bro. Xác minh qua bên thứ ba do chính viewer kết nối.
- Không đưa tín hiệu / khuyên lệnh cho người tham gia.
- Gift không mua được vốn, lệnh hay lợi thế. Giải thưởng minh bạch, ghi rõ điều kiện.
- Chống all-in phút cuối: đòn bẩy/lot cố định, tối thiểu số lệnh, xếp hạng có tính drawdown.
- Mỗi tài khoản nền tảng một slot (chống sybil). Disclaimer cố định, giới hạn độ tuổi.

## IB (mời gia nhập IB của sàn) — chỉ sau khi có cộng đồng
- Công khai rõ bro là IB và nhận hoa hồng, ghi cố định trên stream và mô tả.
- Không gắn điều kiện IB vào cuộc thi.
- Không thưởng theo khối lượng giao dịch, không khoe đòn bẩy cao, không hứa lợi nhuận.
- Xung đột lợi ích: IB hưởng lợi khi viewer trade nhiều, nên các luật trên là bắt buộc.

## Việc chưa kiểm chứng (cần Bro tự làm)
- Hỏi người am hiểu pháp lý về mô hình cuộc thi có tiền thật và IB tại Việt Nam.
- Đọc Community Guidelines của nền tảng live định dùng (TikTok / YouTube).
- Kiểm TikTok có cấp stream key và cách đọc chat/gift hợp lệ.

## Câu hỏi còn mở
1. Một "lượt đào" = một vị thế hay một chuỗi lệnh (rổ)?
2. Điểm dừng rủi ro: lấy lỗ tối đa hay số lệnh tối đa mỗi buổi, ngưỡng bao nhiêu?
3. MT5 lấy dữ liệu ở Mac (investor) hay VPS?
4. Phiên bản Godot đang cài?
