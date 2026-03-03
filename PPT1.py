import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(
    page_title="Python • NumPy • Pandas • Matplotlib – Code + Result",
    page_icon="🐍",
    layout="wide"
)

st.sidebar.title("Learning Lab")
section = st.sidebar.radio("Section", [
    "🏠 Home",
    "🐍 Basic Python – 20",
    "🔢 NumPy – 20",
    "📊 Pandas – 20",
    "📈 Matplotlib – 20"
])

# ────────────────────────────────────────────────
# HOME
# ────────────────────────────────────────────────
if section == "🏠 Home":
    st.title("🐍 Python – Code + Result Lab")
    st.markdown("""
Each concept shows:
• brief explanation
• **the exact code** being executed
• live result / output / visualization

Expand any block to explore.
""")

# ────────────────────────────────────────────────
# BASIC PYTHON – 20
# ────────────────────────────────────────────────
elif section == "🐍 Basic Python – 20":
    st.header("🐍 Basic Python – 20 Concepts")

    with st.expander("1. Variables & assignment"):
        a = st.slider("a", -10, 30, 7)
        b = st.slider("b", -10, 30, 4)
        st.code(f"""
a = {a}
b = {b}
result = a + b
print(result)
""")
        st.success(f"Result: **{a + b}**")

    with st.expander("2. Basic data types"):
        val = st.text_input("Enter value", "python42")
        st.code(f"""
value = "{val}"
print(type(value).__name__)
""")
        st.info(f"→ {type(val).__name__}")

    with st.expander("3. Arithmetic operators"):
        x = st.number_input("x", 1, 50, 12)
        y = st.number_input("y", 1, 50, 5)
        st.code(f"""
x = {x}
y = {y}
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** 2)
""")
        st.write(f"{x+y} {x-y} {x*y} {x/y:.2f} {x//y} {x%y} {x**2}")

    with st.expander("4. String methods"):
        txt = st.text_input("Text", "hello world")
        st.code(f"""
text = "{txt}"
print(text.upper())
print(text.lower())
print(text[::-1])
""")
        st.write(txt.upper(), " | ", txt.lower(), " | ", txt[::-1])

    with st.expander("5. Lists – creation & stats"):
        nums = st.multiselect("Numbers", range(1,11), [3,6,9])
        st.code(f"""
lst = {nums}
print(sum(lst), len(lst), min(lst), max(lst))
""")
        if nums:
            st.write(sum(nums), len(nums), min(nums), max(nums))

    with st.expander("6. Indexing & slicing"):
        items = ["apple", "banana", "cherry", "date", "fig"]
        idx = st.slider("Index", 0, 4, 2)
        st.code(f"""
items = {items}
print(items[{idx}])
print(items[1:4])
""")
        st.write(items[idx], " | ", items[1:4])

    with st.expander("7. If / elif / else"):
        score = st.slider("Score", 0, 100, 74)
        st.code(f"""
score = {score}
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)
""")
        grade = "A" if score>=90 else "B" if score>=80 else "C" if score>=70 else "F"
        st.success(grade)

    with st.expander("8. For loop"):
        n = st.slider("n", 1, 15, 8)
        st.code(f"""
for i in range({n}):
    print(i, end=' ')
""")
        st.write(" ".join(str(i) for i in range(n)))

    with st.expander("9. While loop"):
        target = st.slider("Sum ≥", 10, 100, 40)
        total = 0; i = 1
        while total < target:
            total += i; i += 1
        st.code("""
total = 0
i = 1
while total < target:
    total += i
    i += 1
print(total)
""")
        st.write(f"→ {total}")

    with st.expander("10. Defining functions"):
        x = st.number_input("x", 1, 20, 6)
        st.code(f"""
def cube(n):
    return n ** 3
print(cube({x}))
""")
        st.success(x ** 3)

    with st.expander("11. List comprehension"):
        lim = st.slider("Up to", 5, 20, 10)
        st.code(f"""
squares = [x**2 for x in range({lim})]
print(squares)
""")
        st.write([x**2 for x in range(lim)])

    with st.expander("12. Lambda functions"):
        v = st.number_input("Value", -5, 30, 8)
        st.code(f"""
triple = lambda x: x * 3
print(triple({v}))
""")
        st.write((lambda x: x*3)(v))

    with st.expander("13. Dictionaries"):
        st.code("""
scores = {"Ali": 88, "Sara": 94, "Ahmed": 79}
print(scores["Sara"])
print(scores.get("Zara", "Not found"))
""")
        st.write(94); st.write("Not found")

    with st.expander("14. Sets"):
        st.code("""
s = {1,2,2,3,4,4,5}
print(s)
print(3 in s, 7 in s)
""")
        st.write("{1, 2, 3, 4, 5}"); st.write("True False")

    with st.expander("15. Try / except"):
        st.code("""
try:
    print(25 / 0)
except ZeroDivisionError:
    print("Division by zero!")
""")
        st.error("Division by zero!")

    with st.expander("16. Tuples"):
        st.code("""
t = (10, "hello", 3.14)
print(t)
print(t[1])
""")
        st.write("(10, 'hello', 3.14)"); st.write("hello")

    with st.expander("17. f-strings"):
        name = st.text_input("Name", "Ana")
        age = st.slider("Age", 10, 40, 22)
        st.code(f"""
print(f"{name} is {age} years old")
""")
        st.success(f"{name} is {age} years old")

    with st.expander("18. enumerate + range"):
        word = "PYTHON"
        st.code(f"""
for idx, char in enumerate("{word}"):
    print(idx, char)
""")
        for i, c in enumerate(word):
            st.write(i, c)

    with st.expander("19. Common list methods"):
        if "basket" not in st.session_state:
            st.session_state.basket = ["apple", "banana"]
        basket = st.session_state.basket.copy()
        action = st.radio("Action", ["append 'mango'", "pop()", "insert(0,'kiwi')", "remove 'banana'", "clear"], horizontal=True)
        if action == "append 'mango'": basket.append("mango")
        elif action == "pop()" and basket: basket.pop()
        elif action == "insert(0,'kiwi')": basket.insert(0, "kiwi")
        elif action == "remove 'banana'" and "banana" in basket: basket.remove("banana")
        elif action == "clear": basket.clear()
        st.code(f"""
basket = {st.session_state.basket}
# after {action}
print(basket)
""")
        st.write(basket)
        st.session_state.basket = basket

    with st.expander("20. Simulated file reading"):
        content = ["numpy", "pandas", "streamlit"]
        st.code("""
lines = ["numpy", "pandas", "streamlit"]
for line in lines:
    print(line.upper())
""")
        for line in content:
            st.write(line.upper())

