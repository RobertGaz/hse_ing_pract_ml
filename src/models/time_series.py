# Рассматриваем ряд с информацией о средней длительности поездок за каждый час

plt.figure(figsize=(10, 4))
plt.plot(t.index, t.tripduration, color='tab:blue')
plt.show()

# Тренд
t = t[['tripduration']]

fig, axes = plt.subplots(2, 2, sharey=False, sharex=False)
fig.set_figwidth(14)
fig.set_figheight(8)

window =  24
axes[0][0].plot(t.index, t, label='Original')
axes[0][0].plot(t.index, t.rolling(window=window).mean(), label='1-Day Rolling Mean')
axes[0][0].set_title("1-Day Rolling Mean")
axes[0][0].legend(loc='best')

window = 24*7
axes[0][1].plot(t.index, t, label='Original')
axes[0][1].plot(t.index, t.rolling(window=window).mean(), label='1-Week Rolling Mean')
axes[0][1].set_title("1-Week Rolling Mean")
axes[0][1].legend(loc='best')

window = 24*30
axes[1][0].plot(t.index, t, label='Original')
axes[1][0].plot(t.index, t.rolling(window=window).mean(), label='1-Month Rolling Mean')
axes[1][0].set_title("1-Month Rolling Mean")
axes[1][0].legend(loc='best')

window = 24*30*12
axes[1][1].plot(t.index, t, label='Original')
axes[1][1].plot(t.index, t.rolling(window=window).mean(), label='1-Year Rolling Mean')
axes[1][1].set_title("1-Year Rolling Mean")
axes[1][1].legend(loc='best')

plt.tight_layout()
plt.show()


# Сезонность
# Очевидно, годовая

t_pivot = pd.pivot_table(t, values = 'tripduration', columns = t.index.year, index=t.index.month)

t_pivot.plot(figsize=(10,4))
plt.show()


# Итог
plt.figure(figsize=(16,2))
plt.title('Тренд')
plt.plot(t.index, t.rolling(window=24*30*12).mean())
plt.show()

# Оказывается, с весны 2018-го среднее время проката постоянно увеличивается.
# Целых две минуты за полтора года!
# Медленно, но верно :)