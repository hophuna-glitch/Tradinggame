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

## Cập nhật 12/11/2026 (phiên tiếp theo)

### Lệnh tay và cách gom lượt đào (CHỐT)
- Bro chỉ trade tay: lệnh đơn, DCA (thêm cùng chiều), lệnh ngược.
- 1 lượt đào = từ lúc phẳng (không có vị thế XAUUSD) đến lúc phẳng lại. `dig_id` do game gán, MT5 chỉ báo vị thế (`position_id`).
- Mỗi vị thế = một dây thả xuống. Lệnh ngược khác màu, thả phía đối diện. Hiển thị tối đa ~5 dây, phần còn lại gộp thành dây "bó".
- Cần kiểm: tài khoản Exness là hedging hay netting. [CHƯA KIỂM CHỨNG]

### Vùng tối và khui vật phẩm (CHỐT)
- Dây chìm vào vùng tối, không hiện vàng/bom. Độ dài dây theo thời gian lệnh mở, không theo giá. Bỏ cơ chế "móc trôi theo floating P/L".
- Gợi ý mờ cho dây (rung nhẹ / đèn ấm), không lộ vật phẩm.
- Đóng một vị thế: kéo dây lên, khui vật phẩm theo P/L thật. Phẳng hoàn toàn: khui rương kết quả của cả lượt. Nhiều dây đóng cùng lúc thì xếp hàng khui.
- Công khai bảng quy đổi ngưỡng R -> vật phẩm. Khi khui hiện giờ đóng và P/L theo MT5. Game không đổi kết quả.
- DCA không được tôn vinh: thanh "áp lực hầm" tăng theo số lần DCA, lượt DCA lỗ nặng có animation sập hầm rõ ràng.

### Giao diện (CHỐT)
- Bỏ khung MT5 trên stream. Biểu đồ giá XAUUSD nằm trong game (vẽ từ tick MT5).
- Biểu đồ chỉ hiện giá, KHÔNG hiện entry, SL/TP, lot, vị thế hay P/L, để giữ bí ẩn và riêng tư. HUD không hiện P/L đang chạy, chỉ hiện sau khi đóng.
- Cần thêm sự kiện `chart.history` (nến lịch sử khi kết nối).

### Đoán vật phẩm và bảng xếp hạng (CHỐT, chi tiết chờ thiết kế)
- Khung chat xếp top người đoán vật phẩm giỏi nhất. Top 5 được quay random để vào chơi game.
- Điểm không mua được bằng gift. Mỗi dây một lượt đoán, khóa khi lệnh đóng. Cần chống spam và nhiều tài khoản ảo.
- Rủi ro chính sách trung bình (đoán kết quả lệnh), cần đọc guidelines nền tảng trước.
