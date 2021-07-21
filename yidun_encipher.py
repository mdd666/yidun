# -*- encoding: utf-8 -*-
import math
import random
from urllib import parse
import ctypes


def int_overflow(val):
    '实现js大数溢出效果'
    # 这个函数可以得到32位int溢出结果，因为python的int一旦超过宽度就会自动转为long，永远不会溢出，有的结果却需要溢出的int作为参数继续参与运算
    maxint = 2147483647
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shift(n, i):
    '实现js逻辑右移(无符号右移) >>>'
    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)


T = [0, 1996959894, 3993919788, 2567524794, 124634137, 1886057615, 3915621685, 2657392035, 249268274, 2044508324,
     3772115230, 2547177864, 162941995, 2125561021, 3887607047, 2428444049, 498536548, 1789927666, 4089016648,
     2227061214, 450548861, 1843258603, 4107580753, 2211677639, 325883990, 1684777152, 4251122042, 2321926636,
     335633487, 1661365465, 4195302755, 2366115317, 997073096, 1281953886, 3579855332, 2724688242, 1006888145,
     1258607687, 3524101629, 2768942443, 901097722, 1119000684, 3686517206, 2898065728, 853044451, 1172266101,
     3705015759, 2882616665, 651767980, 1373503546, 3369554304, 3218104598, 565507253, 1454621731, 3485111705,
     3099436303, 671266974, 1594198024, 3322730930, 2970347812, 795835527, 1483230225, 3244367275, 3060149565,
     1994146192, 31158534, 2563907772, 4023717930, 1907459465, 112637215, 2680153253, 3904427059, 2013776290,
     251722036, 2517215374, 3775830040, 2137656763, 141376813, 2439277719, 3865271297, 1802195444, 476864866,
     2238001368, 4066508878, 1812370925, 453092731, 2181625025, 4111451223, 1706088902, 314042704, 2344532202,
     4240017532, 1658658271, 366619977, 2362670323, 4224994405, 1303535960, 984961486, 2747007092, 3569037538,
     1256170817, 1037604311, 2765210733, 3554079995, 1131014506, 879679996, 2909243462, 3663771856, 1141124467,
     855842277, 2852801631, 3708648649, 1342533948, 654459306, 3188396048, 3373015174, 1466479909, 544179635,
     3110523913, 3462522015, 1591671054, 702138776, 2966460450, 3352799412, 1504918807, 783551873, 3082640443,
     3233442989, 3988292384, 2596254646, 62317068, 1957810842, 3939845945, 2647816111, 81470997, 1943803523,
     3814918930, 2489596804, 225274430, 2053790376, 3826175755, 2466906013, 167816743, 2097651377, 4027552580,
     2265490386, 503444072, 1762050814, 4150417245, 2154129355, 426522225, 1852507879, 4275313526, 2312317920,
     282753626, 1742555852, 4189708143, 2394877945, 397917763, 1622183637, 3604390888, 2714866558, 953729732,
     1340076626, 3518719985, 2797360999, 1068828381, 1219638859, 3624741850, 2936675148, 906185462, 1090812512,
     3747672003, 2825379669, 829329135, 1181335161, 3412177804, 3160834842, 628085408, 1382605366, 3423369109,
     3138078467, 570562233, 1426400815, 3317316542, 2998733608, 733239954, 1555261956, 3268935591, 3050360625,
     752459403, 1541320221, 2607071920, 3965973030, 1969922972, 40735498, 2617837225, 3943577151, 1913087877,
     83908371, 2512341634, 3803740692, 2075208622, 213261112, 2463272603, 3855990285, 2094854071, 198958881,
     2262029012, 4057260610, 1759359992, 534414190, 2176718541, 4139329115, 1873836001, 414664567, 2282248934,
     4279200368, 1711684554, 285281116, 2405801727, 4167216745, 1634467795, 376229701, 2685067896, 3608007406,
     1308918612, 956543938, 2808555105, 3495958263, 1231636301, 1047427035, 2932959818, 3654703836, 1088359270,
     936918e3, 2847714899, 3736837829, 1202900863, 817233897, 3183342108, 3401237130, 1404277552, 615818150,
     3134207493, 3453421203, 1423857449, 601450431, 3009837614, 3294710456, 1567103746, 711928724, 3020668471,
     3272380065, 1510334235, 755167117]