# ────────────────────────────────────────────────
# NUMPY – 20
# ────────────────────────────────────────────────
elif section == "🔢 NumPy – 20":
    st.header("🔢 NumPy – 20 Concepts")

    with st.expander("1. np.array creation"):
        st.code("""
import numpy as np
a = np.array([5, 12, 19, 23])
print(a)
""")
        st.write(np.array([5,12,19,23]))

    with st.expander("2. np.arange"):
        col1, col2, col3 = st.columns(3)
        with col1: start = st.slider("Start", -20, 100, 0, key="npar_start")
        with col2: stop  = st.slider("Stop",  start+1, 200, 30, key="npar_stop")
        with col3: step  = st.slider("Step",  1, 20, 3, key="npar_step")
        arr = np.arange(start, stop, step)
        st.code(f"np.arange({start}, {stop}, {step})")
        st.write(arr)

    with st.expander("3. reshape"):
        st.code("""
arr = np.arange(12)
print(arr.reshape(3,4))
""")
        st.write(np.arange(12).reshape(3,4))

    with st.expander("4. Vectorized operations"):
        arr = np.arange(1, 8)
        st.code("""
arr = np.arange(1,8)
print(arr ** 2)
""")
        st.line_chart(arr ** 2)

    with st.expander("5. Broadcasting"):
        a = np.arange(5)
        st.code("""
a = np.arange(5)
print(a + 100)
print(a * 3)
""")
        st.write(a + 100); st.write(a * 3)

    with st.expander("6. Random numbers"):
        st.code("""
np.random.seed(42)
print(np.random.rand(6))
""")
        st.write(np.random.rand(8))

    with st.expander("7. Mean"):
        arr = np.array([4, 8, 15, 16, 23, 42])
        st.code("""
arr = np.array([4,8,15,16,23,42])
print(arr.mean())
""")
        st.write(f"→ {arr.mean():.2f}")

    with st.expander("8. Standard deviation"):
        arr = np.array([4, 8, 15, 16, 23, 42])
        st.code("""
print(arr.std())
""")
        st.write(f"→ {arr.std():.2f}")

    with st.expander("9. Boolean indexing"):
        arr = np.array([3,8,1,12,5,9,0,15])
        st.code("""
arr = np.array([3,8,1,12,5,9,0,15])
print(arr[arr > 7])
""")
        st.write(arr[arr > 7])

    with st.expander("10. min / max / sum"):
        arr = np.random.randint(0, 100, 10)
        st.code("""
print(arr.min(), arr.max(), arr.sum())
""")
        st.write(arr.min(), arr.max(), arr.sum())

    with st.expander("11. Advanced slicing"):
        arr = np.arange(30)
        st.code("""
arr = np.arange(30)
print(arr[5:25:3])
""")
        st.write(arr[5:25:3])

    with st.expander("12. Copy vs view"):
        a = np.array([1,2,3,4]); v = a.view(); v[0] = 99
        st.code("""
a = np.array([1,2,3,4])
v = a.view()
v[0] = 99
print(a)  # changed!
""")
        st.write(a)

    with st.expander("13. vstack / hstack"):
        a = np.array([1,2,3]); b = np.array([10,20,30])
        st.code("""
print(np.vstack((a,b)))
print(np.hstack((a,b)))
""")
        st.write(np.vstack((a,b))); st.write(np.hstack((a,b)))

    with st.expander("14. Transpose"):
        m = np.array([[1,2,3],[4,5,6]])
        st.code("""
print(m.T)
""")
        st.write(m.T)

    with st.expander("15. Dot / matmul"):
        a = np.array([1,2,3]); b = np.array([4,5,6])
        st.code("""
print(np.dot(a, b))
""")
        st.write(np.dot(a, b))

    with st.expander("16. np.where"):
        arr = np.array([-4,-1,0,3,7])
        st.code("""
print(np.where(arr > 0, "positive", "non-positive"))
""")
        st.write(np.where(arr > 0, "positive", "non-positive"))

    with st.expander("17. Sorting"):
        a = np.random.randint(0, 100, 12)
        st.code("""
print(np.sort(a))
""")
        st.write(np.sort(a))

    with st.expander("18. Unique & counts"):
        vals = np.array([2,2,5,5,5,7,9,2,7])
        st.code("""
u, cnt = np.unique(vals, return_counts=True)
print(u)
print(cnt)
""")
        st.write(np.unique(vals, return_counts=True)[0])
        st.write(np.unique(vals, return_counts=True)[1])

    with st.expander("19. linspace"):
        st.code("""
print(np.linspace(0, 10, 9))
""")
        st.write(np.linspace(0, 10, 9))

    with st.expander("20. Simple meshgrid"):
        x = np.array([0,1,2]); y = np.array([10,20,30])
        X, Y = np.meshgrid(x, y)
        st.code("""
X, Y = np.meshgrid([0,1,2], [10,20,30])
print(X)
""")
        st.write(X)

