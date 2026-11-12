"""Cắt sprite sheet thành từng frame riêng theo vùng pixel liền nhau.

Dùng: python3 tools/cut_sprites.py <file_sheet> <tiền_tố> <thư_mục_ra> [khoảng_cách] [số_hàng]
- Tìm các dải hàng có pixel, rồi trong từng dải tìm các cột có pixel tách nhau.
- Mỗi frame được căn đáy giữa trong canvas cùng kích thước để animation không nhảy.
- Khoảng_cách (mặc định 3 px) là khe trống tối thiểu để tách hai frame.
"""
import os
import sys

import numpy as np
from PIL import Image


def runs(mask, gap=1):
    out, s, last = [], None, None
    for i, v in enumerate(mask):
        if v:
            if s is None:
                s = i
            elif i - last > gap:
                out.append((s, last + 1))
                s = i
            last = i
    if s is not None:
        out.append((s, last + 1))
    return out


def cut(src, prefix, outdir, gap=3, rows=0):
    im = Image.open(src).convert("RGBA")
    alpha = np.array(im)[:, :, 3] > 20
    H = alpha.shape[0]
    if rows:
        # Hàng không có khe trống: chia đều theo số hàng.
        bands = [(round(i * H / rows), round((i + 1) * H / rows)) for i in range(rows)]
    else:
        bands = runs(alpha.any(axis=1), gap=1)
    frames = []
    for y0, y1 in bands:
        for x0, x1 in runs(alpha[y0:y1].any(axis=0), gap=gap):
            sub = alpha[y0:y1, x0:x1]
            ys = np.where(sub.any(axis=1))[0]
            xs = np.where(sub.any(axis=0))[0]
            frames.append(im.crop((x0 + xs[0], y0 + ys[0], x0 + xs[-1] + 1, y0 + ys[-1] + 1)))
    if not frames:
        print(f"{prefix}: không tìm thấy pixel")
        return
    W2 = max(f.width for f in frames)
    H2 = max(f.height for f in frames)
    os.makedirs(outdir, exist_ok=True)
    for i, f in enumerate(frames):
        canvas = Image.new("RGBA", (W2, H2), (0, 0, 0, 0))
        canvas.paste(f, ((W2 - f.width) // 2, H2 - f.height))
        canvas.save(os.path.join(outdir, f"{prefix}_{i:02d}.png"))
    print(f"{prefix}: {len(frames)} frame, khung {W2}x{H2}")


if __name__ == "__main__":
    args = sys.argv[1:]
    gap = int(args[3]) if len(args) > 3 else 3
    rows = int(args[4]) if len(args) > 4 else 0
    cut(args[0], args[1], args[2], gap, rows)
