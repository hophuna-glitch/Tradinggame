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

## SpriteCook Full Pack (51) — prompt ô "describe your own style"
Thể loại chọn sẵn: Platformer + Metroidvania (đều là side view, hợp game).

**Bản ngắn (nếu ô giới hạn ký tự):**
Cozy hi-bit 16-bit pixel art, side-view cross-section of a mossy underground gold mine, misty teal twilight forest with white-trunk trees, brown brick earth draped in bright moss, dark slate caves, warm amber glow only on gold, lanterns and furnaces, chibi miners with big heads, soft dark outlines, quiet moody palette

**Bản đầy đủ:**
Hi-bit 16-bit pixel art for a side-view gold mining game, shown as a cross-section diorama of a mine under a forest. Misty desaturated teal twilight sky, layered silhouette forest, tall white-trunk trees with round mossy-green canopies. Thick bright moss and hanging vines draped over warm brown brick-textured earth; below it red-brown clay, dark slate stone caves with cool blue-grey highlights, and deep violet crystal rock. Warm amber and orange used only for gold, lanterns and furnace fire. Chibi characters about two heads tall with big heads, simple dot eyes, readable silhouettes. Clean hand-placed pixels, soft selective dark outlines, flat orthographic side view, no perspective. 32x32 tiles, characters about 48px tall, transparent backgrounds, no text. Quiet, cozy, moody, restrained.

# BỔ SUNG v2 — cuộn dây, animation nhân vật chính, lỗ dây (theo mockup cuộn dây kiểu Gold Miner)

Quy ước kích thước: nhân vật chính cao khoảng 80px trong sheet SpriteCook. Cuộn dây cao khoảng 40–45px (≈ nửa nhân vật), máy cấp 3–4 cao tối đa 70px.

## A. Máy cuộn dây 4 cấp (tạo ảnh tĩnh trước, rồi dùng Animate)
Style anchor: `Hi-bit pixel art, clean hand-placed pixels, flat side-view orthographic, chunky dark outline, misty teal twilight palette, warm amber only for lights, transparent background, no text.`

**Cấp 1 — Thường (khung gỗ, tay quay):**
```
[Style anchor] Classic gold-mining cable reel: a wooden spool wound with thick black cable, mounted between two wooden flanges on a small wooden A-frame stand, an iron-tipped wooden hand crank on the left side, mossy base, weathered, about 45px tall. Animation 6 frames: the crank makes one full turn, the spool rotates with it, a light mark moves across the wound cable.
```
**Cấp 2 — Tốt (khung sắt, bánh răng):**
```
[Style anchor] Iron gold-mining cable reel on a riveted steel A-frame, steel cable wound on the spool, a large spoked gear on the right meshing with a small pinion gear and crank on the left, cool blue-grey metal with pale highlights, about 45px tall. Animation 6 frames: crank turns, pinion and big gear rotate in opposite directions, spool turns slowly.
```
**Cấp 3 — Hiếm (máy hơi nước):**
```
[Style anchor] Small steam-powered mining winch: a copper boiler with brass bands and a short chimney on the right, a steel cable spool on a dark iron frame on the left, a piston rod driving a spoked flywheel, firebox window glowing amber, about 60px tall. Animation 6 frames: piston stroke, flywheel rotates, spool turns, firebox flickers. Separate 5-frame smoke puff sprite on transparent background.
```
**Cấp 4 — Xịn (lõi hổ phách):**
```
[Style anchor] Refined dark-slate mining winch with brass trim: a spool wound with polished gold chain on a slim frame, beside it a rectangular engine with a round amber crystal core glowing softly in the centre, three small orbiting light motes, slim brass antenna with a tiny lamp, restrained and elegant, no neon, about 60px tall. Animation 6 frames: core pulses, motes orbit, spool turns steadily, antenna lamp blinks.
```

## B. Animation cúi xoay tay quay cho 5 nhân vật chính (dùng Animate của SpriteCook)
Nhân vật: thợ đào, học sinh, ông cụ, chú bụng bự, cô gái.
```
Animate this character turning a hand crank, 6-frame loop. Body leans forward from the hips toward the right, head tilted down, both hands out in front at waist height gripping an invisible crank handle, arms moving in a circle one full turn across the loop. Feet stay fixed on the ground. Keep identical head size, outline weight and colours in every frame, same frame size, transparent background.
```
Lưu ý: tay cầm tay quay vô hình vì cuộn dây là sprite riêng, game ghép chúng lại.

## C. Animation vui và buồn cho 5 nhân vật chính (4 frame mỗi loại)
```
Animate this character cheering, 4-frame loop: both arms thrown up, a small hop upward 2px, then landing. Keep head size, outline and colours identical, same frame size.
```
```
Animate this character disappointed, 4-frame loop: shoulders drop, head tilts down, one slow shake of the head. Keep head size, outline and colours identical, same frame size.
```