# ────────────────────────────────────────────────
# PANDAS – 20
# ────────────────────────────────────────────────
elif section == "📊 Pandas – 20":
    st.header("📊 Pandas – 20 Concepts")

    df = pd.DataFrame({
        "name":  ["Ali","Sara","Ahmed","Ayesha","Usman","Hina","Bilal"],
        "math":  [78, 92, 85, 96, 71, 89, 64],
        "cs":    [88, 95, 82, 91, 79, 94, 77],
        "city":  ["Lhr","Khi","Lhr","Isb","Khi","Lhr","Fsd"]
    })

    with st.expander("1. Create DataFrame"):
        st.code("""
df = pd.DataFrame({
    "name": [...], "math": [...], ...
})
print(df.head())
""")
        st.dataframe(df.head())

    with st.expander("2. columns & index"):
        st.code("""
print(df.columns)
print(df.index)
""")
        st.write(df.columns.tolist()); st.write(df.index)

    with st.expander("3. Select column"):
        st.code("""
print(df["math"])
""")
        st.write(df["math"])

    with st.expander("4. Select multiple columns"):
        st.code("""
print(df[["name", "cs"]])
""")
        st.dataframe(df[["name", "cs"]])

    with st.expander("5. Filter rows"):
        thresh = st.slider("math >", 60, 100, 85)
        st.code(f"""
print(df[df["math"] > {thresh}])
""")
        st.dataframe(df[df["math"] > thresh])

    with st.expander("6. Sorting"):
        st.code("""
print(df.sort_values("cs", ascending=False))
""")
        st.dataframe(df.sort_values("cs", ascending=False))

    with st.expander("7. Mean of numeric columns"):
        st.code("""
print(df[["math","cs"]].mean())
""")
        st.write(df[["math","cs"]].mean())

    with st.expander("8. Create new column"):
        df_temp = df.copy()
        df_temp["total"] = df_temp["math"] + df_temp["cs"]
        st.code("""
df["total"] = df["math"] + df["cs"]
print(df[["name","total"]])
""")
        st.dataframe(df_temp[["name","total"]])

    with st.expander("9. describe()"):
        st.code("""
print(df.describe())
""")
        st.dataframe(df.describe())

    with st.expander("10. Bar chart (plotly)"):
        fig = px.bar(df, x="name", y="math", color="city")
        st.code("""
fig = px.bar(df, x="name", y="math", color="city")
""")
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("11. loc vs iloc"):
        st.code("""
print(df.loc[0:2, ["name","math"]])
print(df.iloc[0:3, [0,1]])
""")
        st.dataframe(df.loc[0:2, ["name","math"]])

    with st.expander("12. value_counts"):
        st.code("""
print(df["city"].value_counts())
""")
        st.write(df["city"].value_counts())

    with st.expander("13. groupby + mean"):
        st.code("""
print(df.groupby("city")[["math","cs"]].mean())
""")
        st.dataframe(df.groupby("city")[["math","cs"]].mean().round(1))

    with st.expander("14. concat"):
        extra = pd.DataFrame({"name":["Zara"],"math":[83],"cs":[90],"city":["Lhr"]})
        combined = pd.concat([df, extra], ignore_index=True)
        st.code("""
combined = pd.concat([df, extra], ignore_index=True)
""")
        st.dataframe(combined.tail(2))

    with st.expander("15. pivot_table"):
        st.code("""
print(df.pivot_table(values="cs", index="city", aggfunc="mean"))
""")
        st.dataframe(df.pivot_table(values="cs", index="city", aggfunc="mean").round(1))

    with st.expander("16. Missing values"):
        df_m = df.copy(); df_m.iloc[3,1] = None
        st.code("""
print(df_m.isna().sum())
""")
        st.write(df_m.isna().sum())

    with st.expander("17. drop_duplicates"):
        dup = pd.concat([df, df.head(2)], ignore_index=True)
        st.code("""
clean = dup.drop_duplicates()
print(len(clean))
""")
        st.write(len(dup.drop_duplicates()))

    with st.expander("18. rename columns"):
        renamed = df.rename(columns={"math":"Mathematics", "cs":"Computer Science"})
        st.code("""
print(df.rename(columns={"math":"Mathematics"}).columns)
""")
        st.write(renamed.columns.tolist())

    with st.expander("19. query"):
        st.code("""
print(df.query("math > 85 and city == 'Lhr'"))
""")
        st.dataframe(df.query("math > 85 and city == 'Lhr'"))

    with st.expander("20. Scatter plot"):
        df["total"] = df["math"] + df["cs"]
        fig = px.scatter(df, x="math", y="cs", color="city", size="total")
        st.code("""
fig = px.scatter(df, x="math", y="cs", color="city", size="total")
""")
        st.plotly_chart(fig, use_container_width=True)

