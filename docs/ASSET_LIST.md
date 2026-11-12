# ASSET LIST v1 — Gold Miner Live

Tham chiếu art: ảnh diorama Bro chọn (mặt cắt hầm mỏ nhiều tầng, rừng teal sương mù, cây thân trắng, rêu phủ đất gạch nâu, hang đá xám tối, lò lửa cam, đống vàng, nấm đỏ, nhân vật chibi đầu to).

## Thông số kỹ thuật đề xuất
- Độ phân giải gốc của game: 360×640, phóng ×3 lên 1080×1920 (9:16), giữ pixel sắc (nearest).
- Tile 32×32. Nhân vật cao khoảng 48px. Vật phẩm 32×32. Máy đào khoảng 64×64.
- Mọi sprite: PNG nền trong suốt, sprite sheet ngang, các frame cùng kích thước, nhân vật đứng giữa frame.

Ký hiệu ưu tiên: **P1** cần cho Giai đoạn 1 · **P2** thêm sau.

## A. Bối cảnh (tách lớp để làm parallax và chuyển động)
| # | Asset | Animation | Ưu tiên |
|---|---|---|---|
| A1 | Bầu trời hoàng hôn teal (gradient) | tĩnh, game tự đổi màu theo giờ | P1 |
| A2 | Lớp rừng xa (bóng cây mờ) | tĩnh, trôi parallax chậm | P1 |
| A3 | Lớp rừng giữa | tĩnh | P1 |
| A4 | Cây thân trắng lớn, tán tách riêng | tán lay gió 4 frame | P1 |
| A5 | Bụi cây, dương xỉ, cỏ (3–4 cụm) | lay gió 4 frame | P1 |
| A6 | Dây leo / rêu rủ xuống mép đất | đung đưa 4 frame | P1 |
| A7 | Nấm đỏ, hộp gỗ, thùng, chum đất | tĩnh | P1 |
| A8 | Dải sương mù | tĩnh, game cho trôi | P1 |
| A9 | Hạt mưa, vệt nước bắn | 3 frame | P2 |

## B. Địa hình và hầm
| # | Asset | Animation | Ưu tiên |
|---|---|---|---|
| B1 | Mép cỏ rêu trên cùng (tile lặp ngang) | tĩnh | P1 |
| B2 | 4 tầng đất: đất gạch nâu, đất sét đỏ, đá xám xanh, đá tím pha lê (tile lặp 2 chiều) | tĩnh | P1 |
| B3 | Tường hang tối phía sau | tĩnh | P1 |
| B4 | Thang gỗ, cột chống hầm, sàn gỗ | tĩnh | P2 |
| B5 | Đèn lồng treo tường | lửa nhấp nháy 4 frame | P1 |
| B6 | Lò luyện có lửa cam (như ảnh tham chiếu) | lửa 4 frame | P2 |
| B7 | Đống vàng nhỏ trang trí | lấp lánh 4 frame | P2 |
| B8 | Pha lê tím trong đá | phát sáng 4 frame | P2 |

## C. Nhân vật
| # | Asset | Animation | Ưu tiên |
|---|---|---|---|
| C1 | Thợ đào chính (mũ đỏ có đèn, yếm xanh) | idle thở 4, chớp mắt 2, quay tay 6, kéo cần gạt 4, vui 4, buồn 4 | P1 |
| C2 | Bạn đồng hành (khung nhân vật cơ bản, 4 màu) | idle 4, vẫy tay 4 | P1 |
| C3 | Bạn nữ tóc dài | đi 6, đứng 2 | P1 |
| C4 | Người dắt chó + chó | người đi 6, chó chạy 4, vẫy đuôi 2 | P1 |
| C5 | Anh mặc vest xách cặp | đi 6, đứng 2 | P1 |
| C6 | Cụ già chống gậy | đi 6, đứng 2 | P2 |
| C7 | Học sinh đeo balo | đi 6, đứng 2 | P2 |
| C8 | Chim | vỗ cánh 4 | P1 |
| C9 | Thỏ hoặc sóc chạy qua | chạy 4 | P2 |

## D. Máy đào (skin 4 cấp)
| # | Asset | Animation | Ưu tiên |
|---|---|---|---|
| D1 | Tời gỗ quay tay | tay quay + trống 4 | P1 |
| D2 | Tời sắt bánh răng | bánh răng 4 | P2 |
| D3 | Máy hơi nước | piston + bánh đà 6, lửa lò 3 | P2 |
| D4 | Lõi hổ phách | lõi phát sáng 6 | P2 |

## E. Dây và móc
| # | Asset | Animation | Ưu tiên |
|---|---|---|---|
| E1 | Dây thừng (tile dọc) | tĩnh | P1 |
| E2 | Cáp thép, xích sắt, xích vàng (tile dọc) | xích vàng lấp lánh 4 | P2 |
| E3 | Móc / gàu múc | mở, đóng 2 | P1 |
| E4 | Ròng rọc trên ray | quay 4 | P1 |

## F. Vật phẩm và phần thưởng
| # | Asset | Animation | Ưu tiên |
|---|---|---|---|
| F1 | Vàng cục | lấp lánh 4 | P1 |
| F2 | Thanh vàng | lấp lánh 4 | P1 |
| F3 | Kim cương | lấp lánh 4 | P1 |
| F4 | Đá | tĩnh | P1 |
| F5 | Giày cũ | tĩnh | P1 |
| F6 | Bom | ngòi cháy 4 | P1 |
| F7 | Túi bí ẩn | lắc 4 | P1 |
| F8 | Rương kết quả | đóng, rung, mở 6 | P1 |

## G. Hiệu ứng (FX)
| # | Asset | Animation | Ưu tiên |
|---|---|---|---|
| G1 | Bụi đất bốc lên | 5 | P1 |
| G2 | Lấp lánh / sao | 4 | P1 |
| G3 | Nổ bom | 6–8 | P1 |
| G4 | Đá rơi sập hầm | 6 | P1 |
| G5 | Khói | 5 | P2 |
| G6 | Mưa vàng / đồng xu bung | 6 | P2 |
| G7 | Đom đóm | 2 | P1 |

## H. Giao diện (UI)
| # | Asset | Ghi chú | Ưu tiên |
|---|---|---|---|
| H1 | Khung panel 9-slice (gỗ + đá) | dùng cho HUD, chat, bảng xếp hạng | P1 |
| H2 | Bảng tên trên đầu 9-slice | top 5 đi lại | P1 |
| H3 | Icon: độ sâu, kỷ lục, đồng hồ, MT5 online/offline, R | 16×16 | P1 |
| H4 | Nút bấm (thường, nhấn) | màn chọn nhân vật | P1 |
| H5 | Thanh tiến độ (hầm chung, áp lực hầm) | | P1 |

Font chữ không làm bằng SpriteCook. Dùng font pixel có hỗ trợ tiếng Việt đầy đủ dấu (cần kiểm license).

## Animation tạo cảm giác "sống"
Xếp theo hiệu quả trên công sức:
1. Thợ đào thở và chớp mắt (luôn chạy).
2. Tán cây, cỏ, dây leo lay gió.
3. Đom đóm, sương trôi, đèn lồng nhấp nháy.
4. Chim bay qua, người đi lại có tên.
5. Máy đào chạy khi thả và kéo dây.
6. Khoảnh khắc khui: lấp lánh, rương mở, bom nổ, hầm sập.
7. Thời tiết và giờ trong ngày (game tự xử lý bằng màu, không cần thêm sprite trừ mưa).
