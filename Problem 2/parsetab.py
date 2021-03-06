
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '9EAD64998D5C2F9122AF62CD131AD828'
    
_lr_action_items = {'ORDINAL':([0,10,],[1,13,]),'AND':([15,],[17,]),'WORD':([0,2,4,12,13,16,18,],[2,10,12,15,16,18,19,]),'NUMBER':([0,],[4,]),'.':([11,],[14,]),'PARTRIDGE':([4,],[11,]),'MY':([0,],[7,]),',':([19,],[20,]),'$end':([0,1,2,3,4,5,6,7,8,9,14,15,17,20,],[-13,-3,-2,-7,-4,0,-6,-1,-5,-8,-10,-11,-12,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[5,]),'empty':([0,],[9,]),'day':([0,],[8,]),'gift':([0,],[3,]),'partridge':([0,],[6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> MY','start',1,'p_start','PLY12days.py',78),
  ('start -> WORD','start',1,'p_start','PLY12days.py',79),
  ('start -> ORDINAL','start',1,'p_start','PLY12days.py',80),
  ('start -> NUMBER','start',1,'p_start','PLY12days.py',81),
  ('start -> day','start',1,'p_start','PLY12days.py',82),
  ('start -> partridge','start',1,'p_start','PLY12days.py',83),
  ('start -> gift','start',1,'p_start','PLY12days.py',84),
  ('start -> empty','start',1,'p_start','PLY12days.py',85),
  ('day -> WORD WORD ORDINAL WORD WORD WORD ,','day',7,'p_day','PLY12days.py',90),
  ('partridge -> NUMBER PARTRIDGE .','partridge',3,'p_partridge','PLY12days.py',95),
  ('gift -> NUMBER WORD WORD','gift',3,'p_gift','PLY12days.py',100),
  ('gift -> NUMBER WORD WORD AND','gift',4,'p_gift_and','PLY12days.py',105),
  ('empty -> <empty>','empty',0,'p_empty','PLY12days.py',109),
]
