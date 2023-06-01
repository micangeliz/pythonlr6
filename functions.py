from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px


# 1.1 Matplotlib
def matplotlibAny():
    x = [0, 15, 30]
    y = [20, 35, 0]

    plt.plot(x, y, 'blue', linewidth=3, label='line1-width-3')

    plt.legend(loc=0)
    plt.xlabel("x-axis", fontsize=11)
    plt.ylabel("y-axis", fontsize=11)
    plt.title("1.1 Обычный линейный график с помощью чистого matplotlib", fontsize=13)
    plt.show()


# 1.2 Matplotlib
def matplotlibAlcohol(df):
    fig = plt.figure()
    sp1 = fig.add_subplot(121)
    sp2 = fig.add_subplot(122)

    sp1.title.set_text('1.2.1 Зависимость чрезмерного (>3)\n ежедневного употребления \nалкоголя от возраста учеников')
    sp2.title.set_text('1.2.2 Зависимость количества учеников \nвозрастом 15 лет от их еженедельного\n употребления '
                       'алкоголя')

    plt.subplot(121)
    Dalcs = df[df["Dalc"] > 3]["age"].value_counts()
    plt.xlabel("возраст", fontsize=11)
    plt.ylabel("количество", fontsize=11)
    plt.bar(Dalcs.index, Dalcs)

    plt.subplot(122)
    Walcs = df[df["age"] == 15]["Walc"].value_counts()
    plt.xlabel("оценка Walc", fontsize=11)
    plt.ylabel("количество", fontsize=11)
    plt.scatter(Walcs.index, Walcs)
    plt.show()


# 2.1 plot1
def boxplot(df):
    df.boxplot(column=["freetime"], by=["Dalc"])
    plt.suptitle('')
    plt.title("\n\n2.1 Зависимость ежедневного употребления алкоголя \n от свободного времени ученика")
    plt.show()


# 2.2 plot2
def plotFreetime(df):
    df[df["age"] == 15].plot(
        x="famrel", y="freetime", kind='scatter', title="2.2 Зависимость свободного времени от\n отношения в семье "
                                                        "учеников возрастом 15 лет")
    plt.show()


# 2.3 plot3
def plotTopMarks(df):
    top_5 = df.sort_values(by="G3", ascending=False).head()
    top_5.plot(x="Walc", y="G3", kind="bar", rot=5, fontsize=4, title="2.3 Топ оценок по G3 и соответствующие оценки "
                                                                      "Walc")
    plt.show()


# 3.1 Seaborn .pairplot
def pairplot(df):
    sns.pairplot(data=df, vars=["health", "famrel", "Dalc"])
    plt.show()


# 3.2 Seaborn .jointplot
def jointplot(df):
    sns.jointplot(data=df, x="health", y="famrel", palette='bright', hue='famrel')
    plt.show()


# 3.3 Seaborn .violinplot
def violinplot(df):
    sns.violinplot(data=df, x="famrel", y="Pstatus")
    plt.title("3.3 Скрипичная диаграмма для параметров 'семейные отношения' и 'статус проживания семьи' учеников")
    plt.show()


# 3.4 Seaborn .heatmap
def heatmam(df):
    best_marks = df["G3"].value_counts().head(15).index
    df1 = df[df["G3"].isin(best_marks)][
        ["famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]]
    sns.set(font_scale=1.15)
    plt.figure(figsize=(8, 4))
    sns.heatmap(
        df1.corr(),
        cmap='RdBu_r',  # задаёт цветовую схему
        annot=True,  # рисует значения внутри ячеек
        vmin=-1, vmax=1)  # указывает начало цветовых кодов от -1 до 1.

    # Близость к единице означает сильно выраженную положительную линейную зависимость, а близость к -1 —
    # сильно выраженную отрицательную зависимость

    plt.title("3.4 Тепловая карта данных, отражающая меру линейных отношений данных")
    plt.show()


# 4 Plotly
def plotly(df):
    fig = px.sunburst(df, path=['Pstatus', 'guardian', 'freetime'], values='absences')
    fig.show()