# ────────────────────────────────────────────────
# MATPLOTLIB – 20  (Mathematical Visualizations)
# ────────────────────────────────────────────────
elif section == "📈 Matplotlib – 20":
    st.header("📈 Matplotlib – 20 Mathematical Visualizations")
    st.markdown("Visualize complex mathematical equations step-by-step using **matplotlib**.")

    # ── 1. Basic Sine Wave ──────────────────────
    with st.expander("1. Sine Wave — y = sin(x)"):
        st.markdown("The fundamental trigonometric wave. Amplitude = 1, Period = 2π.")
        freq = st.slider("Frequency multiplier", 1, 5, 1, key="m1")
        x = np.linspace(0, 2 * np.pi, 500)
        y = np.sin(freq * x)
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(x, y, color="#e63946", linewidth=2)
        ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
        ax.set_title(f"y = sin({freq}x)", fontsize=14)
        ax.set_xlabel("x"); ax.set_ylabel("y")
        ax.grid(True, alpha=0.3)
        st.code(f"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 500)
y = np.sin({freq} * x)

fig, ax = plt.subplots()
ax.plot(x, y, color="#e63946", linewidth=2)
ax.set_title("y = sin({freq}x)")
plt.show()
""")
        st.pyplot(fig); plt.close()

    # ── 2. Multiple trig functions ───────────────
    with st.expander("2. sin, cos, tan — Comparing Trig Functions"):
        st.markdown("Plot sin, cos, and clamped tan on the same axes to see their relationships.")
        x = np.linspace(-2 * np.pi, 2 * np.pi, 600)
        tan = np.tan(x)
        tan[np.abs(tan) > 5] = np.nan   # clip discontinuities
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.plot(x, np.sin(x), label="sin(x)", color="#457b9d", linewidth=2)
        ax.plot(x, np.cos(x), label="cos(x)", color="#e63946", linewidth=2)
        ax.plot(x, tan,       label="tan(x) [clipped]", color="#2a9d8f", linewidth=1.5, linestyle="--")
        ax.axhline(0, color="gray", linewidth=0.6)
        ax.set_ylim(-5, 5); ax.legend(); ax.grid(True, alpha=0.3)
        ax.set_title("Trigonometric Functions", fontsize=14)
        st.code("""
x = np.linspace(-2*np.pi, 2*np.pi, 600)
tan = np.tan(x)
tan[np.abs(tan) > 5] = np.nan  # remove discontinuities

ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)")
ax.plot(x, tan,       label="tan(x) [clipped]", linestyle="--")
ax.legend()
""")
        st.pyplot(fig); plt.close()

    # ── 3. Quadratic & Polynomial ───────────────
    with st.expander("3. Quadratic — y = ax² + bx + c"):
        st.markdown("Interactively control coefficients and watch the parabola change in real time.")
        c1, c2, c3 = st.columns(3)
        a = c1.slider("a", -5, 5, 1, key="m3a")
        b = c2.slider("b", -10, 10, 0, key="m3b")
        c = c3.slider("c", -20, 20, 0, key="m3c")
        x = np.linspace(-10, 10, 400)
        y = a*x**2 + b*x + c
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x, y, color="#6a0572", linewidth=2.5)
        ax.axhline(0, color="gray", linewidth=0.6, linestyle="--")
        ax.axvline(0, color="gray", linewidth=0.6, linestyle="--")
        ax.set_title(f"y = {a}x² + {b}x + {c}", fontsize=14)
        ax.grid(True, alpha=0.3); ax.set_ylim(-100, 100)
        st.code(f"""
x = np.linspace(-10, 10, 400)
y = {a}*x**2 + {b}*x + {c}
ax.plot(x, y)
ax.set_title("y = {a}x² + {b}x + {c}")
""")
        st.pyplot(fig); plt.close()

    # ── 4. Exponential & Logarithm ──────────────
    with st.expander("4. Exponential & Logarithm — eˣ and ln(x)"):
        st.markdown("eˣ grows unboundedly while ln(x) is its inverse — mirror images across y=x.")
        x_exp = np.linspace(-3, 3, 400)
        x_log = np.linspace(0.01, 8, 400)
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.plot(x_exp, np.exp(x_exp),  label="eˣ",    color="#e63946", linewidth=2)
        ax.plot(x_log, np.log(x_log),  label="ln(x)", color="#457b9d", linewidth=2)
        ax.plot([-3,8], [-3,8], label="y = x (mirror)", color="gray", linestyle=":", linewidth=1)
        ax.set_ylim(-4, 8); ax.set_xlim(-3, 8)
        ax.legend(); ax.grid(True, alpha=0.3)
        ax.set_title("eˣ  vs  ln(x) — Inverse Functions", fontsize=14)
        st.code("""
x_exp = np.linspace(-3, 3, 400)
x_log = np.linspace(0.01, 8, 400)

ax.plot(x_exp, np.exp(x_exp), label="eˣ")
ax.plot(x_log, np.log(x_log), label="ln(x)")
ax.plot([-3,8], [-3,8], label="y=x", linestyle=":")
""")
        st.pyplot(fig); plt.close()

    # ── 5. Taylor Series Approximation ──────────
    with st.expander("5. Taylor Series — Approximating sin(x)"):
        st.markdown("Add more terms of the Taylor series and watch it converge to sin(x): `sin(x) ≈ x - x³/3! + x⁵/5! - ...`")
        terms = st.slider("Number of terms", 1, 6, 3, key="m5")
        x = np.linspace(-2*np.pi, 2*np.pi, 600)
        approx = np.zeros_like(x)
        import math
        for n in range(terms):
            k = 2*n + 1
            approx += ((-1)**n * x**k) / math.factorial(k)
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.plot(x, np.sin(x), label="sin(x) — exact", color="#2a9d8f", linewidth=2.5)
        ax.plot(x, approx,    label=f"Taylor ({terms} terms)", color="#e9c46a",
                linewidth=2, linestyle="--")
        ax.set_ylim(-3, 3); ax.legend(); ax.grid(True, alpha=0.3)
        ax.set_title(f"Taylor Series Approximation of sin(x) — {terms} term(s)", fontsize=13)
        st.code(f"""
