# GOLD MINER LIVE — HANDOFF SANG CLAUDE CODE

Tổng hợp phiên 24/10/2026 – 12/11/2026. Đọc hết file này trước khi làm bất cứ thứ gì.

**Trạng thái thật:** chưa có code game, chưa có EA bridge, chưa có project Godot. Đã có: concept, kiến trúc, 1 mockup layout (art bị loại), bộ prompt art, và một loạt giả định chưa kiểm chứng.

Quy ước nhãn:
- **[CHỐT]** Bro đã tự nói / tự chọn.
- **[ĐỀ XUẤT]** Claude đề xuất, Bro chưa xác nhận rõ.
- **[CHƯA KIỂM CHỨNG]** Chưa có nguồn chắc hoặc chưa test thật.

---

## 0. Cách làm việc với Bro (áp dụng cho cả phiên Claude Code)

- Tiếng Việt. Xưng "tôi", gọi Bro là "bro". Thuật ngữ chuyên ngành giữ tiếng Anh, lần đầu kèm nghĩa tiếng Việt trong ngoặc.
- Ngắn gọn, thẳng thắn, vào trọng tâm. Không giải thích dài dòng.
- Quyết định quan trọng: nêu giả định và hỏi trước. Việc nhỏ, rõ: làm luôn.
- Brief mơ hồ thì hỏi lại, không tự suy diễn.
- Phương án sáng tạo: đưa 3 hướng hợp lý nhất, nêu khác biệt để Bro chọn.
- Phản biện khi thấy cách đơn giản hơn, kể cả khi không được hỏi.
- Chỉ làm đúng phạm vi. Sửa cái có sẵn thì chỉ đụng phần cần sửa, thấy chỗ khác có vấn đề thì nêu ra, không tự sửa.
- Việc nhiều bước: nêu kế hoạch ngắn kèm cách kiểm tra trước khi làm.
- Prompt hình ảnh viết theo góc nhìn đạo diễn hình (bố cục, góc máy, ống kính, ánh sáng, màu, chất liệu, cảm xúc). Gu: quiet luxury, tinh tế, không phô trương.
- Bro là đạo diễn hình ảnh, không phải dev chuyên. Code phải kèm file tree, lệnh chạy và bước test rõ ràng.

---

## 1. Dự án là gì

Game kiểu Gold Miner cổ điển, pixel art, chạy trên Godot, kết nối MT5 (XAUUSD) để livestream. Bro vào/đóng lệnh trực tiếp trên MT5; game chỉ **trình diễn** kết quả. Mục tiêu giải trí: vui, tương tác với người xem.

**Quy tắc không được phá (từ brief gốc, [CHỐT]):**
1. MT5 là nguồn sự thật duy nhất. Game không nằm trong đường thực thi lệnh.
2. Game sập / mất mạng livestream không được ảnh hưởng lệnh thật.
3. Chỉ coi lệnh đã đóng khi MT5 xác nhận (không phải lúc bấm nút).
4. Gift / chat / viewer **không bao giờ** mở, đóng, sửa lệnh. Chỉ tác động lớp giải trí.
5. Không đưa credential, password, số tài khoản, API secret vào code, log, prompt hay frontend.
6. Bắt đầu bằng **tài khoản demo**. Không dùng real account cho test ban đầu.
7. Không đưa Balance / Equity / Margin ra luồng stream.

---

## 2. Quyết định theo từng mảng