E = [120, 85, -95, -84, 122, 38, -16, -53, -11, 16, 55, 3, 125, -29, 32, -128, -94, 77, 15, 106, -88, -100, -34, 88, 78,
     105, -104, -90, -70, 90, -119, -28, -19, -47, -111, 117, -105, -62, -35, 2, -14, -32, 114, 23, -21, 25, -7, -92,
     96, -103, 126, 112, -113, -65, -109, -44, 47, 48, 86, 75, 62, -26, 72, -56, -27, 66, -42, 63, 14, 92, 59, -101, 19,
     -33, 12, -18, -126, -50, -67, 42, 7, -60, -81, -93, -86, 40, -69, -37, 98, -63, -59, 108, 46, -45, 93, 102, 65,
     -79, 73, -23, -46, 37, -114, -15, 44, -54, 99, -10, 60, -96, 76, 26, 61, -107, 18, -116, -55, -40, 57, -76, -82,
     45, 0, -112, -77, 29, 43, -30, 109, -91, -83, 107, 101, 81, -52, -71, 84, 36, -41, 68, 39, -75, -122, -6, 11, -80,
     -17, -74, -73, 35, 49, -49, -127, 80, 103, 79, -25, 52, -43, 56, 41, -61, -24, 17, -118, 115, -38, 8, -78, 33, -85,
     -106, 58, -98, -108, 94, 116, -125, -51, -9, 71, 82, 87, -115, 9, 69, -123, 123, -117, 113, -22, -124, -87, 64, 13,
     21, -89, -2, -99, -97, 1, -4, 34, 20, 83, 119, 30, -12, -110, -66, 118, -48, 6, -36, 104, -58, -102, 97, 5, -20,
     31, -72, 70, -39, 67, -68, -57, 110, 89, 51, 10, -120, 28, 111, 127, 22, -3, 54, 53, -1, 100, 74, 50, 91, 27, -31,
     -5, -64, 124, -121, 24, -13, 95, 121, -8, 4]
s = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

random_toggle = True  #


def g() -> list:
    return ["i", "/", "x", "1", "X", "g", "U", "0", "z", "7", "k", "8", "N", "+", "l", "C", "p", "O", "n", "P", "r",
            "v", "6", "\\", "q", "u", "2", "G", "j", "9", "H", "R", "c", "w", "T", "Y", "Z", "4", "b", "f", "S", "J",
            "B", "h", "a", "W", "s", "t", "A", "e", "o", "M", "I", "E", "Q", "5", "m", "D", "d", "V", "F", "L", "K",
            "y"]


def b() -> str:
    return "3"


def m(e: list, t: int, i: int):
    a = g()
    s = b()
    l = []
    if i == 1:
        n = e[t]
        r = 0
        o = 0
        l.append(a[unsigned_right_shift(n, 2) & 63])
        l.append(a[(n << 4 & 48) + (unsigned_right_shift(r, 4) & 15)])
        l.append(s)
        l.append(s)
    elif i == 2:
        n = e[t]
        r = e[t + 1]
        o = 0
        l.append(a[unsigned_right_shift(n, 2) & 63])
        l.append(a[(n << 4 & 48) + (unsigned_right_shift(r, 4) & 15)])
        l.append(a[(r << 2 & 60) + (unsigned_right_shift(o, 6) & 3)])
        l.append(s)
    elif i == 3:
        n = e[t]
        r = e[t + 1]
        o = e[t + 2]
        l.append(a[unsigned_right_shift(n, 2) & 63])
        l.append(a[(n << 4 & 48) + (unsigned_right_shift(r, 4) & 15)])
        l.append(a[(r << 2 & 60) + (unsigned_right_shift(o, 6) & 3)])
        l.append(a[63 & o])
    else:
        raise RuntimeError("1010")
    return "".join(l)


def _(e: list) -> str:
    if len(e) == 0:
        return ""
    t = 3
    i = []
    n = 0
    while True:
        if n >= len(e):
            break
        if n + t > len(e):
            i.append(m(e, n, len(e) - n))
            break
        i.append(m(e, n, t))
        n += t
    return "".join(i)


def B(e: str):
    t = "14731382d816714fC59E47De5dA0C871D3F"
    i = e + k(e)
    n = c(i)
    r = c(t)
    o = L(n, r)
    return _(o)


def k(e: str):
    return S(c(e))


def f(e: str) -> list:
    if len(e) == 0:
        return []
    i = []
    r = 0
    for o in range(int(len(e) / 2)):
        a = int(e[r], 16) << 4
        r += 1
        s = int(e[r], 16)
        r += 1
        i.append(__toByte(a + s))
    return i


def c(e: str):
    i = []
    t = parse.quote(e, safe='', encoding=None, errors=None)
    r = 0
    while True:
        if r < len(t):
            if t[r] == "%":
                if r + 2 >= len(t):
                    raise RuntimeError("1009")
                i.append(f(f"{t[r + 1]}{t[r + 2]}")[0])
                r += 3
            else:
                i.append(ord(t[r]))
                r += 1
            continue
        break
    return i


def S(e: list):
    t = 4294967295
    for n in e:
        # t = t >>> 8 ^ T[255 & (t ^ n)]
        # js中位运算的数值范围为-2147483648~2147483647（带符号位的32位），t值需要做溢出处理，导致与Python中直接异或运算结果不同

        # execjs.eval方法实现
        # _ = T[execjs.eval(f"255 & ({t} ^ {n})")]
        # t = execjs.eval(f"{t} >>> 8 ^ {_}")
        t = unsigned_right_shift(t, 8) ^ int(int_overflow(T[255 & (int_overflow(t) ^ int_overflow(n))]))
    return d(int_overflow(4294967295) ^ t)


