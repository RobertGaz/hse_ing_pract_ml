plt.figure(figsize=(15, 7))
# Исключим неполный 2019 год из данных для визуализации
df[df.year!=2019].year.value_counts(sort=False).plot.bar(color='pink')
plt.title('Количество поездок по годам')
plt.show()

# 1) Количество поездок по месяцам
# Ближе к лету становится больше поездок.
# Судя по гистограмме, велосезон - с мая по октбярь.


plt.figure(figsize=(15, 7))
# Исключим неполный 2019 год из данных для визуализации
df[df.year != 2019].month.value_counts(sort=False).plot.bar(color='khaki')
plt.title('Количество поездок по месяцам')
plt.show()

# 2) Количество поездок по дням недели
# Судя по гистограмме, какая-то часть клиентов сервиса используют эти велосипеды для поездки на работу/учёбу.

plt.figure(figsize=(15, 7))
df.week_day.value_counts(sort=False).plot.bar(color='gray')
plt.title('Количество поездок по дням недели')
plt.show()


# 3) Количество поездок по времени дня
# Два пика поездок приходятся на время, в которое обычно люди едут на работу / с работы

plt.figure(figsize=(15, 7))
df.hour.value_counts(sort=False).plot.bar(color='aquamarine')
plt.title('Количество поездок по времени дня')
plt.show()


# А как обстоят дела в выходные?
# В выходные люди катаются в основном днём:

plt.figure(figsize=(15, 7))
df[df.week_day > 5].hour.value_counts(sort=False).plot.bar(color='lavender')
plt.title('Количество поездок по времени дня в выходные')
plt.show()

# Но в будни в это время дня всё равно значительно больше поездок.

# 4) Количество поездок в зависимости от возраста и от пола.
# Среди тех, кто предоставил данные о возрасте и поле наблюдается следующая картина:
# Верхний график соответствует мужчинам, нижний - женщинам.

plt.figure(figsize=(15, 7))
df[df.gender=='Male'].age.value_counts(sort=False).plot.line(color='yellowgreen')
df[df.gender=='Female'].age.value_counts(sort=False).plot.line(color='yellow')
plt.xticks(ticks=list(range(5,125,5)))
plt.xlabel('Возраст')
plt.title('Количество поездок в зависимости от возраста и от пола')
plt.show()


# 5) Распределение длительности поездок.
# Похоже на логнормальное распределение

plt.figure(figsize=(15, 7))
df.tripduration.plot.hist(bins=320)
plt.title('Распределение длительности поездок')
plt.xlabel('Длительность поездки в минутах')
plt.show()

# 6) Медианная продолжительность поездки у женщин немного больше, чем у мужчин.
# Возможно это связано с тем, что они катаются медленнее.
# Сравнение квартилей и порога статистически значимой выборки также может указывать на это.

plt.style.use('default')
sns.boxplot(y="gender", x="tripduration", data=df, orient="h")
plt.show()


# 7) Наибольшим спросом велопрокат пользуется у людей 25-35 лет:

plt.figure(figsize=(18, 10))
df[df.age<80].age.value_counts(sort=False).plot.bar()
plt.show()

# 8) Ещё оказывается, что в велосезон люди катаются дольше:

# plt.rc('figure', figsize=(7, 9))
sns.boxplot(y="month", x="tripduration", palette="Set3", width=0.6, data=df, orient="h")
plt.show()


# 9) В будни поездки короче, чем в выходные
# Видимо в выходные люди чуть меньше торопятся

plt.rc('figure', figsize=(7, 7))
sns.boxplot(y="week_day", x="tripduration", palette="Set2", width=0.6, data=df, orient="h")
plt.show()