### 2.1 Nền tảng live
- **[CHỐT]** TikTok là lựa chọn ban đầu. Bro tự lo phần follower. Có thể live nền tảng khác.
- Bố cục 3 nguồn (game + MT5 điện thoại + camera) gần như bắt buộc ghép bằng **OBS trên Mac rồi đẩy RTMP**. Live thuần bằng điện thoại không ghép được game từ Mac.
- **[CHƯA KIỂM CHỨNG]** TikTok có cấp stream key cho tài khoản Bro không (nguồn thứ cấp nói cần ≥1.000 follower; một nguồn nói bản Live Studio cho Mac đang beta). Bro cần tự kiểm trong app.
- **[ĐỀ XUẤT]** Test prototype trên YouTube Live (mở, nhận RTMP, đọc chat qua API), thêm TikTok sau.
- **[CHƯA KIỂM CHỨNG]** Chính sách từng nền tảng về live trade kèm gift/donate. Không tìm được nguồn chính thức. Bro phải đọc Community Guidelines của nền tảng định dùng.
- **[CHƯA KIỂM CHỨNG]** Cách nhận event gift/chat/like hợp lệ cho tài khoản của Bro (TikFinity-kiểu plugin bên thứ ba, hay cách khác).

### 2.2 KPI và vòng chơi
- **[CHỐT]** Không dừng game khi đạt KPI. Số lệnh mỗi phiên không giới hạn.
- **[CHỐT]** Map đi **sâu dần** khi lên level (hướng "độ sâu").
- **[ĐỀ XUẤT]** KPI = cơ chế lên level (mỗi level có mục tiêu mới cao hơn), không còn là điểm dừng.
- **[ĐỀ XUẤT, chưa được trả lời]** Thêm **một điểm dừng theo rủi ro** (lỗ tối đa/phiên hoặc số lệnh tối đa). Chạm ngưỡng thì game hiện "MINING PAUSED" công khai. Lý do: bỏ điểm dừng KPI thì game thành cỗ máy thưởng cho việc trade thêm.
- **[CHƯA CHỐT]** Session P/L tính realized hay gồm floating? Có tính commission/swap không?

### 2.3 Gameplay và tương tác viewer
Tách **2 layer**:
- **Layer A (trade-driven, dữ liệu thật):** móc/dây theo lệnh MT5.
- **Layer B (viewer-driven, thuần giải trí):** gift/chat/like chỉ chạy ở đây. Không ảnh hưởng lệnh, không ảnh hưởng số liệu thật.

**[ĐỀ XUẤT] Mapping kết quả → vật phẩm (không random, theo P/L thật):**

| Kết quả lệnh | Vật phẩm |
|---|---|
| Lời nhỏ | vàng nhỏ |
| Lời lớn | thanh vàng / kim cương |
| Hòa vốn | đá |
| Lỗ | giày cũ |
| Lỗ nặng | bom |

Lệnh lỗ phải có animation riêng (không chỉ ăn mừng khi lời, kẻo game cổ vũ trade bằng mọi giá). Độ lớn vật phẩm ăn theo số tiền thật. Game được phép làm chậm / rung / dồn nhạc, **không được đổi kết quả**.

**[ĐỀ XUẤT] Cơ chế "hay": móc trôi theo floating P/L khi lệnh còn mở.** Đang lời thì móc trôi gần vàng, đang lỗ thì trôi về phía bom, tạo hồi hộp. Bro chưa xác nhận cơ chế này.

**3 hướng Layer B (MVP đề xuất làm 1 + 3, hướng 2 để sau):**
1. Co-op mining: chat gõ `!dig`, `!bomb` (có cooldown), thanh "hầm mỏ chung" đầy dần nhờ like/chat thì mở sự kiện/boss. Lấp dead air giữa các lệnh.
2. Dự đoán giá lên/xuống + leaderboard. Giữ chân tốt nhất nhưng **rủi ro chính sách cao nhất**; điểm không được mua bằng gift (kẻo giống cờ bạc).
3. Gift spectacle: hiệu ứng thuần thị giác (mưa kim cương, nổ dynamite, thanh vàng khắc tên người tặng).

Thêm: hiện tên viewer (thợ đào của ai, top gifter), túi bí ẩn do chat vote (phần thưởng chỉ là skin/hiệu ứng), slow-mo + sound design lúc đóng lệnh.

Mining Credits từ gift: các mức quy đổi trong brief gốc (Nugget +1, Diamond +3...) chỉ là ví dụ, chưa chốt.