def d(e: int) -> str:
    t = j(e)
    return u(t)


def j(e: int) -> list:
    t = []
    t.append(unsigned_right_shift(e, 24) & 255)
    t.append(unsigned_right_shift(e, 16) & 255)
    t.append(unsigned_right_shift(e, 8) & 255)
    t.append(e & 255)
    return t


def u(e: list) -> str:
    i = []
    for n in e:
        i.append(l(n))
    return "".join(i)


def l(e: int) -> str:
    t = []
    t.append(s[unsigned_right_shift(e, 4) & 15])
    t.append(s[e & 15])
    return "".join(t)


def __toByte(e: int) -> list:
    if e < -128:
        return __toByte(128 - (-128 - e))
    elif (e >= -128 and e <= 127):
        return e
    else:
        return __toByte(-129 + e - 127)


def N() -> list:
    e = []
    for _ in range(4):
        if random_toggle is True:
            i = random.randint(0, 256)
        else:
            i = 135
        e.append(__toByte(i))
    return e


def h(e: list, t: int, i: int) -> list:
    n = []
    if len(e) == 0:
        return n
    if len(e) < i:
        raise RuntimeError("1003")
    for r in range(i):
        n.append(e[t + r])
    return n


def I(e: list) -> list:
    R: int = 4  # js中常量
    t = []
    if len(e) == 0:
        return y(R)
    if len(e) >= R:
        _ = h(e, 0, R)
        return _

    for i in range(R):
        t.append(e[i % len(e)])
    return t


def o(e: int, t: int) -> int:
    return __toByte(__toByte(e) ^ __toByte(t))


def a(e: list, t: list) -> list:
    if len(e) != len(t):
        return e
    i = []
    for r in range(len(e)):
        i.append(o(e[r], t[r]))
    return i


def p(e: list, t: int, i: list, n: int, r: int) -> list:
    if len(e) == 0:
        return i
    if len(e) < r:
        raise RuntimeError("1003")
    for o in range(r):
        if n + o < len(i):
            i[n + o] = e[t + o]
        else:
            i.append(e[t + o])
    return i


def X(e: list):
    C = 4
    O = 4
    if len(e) == 0:
        return y(4)
    t = len(e)
    i = 0
    i = C - t % C - O if (t % C <= C - O) else 2 * C - t % C - O
    n = []
    p(e, 0, n, 0, t)
    for r in range(i):
        # n[t + r] = 0
        n.append(0)
    o = j(t)
    p(o, 0, n, t + i, O)
    return n


def x(e: list) -> list:
    C = 4
    t = []
    i = 0
    n = len(e) / C
    r = 0
    while True:
        if r >= n:
            break
        # t[r] = []
        t.append([])
        for o in range(C):
            t[r].append(e[i])
            i += 1
        r += 1
    return t


def M(e: list, t: int) -> list:
    i = __toByte(t)
    n = []
    for a in range(len(e)):
        n.append(o(e[a], i))
    return n


def n(e: int, t: int) -> int:
    return __toByte(e + t)


def D(e: list, t: int) -> list:
    i = __toByte(t)
    r = []
    for a in range(len(e)):
        r.append(n(e[a], i))
    return r


def V(e: list):
    t = M(e, 56)
    i = D(t, -40)
    n = M(i, 103)
    return n


def r(e: list, t: list):
    if t is None:
        return e
    i = []
    for o in range(len(e)):
        i.append(n(e[o], t[o % len(t)]))
    return i


def A(e: int) -> int:
    t = unsigned_right_shift(e, 4) & 15
    i = 15 & e
    n = 16 * t + i
    return E[n]


def P(e: list) -> list:
    t = []
    for i in range(len(e)):
        t.append(A(e[i]))
    return t


def L(e: list, t: list):
    C = 4
    i = N()
    t = I(t)
    t = a(t, I(i))
    t = I(t)
    n = t
    o = X(e)
    s = x(o)
    l = []
    p(i, 0, l, 0, 4)  # 原始js代码中，常量$=4
    for f in range(len(s)):
        c = V(s[f])
        j = a(c, t)
        d = r(j, n)
        j = a(d, n)
        h = P(j)
        h = P(h)
        p(h, 0, l, f * C + 4, C)
        n = h
        # print(f, l)
    return l


def i(e, t) -> str:
    value1 = []
    for n in range(len(t)):
        temp1 = ord(t[n])
        temp2 = ord(e[math.floor(n % len(e))])
        value1.append(temp1 ^ temp2)
    return _(value1)

def get_uuid():
    i = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    a = []
    for _ in range(32):
        a.append(random.choice(i))
    return "".join(a)

if __name__ == '__main__':
    print(B(get_uuid()))
    print(i("6b21445e66be8cbf1ea785151cdca405", "1,0"))