## D. Dây (tile lặp dọc, 4 loại, mỗi loại có màu cho hai chiều lệnh)
```
[Style anchor] Seamless vertical tile, narrow strip about 10px wide, repeating top to bottom: (1) twisted hemp rope, warm brown; (2) braided steel cable, pale grey with small glints; (3) iron chain, alternating front and side links; (4) polished gold chain with faint amber glow. Each type also as a cool teal-tinted variant.
```

## E. Lỗ chui dây trên mặt đất (4 loại, thay thanh ray cũ)
```
[Style anchor] Small hole in the ground seen from the side where a rope enters the earth, about 28px wide: a dark opening with a rim ring and a few small pebbles and moss, four versions by material: (1) rough wooden collar, (2) riveted steel ring, (3) stone ring, (4) brass ring with a gold inlay. Transparent background.
```

## B v2 — Animate xoay tay quay, tay đi đúng vòng tròn của máy (thay bản B cũ)
Hình học (khớp mockup): nhân vật đứng bên TRÁI cuộn dây, quay mặt sang PHẢI. Trục tay quay nằm trước bụng nhân vật, ngang thắt lưng. Tay quay xoay THEO CHIỀU KIM ĐỒNG HỒ (nhìn từ phía người xem), 8 frame, mỗi frame 45°. Game đồng bộ frame theo góc quay của máy, nên frame 1 phải là tay ở vị trí 12 giờ.

| Frame | Vị trí tay (đồng hồ) | Thân người |
|---|---|---|
| 1 | 12 giờ, cao nhất | thẳng, nhô lên 1px |
| 2 | 1 giờ 30 | nghiêng tới nhẹ |
| 3 | 3 giờ, xa nhất | nghiêng tới nhiều nhất, tay duỗi |
| 4 | 4 giờ 30 | nghiêng tới, bắt đầu hạ |
| 5 | 6 giờ, thấp nhất | cúi thấp nhất, hạ 2px |
| 6 | 7 giờ 30 | bắt đầu ngả về |
| 7 | 9 giờ, gần người nhất | ngả về, khuỷu gập |
| 8 | 10 giờ 30 | đứng lên lại |

**Bản A (đề xuất): vẽ luôn tay quay trong animation** để tay và tay quay khớp tuyệt đối. Máy cuộn dây sẽ xuất bản không có tay quay.
```
Animate this character turning a hand crank, side view facing right, 8-frame loop, 45 degrees per frame, clockwise as seen by the viewer. Draw the crank as part of the animation: a fixed axle point in front of the character's belly at waist height, a short dark iron crank arm about one third of the head width long, and a small wooden handle at its end. Both hands grip the wooden handle in every frame and follow it exactly around the circle. Frame 1: handle at 12 o'clock (top), body upright, raised 1px. Frame 2: handle at 1:30, body leans forward slightly. Frame 3: handle at 3 o'clock (farthest from the body), arms fully extended, maximum forward lean. Frame 4: handle at 4:30, still leaning forward, starting to lower. Frame 5: handle at 6 o'clock (bottom), deepest crouch, body lowered 2px, knees bent. Frame 6: handle at 7:30, body starts to pull back. Frame 7: handle at 9 o'clock (closest to the body), elbows bent, body leaning back slightly. Frame 8: handle at 10:30, rising back toward frame 1. The axle point stays at exactly the same pixel position in all 8 frames. Feet stay planted at the same pixels in all frames. Same head size, same face (simple vertical black oval eyes, no eyebrows), same outline and colours, same frame size, transparent background.
```

**Bản B: tay quay vô hình** (máy giữ tay quay riêng, khó khớp hơn):
```
Animate this character turning an invisible hand crank, side view facing right, 8-frame loop, 45 degrees per frame, clockwise as seen by the viewer. Both hands are closed together around one invisible handle and trace a perfect circle in front of the belly at waist height, radius about one third of the head width, centred on a fixed point that never moves. Frame 1: hands at 12 o'clock, body upright, raised 1px. Frame 2: 1:30, slight forward lean. Frame 3: 3 o'clock, arms fully extended, maximum forward lean. Frame 4: 4:30, starting to lower. Frame 5: 6 o'clock, deepest crouch, body lowered 2px. Frame 6: 7:30, pulling back. Frame 7: 9 o'clock, elbows bent close to the body. Frame 8: 10:30, rising back. Hands are not fists and never punch forward; the motion is a smooth circle. Feet planted at the same pixels in all frames. Same head size, same face (simple vertical black oval eyes, no eyebrows), same outline and colours, same frame size, transparent background.
```
Kiểm tra sau khi tạo: xếp 8 frame chồng lên nhau, vị trí tay phải vẽ thành một vòng tròn đều; trục (bản A) và bàn chân không được xê dịch pixel nào.