### 2.4 Bố cục khung 9:16
- **[CHỐT]** Cả khung 9:16: game ~65–70%, dải dưới chia MT5 + camera.
- Mockup đã dựng ở 540×960: game 540×630 (HUD trên cùng, thước độ sâu LV1–LV4, thợ đào, móc/dây, toast gift, thanh Team Energy), dải dưới 330px gồm khung MT5 đã che dữ liệu (248×292) và khung camera (248×292).
- HUD hiển thị: LEVEL, SESSION P/L, KPI (kèm thanh tiến độ lên level), TRADE P/L, BALANCE = PRIVATE.
- Mockup (artifact, chỉ để tham khảo layout): https://claude.ai/artifact/LTTrcWLumGhTD1Cdditfwa
- **Art của mockup bị Bro loại ("xấu").** Chỉ giữ layout và danh sách thành phần HUD; không dùng lại art vẽ bằng code.
- **[CHƯA KIỂM CHỨNG]** Chưa test độ đọc được của chữ 12px (Press Start 2P) trên điện thoại thật.

### 2.5 Art
- **[CHỐT]** Phong cách pixel art, tham chiếu 2 ảnh Bro gửi (hiệp sĩ pixel và cảnh hầm mỏ nhiều tầng: nền teal hoàng hôn, thân cây trắng, rêu, đất gạch nâu).
- **[CHỐT]** Đang thử **SpriteCook** (app.spritecook.ai). Bro tạo được một ảnh concept đẹp gồm: cảnh mặt đất + thợ đào đội mũ có đèn + 4 tầng đất (dirt, clay, stone, deep tím) + 6 vật phẩm (vàng, kim cương, đá, giày, bom, túi bí ẩn). Bro nói "khá đẹp". Chưa rõ Bro đã bấm "Chọn khái niệm này" chưa.
- Ảnh concept là ảnh ghép sẵn, **chưa dùng ngay được**: cần từng sprite riêng nền trong suốt. Joystick/nút cuốc/khu dương xỉ mờ là thừa, bỏ.
- Còn thiếu: móc câu 2 trạng thái (thả / kéo về), thanh vàng, cây/nấm/hộp gỗ mặt đất, thợ đào idle 4 frame. Dây vẽ bằng code (độ dài đổi theo giá).
- **[CHƯA KIỂM CHỨNG]** SpriteCook: xuất PNG nền trong suốt? kích thước pixel mỗi file? tileset có ghép liền (thử 3×3)? idle có giữ nhân vật giữa các frame? 1 lần tạo tốn bao nhiêu credit (free: 40 credit/30 ngày)? Trang của họ tự nhận dùng thương mại được, nhưng 0 review độc lập trên Capterra và trang so sánh với PixelLab do chính họ viết. **Bro phải đọc Terms of Service trước khi dùng cho stream có nhận gift.**
- Phương án dự phòng: pack tileset trên itch.io (cùng một tác giả cho tileset + nhân vật + vật phẩm, kiểm license thương mại, chụp lại trang license); hoặc AI cho background + pack cho vật phẩm; hoặc thuê pixel artist cho bản chính thức.
- Không copy asset có bản quyền (Gold Miner gốc, nhân vật có sẵn).

**Style anchor (dán đầu mọi prompt):**
> Hi-bit pixel art, clean hand-placed pixels, soft selective dark outlines, side view orthographic, flat eye-level camera, no perspective. Muted twilight palette: desaturated teal shadows, mossy green, warm brown brick-textured earth, slate stone. Warm amber reserved for gold and glow only. Soft rim light from top-left, cool ambient shadow. Quiet, moody, restrained. Transparent background, no text, no UI.

**Test 1 – tileset 4 tầng:** `[Style anchor]` Seamless horizontal tileset of four underground strata, each as its own tile row: (1) brown brick-like dirt with fine pebbles, mossy green fringe on top edge; (2) red-brown clay, smoother, darker cracks; (3) dark slate stone with cool blue-grey highlights and a few faint cyan mineral specks; (4) deep violet cave rock, near-black with scattered purple crystal flecks. Each row tiles left-right and top-bottom without visible seams. Consistent pixel size across all four.

