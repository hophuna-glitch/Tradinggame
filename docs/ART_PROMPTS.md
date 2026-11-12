# ART PROMPTS — máy đào, dây, sinh vật nền

Dán **Style anchor** (xem `docs/HANDOFF.md` mục 2.5) lên đầu mỗi prompt. Mỗi sprite xuất PNG nền trong suốt, cùng cỡ pixel với thợ đào.

## Máy đào (skin theo 4 cấp)
Yêu cầu chung: side view, đặt trên mặt đất bên phải thợ đào, rộng khoảng 1.2–1.5 lần thợ đào, có trống cuốn dây nhìn thấy rõ. Mỗi máy cần 4–6 frame vòng lặp và tách riêng phần chuyển động nếu công cụ cho phép.

1. **Thường — Tời gỗ quay tay:** `[Style anchor]` Hand-cranked wooden mine windlass, two rough timber A-frame posts, a rope-wrapped wooden drum between them, iron crank handle on the left side, worn planks, moss on the base. 4-frame loop: crank handle rotating one full turn, drum turning.
2. **Tốt — Tời sắt bánh răng:** `[Style anchor]` Cast-iron geared mine winch, one large spoked gear meshing with a small pinion, riveted base plate, steel cable drum, crank wheel with handle, cool blue-grey metal with pale highlights. 4-frame loop: gears turning in opposite directions.
3. **Hiếm — Máy hơi nước:** `[Style anchor]` Small steam-powered mine hoist, copper boiler with brass bands, short chimney, firebox window glowing amber, piston rod driving a spoked flywheel, chain drum. 6-frame loop: piston stroke, flywheel turning, firebox flicker. Smoke puffs as a separate sprite.
4. **Xịn — Lõi hổ phách:** `[Style anchor]` Refined dark slate mining engine with brass trim, a round amber crystal core glowing softly in the centre, three small orbiting light motes, slim brass antenna with a tiny lamp, restrained and elegant, no neon. 6-frame loop: core pulsing, motes orbiting.

## Dây (tile lặp dọc, 4 loại, mỗi loại 2 màu cho hai chiều lệnh)
`[Style anchor]` Seamless vertical tile, narrow strip, tiles top-to-bottom: (1) twisted hemp rope, warm brown; (2) braided steel cable, pale grey with glints; (3) iron chain, alternating front and side links; (4) polished gold chain with faint amber glow. Provide a cool teal-tinted variant of each.

## Thợ đào (animation theo máy)
- Máy cấp 1–2: thợ đào quay tay, 4–6 frame (`turning a crank with both hands, body leaning with each turn`).
- Máy cấp 3–4: thợ đào đứng vận hành cần gạt, 4 frame (`pulling a lever, then idle watching the machine`).
- Chung: idle 4 frame, vui khi lời 4 frame, thất vọng khi lỗ 4 frame.

## Sinh vật nền
- **Chim:** `[Style anchor]` Small dark bird silhouette, side view, 4-frame wing flap loop, very small sprite.
- **Người đi lại (top 5 người đoán):** `[Style anchor]` Townsperson walking, side view, chibi proportions matching the miner but about 70% of his height, 6-frame walk cycle plus 2-frame idle, muted colours so they sit behind the miner. Mỗi người một sprite sheet riêng: (1) young woman with long hair and a dress; (2) person in a hoodie walking a small dog on a leash, dog has its own 4-frame trot; (3) man in a dark suit carrying a briefcase; (4) old man with a hat and a walking cane; (5) student with a backpack. Thêm biến thể sau: người gánh hàng, thợ mỏ xách đèn.

## Tiêu chí chấm
- Bốn máy đặt cạnh nhau phải thấy rõ thứ bậc từ thô sơ đến tinh xảo, nhưng cùng một thế giới.
- Thu nhỏ còn khoảng 64px vẫn nhận ra máy nào.
- Màu ấm (amber) chỉ dùng cho vàng, lửa và lõi máy cấp cao.