import math
approx = np.zeros_like(x)
for n in range({terms}):
    k = 2*n + 1
    approx += ((-1)**n * x**k) / math.factorial(k)

ax.plot(x, np.sin(x), label="sin(x) exact")
ax.plot(x, approx,    label="Taylor approx", linestyle="--")
""")
        st.pyplot(fig); plt.close()

    # ── 6. Damped Oscillation ───────────────────
    with st.expander("6. Damped Oscillation — e^(−αt)·sin(ωt)"):
        st.markdown("Models real-world oscillations that lose energy over time (springs, circuits, pendulums).")
        alpha = st.slider("Damping α", 0.0, 2.0, 0.3, 0.1, key="m6a")
        omega = st.slider("Frequency ω", 1, 10, 5, key="m6w")
        t = np.linspace(0, 10, 1000)
        y = np.exp(-alpha * t) * np.sin(omega * t)
        envelope = np.exp(-alpha * t)
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.plot(t, y, color="#e63946", linewidth=1.8, label="Damped signal")
        ax.plot(t,  envelope, color="gray", linewidth=1, linestyle="--", label="+envelope")
        ax.plot(t, -envelope, color="gray", linewidth=1, linestyle="--", label="-envelope")
        ax.fill_between(t, -envelope, envelope, alpha=0.07, color="blue")
        ax.set_title(f"y = e^(−{alpha}t) · sin({omega}t)", fontsize=14)
        ax.legend(); ax.grid(True, alpha=0.3)
        st.code(f"""
t = np.linspace(0, 10, 1000)
y = np.exp(-{alpha} * t) * np.sin({omega} * t)
envelope = np.exp(-{alpha} * t)

ax.plot(t, y, label="Damped signal")
ax.plot(t, envelope, linestyle="--", label="envelope")
""")
        st.pyplot(fig); plt.close()

    # ── 7. Lissajous Figures ────────────────────
    with st.expander("7. Lissajous Figures — Parametric Curves"):
        st.markdown("Produced by two perpendicular sinusoidal oscillations. Common in oscilloscopes and physics.")
        col1, col2, col3 = st.columns(3)
        nx = col1.slider("freq x", 1, 6, 3, key="lix")
        ny = col2.slider("freq y", 1, 6, 2, key="liy")
        delta = col3.slider("phase δ (×π/4)", 0, 8, 1, key="lid") * np.pi / 4
        t = np.linspace(0, 2*np.pi, 1000)
        x = np.sin(nx * t + delta)
        y = np.sin(ny * t)
        fig, ax = plt.subplots(figsize=(5, 5))
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        from matplotlib.collections import LineCollection
        from matplotlib.colors import LinearSegmentedColormap
        colors = plt.cm.plasma(np.linspace(0, 1, len(segments)))
        lc = LineCollection(segments, colors=colors, linewidth=1.5)
        ax.add_collection(lc); ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2)
        ax.set_aspect("equal"); ax.set_title(f"Lissajous: {nx}:{ny}, δ={delta:.2f}", fontsize=13)
        ax.grid(True, alpha=0.2); ax.set_facecolor("#0d0d0d")
        fig.patch.set_facecolor("#0d0d0d")
        ax.tick_params(colors="white"); ax.title.set_color("white")
        st.code(f"""
t = np.linspace(0, 2*np.pi, 1000)
x = np.sin({nx} * t + {delta:.2f})
y = np.sin({ny} * t)

ax.plot(x, y)   # parametric plot
""")
        st.pyplot(fig); plt.close()

    # ── 8. Fourier Components ───────────────────
    with st.expander("8. Fourier Series — Building a Square Wave"):
        st.markdown("A square wave can be built by summing odd harmonics of sine waves (Fourier series).")
        n_harmonics = st.slider("Harmonics", 1, 20, 5, key="m8")
        x = np.linspace(-np.pi, np.pi, 1000)
        square = np.zeros_like(x)
        fig, ax = plt.subplots(figsize=(9, 4))
        for k in range(1, 2*n_harmonics, 2):
            harmonic = (4 / (np.pi * k)) * np.sin(k * x)
            ax.plot(x, harmonic, linewidth=0.8, alpha=0.5)
            square += harmonic
        ax.plot(x, square, color="white", linewidth=2.5, label="Sum (square wave approx)")
        ax.set_facecolor("#1a1a2e"); fig.patch.set_facecolor("#1a1a2e")
        ax.tick_params(colors="white"); ax.yaxis.label.set_color("white")
        ax.legend(facecolor="#333", labelcolor="white")
        ax.set_title(f"Fourier Series: Square Wave ({n_harmonics} odd harmonics)", color="white", fontsize=13)
        ax.grid(True, alpha=0.2)
        st.code(f"""
x = np.linspace(-np.pi, np.pi, 1000)
square = np.zeros_like(x)
for k in range(1, {2*n_harmonics}, 2):          # odd harmonics only
    square += (4 / (np.pi * k)) * np.sin(k * x)

