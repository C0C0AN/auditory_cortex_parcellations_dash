# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

main_md = dcc.Markdown('''

This site is an effort to make scientific data (in this case, auditory cortex parcellations)
more **standardised**, **accessible**, **interactive**, **useful** and **open**.

It is currently an online companion to the research, 
*"Automated Localization and Parcellation of Auditory Cortex Areas"*, done by myself ([Peer Herholz](https://peerherholz.github.io/)) and co-authors.


You might find these links useful:

- [The ALPACA toolbox website](https://github.com/C0C0AN/ALPACA)
- [The ALPACA toolbox GitHub repository](https://github.com/C0C0AN/ALPACA)


For questions or if you want to contribute, please feel free to contact me at herholz(dot)s(dot)peer(at)gmail(dot)com.

''')


layout = html.Div([
    html.H2('About',
    style={
        'textAlign': 'center',
        'marginBottom': 25,
        'marginTop': 25,
    }),
    main_md,
],
style={
    'marginBottom': 25,
    'marginTop': 25,
    'marginLeft': '5%',
    'maxWidth': '90%',
})
