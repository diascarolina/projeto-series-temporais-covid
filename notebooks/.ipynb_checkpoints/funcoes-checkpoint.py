import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# configurações de cores
GRAY1, GRAY2, GRAY3 = '#231F20', '#414040', '#555655'
GRAY4, GRAY5, GRAY6 = '#646369', '#76787B', '#828282'
GRAY7, GRAY8, GRAY9 = '#929497', '#A6A6A5', '#BFBEBE'
BLUE1, BLUE2, BLUE3, BLUE4 = '#174A7E', '#4A81BF', '#94B2D7', '#94AFC5'
RED1, RED2 = '#C3514E', '#E6BAB7'
GREEN1, GREEN2 = '#0C8040', '#9ABB59'
ORANGE1 = '#F79747'

# configurações da fonte utilizada nos gráficos
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.bf'] = 'Arial:bold'
plt.rcParams['mathtext.it'] = 'Arial:italic'

def plotar_linha(x, y, dados, title='', subtitle='', xlabel='', ylabel='', color=''):
    '''
    Funcao que plota um gráfico de linha, com o eixo x representando uma data.
    '''
    fig, ax = plt.subplots(figsize = (12, 6))
    plt.sca(ax)
    sns.lineplot(x=x, y=y, data=dados, linewidth = 2, color=color)
    plt.ylabel(ylabel, fontdict = {'fontsize': 20}, color = GRAY3)
    plt.xlabel(xlabel, fontdict = {'fontsize': 20}, color = GRAY3)
    plt.title(title + '\n',  loc = 'left', fontsize = 25, color = GRAY4)
    plt.text(0,1.03, subtitle, color=GRAY5, transform=ax.transAxes, fontsize=20)
    ax.tick_params(color = 'darkgrey', bottom = 'off')
    ax.spines['bottom'].set_color('darkgrey')
    ax.spines['left'].set_color('darkgrey')
    ax.spines['right'].set_color('darkgrey')
    ax.spines['top'].set_visible(False)
    ax.spines['top'].set_visible(False)
    for i in ax.get_yticklabels() + ax.get_xticklabels():
        i.set_fontsize(15)
        i.set_color(GRAY3)
    for i in ax.get_yticklabels() + ax.get_xticklabels():
        i.set_fontsize(15)
        i.set_color(GRAY3)
    plt.show()