ax.plot(x, square, label="Square wave approx")
""")
        st.pyplot(fig); plt.close()

    # ── 9. 3D Surface Plot ──────────────────────
    with st.expander("9. 3D Surface — z = sin(r)/r  (Sinc Function)"):
        st.markdown("The 2D sinc function — fundamental in signal processing and optics.")
        fig = plt.figure(figsize=(8, 5))
        ax3d = fig.add_subplot(111, projection="3d")
        x = np.linspace(-8, 8, 120)
        y = np.linspace(-8, 8, 120)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2) + 1e-10
        Z = np.sin(R) / R
        surf = ax3d.plot_surface(X, Y, Z, cmap="plasma", alpha=0.9, linewidth=0)
        fig.colorbar(surf, shrink=0.5, aspect=8)
        ax3d.set_title("z = sin(r)/r  (2D Sinc)", fontsize=13)
        ax3d.set_xlabel("x"); ax3d.set_ylabel("y"); ax3d.set_zlabel("z")
        st.code("""
X, Y = np.meshgrid(np.linspace(-8,8,120), np.linspace(-8,8,120))
R = np.sqrt(X**2 + Y**2) + 1e-10
Z = np.sin(R) / R

ax.plot_surface(X, Y, Z, cmap="plasma")
""")
        st.pyplot(fig); plt.close()

    # ── 10. Contour Plot ────────────────────────
    with st.expander("10. Contour Plot — Gaussian Bell Surface"):
        st.markdown("Contour lines connect points of equal value — like a topographic map.")
        x = np.linspace(-4, 4, 200)
        y = np.linspace(-4, 4, 200)
        X, Y = np.meshgrid(x, y)
        Z = np.exp(-(X**2 + Y**2))
        fig, axes = plt.subplots(1, 2, figsize=(11, 4))
        c1 = axes[0].contourf(X, Y, Z, levels=20, cmap="viridis")
        axes[0].set_title("contourf (filled)"); plt.colorbar(c1, ax=axes[0])
        c2 = axes[1].contour(X, Y, Z, levels=15, cmap="coolwarm")
        axes[1].set_title("contour (lines)"); plt.colorbar(c2, ax=axes[1])
        for a in axes: a.set_aspect("equal"); a.grid(True, alpha=0.2)
        st.code("""
Z = np.exp(-(X**2 + Y**2))           # 2D Gaussian

ax.contourf(X, Y, Z, levels=20, cmap="viridis")   # filled
ax.contour(X, Y, Z, levels=15, cmap="coolwarm")   # lines
""")
        st.pyplot(fig); plt.close()

    # ── 11. Polar Plot ──────────────────────────
    with st.expander("11. Polar Plot — Rose Curves  r = cos(nθ)"):
        st.markdown("Polar coordinates produce beautiful petal curves. `n` controls the number of petals.")
        n_petals = st.slider("n (petals)", 1, 8, 3, key="m11")
        theta = np.linspace(0, 2*np.pi, 1000)
        r = np.abs(np.cos(n_petals * theta))
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={"projection": "polar"})
        ax.plot(theta, r, color="#e63946", linewidth=2)
        ax.fill(theta, r, alpha=0.2, color="#e63946")
        ax.set_title(f"Rose Curve: r = |cos({n_petals}θ)|", pad=20, fontsize=13)
        ax.set_facecolor("#f0f0f0")
        st.code(f"""
theta = np.linspace(0, 2*np.pi, 1000)
r = np.abs(np.cos({n_petals} * theta))

ax = plt.subplot(projection="polar")
ax.plot(theta, r)
""")
        st.pyplot(fig); plt.close()

    # ── 12. Spiral ──────────────────────────────
    with st.expander("12. Archimedean Spiral — r = aθ"):
        st.markdown("The Archimedean spiral keeps a constant distance between turns, unlike the golden spiral.")
        a = st.slider("a (spacing)", 0.1, 2.0, 0.5, 0.1, key="m12")
        turns = st.slider("Turns", 1, 10, 4, key="m12t")
        theta = np.linspace(0, turns * 2 * np.pi, 2000)
        r = a * theta
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={"projection": "polar"})
        ax.plot(theta, r, color="#264653", linewidth=1.5)
        ax.set_title(f"Archimedean Spiral  r = {a}θ  ({turns} turns)", pad=20, fontsize=12)
        st.code(f"""
theta = np.linspace(0, {turns}*2*np.pi, 2000)
r = {a} * theta

ax = plt.subplot(projection="polar")
ax.plot(theta, r)
""")
        st.pyplot(fig); plt.close()

    # ── 13. Subplots Grid ───────────────────────
    with st.expander("13. Subplots Grid — Four Functions Side by Side"):
        st.markdown("Use `plt.subplots(rows, cols)` to arrange multiple plots in a grid.")
        x = np.linspace(-3, 3, 300)
        funcs = [
            ("sin(x)",          np.sin(x),       "#e63946"),
            ("x² − 2",          x**2 - 2,        "#457b9d"),
            ("eˣ",              np.exp(x),        "#2a9d8f"),
            ("1/(1+e^−x)",      1/(1+np.exp(-x)), "#e9c46a"),
        ]
        fig, axes = plt.subplots(2, 2, figsize=(9, 6))
        for ax, (label, y, col) in zip(axes.flat, funcs):
            ax.plot(x, y, color=col, linewidth=2)
            ax.set_title(label, fontsize=12)
            ax.grid(True, alpha=0.3); ax.axhline(0, color="gray", linewidth=0.6)
        plt.tight_layout()
        st.code("""
