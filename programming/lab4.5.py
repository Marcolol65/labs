def move(n, x, y):
    stack = [(1, n, x, y)]
    while stack:
        phase, disks, src, dst = stack.pop()
        if phase == 1:
            if disks == 1:
                print(f"Move disk from rod {src} to rod {dst}")
            else:
                stack.append((3, disks-1, 6-src-dst, dst))
                stack.append((1, 1, src, dst))
                stack.append((2, disks-1, src, dst))
        elif phase == 2:
            print(f"Move disk from rod {src} to rod {dst}")
        elif phase == 3:
            stack.append((1, disks-1, src, 6-src-dst))
            stack.append((1, 1, src, dst))
            stack.append((2, disks-1, 6-src-dst, dst))

move(3, 1, 3)