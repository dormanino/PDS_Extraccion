import collections


class PdsAGRMZDataModels:
    def __init__(self, abm_saa=None, la=None, lt=None, bu_su=None, pos=None, hws=None,
                 sp=None, r=None, p=None, asa=None, em_ab=None, em_bis=None, benennung=None, asb=None,
                 t_a=None, vkfbez=None, pws1=None, qu1=None, pws2=None, qu2=None, da=None, anz=None,
                 t_b=None, bg=None, code=None, pruef=None, add_info=None, bm=None, kg=None):
        self.abm_saa = abm_saa
        self.la = la
        self.lt = lt
        self.bu_su = bu_su
        self.pos = pos
        self.hws = hws
        self.sp = sp
        self.r = r
        self.p = p
        self.asa = asa
        self.em_ab = em_ab
        self.em_bis = em_bis
        self.benennung = benennung
        self.asb = asb
        self.t_a = t_a
        self.t_b = t_b
        self.vkfbez = vkfbez
        self.pws1 = pws1
        self.qu1 = qu1
        self.pws2 = pws2
        self.qu2 = qu2
        self.da = da
        self.anz = anz
        self.bg = bg
        self.code = code
        self.pruef = pruef
        self.add_info = add_info
        self.bm = bm
        self.kg = kg

    def create_agrmz_dict(self):
        dict_agrmz = collections.OrderedDict()
        dict_agrmz['abm_saa'] = self.abm_saa
        dict_agrmz['la'] = self.la
        dict_agrmz['lt'] = self.lt
        dict_agrmz['bu_su'] = self.bu_su
        dict_agrmz['pos'] = self.pos
        dict_agrmz['hws'] = self.hws
        dict_agrmz['sp'] = self.sp
        dict_agrmz['r'] = self.r
        dict_agrmz['p'] = self.p
        dict_agrmz['asa'] = self.asa
        dict_agrmz['em_ab'] = self.em_ab
        dict_agrmz['em_bis'] = self.em_bis
        dict_agrmz['benennung'] = self.benennung
        dict_agrmz['asb'] = self.asb
        dict_agrmz['t_a'] = self.t_a
        dict_agrmz['t_b'] = self.t_b
        dict_agrmz['vkfbez'] = self.vkfbez
        dict_agrmz['pws1'] = self.pws1
        dict_agrmz['qu1'] = self.qu1
        dict_agrmz['pws2'] = self.pws2
        dict_agrmz['qu2'] = self.qu2
        dict_agrmz['da'] = self.da
        dict_agrmz['anz'] = self.anz
        dict_agrmz['bg'] = self.bg
        dict_agrmz['code'] = self.code
        dict_agrmz['pruef'] = self.pruef
        dict_agrmz['add_info'] = self.add_info
        dict_agrmz['bm'] = self.bm
        dict_agrmz['kg'] = self.kg
        return dict_agrmz