fig, axes = plt.subplots(2, 2, figsize=(9, 6))
funcs = [sin(x), x**2-2, exp(x), sigmoid(x)]
for ax, (label, y, col) in zip(axes.flat, funcs):
    ax.plot(x, y, color=col)
    ax.set_title(label)
plt.tight_layout()
""")
        st.pyplot(fig); plt.close()

    # ── 14. Histogram of Normal Distribution ────
    with st.expander("14. Histogram + PDF Overlay — Normal Distribution"):
        st.markdown("Visualize how data sampled from N(μ,σ) compares with the true probability density function.")
        mu    = st.slider("Mean μ", -5, 5, 0, key="m14m")
        sigma = st.slider("Std σ", 1, 5, 1, key="m14s")
        n_pts = st.slider("Sample size", 200, 5000, 1000, step=100, key="m14n")
        np.random.seed(42)
        data = np.random.normal(mu, sigma, n_pts)
        x_pdf = np.linspace(mu - 4*sigma, mu + 4*sigma, 300)
        pdf = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x_pdf-mu)/sigma)**2)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(data, bins=40, density=True, color="#457b9d", alpha=0.6, label="Sampled data")
        ax.plot(x_pdf, pdf, color="#e63946", linewidth=2.5, label="True PDF")
        ax.set_title(f"Normal Distribution  N({mu}, {sigma}²) — n={n_pts}", fontsize=13)
        ax.legend(); ax.grid(True, alpha=0.3)
        st.code(f"""
data = np.random.normal({mu}, {sigma}, {n_pts})
pdf = (1/({sigma}*√(2π))) * exp(-0.5*((x-{mu})/{sigma})²)

ax.hist(data, bins=40, density=True)   # histogram
ax.plot(x_pdf, pdf, label="True PDF")  # overlay
""")
        st.pyplot(fig); plt.close()

    # ── 15. Vector Field ────────────────────────
    with st.expander("15. Vector Field — Gradient of a Scalar Field"):
        st.markdown("Quiver plots show direction and magnitude of a vector field. Here: gradient of z = sin(x)·cos(y).")
        x = np.linspace(-np.pi, np.pi, 15)
        y = np.linspace(-np.pi, np.pi, 15)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(X) * np.cos(Y)
        U = np.cos(X) * np.cos(Y)   # ∂z/∂x
        V = -np.sin(X) * np.sin(Y)  # ∂z/∂y
        fig, ax = plt.subplots(figsize=(7, 6))
        background = ax.contourf(X, Y, Z, levels=20, cmap="RdYlBu", alpha=0.6)
        ax.quiver(X, Y, U, V, scale=25, width=0.003, color="black", alpha=0.8)
        plt.colorbar(background, ax=ax)
        ax.set_title("Vector Field — ∇(sin(x)·cos(y))", fontsize=13)
        ax.set_xlabel("x"); ax.set_ylabel("y")
        st.code("""
U = np.cos(X) * np.cos(Y)    # ∂z/∂x  (gradient x)
V = -np.sin(X) * np.sin(Y)   # ∂z/∂y  (gradient y)

ax.contourf(X, Y, Z, cmap="RdYlBu")
ax.quiver(X, Y, U, V)         # arrows
""")
        st.pyplot(fig); plt.close()

    # ── 16. Complex Numbers — Mandelbrot ────────
    with st.expander("16. Fractal — Mandelbrot Set"):
        st.markdown("The Mandelbrot set: c ∈ ℂ such that |z_{n+1} = z_n² + c| stays bounded. Pure math made visual.")
        iters = st.slider("Max iterations", 20, 120, 60, key="m16")
        xmin, xmax = -2.5, 1.0
        ymin, ymax = -1.25, 1.25
        w, h = 300, 250
        x = np.linspace(xmin, xmax, w)
        y = np.linspace(ymin, ymax, h)
        C = x[np.newaxis, :] + 1j * y[:, np.newaxis]
        Z = np.zeros_like(C)
        M = np.zeros(C.shape, dtype=int)
        for i in range(iters):
            mask = np.abs(Z) <= 2
            Z[mask] = Z[mask]**2 + C[mask]
            M[mask] += 1
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.imshow(M, extent=[xmin, xmax, ymin, ymax],
                  cmap="inferno", origin="lower", aspect="auto")
        ax.set_title(f"Mandelbrot Set  (max {iters} iterations)", fontsize=13)
        ax.set_xlabel("Re(c)"); ax.set_ylabel("Im(c)")
        st.code(f"""
C = x + 1j*y        # complex grid
Z = np.zeros_like(C)
for i in range({iters}):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask]**2 + C[mask]  # Mandelbrot iteration

ax.imshow(M, cmap="inferno")
""")
        st.pyplot(fig); plt.close()

    # ── 17. Differential Equation Euler's Method ─
    with st.expander("17. Euler's Method — Solving dy/dx = −ky"):
        st.markdown("Numerically solve the ODE dy/dx = −ky using Euler's forward method. Exact solution: y = e^(−kx).")
        k     = st.slider("k (decay rate)", 0.1, 3.0, 0.8, 0.1, key="m17k")
        steps = st.slider("Step size h", 1, 50, 10, key="m17s")
        h = 1.0 / steps
        n = int(5 / h)
        x_e = np.array([i * h for i in range(n+1)])
        y_e = np.zeros(n+1); y_e[0] = 1.0
        for i in range(n):
            y_e[i+1] = y_e[i] + h * (-k * y_e[i])
        x_exact = np.linspace(0, 5, 400)
        y_exact = np.exp(-k * x_exact)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x_exact, y_exact, color="#2a9d8f", linewidth=2.5, label="Exact: e^(−kx)")
        ax.plot(x_e, y_e, "o--", color="#e63946", linewidth=1.5, markersize=4, label=f"Euler (h={h:.2f})")
        ax.set_title(f"Euler's Method  dy/dx = −{k}y   (h = {h:.3f})", fontsize=13)
        ax.legend(); ax.grid(True, alpha=0.3)
        st.code(f"""