**Test 2 – 6 vật phẩm:** `[Style anchor]` Set of six separate game item sprites, centered, one per cell, equal scale, readable at small size: (1) small raw gold nugget, warm amber with pale yellow highlight; (2) cyan-white diamond, faceted; (3) grey boulder, blocky; (4) worn leather boot, cracked and muddy; (5) round black bomb with short lit fuse, red spark; (6) tied burlap sack with a gold question mark. Same light direction and outline weight across all six.

**Test 3 – thợ đào idle:** `[Style anchor]` Original miner character, front-facing three-quarter idle pose, stocky chibi proportions, red cap with small amber headlamp, blue overalls, brown work boots, holding a coiled rope. Subtle 4-frame idle loop: gentle breathing, slight head tilt. Even frame grid, same size each frame, transparent background.

Tiêu chí chấm: đồng bộ bộ vật phẩm; thu nhỏ ~48px vẫn phân biệt được vàng/kim cương/bom; tile 3×3 không thấy đường nối; vàng là điểm ấm duy nhất.

### 2.6 Engine
- **[CHỐT]** Godot 4. Bro muốn tự tuỳ chỉnh bằng editor (kéo sprite, chỉnh vị trí, animation).
- **[CHƯA BIẾT]** Phiên bản Godot Bro cài (Claude đã hỏi, chưa có câu trả lời). Mac mini đã cài chưa.
- Claude không chạy được Godot trong phiên chat, nên vòng test là: Claude viết project → Bro chạy → báo lỗi/ảnh chụp lại.
- Loại bỏ: GameMaker (bản free chỉ non-commercial), Construct 3 (free giới hạn 50 events, 2 layers). GDevelop chưa xác nhận hỗ trợ WebSocket/socket.

---

## 3. Kiến trúc

**[ĐỀ XUẤT, chưa được xác nhận]** Ba phần chạy riêng, nối bằng một **hợp đồng sự kiện** cố định:

```
MT5 ──> [Giao thức dữ liệu] ──> [Gameplay engine] ──> [Giao diện]
         chuyển sự kiện thật     quyết định diễn ra sao    vẽ ra màn hình
```

- MT5 quyết định **CÁI GÌ** xảy ra; game quyết định **NHƯ THẾ NÀO** diễn ra. Giao thức chỉ báo đúng sự việc, không thêm thắt.
- Tách riêng để: test độc lập (dùng bảng giả lập khi chưa có MT5), MT5/game sập không kéo nhau, đổi art/luật không đụng phần MT5.
- Hai loại sự kiện tách bạch: `trade.*` (từ MT5) và `viewer.*` (từ nền tảng live). `viewer.*` không bao giờ đi vào đường giao dịch.

**Bảng sự kiện → dàn dựng (đề xuất):**

| Sự kiện từ MT5 | Gameplay |
|---|---|
| Không có lệnh | Móc đung đưa chờ; viewer chơi Layer B |
| Mở lệnh | Móc thả xuống |
| Floating P/L đổi | Móc trôi về phía vàng (lời) / bom (lỗ) |
| MT5 xác nhận đóng | Chộp vật phẩm ứng với kết quả thật, kéo lên |
| Session P/L đạt KPI | Lên level, map xuống tầng sâu hơn |

Tên sự kiện nháp để chốt hợp đồng: `trade.snapshot`, `trade.tick`, `trade.open`, `trade.update`, `trade.close`, `bridge.heartbeat`, `viewer.gift`, `viewer.like`, `viewer.chat`.

---

## 4. Đường truyền MT5 → Godot (phần cần độ trễ thấp)

