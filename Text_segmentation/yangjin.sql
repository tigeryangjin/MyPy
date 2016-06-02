select text
  from (select text, trunc(pm / 10) + 1 pm
          from (select 'copy from ' || (case
                         when instr(key_value_1, '13') = 1 then
                          'bbgdq'
                         when instr(key_value_1, '120072') = 1 then
                          'bbgdq'
                         when instr(key_value_1, '120040') = 1 then
                          'bbgdq'
                         else
                          'bbgcs'
                       end) || '/drowssap@' || key_value_1 || chr(32) || 'to' ||
                       chr(32) || 'bbgcs/drowssap@XL120017N159' || chr(32) ||
                       'INSERT' || chr(32) || 'dpm001' || chr(32) ||
                       'using select * from (select * from (select b.dsp0103 shopid,a.dsp0103 shopname from dsp001 a,dsp001 b where a.dsp0101=" 0016 " and b.dsp0101=" 0010 ") shop,(select sd0101,sd0102,dg0102,sd0103,sd0104,sd0105,amt,sd0106,da0102,sd0107,sd0108,sd0109,sd0110,pmttype_desc,vipno from sd001 sd,da001 da,salemaster sa,dg001 dg ,pmt_priority pm where sd.sale_nbr in (select sale_nbr from sd002 where sd0201=" 20160522 " and sd0205=" 16 " and sd0209>=" 21 :00 " and sd0206>=" 50 ") and sd.sale_nbr=sa.sale_nbr and da0101=sd0107 and sd0102=dg0101 and sd0110=pmttype(+)));' ||
                       chr(59) || chr(10) text,
                       a.key_value_1,
                       store_name,
                       a.state,
                       description,
                       (case
                         when store_format in (1, 2) then
                          1
                         else
                          2
                       end) store_format,
                       row_number() over(partition by store_format order by a.state, key_value_1) pm
                  from addr a, State b, store c
                 where a.state = b.State
                   and a.key_value_1 = c.store
                   and key_value_1 < '140000'
                   and addr_type in (01)
                   and module = 'ST'))