h = {h:.3f}   # step size
y[0] = 1.0
for i in range(n):
    y[i+1] = y[i] + h * (-{k} * y[i])  # Euler step

ax.plot(x_exact, np.exp(-{k}*x_exact), label="Exact")
ax.plot(x_euler, y_euler, "o--",        label="Euler")
""")
        st.pyplot(fig); plt.close()

    # ── 18. Probability Distributions ───────────
    with st.expander("18. Probability Distributions Comparison"):
        st.markdown("Compare Normal, Uniform, and Exponential distributions side by side on the same plot.")
        np.random.seed(0)
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        datasets = [
            (np.random.normal(0, 1, 2000),       "Normal(0,1)",       "#457b9d", "bell-shaped"),
            (np.random.uniform(-3, 3, 2000),      "Uniform(−3,3)",     "#2a9d8f", "flat"),
            (np.random.exponential(1.0, 2000),    "Exponential(λ=1)",  "#e63946", "right-skewed"),
        ]
        for ax, (data, title, col, desc) in zip(axes, datasets):
            ax.hist(data, bins=40, color=col, alpha=0.8, density=True, edgecolor="white", linewidth=0.3)
            ax.set_title(f"{title}\n({desc})", fontsize=11)
            ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.code("""
normal  = np.random.normal(0, 1, 2000)
uniform = np.random.uniform(-3, 3, 2000)
expo    = np.random.exponential(1.0, 2000)

fig, axes = plt.subplots(1, 3)
for ax, data in zip(axes, [normal, uniform, expo]):
    ax.hist(data, bins=40, density=True)
""")
        st.pyplot(fig); plt.close()

    # ── 19. Animated-Style — Phase Portrait ─────
    with st.expander("19. Phase Portrait — Pendulum ODE"):
        st.markdown("Phase portraits show trajectories of a dynamical system in state space (θ vs θ̇).")
        fig, ax = plt.subplots(figsize=(8, 6))
        theta = np.linspace(-np.pi, np.pi, 25)
        omega = np.linspace(-4, 4, 25)
        TH, OM = np.meshgrid(theta, omega)
        g, L = 9.81, 1.0
        dTH = OM
        dOM = -(g/L) * np.sin(TH)
        speed = np.sqrt(dTH**2 + dOM**2)
        ax.streamplot(TH, OM, dTH, dOM, color=speed, cmap="plasma", linewidth=1, density=1.5)
        ax.set_xlabel("θ (angle)", fontsize=12); ax.set_ylabel("θ̇ (angular velocity)", fontsize=12)
        ax.set_title("Phase Portrait — Nonlinear Pendulum  θ̈ = −(g/L)sin(θ)", fontsize=13)
        ax.axhline(0, color="white", linewidth=0.5, alpha=0.3)
        ax.set_facecolor("#0d0d0d"); fig.patch.set_facecolor("#0d0d0d")
        ax.tick_params(colors="white"); ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white"); ax.title.set_color("white")
        st.code("""
# Pendulum ODE:  dθ/dt = ω,  dω/dt = -(g/L)*sin(θ)
TH, OM = np.meshgrid(theta, omega)
dTH = OM
dOM = -(g/L) * np.sin(TH)

ax.streamplot(TH, OM, dTH, dOM, color=speed, cmap="plasma")
""")
        st.pyplot(fig); plt.close()

    # ── 20. Heat Equation Visualization ─────────
    with st.expander("20. PDE Visualization — Heat Equation u(x,t)"):
        st.markdown(
            "Solution to the 1D heat equation: `u(x,t) = Σ Bₙ·sin(nπx)·e^(−n²π²t)` "
            "showing how temperature evolves over time."
        )
        t_plot = st.slider("Time t", 0.00, 0.50, 0.05, 0.01, key="m20")
        x = np.linspace(0, 1, 400)
        n_terms = 30
        u = np.zeros_like(x)
        for n in range(1, n_terms + 1, 2):  # odd terms only
            Bn = 4 / (n * np.pi)
            u += Bn * np.sin(n * np.pi * x) * np.exp(-(n**2) * (np.pi**2) * t_plot)
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.fill_between(x, u, alpha=0.25, color="#e63946")
        ax.plot(x, u, color="#e63946", linewidth=2.5)
        ax.plot(x, np.ones_like(x), color="gray", linewidth=1, linestyle=":", label="t=0 (initial)")
        ax.set_ylim(-0.1, 1.2); ax.set_xlabel("x"); ax.set_ylabel("u(x,t)")
        ax.set_title(f"Heat Equation Solution  u(x, t={t_plot:.2f})", fontsize=13)
        ax.legend(); ax.grid(True, alpha=0.3)
        st.code(f"""
x = np.linspace(0, 1, 400)
u = np.zeros_like(x)
for n in range(1, {n_terms}, 2):      # Fourier sine series
    Bn = 4 / (n * np.pi)
    u += Bn * sin(n*pi*x) * exp(-n²*π²*{t_plot:.2f})

ax.plot(x, u)   # temperature profile at t={t_plot:.2f}
""")
        st.pyplot(fig); plt.close()