**Delay nằm ở đâu:** (1) broker → MT5, ngoài tầm kiểm soát; (2) MT5 → game cùng máy, rất nhỏ (ước tính, chưa đo); (3) game → người xem qua nền tảng live, thường vài giây (chưa kiểm số liệu); (4) hình MT5 trên điện thoại cũng trễ riêng. Mục tiêu là **đồng bộ**, không phải zero delay: game cần **bộ đệm trễ chỉnh được 0–1s** để khớp hình MT5.

**[ĐỀ XUẤT] Thiết kế:**
- **EA bridge nhỏ** (MQL5) trên chart riêng, làm **TCP client**, mở kết nối một lần và giữ (không connect mỗi tick). Mỗi dòng một JSON ngắn.
- **Godot làm server** trên `127.0.0.1` bằng `TCPServer`. EA gửi TCP thô → **không dùng `WebSocketPeer`** (Claude đã sửa câu trả lời trước). MVP bỏ Python trung gian để bớt một hop.
- Tick tối đa 10–20 lần/giây, chỉ giữ giá mới nhất; Godot nội suy lên 60fps.
- Sự kiện lệnh gửi ngay (không giới hạn tần suất), kèm **số thứ tự tăng dần** để bỏ trùng và phát hiện mất gói.
- Lệnh chỉ coi là đóng khi giao dịch đã được ghi nhận (dựa `OnTradeTransaction`, loại transaction chính xác cần xác minh trên tài liệu khi viết EA).
- Kết nối lại: EA gửi snapshot vị thế đang mở. Heartbeat mỗi 1 giây; mất nhịp thì HUD hiện "MT5 OFFLINE" thay vì đứng hình.
- EA chỉ gửi, không chờ game trả lời (game lag không làm EA treo). Cần kiểm timeout của `SocketSend`.

**Vị trí MT5 — chưa chốt:**
- Hiện MT5 (và EA trade) chạy trên **VPS**. Bro nói có thể dùng MT5 trên Mac mini thay thế.
- **[ĐỀ XUẤT] Hướng Mac:** cài MT5 trên Mac mini (trình cài chính thức của MetaQuotes chạy qua Wine, ghi hỗ trợ Apple Silicon), đăng nhập cùng tài khoản bằng **investor password (chỉ xem)**; **chỉ chạy EA bridge ở đó, tuyệt đối không chạy EA trade (OngMat) trên terminal Mac** để tránh vào lệnh trùng. Game và bridge không thể đặt lệnh dù có lỗi. Lệnh vẫn bấm trên MT5 điện thoại / VPS. Terminal Mac sập thì game báo OFFLINE, giao dịch thật không ảnh hưởng.
- **Dự phòng:** Windows VPS có RDP, đẩy dữ liệu về Mac qua kết nối mã hóa. Delay phụ thuộc vị trí VPS nhưng buffer đồng bộ vẫn xử lý được.
- Loại **MQL5 VPS (MetaQuotes Virtual Hosting)** khỏi phương án bridge: cấm DLL, không có RDP/desktop, trang quy định không nói gì về socket.

**[CHƯA KIỂM CHỨNG] — phải test thật:**
1. Socket từ MT5 (Wine) sang Godot bản macOS native.
2. `SocketConnect` cần thêm địa chỉ vào danh sách cho phép ở Tools > Options > EA Trading (tài liệu có ghi, diễn đàn chỉ gợi ý chung chung).
3. Đăng nhập investor có nhận được `OnTradeTransaction` không. Nếu không → đọc danh sách vị thế + lịch sử deal theo chu kỳ ngắn.
4. Chính sách Exness khi cùng một tài khoản đăng nhập nhiều terminal đồng thời.

**Bài test đầu tiên (~10 phút):** EA gửi "ping" kèm timestamp, Godot in ra, đo vòng đi–về. Đạt khi trễ ổn định dưới ~10ms và chạy 10 phút liền không rớt.

---

## 5. Câu hỏi còn mở (cần Bro trả lời, hỏi từng câu một)

