r"""Generation script for ISO 4032 nut"""

from ccad.model import prism, filling, ngon, cylinder

m_max = {{ m_max }}
s_max = {{ s_max }}
d_a_min = {{ d_a_min }}

body = prism(filling(ngon(2 / 3**.5 * s_max / 2., 6)), (0, 0, m_max))

hole = cylinder(d_a_min / 2., m_max)

__shape__ = (body - hole).shape

__anchors__ = {"nut_bottom": {"p": (0., 0., 0.),
                              "u": (0., 0., -1.),
                              "v": (1., 0., 0.),
                              "dimension": d_a_min},
               "nut_top": {"p": (0., 0., m_max),
                           "u": (0., 0., 1.),
                           "v": (1., 0., 0.),
                           "dimension": d_a_min}}
