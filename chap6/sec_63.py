import math
# p1,p2を1:2に内分するs
# p1,p2を2:1に内分するt
# sを中心にtを反時計回りに60°回転させて得られる点u

def koch(n,p1,p2):
    if n == 0:
        return

    sx = (p1[0] * 2 + p2[0] * 1) / 3
    sy = (p1[1] * 2 + p2[1] * 1) / 3
    s = [sx, sy]

    tx = (p1[0] * 1 + p2[0] * 2) / 3
    ty = (p1[1] * 1 + p2[1] * 2) / 3
    t = [tx, ty]

    cos_60 = math.cos(math.radians(60))
    sin_60 = math.sin(math.radians(60))

    ux = (tx - sx) * cos_60 - (ty - sy) * sin_60 + sx
    uy = (tx - sx) * sin_60 + (ty - sy) * cos_60 + sy
    u = [ux, uy]

    koch(n-1, p1, s)
    print('{:.8f} {:.8f}'.format(s[0],s[1]))
    koch(n-1, s, u)
    print('{:.8f} {:.8f}'.format(u[0],u[1]))
    koch(n-1, u, t)
    print('{:.8f} {:.8f}'.format(t[0],t[1]))
    koch(n-1, t, p2)

n = int(input())
p1 = [0,0]
p2 = [100,0]

print('{:.8f} {:.8f}'.format(p1[0],p1[1]))
koch(n,p1,p2)
print('{:.8f} {:.8f}'.format(p2[0],p2[1]))