1. **Mac hay VPS** cho terminal lấy dữ liệu? (Claude đã đề xuất Mac + investor, chưa nhận xác nhận.)
2. **Móc trôi theo floating P/L** có hợp ý không?
3. **Điểm dừng theo rủi ro** (lỗ tối đa / số lệnh tối đa mỗi phiên): lấy cái nào, hay không dùng?
4. **Một "lượt đào" = một vị thế hay một chuỗi lệnh (rổ)?** Nếu có lúc nhiều vị thế mở cùng lúc thì hợp đồng sự kiện phải định nghĩa rõ.
5. Session P/L: realized hay gồm floating, có tính commission/swap không?
6. Phiên bản Godot đang cài?
7. Nền tảng live định dùng trước (YouTube test hay TikTok luôn) và đã có stream key chưa?
8. Đã bấm "Chọn khái niệm này" trên SpriteCook chưa, và đã kiểm xuất PNG nền trong suốt + kích thước pixel chưa?
9. Mức độ riêng tư HUD: thấp / vừa (đề xuất ban đầu: ẩn balance/equity/lot) / cao.

---

## 6. Việc tiếp theo (thứ tự đề xuất)

1. **Chốt hợp đồng sự kiện** (tên, dữ liệu kèm theo, thứ tự, xử lý mất gói) dựa trên mục 3 và các câu hỏi 2–5.
2. **Phase 1 — Godot prototype dữ liệu giả:** màn 9:16, HUD, móc/dây, vật phẩm placeholder, tầng đất, và **bảng giả lập sự kiện** (nút: mở lệnh / đóng lời / đóng lỗ / gift / like). Chưa nối MT5. Cách kiểm: bấm từng nút ra đúng animation, tắt/mở "MT5" giả lập thấy OFFLINE/online đúng.
3. **Test ping EA ↔ Godot** (mục 4) trên demo, đo độ trễ thật.
4. **Art:** hoàn tất test SpriteCook (3 prompt ở mục 2.5), kiểm license, xuất PNG; Bro kéo sprite vào Godot, gửi ảnh chụp để chỉnh.
5. **Phase 2 — EA bridge thật** (demo): tick, mở/đóng vị thế, snapshot, heartbeat, reconnect.
6. **Phase 3 — nối gameplay:** móc theo floating P/L, đóng lệnh theo xác nhận, KPI/level, Layer B.
7. **Phase 4 — layout livestream:** ghép OBS (game + MT5 điện thoại + camera), kiểm privacy mask và thông báo hệ thống, test độc lập đọc được trên điện thoại, xác nhận đường phát.
8. **Phase 5 — ổn định:** chạy nhiều phiên demo, đo độ trễ, test crash/reconnect/restart. Chỉ cân nhắc real account sau khi xong, và game vẫn không bao giờ gửi lệnh.

---

## 7. Nguồn đã dùng

- TikTok Live Studio / yêu cầu stream key: https://blog.eklipse.gg/beginner-guide-2/tiktok-live-studio-setup-guide.html , https://blog.tikfinity.com/?p=3719 , https://blog.tikfinity.com/?p=7010
- SpriteCook: https://www.spritecook.ai/game-sprite-generator , https://www.capterra.com/p/10040240/SpriteCook/ , https://www.spritecook.ai/compare/pixellab (trang so sánh do chính vendor viết)
- Cài MT5 trên Mac (Wine): https://www.metatrader5.com/en/terminal/help/start_advanced/install_mac
- `SocketConnect` (MQL5): https://www.mql5.com/zh/docs/network/socketconnect
- Quy định MetaTrader VPS: https://www.mql5.com/en/vps/rules ; blog nhà cung cấp VPS (cần đối chiếu): https://newyorkcityservers.com/blog/mql5-vps-vs-windows-vps
- Godot `WebSocketPeer` (đã quyết định không dùng): https://docs.godotengine.org/en/4.3/classes/class_websocketpeer.html
- GameMaker: https://gamemaker.io/get ; Construct vs GDevelop: https://app.cinevva.com/guides/construct-vs-gdevelop
