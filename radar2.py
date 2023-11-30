from mplsoccer import Radar, FontManager, grid
import matplotlib.pyplot as plt

#Inizializzazione delle colonne con params
params=['Goal','Shoot','Shoot Target','Sh/90','SoT/90','G/Sh','G/SoT','Dist','FK','PK','xG']
#Inizializzazione di valori minimi e massimi a secondo dei dati da analizzare
low=[0,0,0,0.0,0.0,0.0,0.0,0.0,0,0,0.0]
high=[35,150,80,10.0,5.0,1.0,1.0,30.0,5,10,30.0]




radar = Radar(params, low, high,round_int=[False]*len(params),
              num_rings=4,  # numero di cerchi da visualizzare nel bulls eye (escluso il centro)
              ring_width=1, center_circle_radius=1)

#Presi alcuni font online
URL1 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
        'SourceSerifPro-Regular.ttf')
serif_regular = FontManager(URL1)
URL2 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
        'SourceSerifPro-ExtraLight.ttf')
serif_extra_light = FontManager(URL2)
URL3 = ('https://raw.githubusercontent.com/google/fonts/main/ofl/rubikmonoone/'
        'RubikMonoOne-Regular.ttf')
rubik_regular = FontManager(URL3)
URL4 = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf'
robotto_thin = FontManager(URL4)
URL5 = ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
        'RobotoSlab%5Bwght%5D.ttf')
robotto_bold = FontManager(URL5)

#valori di numerici assegnati secondo l'ordine di params presi su https://urlis.net/9syvn8c5 (shortlink di FbRef)"
lautaro_values2021=[17,107,37,3.76,1.30,0.14,0.41,14.9,0,2,15.2]
lautaro_values2022=[21,112,47,4.42,1.85,0.16,0.38,13.8,0,3,20.9]
lautaro_values2023=[21,125,51,4.37,1.78,0.16,0.39,15.1,0,1,18.1]


# plot radar
# creazione del radar con mplsoccer:
fig, axs = grid(figheight=14, grid_height=0.915, title_height=0.06, endnote_height=0.025,
                title_space=0, endnote_space=0, grid_key='radar', axis=False)

# plot radar
fig, ax = radar.setup_axis()

rings_inner = radar.draw_circles(ax=ax, facecolor='#ffb2b2', edgecolor='#fc5f5f')

radar1, vertices1 = radar.draw_radar_solid(lautaro_values2021, ax=ax,
                                           kwargs={'facecolor': '#aa65b2',
                                                   'alpha': 0.6,
                                                   'edgecolor': '#216352',
                                                   'lw': 3})

radar2, vertices2 = radar.draw_radar_solid(lautaro_values2022, ax=ax,
                                           kwargs={'facecolor': '#66d8ba',
                                                   'alpha': 0.6,
                                                   'edgecolor': '#216352',
                                                   'lw': 3})

radar3, vertices3 = radar.draw_radar_solid(lautaro_values2023, ax=ax,
                                           kwargs={'facecolor': '#697cd4',
                                                   'alpha': 0.6,
                                                   'edgecolor': '#222b54',
                                                   'lw': 3})

ax.scatter(vertices1[:, 0], vertices1[:, 1],
           c='#aa65b2', edgecolors='#502a54', marker='o', s=150, zorder=2)
ax.scatter(vertices2[:, 0], vertices2[:, 1],
           c='#66d8ba', edgecolors='#216352', marker='o', s=150, zorder=2)
ax.scatter(vertices3[:, 0], vertices3[:, 1],
           c='#697cd4', edgecolors='#222b54', marker='o', s=150, zorder=2)

range_labels = radar.draw_range_labels(ax=ax, fontsize=25, fontproperties=robotto_thin.prop)
param_labels = radar.draw_param_labels(ax=ax, fontsize=25, fontproperties=robotto_thin.prop)
#endnote=note a margine. title=scritte
endnote_text = axs['endnote'].text(0.99, 0.5, 'Inspired By: StatsBomb / Rami Moghadam', fontsize=15,
                                   fontproperties=robotto_thin.prop, ha='right', va='center')
title1_text = axs['title'].text(0.01, 0.65, 'Lautaro Martinez', fontsize=25, color='#01c49d',
                                fontproperties=robotto_bold.prop, ha='left', va='center')
title2_text = axs['title'].text(0.01, 0.25, 'Inter 2020/2021', fontsize=15,
                                fontproperties=robotto_thin.prop,
                                ha='left', va='center', color='#01c49d')
title3_text = axs['title'].text(0.51, 0.65, 'Lautaro Martinez', fontsize=25,
                                fontproperties=robotto_bold.prop,
                                ha='center', va='center', color='#d80499')
title4_text = axs['title'].text(0.51, 0.25, 'Inter 2021/2022', fontsize=15,
                                fontproperties=robotto_thin.prop,
                                ha='center', va='center', color='#d80499')
title5_text = axs['title'].text(0.99, 0.65, 'Lautaro Martinez', fontsize=25,
                                fontproperties=robotto_bold.prop,
                                ha='right', va='center', color='#222b54')
title6_text = axs['title'].text(0.99, 0.25, 'Inter 2022/2023', fontsize=15,
                                fontproperties=robotto_thin.prop,
                                ha='right', va='center', color='#222b54')
#print del plot
print(plt.show())